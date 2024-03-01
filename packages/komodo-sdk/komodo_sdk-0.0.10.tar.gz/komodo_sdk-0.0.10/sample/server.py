import os.path

from komodo import KomodoApp
from komodo.core.sources.filesystem import Filesystem
from komodo.loaders.appliance_loader import ApplianceLoader
from komodo.models.framework.runners import run_appliance
from komodo.server.fast import app
from komodo.server.globals import set_appliance_for_fastapi


def build() -> KomodoApp:
    app = KomodoApp(shortcode='sample', name='Sample', purpose='To test the Komodo Appliances SDK')
    return app


SAMPLE_APP = app
KOMODO_APP = build()
set_appliance_for_fastapi(KOMODO_APP)


def build_and_run():
    app = build()
    prompt = '''
        Summarize the following text in 5 words and translate into Spanish, Hindi and German:
        This is a sample application using the new Komodo 9 SDK.
    '''
    response = run_appliance(app, prompt)
    print(response.text)


def load_and_run():
    app = ApplianceLoader.load('sample')
    prompt = '''
        Summarize the following text in 5 words and translate into Spanish, Hindi and German:
        This is a sample application using the new Komodo 9 SDK.
    '''
    response = run_appliance(app, prompt)
    print(response.text)


def run_server():
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)  # noinspection PyTypeChecker


if __name__ == '__main__':
    app = KOMODO_APP
    fs = Filesystem(name="Sample Docs", source=os.path.dirname(__file__))
    items = fs.list_items()
    for i in items:
        print(fs.get_item(i))
        
    app.add_data_source(fs)
