from task.app.client import DialClient
from task.models.conversation import Conversation
from task.models.message import Message
from task.models.role import Role

# HINT: All available models you can find here: https://ai-proxy.lab.epam.com/openai/models

# The main goal of this task is to explore the functional capabilities of DIAL to be able to work with different
# LLMs through unified API.
#
# We call the SAME question to 3 different models (OpenAI, Anthropic, Google) through the
# SAME DIAL endpoint, and compare how each model responds.
# This demonstrates the "unified API" concept — one interface, many backends.

DIAL_ENDPOINT = "https://ai-proxy.lab.epam.com/openai/deployments/{model}/chat/completions"
DEFAULT_SYSTEM_PROMPT = "You are an assistant who answers concisely and informatively."
USER_QUESTION = "What LLMs can do?"

MODELS = [
    "gpt-4o",                        # OpenAI
    "gpt-4.1-nano-2025-04-14",     # OpenAI lightweight
    "gemini-2.0-flash",              # Google  (gemini-2.5-pro requires higher access tier)
]

for model in MODELS:
    print("\n" + "#" * 108)
    print(f"# MODEL: {model}")
    print("#" * 108)

    client = DialClient(endpoint=DIAL_ENDPOINT, deployment_name=model)

    conversation = Conversation()
    conversation.add_message(Message(Role.SYSTEM, DEFAULT_SYSTEM_PROMPT))
    conversation.add_message(Message(Role.USER, USER_QUESTION))

    client.get_completion(
        messages=conversation.get_messages(),
        print_request=True,       # Show the outgoing request so we can see the endpoint + body
        print_only_content=True,  # Show only the text response (not the full JSON) for easy comparison
    )