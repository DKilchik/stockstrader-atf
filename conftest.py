import pytest
import os
import platform
import allure
import tempfile
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from extention import Element


def pytest_addoption(parser):
    """
    Пример имплементации параметров командной строки в pytest
    """
    parser.addoption("--headless", action="store_true",
                     help="Switch on the headless mode")
    parser.addoption("--docker", action="store_true",
                     help="Switch on Configuration options to run in docker")

@pytest.fixture(scope="session", autouse=True)
def generate_environment():
    """
    Пример фикстуры с параметром scope="session"
    Функция генерирует содержимое файла environment.properties для allure отчета
    """
    yield
    try:
        report = os.path.join('allure-results', 'environment.properties')
        with open(report, "w") as file:
            env = {
                "os_platform": platform.system(),
                "os_release": platform.release(),
                "os_version": platform.version()
                }
            for key in env:
                file.write(f"{key} = {env[key]}\n")
    except:
        pass

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
    Пример реализации pytest hooks.
    Функция помогает определить результат теста и передает его в tearDown
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture
def browser(request):
    """
    Базовая фикстура. Используется для открытия и передачи веб-драйвера в тестовые шаги
    При падении теста реализует добавление скриншота в отчет allure
    """
    options = Options()
    options.add_argument("--start-maximized")
    if request.config.getoption("--headless"):
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
    if request.config.getoption("--docker"):
        user_data_dir = tempfile.mkdtemp()
        options.add_argument(f"--user-data-dir={user_data_dir}")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
    driver = Chrome(options=options)
    yield driver
    if request.node.rep_call.failed:
        try:
            allure.attach(driver.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
        except:
            pass
    driver.quit()


def close_cookie_popup_if_present(browser):
    """
    Вспомогательная фикстура обработки поп-апа куки
    Замедляет прохождение теста, что вероятно, является желательным для демонстрации, но
    неприемлемым для коммерческого использования. В коммерческой среде обход поп-апа
    предпочтительно реализовать иным способом
    """
    try:
        host_locator = (By.XPATH,"//ion-button[text()='Allow']")
        target_locator = (By.CSS_SELECTOR,"ion-button[translate='cookies.allow'] button.button-native")
        Element(browser, host_locator, timeout=0.2, poll_frequency=0.04).shadow_child(target_locator).click(js=True)
    except WebDriverException as e:
        print(e)


def pytest_bdd_before_step(request, feature, scenario, step, step_func):
    """
    Пример реализации pytest_bdd hooks. Вызывается перед каждым тестовым шагом
    """
    browser = request.getfixturevalue("browser")
    close_cookie_popup_if_present(browser)

def pytest_bdd_after_step(request, feature, scenario, step, step_func):
    """
    Пример реализации pytest_bdd hooks. Вызывается после каждого тестового шага
    """
    browser = request.getfixturevalue("browser")
    close_cookie_popup_if_present(browser)
