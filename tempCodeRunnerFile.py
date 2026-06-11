import shutil
from colorama import Fore, Back, Style, init

init(autoreset=True)

# PEGA A LARGURA DO TERMINAL E SUBTRAI 2 (O PRINT DO MENU BUGA USANDO A LARGURA COMPLETA)
larguraTerminal = (shutil.get_terminal_size().columns - 2) 

menu = Fore.YELLOW + '''
________                                             _________            .___    ._.
\______ \  __ __  ____    ____   ____  ____   ____   \_   ___ \  ____   __| _/____| |
 |    |  \|  |  \/    \  / ___\_/ __ \/  _ \ /    \  /    \  \/ /  _ \ / __ |/ __ \ |
 |    `   \  |  /   |  \/ /_/  >  ___(  <_> )   |  \ \     \___(  <_> ) /_/ \  ___/\|
/_______  /____/|___|  /\___  / \___  >____/|___|  /  \______  /\____/\____ |\___  >_
        \/           \//_____/      \/           \/          \/            \/    \/\/
      

  ___      _    _          
 |_ _|_ _ (_)__(_)__ _ _ _ 
  | || ' \| / _| / _` | '_|
 |___|_||_|_\__|_\__,_|_|  
                           
  ___       _     
 / __| __ _(_)_ _ 
 \__ \/ _` | | '_|
 |___/\__,_|_|_|  
                  
'''

# DESENHA O MENU, CENTRALIZANDO CADA LINHA INDIVIDUALMENTE DE ACORDO COM A LARGURA DO TERMINAL
for linha in menu.splitlines():
    print(linha.center(larguraTerminal))