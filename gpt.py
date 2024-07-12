from g4f.client import Client
from g4f import Provider
from g4f import Model
from prettier import Prettier
import click


@click.command()
@click.option('--answer', prompt=True, required=True)
@click.option('--provider', type=click.Choice(Provider.__all__+[None]), default=None)
@click.option('--model', type=click.Choice(Model.__all__()), default='gpt-3.5-turbo')
def ask_gpt(answer: str, provider: str, model: str):
    client = Client()
    prettier = Prettier()

    chat_completion = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": answer}], 
        stream=True,
        provider=provider)

    for completion in chat_completion:
        prettier.print(completion.choices[0].delta.content or "")

    
if __name__ == '__main__':
    ask_gpt()