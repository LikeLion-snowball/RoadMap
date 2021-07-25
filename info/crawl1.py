from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_argument("--headless")

# driver = webdriver.Chrome('/Users/yujin/sookmyung/chromedriver', options=chrome_options)
driver = webdriver.Chrome('/Users/yujin/sookmyung/chromedriver')


driver.get('https://www.saramin.co.kr/zf_user/jobs/list/job-category?cat_cd=404%2C407%2C408%2C402%2C409%2C405%2C417%2C403%2C411%2C416&panel_type=&search_optional_item=n&search_done=y&panel_count=y')
driver.implicitly_wait(3)

html = BeautifulSoup(driver.page_source, 'html.parser')
titles = html.select('#banner_list > div:nth-child(1) > ul > li')

list = []
link_root = "https://www.saramin.co.kr"

for title in titles:
    if title.select_one('a > span.corp') :
        link = link_root + title.select_one('a')["href"]
        date = title.select_one('span.date').text
        corp = title.select_one('a > span.corp').text
        tit = title.select_one('a > strong.tit').text
        # desc = title.select_one('a > ul').text
        # desc = desc.replace("\n", " ")
        logo = title.select_one('a.link > span.logo > img')['src']
        career = title.select_one('a > ul > li:nth-child(1)').text
        academic = title.select_one('a > ul > li:nth-child(2)').text
        area = title.select_one('a > ul > li:nth-child(3)').text
        
        print(corp)
        print(link)
        print(logo)
        print(date)
        print(tit)
        print(career)
        print(academic)
        print(area)
        print()


driver.close()