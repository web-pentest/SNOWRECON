#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import platform
import shutil

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def show_banner():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print(Colors.CYAN + "╔══════════════════════════════════════════════════════════════════╗")
    print("║  ❄️  SNOWRECON v1.0 - Легальный OSINT-фреймворк             ❄️    ║")
    print("║  ═══════════════════════════════════════════════════════════     ║")
    print("║        🎄   Снег идёт, данные текут   🎄                          ║")
    print("║            \"Разведка без последствий\"                          ║")
    print("╚══════════════════════════════════════════════════════════════════╝" + Colors.END)

def show_disclaimer():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print(Colors.RED + "╔══════════════════════════════════════════════════════════════════╗")
    print("║  ⚠️  DISCLAIMER                                                  ║")
    print("║                                                                  ║")
    print("║  Данный инструмент предназначен ТОЛЬКО для:                      ║")
    print("║    • Тестирования своих собственных систем                       ║")
    print("║    • OSINT-исследований с разрешения цели                        ║")
    print("║    • Образовательных целей                                       ║")
    print("║                                                                  ║")
    print("║  Незаконное использование преследуется по закону.                ║")
    print("║  Автор не несёт ответственности за ваши действия.                ║")
    print("╚══════════════════════════════════════════════════════════════════╝" + Colors.END)
    input(Colors.CYAN + "Нажмите Enter для продолжения..." + Colors.END)

def check_and_install_tools():
    tools = ['sherlock', 'theHarvester', 'holehe', 'whatweb', 'nmap', 'photon']
    missing = []
    for tool in tools:
        if not shutil.which(tool):
            missing.append(tool)
    if missing:
        print(Colors.YELLOW + "⚠️ Отсутствуют: " + ", ".join(missing) + Colors.END)
        answer = input(Colors.CYAN + "Установить? (y/n): " + Colors.END)
        if answer.lower() == 'y':
            for tool in missing:
                if tool in ['sherlock', 'holehe', 'photon']:
                    subprocess.run([sys.executable, '-m', 'pip', 'install', tool])
                else:
                    system = platform.system()
                    if system == 'Linux':
                        subprocess.run(['sudo', 'apt', 'install', '-y', tool])
                    elif system == 'Darwin':
                        subprocess.run(['brew', 'install', tool])
                    else:
                        print(Colors.RED + "Установи вручную: " + tool + Colors.END)
        else:
            print(Colors.RED + "Некоторые функции будут недоступны" + Colors.END)
    else:
        print(Colors.GREEN + "✅ Все инструменты установлены" + Colors.END)

def run_sherlock():
    username = input(Colors.CYAN + "Введите username: " + Colors.END)
    if username:
        subprocess.run(['sherlock', username])

def run_theharvester():
    domain = input(Colors.CYAN + "Введите домен: " + Colors.END)
    if domain:
        subprocess.run(['theHarvester', '-d', domain, '-b', 'all'])

def run_holehe():
    email = input(Colors.CYAN + "Введите email: " + Colors.END)
    if email:
        subprocess.run(['holehe', email])

def run_whatweb():
    url = input(Colors.CYAN + "Введите URL: " + Colors.END)
    if url:
        subprocess.run(['whatweb', url])

def run_nmap():
    target = input(Colors.CYAN + "Введите IP или домен: " + Colors.END)
    if target:
        subprocess.run(['nmap', '-T4', '-F', target])

def run_photon():
    url = input(Colors.CYAN + "Введите URL: " + Colors.END)
    if url:
        subprocess.run(['photon', '-u', url])

def run_all():
    print(Colors.YELLOW + "Комплексный сбор в разработке" + Colors.END)
    input(Colors.CYAN + "Нажмите Enter..." + Colors.END)

