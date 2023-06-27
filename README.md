# itbastion-internship

Репозиторий предназначен для выполнения заданий на стажировку в компании "Айти Бастион"

В данной ветке опубликован пробный проект блога на фреймворке `flask`.

## Использование

1. Клонировать репозиторий
2. Открыть терминал в папке проекта
3. Последовательно выполнить в терминале следующие команды

```powershell
python -m venv venv

venv\Scripts\activate.bat # для Windows
source venv/bin/activate # для Linux/MacOS

pip install -r requirements.txt
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


## Работа с `pytest` и `allure-pytest`

После установки указанных модулей проделал следующие шаги:

1. Создадим папку `tests` - в ней будем хранить все тесты;
2. В папке `tests` создадим файл `test_routes.py`, в котором напишем три теста:
   1. Тест на существование главной страницы;
   2. Тест на проверку наличия кнопки "New post" на страницах;
   3. Тест на отсутствие страницы `/about`;
3. Скачаем [последний релиз](https://github.com/allure-framework/allure2/releases/tag/2.22.4) с официального репозитория, для удобства поместим его в папку с проектом;
4. Выполним команду для создания отчета о тестах:

```powershell
pytest --alluredir=\tests_allure .\tests\test_routes.py
```

5. Выполним команду для открытия отчета о тестах:

```powershell
.\allure-2.22.4\bin\allure.bat serve \tests_allure
```

Откроется вкладка в браузере по умолчанию со следующими данными:

![alt](https://sun9-69.vkuserphoto.ru/impg/9DSQ6p4yYNOhabjTLQ4Q_K9-ORBQlO-HzJI_yQ/nI2feCEtBgc.jpg?size=1858x1080&quality=96&sign=28c209454f75e21993fffc90c3a75ddf&type=album)

![alt2](https://sun9-18.vkuserphoto.ru/impg/uCDd5k93sOlFIzZq0QY4W2k0asazEasT_bwr8A/3UzMArrsSEs.jpg?size=1858x1080&quality=96&sign=4af3b78e6aaed486cc47302dc96b0a90&type=album)



Лог командной строки
```powershell
(venv) B:\GITHUB\itbastion-internship>pytest --alluredir=\tests_allure .\tests\test_routes.py
==================== test session starts ====================
platform win32 -- Python 3.11.1, pytest-7.4.0, pluggy-1.2.0
rootdir: B:\GITHUB\itbastion-internship
plugins: allure-pytest-2.13.2
collected 3 items

tests\test_routes.py ...                               [100%]

===================== 3 passed in 0.48s =====================

(venv) B:\GITHUB\itbastion-internship>.\allure-2.22.4\bin\allure.bat serve \tests_allure
Generating report to temp directory...
Report successfully generated to C:\Users\podst\AppData\Local\Temp\1346380726951362918\allure-report
Starting web server...
2023-06-27 22:59:45.537:INFO::main: Logging initialized @2795ms to org.eclipse.jetty.util.log.StdErrLog
Server started at <http://26.137.65.188:62814/>. Press <Ctrl+C> to exit
```




