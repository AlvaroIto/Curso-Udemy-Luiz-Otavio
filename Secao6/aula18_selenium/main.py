from time import sleep
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromeddriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'

def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.addd_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)
    
    chrome_sevice = Service(ChromeDriverManager().install())

    browser = webdriver.Chrome(service=chrome_sevice, options=chrome_options)

    return browser

if __name__ == '__main__':
    # Example
    options = ('--disable-gpu', '--no-sandbox',)
    browser = make_chrome_browser(*options)

    #Como antes
    browser.get('https://www.google.com')
    sleep(10)