def show_help():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print(Colors.CYAN + "╔══════════════════════════════════════════════════════════════════╗")
    print("║  ❄️  HELP - Что делает каждый инструмент                             ║")
    print("╚══════════════════════════════════════════════════════════════════╝" + Colors.END)
    print(Colors.GREEN + "[1] Sherlock" + Colors.END + "      — поиск юзернеймов по 300+ соцсетям")
    print(Colors.GREEN + "[2] TheHarvester" + Colors.END + "  — сбор email, доменов, поддоменов")
    print(Colors.GREEN + "[3] Holehe" + Colors.END + "        — проверка email в 100+ сервисах")
    print(Colors.GREEN + "[4] WhatWeb" + Colors.END + "       — определение технологий сайта")
    print(Colors.GREEN + "[5] Nmap" + Colors.END + "          — сканирование портов (топ 100)")
    print(Colors.GREEN + "[6] Photon" + Colors.END + "        — парсинг ссылок и файлов")
    print(Colors.YELLOW + "\nПримеры:" + Colors.END)
    print("  Sherlock     → johndoe")
    print("  TheHarvester → example.com")
    print("  Holehe       → user@gmail.com")
    print("  WhatWeb      → https://example.com")
    print("  Nmap         → 192.168.1.1")
    print("  Photon       → https://example.com")
    input(Colors.CYAN + "\nНажмите Enter для возврата..." + Colors.END)

def show_ad():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print(Colors.CYAN + "╔══════════════════════════════════════════════════════════════════╗")
    print("║  ❄️  Поддержи автора!                                                 ║")
    print("║                                                                    ║")
    print(Colors.GREEN + "     ███████╗██╗  ██╗██████╗ ")
    print("     ██╔════╝██║  ██║██╔══██╗")
    print("     ███████╗███████║██████╔╝")
    print("     ╚════██║██╔══██║██╔═══╝ ")
    print("     ███████║██║  ██║██║     ")
    print("     ╚══════╝╚═╝  ╚═╝╚═╝     " + Colors.CYAN)
    print("║                                                                    ║")
    print("║     GitHub: https://github.com/web-pentest                         ║")
    print("║                                                                    ║")
    print(Colors.YELLOW + "║     ⭐ Поставь звезду, если нравится проект! ⭐                ║" + Colors.CYAN)
    print("╚══════════════════════════════════════════════════════════════════╝" + Colors.END)
    input(Colors.CYAN + "Нажмите Enter для возврата..." + Colors.END)

def main_menu():
    while True:
        show_banner()
        print(Colors.CYAN + "┌────────────────────────────────────────────────────────────┐")
        print("│  " + Colors.GREEN + "[1]" + Colors.CYAN + " Sherlock      — поиск юзернеймов                      │")
        print("│  " + Colors.GREEN + "[2]" + Colors.CYAN + " TheHarvester  — сбор email/доменов                    │")
        print("│  " + Colors.GREEN + "[3]" + Colors.CYAN + " Holehe        — проверка email                        │")
        print("│  " + Colors.GREEN + "[4]" + Colors.CYAN + " WhatWeb       — технологии сайта                      │")
        print("│  " + Colors.GREEN + "[5]" + Colors.CYAN + " Nmap          — сканирование портов                   │")
        print("│  " + Colors.GREEN + "[6]" + Colors.CYAN + " Photon        — парсинг сайта                         │")
        print("├────────────────────────────────────────────────────────────┤")
        print("│  " + Colors.GREEN + "[7]" + Colors.CYAN + " Все вместе    — комплексный сбор (скоро)              │")
        print("├────────────────────────────────────────────────────────────┤")
        print("│  " + Colors.GREEN + "[H]" + Colors.CYAN + " Help          — справка                               │")
        print("│  " + Colors.GREEN + "[R]" + Colors.CYAN + " Реклама       — поддержать автора                     │")
        print("│  " + Colors.GREEN + "[0]" + Colors.CYAN + " Выход                                                 │")
        print("└────────────────────────────────────────────────────────────┘" + Colors.END)
        
        choice = input(Colors.YELLOW + "Выбор: " + Colors.END).lower()
        
        if choice == '1':
            run_sherlock()
        elif choice == '2':
            run_theharvester()
        elif choice == '3':
            run_holehe()
        elif choice == '4':
            run_whatweb()
        elif choice == '5':
            run_nmap()
        elif choice == '6':
            run_photon()
        elif choice == '7':
            run_all()
        elif choice == 'h':
            show_help()
        elif choice == 'r':
            show_ad()
        elif choice == '0':
            print(Colors.GREEN + "До свидания! ❄️" + Colors.END)
            sys.exit(0)
        else:
            print(Colors.RED + "Неверный выбор" + Colors.END)
            input(Colors.CYAN + "Нажмите Enter..." + Colors.END)

if __name__ == "__main__":
    show_disclaimer()
    check_and_install_tools()
    main_menu()
