from urllib.parse import urlparse


class BasePage(object):
    # Беру объект веб-драйвера, адрес страницы и время ожидания элементов
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

    def open_page(self, url):
        self.driver.get(url)


