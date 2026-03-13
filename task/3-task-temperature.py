from task.app.client import DialClient
from task.models.conversation import Conversation
from task.models.message import Message
from task.models.role import Role

DIAL_ENDPOINT = "https://ai-proxy.lab.epam.com/openai/deployments/{model}/chat/completions"
DEFAULT_SYSTEM_PROMPT = "You are an assistant who answers concisely and informatively."
USER_QUESTION = "Describe the sound that the color purple makes when it's angry."

MODEL = "gpt-4o"

TEMPERATURES = [0.0, 0.5, 1.5, 2.0]

for temp in TEMPERATURES:
    print("\n" + "#" * 108)
    print(f"# MODEL: {MODEL}  |  temperature={temp}")
    print("#" * 108)

    client = DialClient(endpoint=DIAL_ENDPOINT, deployment_name=MODEL)
    conversation = Conversation()
    conversation.add_message(Message(Role.SYSTEM, DEFAULT_SYSTEM_PROMPT))
    conversation.add_message(Message(Role.USER, USER_QUESTION))

    client.get_completion(
        messages=conversation.get_messages(),
        print_request=False,
        print_only_content=True,
        temperature=temp,
    )

# --- test the boundary — temperature=2.1 should return an API error ---
print("\n" + "#" * 108)
print(f"# MODEL: {MODEL}  |  temperature=2.1  (INVALID — expect API error)")
print("#" * 108)

try:
    client = DialClient(endpoint=DIAL_ENDPOINT, deployment_name=MODEL)
    conversation = Conversation()
    conversation.add_message(Message(Role.SYSTEM, DEFAULT_SYSTEM_PROMPT))
    conversation.add_message(Message(Role.USER, USER_QUESTION))

    client.get_completion(
        messages=conversation.get_messages(),
        print_request=False,
        print_only_content=True,
        temperature=2.1,
    )
except Exception as e:
    print(f"\n❌ API error as expected: {e}")