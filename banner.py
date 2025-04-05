# banner.py
from rich.console import Console
from rich.text import Text
from time import sleep

console = Console()

fsociety_ascii = r'''
               _.-^^---....,,--       
           _--                  —-_
          <                        >)
          |                         | 
           \._                   _./  
              ```--. . , ; .--'''       
                    | |   |             
                 .-=||  | |=-.   
                 `-=#$%&%$#=-'   
                    | ;  :|     
           _____.,-#%&$@%#&#~,._____
           
             ███████╗███████╗ ██████╗ ██████╗  ██████╗ ██╗   ██╗████████╗██╗
             ██╔════╝██╔════╝██╔════╝ ██╔══██╗██╔═══██╗██║   ██║╚══██╔══╝██║
             █████╗  ███████╗██║  ███╗██████╔╝██║   ██║██║   ██║   ██║   ██║
             ██╔══╝  ╚════██║██║   ██║██╔═══╝ ██║   ██║██║   ██║   ██║   ╚═╝
             ███████╗███████║╚██████╔╝██║     ╚██████╔╝╚██████╔╝   ██║   ██╗
             ╚══════╝╚══════╝ ╚═════╝ ╚═╝      ╚═════╝  ╚═════╝    ╚═╝   ╚═╝
                          Inspired by Mr. Robot × Watch Dogs 2
'''

def show_banner():
    text = Text(fsociety_ascii)
    text.stylize("bold purple", 0, 400)
    text.stylize("bold yellow", 400, len(text))
    console.print(text)
    sleep(1)

if __name__ == "__main__":
    show_banner()
