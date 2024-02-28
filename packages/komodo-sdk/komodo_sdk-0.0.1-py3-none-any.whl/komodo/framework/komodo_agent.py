from komodo.framework.komodo_tool import KomodoTool
from komodo.framework.komodo_user import KomodoUser
from komodo.models.framework.assistant import AssistantRequest, AssistantResponse
from komodo.models.framework.models import OPENAI_GPT35_MODEL
from komodo.models.framework.responder import get_assistant_response


class KomodoAgent:
    def __init__(self, name, instructions, purpose=None, model=OPENAI_GPT35_MODEL, provider="openai",
                 id=None, email=None, reply_as=None, phone=None, chatbot=False, assistant_id=None, tools=None,
                 output_format=None, footer=None):
        self.id = id or name.lower().replace(" ", "_")
        self.name = name
        self.email = email or f"{self.id}@kmdo.app"
        self.reply_as = reply_as or self.email
        self.purpose = purpose or f"An agent to {instructions}"
        self.instructions = instructions
        self.model = model
        self.provider = provider
        self.assistant_id = assistant_id
        self.tools: [KomodoTool] = tools or []
        self.output_format = output_format
        self.footer = footer
        self.phone = phone
        self.chatbot = chatbot

    def __str__(self):
        return f"KomodoAgent: {self.name} ({self.email}), {self.purpose}"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'reply_as': self.reply_as,
            'purpose': self.purpose,
            'instructions': self.instructions,
            'model': self.model,
            'provider': self.provider,
            'assistant_id': self.assistant_id,
            'tools': [tool.to_dict() for tool in self.tools],
            'output_format': self.output_format,
            'footer': self.footer,
            'phone': self.phone,
            'chatbot': self.chatbot
        }

    def add_tool(self, tool):
        self.tools += [tool]

    def run(self, prompt) -> AssistantResponse:
        user = KomodoUser.default_user().to_dict()
        assistant = self.to_dict()
        assistant['tools'] = self.tools
        request = AssistantRequest(user=user, assistant=assistant, prompt=prompt)
        response = get_assistant_response(request)
        return response

    def run_as_tool(self, args) -> str:
        response = self.run(args['system'] + "\n\n" + args['user'])
        return response.text


def data_agent(data_tool):
    return KomodoAgent(id="librarian",
                       name='Librarian Agent',
                       purpose='Retrieves knowledge from private data sources',
                       instructions='Use the data sources to retrieve the information needed for the task.',
                       tools=[data_tool])


def agent_function_definition(agent):
    return {
        "type": "function",
        "function": {
            "name": agent.id,
            "description": agent.purpose,
            "parameters": {
                "type": "object",
                "properties": {
                    "system": {
                        "type": "string",
                        "description": "Specify context and what exactly you need the agent to do in English."
                    },
                    "user": {
                        "type": "string",
                        "description": "The input to be processed by the agent."
                    },
                },
                "required": ["system", "user"]
            }
        }
    }


def get_agent_as_tool(agent):
    return KomodoTool(name=agent.name,
                      definition=agent_function_definition(agent),
                      action=agent.run_as_tool)


def coordinator_agent(agents):
    return KomodoAgent(id="coordinator",
                       name='Coordinator Agent',
                       purpose='Coordinate other agents',
                       instructions='Coordinate the other agents to achieve the goal. Create system and user prompts for each agent based on task requirements and inputs.',
                       tools=[get_agent_as_tool(agent) for agent in agents])
