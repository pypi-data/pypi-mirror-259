from komodo.framework.komodo_agent import KomodoAgent
from komodo.models.framework.models import OPENAI_GPT4_MODEL
from komodo.shared.directory.actions_directory import get_tool_by_name


def summarizer_agent(n=50):
    return KomodoAgent(id="summarizer",
                       name='Summary Agent',
                       purpose='Summarize text',
                       instructions='Please summarize the following text in {} words'.format(n))


def translator_agent(language="languages requested by user"):
    return KomodoAgent(id="translator",
                       name='Translation Agent',
                       purpose='Translate text',
                       instructions='Please translate the following text into {}'.format(language))


def embedhelper_agent():
    return KomodoAgent(id="embedhelper",
                       name='Embed Helper Agent',
                       purpose='Transform text into Q&A json format',
                       model=OPENAI_GPT4_MODEL,
                       instructions='Transform the text into a Q&A json format for use in a chatbot or other application'
                                    'Keep all the information but remove any duplicate or irrelevant information. '
                                    'Do not remove any information that is relevant to the text. '
                                    'For information that does not translate well into Q&A format, include it as blob. '
                                    'Do not leave any information out of the output. '
                                    'You can have many blobs in the output. '
                                    'Format of json: [{q: `question`, a: `answer`}, {blob: `blob`}, {q: `question`, a: `answer`},...]')


def websearch_agent():
    return KomodoAgent(id="webguru",
                       name='Web Search Agent',
                       purpose='Search the web for information',
                       instructions='Find the latest information on the topic of the text using web search tools',
                       tools=[get_tool_by_name("komodo_tavily_search")])


def webscraper_agent():
    return KomodoAgent(id="scraper",
                       name='Web Page Scraper Agent',
                       purpose='Downloads web pages and acts on contents',
                       instructions='Download the web page and extract the information needed as instructed.',
                       tools=[get_tool_by_name("komodo_web_content_extractor")])
