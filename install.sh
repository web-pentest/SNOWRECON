#!/bin/bash

echo "❄️ Устанавливаем SNOWRECON..."

# Создаём виртуальное окружение
python3 -m venv venv

# Активируем
source venv/bin/activate

# Устанавливаем зависимости
pip install -r requirements.txt

echo "✅ Готово!"
echo "Запусти: source venv/bin/activate && python3 snowrecon.py"
