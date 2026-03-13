from task.app.client import DialClient
from task.models.conversation import Conversation
from task.models.message import Message
from task.models.role import Role

DIAL_ENDPOINT = "https://ai-proxy.lab.epam.com/openai/deployments/{model}/chat/completions"
DEFAULT_SYSTEM_PROMPT = "You are an assistant who answers concisely and informatively."
USER_QUESTION = "Explain the key components of a Large Language Model architecture."

MODEL = "gpt-4o"

# ── Round 1: No stop — full baseline response ─────────────────────────────────
print("\n" + "#" * 108)
print("# Round 1 — No stop  →  full response, see all section headers")
print("#" * 108)
client = DialClient(endpoint=DIAL_ENDPOINT, deployment_name=MODEL)
conv = Conversation()
conv.add_message(Message(Role.SYSTEM, DEFAULT_SYSTEM_PROMPT))
conv.add_message(Message(Role.USER, USER_QUESTION))
client.get_completion(messages=conv.get_messages(), print_request=False, print_only_content=True)

# ── Round 2: stop="\n\n" — halt at the first blank line ──────────────────────
print("\n" + "#" * 108)
print('# Round 2 — stop="\\n\\n"  →  halts at the first paragraph break')
print("#" * 108)
client = DialClient(endpoint=DIAL_ENDPOINT, deployment_name=MODEL)
conv = Conversation()
conv.add_message(Message(Role.SYSTEM, DEFAULT_SYSTEM_PROMPT))
conv.add_message(Message(Role.USER, USER_QUESTION))
client.get_completion(
    messages=conv.get_messages(),
    print_request=False,
    print_only_content=False, 
    stop="\n\n",
)

# ── Round 3: stop list — halt when a specific section header appears ──────────
print("\n" + "#" * 108)
print('# Round 3 — stop=["**Transformer Blocks**"]  →  list starts, never reaches that section')
print("#" * 108)
client = DialClient(endpoint=DIAL_ENDPOINT, deployment_name=MODEL)
conv = Conversation()
conv.add_message(Message(Role.SYSTEM, DEFAULT_SYSTEM_PROMPT))
conv.add_message(Message(Role.USER, USER_QUESTION))
client.get_completion(
    messages=conv.get_messages(),
    print_request=False,
    print_only_content=False,
    stop=["**Transformer Blocks**", "**Transformer Block**"],
)

# ── Round 4: guardrail demo — silently block competitor praise ────────────────
print("\n" + "#" * 108)
print('# Round 4 — Guardrail demo: stop competitor praise, finish_reason still "stop"')
print("#" * 108)
client = DialClient(endpoint=DIAL_ENDPOINT, deployment_name=MODEL)
conv = Conversation()
conv.add_message(Message(Role.SYSTEM, DEFAULT_SYSTEM_PROMPT))
conv.add_message(Message(Role.USER, "Compare Apple and Pear smartphones. Which is better?"))
client.get_completion(
    messages=conv.get_messages(),
    print_request=False,
    print_only_content=False,
    stop=["Apple is", "Apple has the best", "Apple leads"],
)