from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By
import time
from pathlib import Path
from typing import Literal


class Upload():
    def __init__(self, dir_dict: dict[str, str] | dict[str, set[str]], value_type: Literal['set', 'str']) -> None:
        self.dir_dict = dir_dict
        self.value_type = value_type

    def run(self):
        driver = Chrome(driver_executable_path='/usr/local/bin/chromedriver')
        driver.get('https://login.123pan.com/centerlogin?redirect_url=https://www.123pan.com/')

        input('登录完成？')

        if self.value_type == 'str':
            self.upload_whole()
        else:
            self.upload_increase()

        self.driver.quit()

    def upload_whole(self):
        for url, dir in self.dir_dict.items():
            self.new_page(url)
            for path in Path(dir).iterdir():
                if path.is_dir() and (path.name.endswith('/d')):
                        continue
                self.upload(path)
                if input('是否继续上传？') == 'n':
                    return

    def upload_increase(self):
        for url, dir_set in self.dir_dict.items():
            self.new_page(url)
            num = 0
            for path in dir_set:
                self.upload(path)
                num += 1
                if input(f'已上传 {num} 个文件，是否继续上传：') == 'n':
                    return

    def new_page(self, url: str):
        self.driver.get(url)
        time.sleep(5)

        upload_button = self.driver.find_element(
            By.CSS_SELECTOR,
            '#app > div > div > section > section > section > main > div > div.homeClass > div:nth-child(1) > div.ant-dropdown-trigger.sysdiv.parmiryButton'
        )
        upload_button.click()
        time.sleep(5)

    def upload(self, path: Path):
        if path.is_file():
            button = '//input[@type="file"]'
        else:
            button = '//input[@type="file" and @webkitdirectory]'
        self.driver.find_element(By.XPATH, button).send_keys(str(path.absolute()))
