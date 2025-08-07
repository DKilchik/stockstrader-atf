## Тестовое задание stockstrader.roboforex.com

### Задача:
* Написать UI-тест на успешный логин
* Требования: использовать фреймворк pytest-bdd

### Решение:
Реализован концепт тестового фреймворка на основе паттерна PageObject <br>
и с использованием инструментов:
* Selenium
* pytest pytest-bdd + плагин pytest-rerunfailures
* allure

### Запуск 
```
Переименуйте файл data.sample.ini в data.ini в директории data
Добавьте валидный username и password в соответствующие поля файла data.ini
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest
```
### Структура проекта

```commandline
stock_trader/
│
├── data/ # Тестовые данные
│ ├── data.ini # данные аккаунта
│ └── test_data.py # утилита чтения конфига
│
├── extention/ # Расширения и обёртки (например, Element)
│ └── element.py
│
├── pages/ # Page Object'ы
│ ├── base_page.py
│ ├── home_page.py
│ └── login_page.py
│
├── utils/ # Вспомогательные утилиты и конфигурации
│ └── config.py
│
├── conftest.py # Фикстуры, хуки, browser setup
│
├── tests/ # Все тестовые компоненты
│ ├── features/ # Gherkin-сценарии
│ │ └── login.feature
│ │
│ ├── step_definitions/ # Реализация шагов BDD
│ │ ├── home_steps.py
│ │ └── login_steps.py
│ │
│ └── tests/ # Файлы, запускающие сценарии (test_*.py)
│ └── test_login.py
│
├── requirements.txt # Зависимости проекта
├── pytest.ini # Конфигурация pytest
└── README.md # Документация проекта
```