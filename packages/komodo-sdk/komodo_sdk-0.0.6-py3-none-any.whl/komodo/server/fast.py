from typing import AsyncGenerator

from fastapi import FastAPI, Header, Depends
from fastapi import HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import StreamingResponse

from komodo.framework.komodo_app import KomodoApp
from komodo.loaders.user_loader import UserLoader
from komodo.models.framework.runners import run_appliance

app = FastAPI()
g_appliance: KomodoApp = KomodoApp(name="Placeholder", shortcode="placeholder",
                                   purpose="Placeholder")  # Replace with the actual appliance object


def get_appliance():
    if not g_appliance:
        raise HTTPException(status_code=404, detail="Appliance not found")
    return g_appliance


def set_appliance_for_fastapi(appliance):
    global g_appliance
    g_appliance = appliance


origins = ["http://localhost:3000", ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],  # Add other methods as needed
    allow_headers=["X-Requested-With", "Content-Type"],
)


def get_email_from_header(x_user_email: str = Header(None)):
    if x_user_email is None:
        raise HTTPException(status_code=400, detail="X-User-Email header missing")
    print("X-User-Email: ", x_user_email)
    user = UserLoader.load(x_user_email)
    if not user:
        raise HTTPException(status_code=401, detail="User not found: " + x_user_email)
    return x_user_email


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {'message': "Welcome to Komodoo AI Appliance: " + g_appliance.name}


@app.get("/api")
async def api_root() -> dict:
    return {"hello": "This is the root of the API. Use /api/v1 to access the API"}


@app.get("/api/v1/user-profile")
async def get_user_profile(email: str = Depends(get_email_from_header)):
    user = UserLoader.load(email)
    return user.to_dict()


@app.get('/api/v1/appliance')
def read_appliance(appliance=Depends(get_appliance)):
    if not appliance:
        raise HTTPException(status_code=404, detail="Appliance not found")

    # Convert the protobuf Appliance object to a dictionary for JSON response
    appliance_dict = {
        "shortcode": 'sample',
        "name": appliance['name'],
        "purpose": appliance['purpose'],
    }

    return appliance_dict


@app.get('/api/v1/appliance/list')
def list_agents(appliance=Depends(get_appliance)):
    return {"agents": [a.to_dict() for a in appliance.agents]}


@app.get('/api/v1/agents')
def read_agents(appliance=Depends(get_appliance)):
    return [a.to_dict() for a in appliance.agents]


@app.api_route('/api/v1/agent/ask', methods=['GET', 'POST'])
def ask_agent(appliance=Depends(get_appliance)):
    message = "how are you doing today"
    reply = run_appliance(appliance, message)
    return {"reply": reply.text, "message": message}


@app.get("/api/v1/ask-streamed")
async def enhance_prompt_streamed(email: str, prompt: str):
    print("email: ", email, "prompt: ", prompt)
    return StreamingResponse(komodo_async_generator(email, prompt), media_type='text/event-stream')


async def komodo_async_generator(email: str, prompt: str) -> AsyncGenerator[str, None]:
    user = UserLoader.load(email)
    for part in []:  # komodo.stream_response(prompt=prompt):
        try:
            yield f"data: {part}\n\n"
        except Exception as e:
            print(e)
            return  # this will close the connection

    print("stream complete")
    yield "event: stream-complete\ndata: {}\n\n"


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)  # noinspection PyTypeChecker
