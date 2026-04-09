#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SNOWRECON v1.0 - Легальный OSINT-фреймворк
Автор: web-pentest
GitHub: https://github.com/web-pentest
"""

import os
import sys
import subprocess
import platform
import shutil
from datetime import datetime

# ========== ЦВЕТА ДЛЯ ТЕРМИНАЛА ==========
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

# ========== ASCII АРТ ==========
def show_banner():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    banner = f"""
{Colors.CYAN}╔════════════════════════════════════════════════════════════════════════════╗
║  ❄️  {Colors.BOLD}{Colors.BLUE}SNOWRECON v1.0 - Легальный OSINT-фреймворк{Colors.END}{Colors.CYAN}                                      ❄️  ║
║  ══════════════════════════════════════════════════════════════════════════  ║
║     {Colors.GREEN}🎄         Снег идёт, данные текут           🎄{Colors.CYAN}                             ║
║         {Colors.YELLOW}"Разведка без последствий"{Colors.CYAN}                                             ║
╚════════════════════════════════════════════════════════════════════════════╝{Colors.END}
"""
    print(banner)

# ========== ДИСКЛЕЙМЕР ==========
def show_disclaimer():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    disclaimer = f"""
{Colors.RED}╔════════════════════════════════════════════════════════════════════════════╗
║  ⚠️  {Colors.BOLD}DISCLAIMER{Colors.END}{Colors.RED}                                                              ║
║                                                                            ║
║  {Colors.YELLOW}Данный инструмент предназначен ТОЛЬКО для:{Colors.RED}                                         ║
║    • Тестирования своих собственных систем                                 ║
║    • OSINT-исследований с разрешения цели                                  ║
║    • Образовательных целей                                                 ║
║                                                                            ║
║  {Colors.YELLOW}Незаконное использование преследуется по закону.{Colors.RED}                                   ║
║  {Colors.YELLOW}Автор не несёт ответственности за ваши действия.{Colors.RED}                                  ║
║                                                                            ║
║  {Colors.GREEN}Нажмите Enter, если согласны и понимаете риски...{Colors.RED}                                   ║
╚════════════════════════════════════════════════════════════════════════════╝{Colors.END}
"""
    print(disclaimer)
    input()

# ========== ПРОВЕРКА И УСТАНОВКА ЗАВИСИМОСТЕЙ ==========
def check_and_install_tools():
    """Проверяет наличие инструментов, устанавливает при отсутствии"""
    tools = {
        'sherlock': 'sherlock',
        'theHarvester': 'theharvester',
        'holehe': 'holehe',
        'whatweb': 'whatweb',
        'nmap': 'nmap',
        'photon': 'photon'
    }
    
    missing = []
    for tool, package in tools.items():
        if not shutil.which(tool):
            missing.append(package)
    
    if missing:
        print(f"{Colors.YELLOW}⚠️ Отсутствуют инструменты: {', '.join(missing)}{Colors.END}")
        answer = input(f"{Colors.CYAN}Установить их? (y/n): {Colors.END}")
        if answer.lower() == 'y':
            install_tools(missing)
        else:
            print(f"{Colors.RED}Некоторые функции будут недоступны{Colors.END}")
    else:
        print(f"{Colors.GREEN}✅ Все инструменты установлены{Colors.END}")

def install_tools(packages):
    """Установка через pip и apt/brew"""
    system = platform.system()
    
    # Установка через pip
    pip_packages = [p for p in packages if p in ['sherlock', 'holehe', 'photon']]
    for pkg in pip_packages:
        subprocess.run([sys.executable, '-m', 'pip', 'install', pkg])
    
    # Установка через пакетный менеджер
    apt_packages = [p for p in packages if p in ['theharvester', 'whatweb', 'nmap']]
    if apt_packages and system == 'Linux':
        subprocess.run(['sudo', 'apt', 'install', '-y'] + apt_packages)
    elif apt_packages and system == 'Darwin':
        subprocess.run(['brew', 'install'] + apt_packages)
    elif apt_packages and system == 'Windows':
        print(f"{Colors.RED}Установите вручную: {apt_packages}{Colors.END}")

# ========== ОБЁРТКИ ДЛЯ ИНСТРУМЕНТОВ ==========
def run_sherlock():
    username = input(f"{Colors.CYAN}Введите username для поиска: {Colors.END}")
    if username:
        subprocess.run(['sherlock', username])

def run_theharvester():
    domain = input(f"{Colors.CYAN}Введите домен (example.com): {Colors.END}")
    if domain:
        subprocess.run(['theHarvester', '-d', domain, '-b', 'all'])

def run_holehe():
    email = input(f"{Colors.CYAN}Введите email для проверки: {Colors.END}")
    if email:
        subprocess.run(['holehe', email])

def run_whatweb():
    url = input(f"{Colors.CYAN}Введите URL (https://example.com): {Colors.END}")
    if url:
        subprocess.run(['whatweb', url])

def run_nmap():
    target = input(f"{Colors.CYAN}Введите IP или домен: {Colors.END}")
    if target:
        subprocess.run(['nmap', '-T4', '-F', target])

def run_photon():
    url = input(f"{Colors.CYAN}Введите URL для парсинга: {Colors.END}")
    if url:
        subprocess.run(['photon', '-u', url])

def run_all():
    print(f"{Colors.YELLOW}Комплексный сбор пока в разработке{Colors.END}")

# ========== HELP ==========
def show_help():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    help_text = f"""
{Colors.CYAN}╔════════════════════════════════════════════════════════════════════════════╗
║  {Colors.BOLD}❄️  HELP - Что делает каждый инструмент{Colors.END}{Colors.CYAN}                                       ║
╚════════════════════════════════════════════════════════════════════════════╝{Colors.END}

