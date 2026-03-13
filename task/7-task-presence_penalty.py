from task.app.client import DialClient
from task.models.conversation import Conversation
from task.models.message import Message
from task.models.role import Role


DIAL_ENDPOINT = "https://ai-proxy.lab.epam.com/openai/deployments/{model}/chat/completions"
DEFAULT_SYSTEM_PROMPT = "You are an assistant who answers concisely and informatively."
USER_QUESTION = "What is entropy in LLM responses?"

MODEL = "gpt-4o"
PENALTIES = [-2.0, 0.0, 1.0, 2.0]

for penalty in PENALTIES:
    print("\n" + "#" * 108)
    print(f"# MODEL: {MODEL}  |  presence_penalty={penalty}")
    print("#" * 108)

    client = DialClient(endpoint=DIAL_ENDPOINT, deployment_name=MODEL)
    conversation = Conversation()
    conversation.add_message(Message(Role.SYSTEM, DEFAULT_SYSTEM_PROMPT))
    conversation.add_message(Message(Role.USER, USER_QUESTION))

    client.get_completion(
        messages=conversation.get_messages(),
        print_request=False,
        print_only_content=True,
        presence_penalty=penalty,
    )