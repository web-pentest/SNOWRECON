#!/bin/bash
echo "❄️ Устанавливаем SNOWRECON..."

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

echo "✅ Готово! Запусти: source venv/bin/activate && python snowrecon.py"
