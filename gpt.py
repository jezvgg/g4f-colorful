from g4f.client import Client
from g4f import Provider
from g4f import Model
from prettier import Prettier
from rich.console import Console
import click
import configparser


config = configparser.ConfigParser(allow_no_value=True)
config.read('./config.ini')
default_provider = config.get('DEFAULT', 'provider') if config.get('DEFAULT', 'provider') else None
default_model = config.get('DEFAULT', 'model')


@click.command()
@click.option('--answer', prompt=True, required=True)
@click.option('--provider', type=click.Choice(Provider.__all__+[None]), default=default_provider)
@click.option('--model', type=click.Choice(Model.__all__()), default=default_model)
def ask_gpt(answer: str, provider: str, model: str):

    config.set('DEFAULT', 'provider', provider)
    config.set('DEFAULT', 'model', model)
    with open('./config.ini', 'w') as file:
        config.write(file)

    client = Client()
    console = Console()
    prettier = Prettier(console)

    chat_completion = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": answer}], 
            stream=True,
            provider=provider)

    with console.status('Запрос отправлен.'):
        for completion in chat_completion:
            generical = completion.choices[0].delta.content
            while not generical: continue
            break

    prettier.print(generical)
    for completion in chat_completion:
        prettier.print(completion.choices[0].delta.content or "")

    
if __name__ == '__main__':
    ask_gpt()