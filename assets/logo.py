import random as range
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.color import reset, reset, orange, gray

logo1 = """
                                 ██▄              ▄██   
                                 ████▄          ▄████   
                                 ██████▄      ▄██████   
                                ▄████████████████████▄  
                              ▄████    ████████    ████▄
                              ██████████████████████████
                              ▀██████████    ██████████▀
                                ▀████████████████████▀   
"""

logo2 = """
            ███████╗ ██████╗ ██╗   ██╗████████╗ ██████╗  ██████╗ ██╗      
            ██╔════╝██╔═══██╗ ██║ ██╔╝╚══██╔══╝██╔═══██╗██║   ██╗██║      
            █████╗  ██║   ██║ █████╔╝    ██║   ██║   ██║██║   ██║██║      
            ██╔══╝  ██║   ██║██╔═██╚╗    ██║   ██║   ██║██║   ██║██║      
            ██║     ╚██████╔╝██║  ██║    ██║    ██████╔╝ ██████╔╝ ███████╗
            ╚═╝      ╚═════╝ ╚═╝  ╚═╝    ╚═╝    ╚═════╝   ╚════╝  ╚══════╝
"""

num = range.randint(1, 2)
def choice_logo(num):
    logo_str = 'logo' + str(num)
    logo_str = globals()[logo_str]
    return logo_str

logo_str = choice_logo(num)

def paint_logo(logo_str,num):
    logo = ''
    if num ==1:
        logo = f'''{orange}{logo_str}{reset}'''
    elif num ==2:
        for char in logo_str:
            if char in '╚╝║╔═╗':
                logo += f'{gray}{char}'
            else:
                logo += f'{orange}{char}'

    return logo
logo = paint_logo(logo_str,num)