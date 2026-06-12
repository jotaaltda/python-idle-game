import shutil, keyboard, os, sys
from colorama import Fore, Back, Style, init

init(autoreset=True)

# VARIÁVEIS GLOBAIS ====
opcao_escolhida = '' 
# ======================

menu = '''
________                                             _________            .___    ._.
\______ \  __ __  ____    ____   ____  ____   ____   \_   ___ \  ____   __| _/____| |
 |    |  \|  |  \/    \  / ___\_/ __ \/  _ \ /    \  /    \  \/ /  _ \ / __ |/ __ \ |
 |    `   \  |  /   |  \/ /_/  >  ___(  <_> )   |  \ \     \___(  <_> ) /_/ \  ___/\|
/_______  /____/|___|  /\___  / \___  >____/|___|  /  \______  /\____/\____ |\___  >_
        \/           \//_____/      \/           \/          \/            \/    \/\/
'''      

opcao_iniciar = '''
  ___      _    _          
 |_ _|_ _ (_)__(_)__ _ _ _ 
  | || ' \| / _| / _` | '_|
 |___|_||_|_\__|_\__,_|_|  
'''

opcao_sair = '''
  ___       _     
 / __| __ _(_)_ _ 
 \__ \/ _` | | '_|
 |___/\__,_|_|_|  
'''
 
creditos = '''
 por ~
 ig: @jotaltda
 git: jotaaltda
                  
'''

while True:

    os.system("cls")

    # PEGA A LARGURA DO TERMINAL E SUBTRAI 2 (O PRINT DO MENU BUGA USANDO A LARGURA COMPLETA)
    largura_terminal = (shutil.get_terminal_size().columns - 2)

    if keyboard.is_pressed('down'):
        opcao_escolhida = 'sair'
    elif keyboard.is_pressed('up'):
        opcao_escolhida = 'iniciar'
    
    # DESENHA O MENU, CENTRALIZANDO CADA LINHA INDIVIDUALMENTE DE ACORDO COM A LARGURA DO TERMINAL
    for linha in menu.splitlines():
        print(Fore.YELLOW + linha.center(largura_terminal))

    if opcao_escolhida == 'iniciar' or opcao_escolhida == '':
        for linha in opcao_iniciar.splitlines():
            print(Fore.GREEN + linha.center(largura_terminal))
    else:
        for linha in opcao_iniciar.splitlines():
            print(Fore.YELLOW + linha.center(largura_terminal))

    if opcao_escolhida == 'sair':
        for linha in opcao_sair.splitlines():
            print(Fore.GREEN + linha.center(largura_terminal))
    else:
        for linha in opcao_sair.splitlines():
            print(Fore.YELLOW + linha.center(largura_terminal))

    for linha in creditos.splitlines():
        print(Fore.YELLOW + linha.center(largura_terminal))

    if keyboard.is_pressed('enter'):
        if opcao_escolhida == 'iniciar':
            ...
        
        if opcao_escolhida == 'sair':
            sys.exit(0)