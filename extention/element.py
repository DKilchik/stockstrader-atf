from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Element:
    """Расширяет функционал объекта WebElement
    Благодаря реализации __getattr__ позволяет передавать вызов доступным в WebElement методам
    При передаче значения True в параметр конструктора auto_search при объявлении экземпляра класса
    будет осуществлен поиск веб-элемента. Найденный веб-элемент будет передан в переменную  __web_element

    Attributes:
    -----------
    _browser - активный инстанс веб-драйвера
    locator - кортеж для поиска веб-элемента формата (By, selector)
    _timeout : int or float - Период неявных ожиданий, использованных в поиске элемента или взаимодействии с ним
    _poll_frequency : int or float - Частота опроса при неявном ожидании
    """

    __web_element = None

    def __init__(self, browser, locator: tuple, timeout, poll_frequency, auto_search=True):
        self._browser = browser
        self.locator = locator
        self._timeout = timeout
        self._poll_frequency = poll_frequency

        # Поиск веб-элемента
        if auto_search:
            self._find()

    def _find(self):
        """
        Осуществляет "ленивый" поиск элемента, используя WebDriverWait
        Найденный объект WebElement передается в __web_element
        Raises:
        -------
        TimeoutException
            - В случае отсутствия элемента на странице
        """
        try:
            self.__web_element = WebDriverWait(
                self._browser, timeout=self._timeout, poll_frequency=self._poll_frequency
            ).until(EC.presence_of_element_located(self.locator))
            return self
        except TimeoutException:
            raise NoSuchElementException(f"The element {self.locator} wasn't find during {self._timeout}")

    def shadow_child(self, target: tuple):
        """
        Осуществляет поиск элемента в Shadow DOM.
        На момент вызова использует значение __web_element в качестве shadow host
        После успешного поиска переписывает __web_element значением найденного элемента
        Parameters:
        -----------
        target: tuple
            - кортеж для поиска веб-элемента формата (By, selector)
        """
        root = self._browser.execute_script('return arguments[0].shadowRoot', self.__web_element)
        self.__web_element = root.find_element(*target)
        return self

    def send_keys(self, keys):
        """
        Осуществляет ввод ключей/значений веб-элементу в интервале self._timeout с частотой self._poll_frequency
        Parameters:
        -----------
        target: keys
            - значение передаваемое элементу
        Raises:
        -------
        ElementNotInteractableException
            - В случае если за заданный интервал элемент не стал интерактивным
        """
        time = 0
        while time <= self._timeout:
            try:
                self.__web_element.send_keys(keys)
                return self
            except ElementNotInteractableException:
                time += self._poll_frequency
        raise ElementNotInteractableException(f"The element {self.locator} wasn't interactable during {self._timeout}")

    def click(self, js=False):
        """
        Расширяет стандартный click() библиотеки Selenium действием с использованием JavaScript
        Parameters:
        -----------
        js: bool
            - В случае получения значения True клик осуществляется JavaScript
        """
        if js:
            self._browser.execute_script("arguments[0].click();", self.__web_element)
            return self
        self.__web_element.click()
        return self

    @property
    def is_present(self) -> bool:
        """
        Проверка наличия элемента с использованием WebDriverWait.
        """
        try:
            WebDriverWait(
                self._browser, timeout=self._timeout, poll_frequency=self._poll_frequency
            ).until(EC.presence_of_element_located(locator=self.locator))
            return True
        except TimeoutException:
            return False

    def __getattr__(self, item):
        """
        Передает вызов объекту WebElement, если метод не найден в текущем объекте
        Example:
        --------
        >>> from extention import Element
        >>> from selenium.webdriver.common.by import By

        >>> Element((By.ID, "exampleId")).clear().send_keys("example")
        """
        return getattr(self.__web_element, item)
