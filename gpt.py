from g4f.client import Client
from g4f import Provider
from prettier import Prettier

client = Client()
prettier = Prettier()

chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Привет, как работать с json на Python?"}], 
    stream=True,
    provider=Provider.You)

for completion in chat_completion:
    prettier.get_text(completion.choices[0].delta.content or "")
    prettier.make_text()

