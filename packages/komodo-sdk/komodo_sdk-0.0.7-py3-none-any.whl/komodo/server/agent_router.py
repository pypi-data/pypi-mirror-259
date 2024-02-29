from typing import AsyncGenerator

from fastapi import Depends, APIRouter
from starlette.responses import StreamingResponse

from komodo.loaders.user_loader import UserLoader
from komodo.models.framework.runners import run_appliance
from komodo.server.globals import get_appliance

router = APIRouter(
    prefix='/api/v1/agent',
    tags=['Agent']
)


@router.api_route('/ask', methods=['GET', 'POST'])
def ask_agent(appliance=Depends(get_appliance)):
    message = "how are you doing today"
    reply = run_appliance(appliance, message)
    return {"reply": reply.text, "message": message}


@router.get("/ask-streamed")
async def enhance_prompt_streamed(email: str, prompt: str):
    print("email: ", email, "prompt: ", prompt)
    return StreamingResponse(komodo_async_generator(email, prompt), media_type='text/event-stream')


async def komodo_async_generator(email: str, prompt: str) -> AsyncGenerator[str, None]:
    user = UserLoader.load(email)
    for part in ["This", "is", "still", "to", "be", "implemented"]:  # komodo.stream_response(prompt=prompt):
        try:
            yield f"data: {part}\n\n"
        except Exception as e:
            print(e)
            return  # this will close the connection

    print("stream complete")
    yield "event: stream-complete\ndata: {}\n\n"
