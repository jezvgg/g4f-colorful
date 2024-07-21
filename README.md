# colorful-g4f

> Linux utility to use [gpt4free](https://github.com/xtekky/gpt4free) in console with colorfull and usefull interface

## Why you need it?
Currently, the use of text assistants like ChatGPT is extremely important and useful. They provide us with instant access to information, saving our time and simplifying the process of finding the answers we need. I often use a text assistant to perform various tasks, such as writing emails, making to-do lists, or even creating blog content. It has become an indispensable tool in my daily life.

And many programmers, that use linux, like to use console. But many of assistents are avaiable only at his websites. [Gpt4free](https://github.com/xtekky/gpt4free) solve this problem and gains API to many chat assiatents. My utility only creates an interface for convenient use of it.

But you can use many of model, like: chatgpt, gpt4, LLAMA3 e.t.c.
The utility saves context and gives you access to swap providers and models. The utility saves your last option, so you don't need to set the provider every time.

Example of use:
![image](https://github.com/user-attachments/assets/28ae19a5-ede1-42b2-bd9a-f9ef4a77cc48)


## How to install?
You need to be installed [python](https://www.python.org) and [rich](https://rich.readthedocs.io/en/stable/introduction.html), [g4f](https://pypi.org/project/g4f/).
Then just enter this commands:

    git clone https://github.com/jezvgg/g4f-colorful.git
    cd g4f-colorful
    pip install --editable .
All Done! How you can use it!

## How to use it
Basic command

    gpt
Activate chat assistent with last settings.

You can also choice assistent and provider, example:

    gpt --provider=You --model=gpt4
