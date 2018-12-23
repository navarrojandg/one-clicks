from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


class Harvester:
    def __init__(self):
        self.options = Options()
        self.options.add_experimental_option('excludeSwitches',['disable-sync'])
        self.options.add_argument('--enable-sync')
        self.options.add_argument('--disable-infobars')
        self.options.add_argument("--window-size=1280,800")
        self.options.add_extension(os.getcwd() + "\\extensions\\auto_refresh_1.3.8_0.crx")
        self.options.add_extension(os.getcwd() + "\\extensions\\youtube_auto_like_2.3.2_0.crx")
        self.options.add_extension(os.getcwd() + "\\extensions\\proxy_switch_omega_2.5.20_0.crx")
        self.browser = webdriver.Chrome(options=self.options)

    def get(self, url):
        self.browser.get(url)

    def close(self):
        self.browser.quit()


if __name__ == '__main__':
    harvesterList = []
    for i in range(input("How many one-click harvesters do you need? ")):
        harvesterList.append(Harvester())
    for harvester in harvesterList:
        harvester.get("https://docs.google.com/document/d/1-sP_nwjdBgXjRnKC-33YRCysb2gFa7Jvo-ScZ-E5Tm8/edit")