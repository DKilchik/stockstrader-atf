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
python - m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest
```