{Colors.GREEN}[1] Sherlock{Colors.END}      — поиск юзернеймов по 300+ соцсетям
{Colors.GREEN}[2] TheHarvester{Colors.END}  — сбор email, доменов, поддоменов, IP
{Colors.GREEN}[3] Holehe{Colors.END}        — проверка email в 100+ сервисах
{Colors.GREEN}[4] WhatWeb{Colors.END}       — определение технологий сайта
{Colors.GREEN}[5] Nmap{Colors.END}          — сканирование портов (топ 100)
{Colors.GREEN}[6] Photon{Colors.END}        — парсинг ссылок и файлов с сайта

{Colors.YELLOW}Примеры:{Colors.END}
  Sherlock     → 'johndoe'
  TheHarvester → 'example.com'
  Holehe       → 'user@gmail.com'
  WhatWeb      → 'https://example.com'
  Nmap         → '192.168.1.1'
  Photon       → 'https://example.com'

{Colors.CYAN}Нажмите Enter для возврата в меню...{Colors.END}
"""
    print(help_text)
    input()

# ========== РЕКЛАМА GITHUB ==========
def show_ad():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    ad_text = f"""
{Colors.CYAN}╔════════════════════════════════════════════════════════════════════════════╗
║  {Colors.BOLD}❄️  Поддержи автора!{Colors.END}{Colors.CYAN}                                                     ║
║                                                                            ║
║  {Colors.GREEN}     ███████╗██╗  ██╗██████╗ {Colors.CYAN}                                            ║
║  {Colors.GREEN}     ██╔════╝██║  ██║██╔══██╗{Colors.CYAN}                                           ║
║  {Colors.GREEN}     ███████╗███████║██████╔╝{Colors.CYAN}                                           ║
║  {Colors.GREEN}     ╚════██║██╔══██║██╔═══╝ {Colors.CYAN}                                           ║
║  {Colors.GREEN}     ███████║██║  ██║██║     {Colors.CYAN}                                           ║
║  {Colors.GREEN}     ╚══════╝╚═╝  ╚═╝╚═╝     {Colors.CYAN}                                           ║
║                                                                            ║
║     {Colors.BOLD}GitHub:{Colors.END} https://github.com/web-pentest                               ║
║                                                                            ║
║     {Colors.YELLOW}⭐ Поставь звезду, если нравится проект! ⭐{Colors.CYAN}                          ║
╚════════════════════════════════════════════════════════════════════════════╝{Colors.END}
"""
    print(ad_text)
    input(f"{Colors.CYAN}Нажмите Enter для возврата в меню...{Colors.END}")

# ========== ГЛАВНОЕ МЕНЮ ==========
def main_menu():
    while True:
        show_banner()
        menu = f"""
{Colors.CYAN}┌────────────────────────────────────────────────────────────────────────────┐
│  {Colors.GREEN}[1]{Colors.CYAN} Sherlock      — поиск юзернеймов по соцсетям                         │
│  {Colors.GREEN}[2]{Colors.CYAN} TheHarvester  — сбор email/доменов/поддоменов                        │
│  {Colors.GREEN}[3]{Colors.CYAN} Holehe        — проверка email в 100+ сервисах                       │
│  {Colors.GREEN}[4]{Colors.CYAN} WhatWeb       — определение технологий сайта                         │
│  {Colors.GREEN}[5]{Colors.CYAN} Nmap (лёгкий) — сканирование портов (top 100)                        │
│  {Colors.GREEN}[6]{Colors.CYAN} Photon        — парсинг ссылок/файлов с сайта                        │
├────────────────────────────────────────────────────────────────────────────┤
│  {Colors.GREEN}[7]{Colors.CYAN} Все вместе    — комплексный сбор по цели (скоро)                     │
├────────────────────────────────────────────────────────────────────────────┤
│  {Colors.GREEN}[H]{Colors.CYAN} Help          — что делает каждый инструмент                        │
│  {Colors.GREEN}[R]{Colors.CYAN} Реклама       — поддержать автора                                   │
│  {Colors.GREEN}[0]{Colors.CYAN} Выход                                                               │
└────────────────────────────────────────────────────────────────────────────┘

{Colors.YELLOW}Выбор:{Colors.END} """, end=""
        print(menu)
        choice = input().lower()
        
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
            print(f"{Colors.GREEN}До свидания! ❄️{Colors.END}")
            sys.exit(0)
        else:
            print(f"{Colors.RED}Неверный выбор, попробуйте снова{Colors.END}")
            input(f"{Colors.CYAN}Нажмите Enter...{Colors.END}")

# ========== ТОЧКА ВХОДА ==========
if __name__ == "__main__":
    show_disclaimer()
    check_and_install_tools()
    main_menu()
