from task.app.client import DialClient
from task.models.conversation import Conversation
from task.models.message import Message
from task.models.role import Role

DIAL_ENDPOINT = "https://ai-proxy.lab.epam.com/openai/deployments/{model}/chat/completions"
DEFAULT_SYSTEM_PROMPT = "You are an assistant who answers concisely and informatively."
USER_QUESTION = "Why is the snow white?"

MODELS = [
    "gpt-4o",
    "gemini-2.0-flash",
]

for model in MODELS:
    print("\n" + "#" * 108)
    print(f"# MODEL: {model}  |  n=3")
    print("#" * 108)

    client = DialClient(endpoint=DIAL_ENDPOINT, deployment_name=model)

    conversation = Conversation()
    conversation.add_message(Message(Role.SYSTEM, DEFAULT_SYSTEM_PROMPT))
    conversation.add_message(Message(Role.USER, USER_QUESTION))

    client.get_completion(
        messages=conversation.get_messages(),
        print_request=True,
        print_only_content=False,
        n=3,  # 3 independent completions
    )
