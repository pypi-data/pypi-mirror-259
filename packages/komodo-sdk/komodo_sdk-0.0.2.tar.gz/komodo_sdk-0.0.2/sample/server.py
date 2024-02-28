from komodo import KomodoApp
from komodo.core.agents.default import translator_agent, summarizer_agent, websearch_agent


def build() -> KomodoApp:
    app = KomodoApp(name='Sample', purpose='To test the Komodo Appliances SDK')
    app.add_agent(summarizer_agent())
    app.add_agent(translator_agent())
    app.add_agent(websearch_agent())
    print(app.capabilities())
    return app


SAMPLE_APP = build().app


def run():
    app = build()
    prompt = '''
        Summarize the following text in 5 words and translate into Spanish, Hindi and German:
        This is a sample application using the new Komodo 9 SDK.
    '''
    response = app.run(prompt)
    print(response.text)


if __name__ == '__main__':
    run()
