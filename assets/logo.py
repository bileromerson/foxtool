import random as range
RESET = "\033[0m"
ORANGE = "\033[38;5;208m"
GRAY = "\033[38;5;240m"
PADRAO = "\033[37m"
BACKGROUND = "\033[48;5;232m"

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

num = range.randint(1, 2)  # Randomly choose between 1 and 2
def choice_logo(num):
    logo_str = 'logo' + str(num)
    logo = globals()[logo_str]
    return logo

def logo_paint(text, num):
    logo = ''
    if num == 1 or num == 2:
      for char in text:
        if char in '█▄▀':
            logo += f"{ORANGE}{char}{RESET}"
        elif char in '╝╚║═╗╔':
            logo += f"{GRAY}{char}{RESET}"
        else:
            logo += f"{PADRAO}{char}{RESET}"
    return logo

logo = logo_paint(choice_logo(num), num) + "\033[97m"

