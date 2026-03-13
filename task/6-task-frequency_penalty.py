from task.app.client import DialClient
from task.models.conversation import Conversation
from task.models.message import Message
from task.models.role import Role

DIAL_ENDPOINT = "https://ai-proxy.lab.epam.com/openai/deployments/{model}/chat/completions"
DEFAULT_SYSTEM_PROMPT = "You are an assistant who answers concisely and informatively."
USER_QUESTION = "Explain the water cycle in simple terms for children."

MODEL = "gpt-4o"

PENALTIES = [
    (-2.0, 300),   
    ( 0.0, None),  
    ( 1.0, None),  
    ( 2.0, None),  
]

for penalty, max_tok in PENALTIES:
    print("\n" + "#" * 108)
    label = f"max_tokens={max_tok}" if max_tok else "no max_tokens cap"
    print(f"# MODEL: {MODEL}  |  frequency_penalty={penalty}  |  {label}")
    print("#" * 108)

    client = DialClient(endpoint=DIAL_ENDPOINT, deployment_name=MODEL)
    conversation = Conversation()
    conversation.add_message(Message(Role.SYSTEM, DEFAULT_SYSTEM_PROMPT))
    conversation.add_message(Message(Role.USER, USER_QUESTION))

    kwargs = dict(
        print_request=False,
        print_only_content=True,   
    )
    if max_tok:
        kwargs["max_tokens"] = max_tok

    client.get_completion(messages=conversation.get_messages(), **kwargs)