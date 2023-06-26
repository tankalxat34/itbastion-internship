# itbastion-internship

Репозиторий предназначен для выполнения заданий на стажировку в компании "Айти Бастион"

В данной ветке опубликован пробный проект блога на фреймворке `flask`.

## Использование

1. Клонировать репозиторий
2. Открыть терминал в папке проекта
3. Последовательно выполнить в терминале следующие команды

```powershell
python -m venv venv

pip install -r requirements.txt

venv\Scripts\activate.bat # для Windows
source venv/bin/activate # для Linux/MacOS
```

4. Создать файл `.env` с переменными окружения

```ini
FLASK_APP=main
FLASK_ENV=development
```

5. Для запуска проекта

```powershell
flask run
```