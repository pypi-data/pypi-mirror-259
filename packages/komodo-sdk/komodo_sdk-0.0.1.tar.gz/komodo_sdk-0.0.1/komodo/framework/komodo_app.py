import json
import os

from flask import Flask, request, jsonify, render_template

from komodo.framework.komodo_agent import KomodoAgent, data_agent, coordinator_agent
from komodo.framework.komodo_datasource import KomodoDataSource
from komodo.framework.komodo_tool import KomodoTool
from komodo.framework.komodo_vectorstore import KomodoVectorStore


class KomodoApp:
    def __init__(self, name, purpose, agents=None, tools=None, sources=None):
        self.name = name
        self.purpose = purpose
        self.agents: [KomodoAgent] = agents or []
        self.tools: [KomodoTool] = tools or []
        self.data_sources: [KomodoDataSource] = sources or []
        self.vector_stores: [KomodoVectorStore] = []
        self.app = Flask(__name__)
        self.app.static_folder = os.path.dirname(__file__) + '/static'
        self.app.template_folder = os.path.dirname(__file__) + '/templates'
        self.setup_routes()
        self.tools.append(self.search_data_tool())
        self.agents.append(data_agent(self.search_data_tool()))

    def add_agent(self, agent):
        self.agents += [agent]

    def get_agent(self, id):
        for a in self.agents:
            if a.id == id:
                return a
        return None

    def get_capabilities_of_agents(self):
        n = 0
        t = []
        for a in self.agents:
            if a.purpose is not None:
                n += 1
                t.append("{}. {}: {}".format(n, a.id, a.purpose))
        return '\n'.join(t)

    def add_tool(self, tool):
        self.tools += [tool]

    def get_tool(self, id):
        for a in self.tools:
            if a.id == id:
                return a
        return None

    def get_capabilities_of_tools(self):
        n = 0
        t = []
        for a in self.tools:
            if a.purpose is not None:
                n += 1
                t.append("{}. {}: {}".format(n, a.id, a.purpose))
        return '\n'.join(t)

    def add_data_source(self, ds1):
        self.data_sources += [ds1]

    def get_data_source(self, source):
        for a in self.data_sources:
            if a.id == source or a.name == source:
                return a
        return None

    def list_data(self, sources=None, metadata=False):
        if isinstance(sources, str):
            sources = sources.split(',')
        sources = sources or self.data_sources

        dataset = []
        for source in sources:
            if isinstance(source, str):
                source = self.get_data_source(source)

            for item in source.list_items():
                data = {'source': source.id, 'type': source.type, 'item': item}
                if metadata:
                    for doc in source.get_item(item):
                        data['metadata'] = doc.metadata
                        print(data)
                        dataset.append(data)
                else:
                    print(data)
                    dataset.append(data)

        return dataset

    def search_data_definition(self):
        return {
            "type": "function",
            "function": {
                "name": "appliance_data_search",
                "description": "Retrieve data from available data sources",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "String to semantic search for in the data sources"
                        }
                    },
                    "required": ["query"]
                }
            }
        }

    def get_data_as_tool_action(self, args):
        text = args['query']
        result = []
        for pc in self.vector_stores:
            result += pc.search(text, top_k=3)

        if len(result) > 0:
            return json.dumps(result)

        return "Found: {}. The answer is 42.".format(args['query'])

    def search_data_tool(self):
        return KomodoTool(name="Appliance Data Search Tool",
                          definition=self.search_data_definition(),
                          action=self.get_data_as_tool_action)

    def add_vector_store(self, store):
        self.vector_stores += [store]

    def get_vector_store(self, source):
        for a in self.vector_stores:
            if a.id == source or a.name == source:
                return a
        return None

    def capabilities(self):
        n = 0
        t = []
        for a in self.agents:
            if a.purpose is not None:
                n += 1
                t.append("{}. {}: {}".format(n, a.id, a.purpose))

        return "I am " + self.name + \
            " appliance and my purpose is " + self.purpose + \
            ". I have agents with these capabilities: \n" + self.get_capabilities_of_agents() + \
            "\n\nI have tools with these capabilities: \n" + self.get_capabilities_of_tools()

    def run(self, prompt):
        agent = coordinator_agent(self.agents)
        return agent.run(prompt)

    def server(self, debug=True):
        self.app.run(debug=debug)

    def setup_routes(self):
        @self.app.route('/', methods=['GET'])
        def home():
            return render_template('index.html')

        # Endpoint to list agents
        @self.app.route('/appliance/list', methods=['GET'])
        def list_agents():
            # return jsonify({"agents": [str(a) for a in self.agents]})
            return jsonify({"agents": [a.to_dict() for a in self.agents]})

        # Endpoint to ask an agent a question
        @self.app.route('/agent/ask', methods=['GET', 'POST'])
        def ask_agent():
            if request.json:
                message = request.json['message']
            else:
                message = request.values.get('message')
            reply = self.run(message)
            return jsonify({"reply": reply.text, "message": message})

        # Endpoint to create a conversation
        @self.app.route('/conversation/create', methods=['POST'])
        def create_conversation():
            # Implement the conversation creation logic
            return jsonify({"status": "Conversation created", "id": "12345"})

        # Endpoint to add a message to a conversation
        @self.app.route('/conversation/converse', methods=['POST'])
        def converse():
            data = request.json
            # Implement the logic to add a message to a conversation
            return jsonify({"status": "Message added to conversation"})

        # Endpoint to retrieve a conversation
        @self.app.route('/conversation/retrieve', methods=['GET'])
        def retrieve_conversation():
            conversation_id = request.args.get('conversationId')
            # Implement the logic to retrieve a conversation
            return jsonify({"id": conversation_id, "messages": []})

        # Endpoint to retrieve an attachment
        @self.app.route('/attachment/retrieve', methods=['GET'])
        def retrieve_attachment():
            attachment_id = request.args.get('attachmentId')
            # Implement the logic to retrieve an attachment
            return jsonify({"id": attachment_id, "data": "Attachment data"})

        # Endpoint to retrieve an attachment
        @self.app.route('/api/chat', methods=['POST'])
        def chat_api():
            data = request.json
            return jsonify({"reply": self.run(data['message']).text, "message": data['message']})
