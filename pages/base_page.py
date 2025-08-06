from extention import Element
from utils import Configuration


class BasePage:
    """
    Класс наследуемый всеми объектами страниц
    Attributes:
    -----------
    _browser - активный инстанс веб-драйвера
    """

    def __init__(self, browser):
        self._browser = browser

    def element(self, locator: tuple, timeout=None, poll_frequency=None, auto_search=True) -> Element:
        """
        Возвращает экземпляр класса Element, расширяющего функционал Selenium
        Parameters:
        -----------
        locator: tuple
            - кортеж для поиска веб-элемента формата (By, selector)
        timeout: int or float | default - значение загружается из глобального конфига
            - Период неявных ожиданий, использованных в поиске элемента или взаимодействии с ним
        poll_frequency: int or float | default - значение загружается из глобального конфига
            - Частота опроса при неявном ожидании
        auto_search: bool
            - При передаче значения True будет осуществлен поиск элемента 
        """
        return Element(
            browser=self._browser,
            locator=locator,
            poll_frequency=poll_frequency or Configuration.POOL_FREQUENCY,
            timeout=timeout or Configuration.TIMEOUT,
            auto_search=auto_search
        )