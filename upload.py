from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from random import randint
from pathlib import Path
from typing import Literal


class Upload():
    def __init__(self, dir_dict: dict[str, str] | dict[str, set[str]], value_type: Literal['set', 'str']) -> None:
        self.dir_dict = dir_dict
        self.value_type = value_type

    def run(self):
        self.driver = Chrome(driver_executable_path='/usr/local/bin/chromedriver')
        self.driver.get('https://login.123pan.com/centerlogin?redirect_url=https://www.123pan.com/')

        input('登录完成？')

        if self.value_type == 'str':
            self.upload_whole()
        else:
            self.upload_increase()

        self.driver.quit()

    def upload_whole(self):
        for url, dir in self.dir_dict.items():
            flag = input(f'{dir}\n上传/跳过(n)/退出(q)？')
            if flag == 'q':
                return
            elif flag == 'n':
                continue
            self.new_page(url)
            for path in Path(dir).iterdir():
                self.upload(path)
                time.sleep(randint(10, 30)/10)

    def upload_increase(self):
        for url, dir_set in self.dir_dict.items():
            flag = input(f'{dir_set}\n上传/跳过(n)/退出(q)？')
            if flag == 'q':
                return
            elif flag == 'n':
                continue
            self.new_page(url)
            for path in dir_set:
                self.upload(path)
                time.sleep(randint(10, 30)/10)

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
            button = 'body > div:nth-child(32) > div > div > ul > li:nth-child(1) > span > div > input[type=file]'
        else:
            button = 'body > div:nth-child(32) > div > div > ul > li:nth-child(2) > span > div > input[type=file]'
        self.driver.find_element(By.CSS_SELECTOR, button).send_keys(str(path.absolute()))

        wait = WebDriverWait(driver=self.driver, timeout=3600)
        check = EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '#Dashboard > div > div > div > div.uppy-Dashboard-inner > div > div.uppy-DashboardContent-new-bar.complete > div.uppy-DashboardContent-new-bar-left > div'),
            '上传完成')
        wait.until(method=check)
        print(f'{str(path)} 上传完成')