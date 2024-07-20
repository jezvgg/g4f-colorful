from rich.syntax import Syntax
from rich.console import Console


class Prettier:
    pretty_text = ''
    other_text = ''
    console: Console


    def __init__(self, console: Console):
        self.console = console


    def get_text(self, text):
        '''
        Get new text to pretty.
        '''
        self.other_text += text


    def clean(self):
        '''
        Clean all text data.
        '''
        self.pretty_text = ''
        self.other_text = ''


    def make_text(self):
        '''
        Making text with rich, based on not prettied text.
        '''
        
        text = self.other_text.replace(self.pretty_text, '')
        
        # text blocks with code we need to pretty separately
        text_blocks = text.split('```')
        text_output = []
        
        if text.count('```') % 2 != 0 or text.count('*') % 2 != 0 or text.count('**') % 2 != 0:
            return ''

        for i,text_block in enumerate(text_blocks):
            if i%2 != 0:
                language = text_block.split('\n')[0] # get syntax of language
                programm = '\n'.join(text_block.split('\n')[1:-1]) # get programm without syntax
                syntax = Syntax(programm, language, line_numbers=False, background_color='#272727')
                self.pretty_text += '```'+text_block+'```'
                self.console.print('\n',syntax)
                text_output.append(syntax)

            if i%2==0:
                # create bold and italic fonts, where ** and *
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
        '''
        shortcut to use get_text and make_text
        '''
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


    