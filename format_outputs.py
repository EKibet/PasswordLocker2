import sys
from tabulate import tabulate

class FormatOutput():
    colors = {
        'success': '\033[92m',
        'warning': '\033[91m',
        'default': '\033[99m',
        'blue': '\033[94m',
        'fail': '\033[91m',
        'end': '\033[0m',
        'yellow': '\033[93m',
        'magenta': '\033[95m'
    }
    def __init__(self,color):
        self.color = Format.colors[color]
        self.layout = self.colors['default']
    def __call__(self,text):
        print(self.color +text+self.layout)