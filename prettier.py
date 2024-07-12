from rich.syntax import Syntax
from rich.console import Console


class Prettier:
    pretty_text = ''
    other_text = ''
    console = Console()


    def __init__(self):
        pass


    def get_text(self, text):
        # print('aded',text)
        self.other_text += text


    def make_text(self):
        
        text = self.other_text.replace(self.pretty_text, '')
        # print('texts', text)
        
        text_blocks = text.split('```')
        text_output = []

        # print(text)
        
        if text.count('```') % 2 != 0 or text.count('*') % 2 != 0 or text.count('**') % 2 != 0:
            return ''

        for i,text_block in enumerate(text_blocks):
            if i%2 != 0:
                # Обработка синтаксиса языка
                language = text_block.split('\n')[0]
                programm = '\n'.join(text_block.split('\n')[1:-1])
                # print(programm, language)
                syntax = Syntax(programm, language, line_numbers=False, background_color='#272727')
                self.pretty_text += '```'+text_block+'```'
                self.console.print('\n',syntax)
                text_output.append(syntax)

            if i%2==0:
                text_block_copy = text_block[:]
                while text_block_copy.count('**') % 2 == 0 and '**' in text_block_copy:
                    text_block_copy = text_block_copy.replace('**', '[b]', 1)
                    text_block_copy = text_block_copy.replace('**', '[/b]', 1)
                
                while text_block_copy.count('*') % 2 == 0 and '*' in text_block_copy:
                    text_block_copy = text_block_copy.replace('*', '[i]', 1)
                    text_block_copy = text_block_copy.replace('*', '[/i]', 1)

                self.pretty_text += text_block
                self.console.print(text_block_copy, style='blue', end='')
                text_output.append(text_block_copy)

        return text_output


    def print(self, text):
        self.get_text(text)
        return self.make_text()

        

if __name__ == '__main__':
    prettier = Prettier()
    prettier.get_text('''
    **Привет**, вот тебе какой-то *код*!
    ```python
    print('Hello world!')
    ```
    ''')

    prettier.make_text()


    