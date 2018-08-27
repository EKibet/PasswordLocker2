import sys
from tabulate import tabulate

class FormatOutput():
    colors = {
        'success': '\033[92m',
        'warning': '\033[91m',
        'defalt': '\033[99m',
        'blue': '\033[94m',
        'fail': '\033[91m',
        'default': '\033[0m',
        'yellow': '\033[93m',
        'magenta': '\033[95m'
    }
    def __init__(self,color):
        self.color = self.colors[color]
        self.layout = self.colors['default']
    def __call__(self,text):
        print(self.color +text+self.layout)

print_s = FormatOutput('success')
print_w = FormatOutput('warning')
print_e = FormatOutput('fail')
print_d = FormatOutput('default')
print_y = FormatOutput('yellow')
input_b = FormatOutput('blue')
print_m = FormatOutput('magenta')
def banner():
    print_y(r"""
                                .- - - - .
                               / . - - -. \
                              / /        \ \
                              | |        | |
                           ___| |________| |___
                         .' |_|        |_|     '.
                         |   PASSWORD  LOCKER   |
                         '.____ ___    ____ ___.'
          
          """)