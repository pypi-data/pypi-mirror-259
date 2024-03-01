from fastapi import APIRouter, HTTPException, Depends
from komodo.proto.model_pb2 import Conversation
from komodo.store.conversations_store import ConversationStore
from typing import List
import json
from google.protobuf.json_format import MessageToJson

conversation_store = ConversationStore()

router = APIRouter(
    prefix='/api/v1/conversation',
    tags=['Conversation']
)

@router.get('/{user_email}/{agent_shortcode}')
async def get_conversations(user_email: str, agent_shortcode: str):
    conversation_store = ConversationStore()
    conversations = conversation_store.retrieve_conversations(user_email, agent_shortcode)

    if not conversations:
        raise HTTPException(status_code=404, detail="Conversations not found")

    # Convert protobuf conversations to JSON and then parse them into dictionaries
    conversations_dicts = [json.loads(MessageToJson(conversation)) for conversation in conversations]

    # Return the list of dictionaries. FastAPI will serialize this into JSON.
    return conversations_dicts
