from task.app.client import DialClient
from task.models.conversation import Conversation
from task.models.message import Message
from task.models.role import Role

DIAL_ENDPOINT = "https://ai-proxy.lab.epam.com/openai/deployments/{model}/chat/completions"
DEFAULT_SYSTEM_PROMPT = "You are an assistant who answers concisely and informatively."
USER_QUESTION = "What is a token when working with LLMs?"

MODEL = "gpt-4o"

MAX_TOKENS_VALUES = [10, 50, 500]

for max_tokens in MAX_TOKENS_VALUES:
    print("\n" + "#" * 108)
    print(f"# MODEL: {MODEL}  |  max_tokens={max_tokens}")
    print("#" * 108)

    client = DialClient(endpoint=DIAL_ENDPOINT, deployment_name=MODEL)
    conversation = Conversation()
    conversation.add_message(Message(Role.SYSTEM, DEFAULT_SYSTEM_PROMPT))
    conversation.add_message(Message(Role.USER, USER_QUESTION))

    client.get_completion(
        messages=conversation.get_messages(),
        print_request=False,
        print_only_content=False,
        max_tokens=max_tokens,
    )