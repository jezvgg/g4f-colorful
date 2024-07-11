from rich.syntax import Syntax
from rich.console import Console


class Prettier:
    pretty_text = ''
    other_text = ''
    console = Console()


    def __init__(self):
        pass


    def get_text(self, text):
        self.other_text += text


    def make_text(self):
        
        text = self.other_text.replace(self.pretty_text, '')
        
        text_blocks = text.split('```')
        text_output = []

        for i,text_block in enumerate(text_blocks):
            if i%2 != 0:
                # Обработка синтаксиса языка
                language = text_block.split('\n')[0]
                programm = '\n'.join(text_block.split('\n')[1:-1])
                syntax = Syntax(programm, language, line_numbers=True, background_color='#272727')
                self.console.print(syntax)
                text_output.append(syntax)
                self.pretty_text += text_block

            if i%2==0:
                while text_block.count('**') % 2 == 0 and '**' in text_block:
                    text_block = text_block.replace('**', '[b]', 1)
                    text_block = text_block.replace('**', '[/b]', 1)
                
                while text_block.count('*') % 2 == 0 and '*' in text_block:
                    text_block = text_block.replace('*', '[i]', 1)
                    text_block = text_block.replace('*', '[/i]', 1)

                self.console.print(text_block, style='blue')
                text_output.append(text_block)
                self.pretty_text += text_block

        return text_output

        

if __name__ == '__main__':
    prettier = Prettier()
    prettier.get_text('''
    **Привет**, вот тебе какой-то *код*!
    ```python
    print('Hello world!')
    ```
    ''')

    prettier.make_text()


    