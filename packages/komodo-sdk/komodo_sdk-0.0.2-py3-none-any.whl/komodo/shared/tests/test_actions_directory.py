import json

from openai.types.beta.threads import RequiredActionFunctionToolCall
from openai.types.beta.threads.required_action_function_tool_call import Function

from komodo.shared.directory.actions_directory import get_tools_outputs
from komodo.shared.tools.web.action_scrape import SCRAPER_ACTION_NAME, scraper_action


def test_get_tools_outputs_parallel():
    tool_calls = []

    ids = ["123", "456", "789"]
    for id in ids:
        fn = Function(name=SCRAPER_ACTION_NAME, arguments=json.dumps({'url': 'https://www.google.com'}))
        call = RequiredActionFunctionToolCall(id=id, function=fn, type="function")
        tool_calls.append(call)

    print("starting")
    outputs = get_tools_outputs([], {"run_id": "12321"}, tool_calls, timeout=10)
    print("completed")

    print(outputs)


def test_scrape_file_1():
    text = scraper_action({
        "url": "https://www.accuweather.com/en/winter-weather/major-winter-storm-brewing-with-snow-ice-and-rain-to-blast-northeast/1608380"})
    print(text)
