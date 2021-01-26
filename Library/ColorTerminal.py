class ColorTerminal:
    """
        Library works only on linux.
        My first library
        Lucas Mendes Barbosa
        Github: Mendes1302
    """
    def __init__(self):
        self.reset = '\033[0;0m'
        self.color = {
            'red': '\033[31m',
            'green': '\033[32m',
            'blue': '\033[34m',
            'cyan': '\033[36m',
            'pink': '\033[35m',
            'yellow': '\033[33m',
            'black': '\033[30m',
            'white': '\033[37m'
        }

        self.style = {
            'bold': '\033[1m',
            'reverse': '\033[2m'
        }

        self.background = {
            'black': '\033[40m',
            'red': '\033[41m',
            'green': '\033[42m',
            'yellow': '\033[43m',
            'blue': '\033[44m',
            'pink': '\033[45m',
            'cyan': '\033[46m',
            'white': '\033[47m'
        }


    def text_style(self, txt, style, return_var=0):
        """
            Choose the style of the terminal:

            Parameters: 
                txt (str): Text for be modified.
                style (str): The chosen style [bold/reverse].
                return_var (int): 0 False 1 True

            Returns:
                str: Modified text.
        """

        if return_var:
            return self.style[style.lower()]+"\b"+txt+self.reset
        else:
            print(self.style[style.lower()], "\b"+txt, self.reset)
    

    def text_color(self, txt, color, return_var=0):
        """
            Choose the color of the terminal:

            Parameters:
                txt (str): Text for be modified.
                style (str): The chosen color [black/red/green/blue/pink/cyan/yellow/white].

            Returns:
                str: Modified text.
        """
        if return_var:
            return self.color[color.lower()]+"\b"+txt+self.reset
        else:
            print(self.color[color.lower()], "\b"+txt, self.reset)
    

    def text_background(self, txt, background, return_var=0):
        """
            Choose the blackground of the terminal:

            Parameters:
                txt (str): Text for be modified.
                style (str): The chosen blackground [black/red/green/blue/pink/cyan/yellow/white].

            Returns:
                str: Modified text.
        """
        if return_var:
            return self.background[background.lower()]+'\b'+txt+self.reset
        else:
            print(self.background[background.lower()], "\b"+txt, self.reset)


    def text_error(self, txt, return_var=0):
        if return_var:
            return self.color['red']+"\b"+txt+self.reset
        else:
            print(self.color['red'], "\b"+txt, self.reset)
    

    def text_info(self, txt, return_var=0):
        if return_var:
            return self.color['green']+"\b"+txt+self.reset
        else:
            print(self.color['green'], "\b"+txt, self.reset)


    def text_warning(self, txt, return_var=0):
        if return_var:
            return self.color['yellow']+"\b"+txt+self.reset
        else:
            print(self.color['yellow'], "\b"+txt, self.reset)
