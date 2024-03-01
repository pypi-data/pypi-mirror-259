from typing import AsyncGenerator
from datetime import datetime
import uuid

from komodo.proto.model_pb2 import Conversation, Message, Mode
from komodo.store.conversations_store import ConversationStore

from fastapi import Depends, APIRouter, HTTPException, Request
from starlette.responses import StreamingResponse

from komodo.models.framework.runners import run_appliance, run_agent
from komodo.server.globals import get_appliance

router = APIRouter(
    prefix='/api/v1/agent',
    tags=['Agent']
)


@router.api_route('/ask', methods=['POST'])
async def ask_agent(request: Request, appliance=Depends(get_appliance)):
    # Extract the email from the request headers
    email = request.headers.get('X-User-Email')
    if not email:
        # If the email header is not provided or is empty, return an error response
        raise HTTPException(status_code=400, detail="Missing 'X-User-Email' in request headers")
    
    # Parse the request body as JSON
    body = await request.json()
    # Extract the message and agent_info fields from the JSON body
    message = body.get("message")
    agent = body.get("agent_info")
    if not message:
        # If the message is not provided, return an error response
        raise HTTPException(status_code=400, detail="Missing 'message' in request body")
    
    # Here you would run your agent with the provided message and agent information
    reply = run_agent(agent, message)

    # Create a Conversation object and populate it
    now = datetime.utcnow().isoformat() + 'Z'  # Format the timestamp in ISO 8601
    agent_shortcode = agent['shortcode']
    conversation = Conversation(
        user_email=email,
        agent_shortcode=agent_shortcode,
        messages=[
            Message(guid=str(uuid.uuid4()), sender=email, text=message, created_at=now),
            Message(guid=str(uuid.uuid4()), sender=agent_shortcode, text=reply.text, created_at=now)
        ]
    )

    # Store the conversation in Redis
    conversation_store = ConversationStore()
    conversation_store.add_conversation(email, agent_shortcode, conversation)
    
    return {"reply": reply.text, "message": message}


@router.get("/ask-streamed")
async def ask_agent_streamed(email: str, prompt: str):
    print("email: ", email, "prompt: ", prompt)
    return StreamingResponse(komodo_async_generator(email, prompt), media_type='text/event-stream')


async def komodo_async_generator(email: str, prompt: str) -> AsyncGenerator[str, None]:
    for part in ["This", "is", "still", "to", "be", "implemented"]:  # komodo.stream_response(prompt=prompt):
        try:
            yield f"data: {part}\n\n"
        except Exception as e:
            print(e)
            return  # this will close the connection

    print("stream complete")
    yield "event: stream-complete\ndata: {}\n\n"
