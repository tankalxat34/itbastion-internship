import unittest
from flask import Flask, jsonify
from flask.testing import FlaskClient
import os
import sys
from bs4 import BeautifulSoup

# Добавляем путь к корневой папке проекта в системный путь
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Импортируем ваш модуль приложения
from main import app


class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        # Создаем тестовый клиент Flask
        self.app = app.test_client()
        # Устанавливаем флаг для тестирования (например, включение режима отладки)
        self.app.testing = True

    def test_home_route(self):
        """
        Проверка на существование главной страницы
        """
        # Тестирование маршрута "/"
        response = self.app.get('/')
        # Проверяем, что получаем ожидаемый ответ
        self.assertEqual(response.status_code, 200)

    def test_newpost_btn_is_being(self):
        """
        Тест на проверку наличия кнопки "New post" на страницах
        """
        response = self.app.get('/')
        soup = BeautifulSoup(response.data, 'html.parser')
        link = soup.select_one('a#create')
        self.assertIsNotNone(link)

    def test_not_about_route(self):
        """
        Проверка на отсутствие страницы `/about`
        """
        # Тестирование маршрута "/"
        response = self.app.get('/about')
        # Проверяем, что получаем ожидаемый ответ
        self.assertEqual(response.status_code, 404)

    def tearDown(self):
        # Метод tearDown выполняется после каждого теста (если есть)
        # Здесь можно выполнять очистку или освобождение ресурсов
        pass


if __name__ == '__main__':
    unittest.main()
