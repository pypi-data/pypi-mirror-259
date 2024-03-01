from komodo.proto.model_pb2 import Conversation
from komodo.store.redis_database import RedisDatabase, get_redis_server

class ConversationStore:
    def __init__(self, database=RedisDatabase.CONVERSATIONS):
        self.redis = get_redis_server(database)

    def add_conversation(self, user_email, agent_id, conversation):
        # Construct the key using the user's email and the agent identifier
        key = f"user:{user_email}:agent:{agent_id}"
        # Serialize the Conversation object to a binary string
        conversation_data = conversation.SerializeToString()
        # Push the serialized data to a Redis list associated with the key
        self.redis.rpush(key, conversation_data)

    def retrieve_conversations(self, user_email, agent_id):
        key = f"user:{user_email}:agent:{agent_id}"
        # Retrieve all serialized Conversation objects from the list associated with the key
        serialized_conversations = self.redis.lrange(key, 0, -1)
        conversations = []
        for serialized_conversation in serialized_conversations:
            # Deserialize each Conversation object
            conversation = Conversation()
            conversation.ParseFromString(serialized_conversation)
            conversations.append(conversation)
        return conversations

    def remove_conversations(self, user_email, agent_id):
        key = f"user:{user_email}:agent:{agent_id}"
        self.redis.delete(key)
