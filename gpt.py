from g4f.client import Client
from g4f import Provider
from prettier import Prettier

client = Client()
prettier = Prettier()

response = client.chat.completions.create(
   model="gpt-3.5-turbo",
   messages=[{"role": "user", "content": "Объясни как работать с json в Python"}],
   provider=Provider.ChatgptFree
)

prettier.get_text(response.choices[0].message.content)
prettier.make_text()
# print(response)
# print(response.choices[0])
# print(response.choices[0].message)
# print(response.choices[0].message.content)

