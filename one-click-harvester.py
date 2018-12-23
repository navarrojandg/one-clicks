from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import threading
import os


class Harvester:
    def __init__(self, proxy):
        self.options = Options()
        self.options.add_experimental_option('excludeSwitches', ['disable-sync', 'enable-automation'])
        self.options.add_experimental_option('detach', True)
        self.options.add_argument('--enable-sync')
        self.options.add_argument('--disable-infobars')
        self.options.add_argument("--window-size=1280,800")
        self.options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")
        if proxy is not None:
            self.options.add_argument("--proxy-server={}".format(proxy))
        self.options.add_extension(os.getcwd() + "\\extensions\\auto_refresh_1.3.8_0.crx")
        self.options.add_extension(os.getcwd() + "\\extensions\\youtube_auto_like_2.3.2_0.crx")
        # self.options.add_extension(os.getcwd() + "\\extensions\\proxy_switch_omega_2.5.20_0.crx")
        self.browser = webdriver.Chrome(options=self.options)

    def get(self, url):
        self.browser.get(url)

    def close(self):
        self.browser.quit()


class HarvesterThread(threading.Thread):
    def __init__(self, id, proxy):
        threading.Thread.__init__(self)
        self.id = id
        self.proxy = proxy

    def run(self):
        print("Starting harvester{} | Proxy: {}".format(self.id, self.proxy))
        har = Harvester(proxy=self.proxy)
        har.get("https://docs.google.com/document/d/1-sP_nwjdBgXjRnKC-33YRCysb2gFa7Jvo-ScZ-E5Tm8/edit")


def read_proxy_list():
    proxyList = []
    with open("PROXY_LIST.txt", "r") as f:
        for line in f:
            proxyList.append(line.strip())
    return proxyList


if __name__ == '__main__':
    proxies = read_proxy_list()
    threadList = []
    for i in range(input("How many harvesters? :")):
        try:
            threadList.append(HarvesterThread(i, proxies.pop()))
        except IndexError:
            threadList.append(HarvesterThread(i, None))
    for t in threadList:
        t.start()
