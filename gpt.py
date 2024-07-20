from g4f.client import Client
from g4f import Provider
from g4f import Model
from prettier import Prettier
from rich.console import Console
import click
import configparser
import os


# Configuration file with last settings of utility
config = configparser.ConfigParser(allow_no_value=True)
config.read('./config.ini')
if not os.path.exists('./config.ini'):
    config.set('DEFAULT', 'provider', None)
    config.set('DEFAULT', 'model', 'gpt-3.5-turbo')
default_provider = config.get('DEFAULT', 'provider') if config.get('DEFAULT', 'provider') else None
default_model = config.get('DEFAULT', 'model')


@click.command()
@click.option('--provider', type=click.Choice(Provider.__all__+[None]), default=default_provider)
@click.option('--model', type=click.Choice(Model.__all__()), default=default_model)
def ask_gpt(provider: str, model: str):

    # Set last settings to configuration file
    config.set('DEFAULT', 'provider', provider)
    config.set('DEFAULT', 'model', model)
    with open('./config.ini', 'w') as file:
        config.write(file)

    client = Client()
    console = Console()
    prettier = Prettier(console)
    chat_history = []
    print('^C to exit')

    while True:

        # get request to model
        answer = input('\nUSER: ')
        chat_history.append({"role": "user", "content": answer})

        # send request to model
        chat_completion = client.chat.completions.create(
                model=model,
                messages=chat_history, 
                stream=True,
                provider=provider)

        # waiting answer from model
        with console.status('Request sent.'):
            for completion in chat_completion:
                generical = completion.choices[0].delta.content
                while not generical: continue
                break

        # model output with stream
        prettier.print('**ASSISTENT**: ')
        prettier.clean()
        prettier.print(generical)
        for completion in chat_completion:
            prettier.print(completion.choices[0].delta.content or "")

        chat_history.append({"role": "assistant", "content": prettier.pretty_text})
        prettier.clean()

    
if __name__ == '__main__':
    ask_gpt()