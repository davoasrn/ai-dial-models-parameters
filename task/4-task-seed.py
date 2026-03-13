from task.app.client import DialClient
from task.models.conversation import Conversation
from task.models.message import Message
from task.models.role import Role

DIAL_ENDPOINT = "https://ai-proxy.lab.epam.com/openai/deployments/{model}/chat/completions"
DEFAULT_SYSTEM_PROMPT = "You are an assistant who answers concisely and informatively."
USER_QUESTION = "Name a random animal."

# ── n=5, NO seed ────────────────────────────────────────────────────
print("\n" + "#" * 108)
print("# MODEL: gpt-4o  |  n=5  |  NO seed  →  expect 5 different animals")
print("#" * 108)

client = DialClient(endpoint=DIAL_ENDPOINT, deployment_name="gpt-4o")
conversation = Conversation()
conversation.add_message(Message(Role.SYSTEM, DEFAULT_SYSTEM_PROMPT))
conversation.add_message(Message(Role.USER, USER_QUESTION))

client.get_completion(
    messages=conversation.get_messages(),
    print_request=False,
    print_only_content=False,  # Need full JSON to see all 5 choices[]
    n=5,
)

# ── n=5, seed=42 ────────────────────────────────────────
print("\n" + "#" * 108)
print("# MODEL: gpt-4o  |  n=5  |  seed=42  →  expect choices to converge")
print("#" * 108)

client = DialClient(endpoint=DIAL_ENDPOINT, deployment_name="gpt-4o")
conversation = Conversation()
conversation.add_message(Message(Role.SYSTEM, DEFAULT_SYSTEM_PROMPT))
conversation.add_message(Message(Role.USER, USER_QUESTION))

client.get_completion(
    messages=conversation.get_messages(),
    print_request=False,
    print_only_content=False,
    n=5,
    seed=42,
)

# ── n=5, seed=42 ─────────────
print("\n" + "#" * 108)
print("# MODEL: gpt-4o  |  n=5  |  seed=42  →  re-run: should match Round 2")
print("#" * 108)

client = DialClient(endpoint=DIAL_ENDPOINT, deployment_name="gpt-4o")
conversation = Conversation()
conversation.add_message(Message(Role.SYSTEM, DEFAULT_SYSTEM_PROMPT))
conversation.add_message(Message(Role.USER, USER_QUESTION))

client.get_completion(
    messages=conversation.get_messages(),
    print_request=False,
    print_only_content=False,
    n=5,
    seed=42,
)

# ── gemini  ───────────────────────────────
print("\n" + "#" * 108)
print("# MODEL: gemini-2.0-flash  |  n=5  |  seed=42  →  seed ignored, expect variety")
print("#" * 108)

client = DialClient(endpoint=DIAL_ENDPOINT, deployment_name="gemini-2.0-flash")
conversation = Conversation()
conversation.add_message(Message(Role.SYSTEM, DEFAULT_SYSTEM_PROMPT))
conversation.add_message(Message(Role.USER, USER_QUESTION))

client.get_completion(
    messages=conversation.get_messages(),
    print_request=False,
    print_only_content=False,
    n=5,
    seed=42,
)