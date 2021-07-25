# import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pandas as pd


def iframe():
    try:
        driver.switch_to.frame("cafe_main")
    except:
        pass

# chrome_options = Options()
# chrome_options.add_argument("--headless")

# driver = webdriver.Chrome('/Users/yujin/sookmyung/chromedriver', options=chrome_options)
driver = webdriver.Chrome('/Users/yujin/sookmyung/chromedriver')


# driver.get('https://m.cafe.naver.com/ca-fe/web/cafes/15754634/menus/1481')
# driver.switch_to.frame("cafe_main")
driver.get('https://cafe.naver.com/specup')
driver.implicitly_wait(3)

driver.find_element_by_xpath('//*[@id="menuLink1481"]').click()
time.sleep(2)

iframe()

for i in range(1, 3):
    html = BeautifulSoup(driver.page_source, 'html.parser')
    titles = html.select('#main-area > div:nth-child(6) > table > tbody > tr')

    list3 = []

    for title in titles:
        list = title.select_one(' td.td_article > div.board-list > div > a').text
        list2 = ''.join(list.split())
        list3.append(list2)

    # list4_sr = pd.Series(list3)
    # print(list4_sr)
    # print(list3)

    for a in range(1, 3):
        driver.find_element_by_xpath(f'//*[@id="main-area"]/div[4]/table/tbody/tr[{a}]/td[1]/div[2]/div/a').click()
        time.sleep(2)

        html = BeautifulSoup(driver.page_source , 'html.parser')
        titles = html.select("h3.title_text")
        content_tags = html.select('div.se-section.se-section-text.se-l-default')
        # 본문 내용을 줄바꿈 기준으로 다 붙이기
        exclude1 = '▼채용공고▼'
        exclude2 = '채용공고 바로 보기(클릭) ​​▼스펙업에서 취준 알차게 하는 방법▼ ​👉기업별 채용소식/정보 가장 빠르게 받기 https://open.kakao.com/o/gg8n52g​​👉자소서 첨삭 무료로! 받기 https://vo.la/EPyx​​🎁자소서&면접 대비 필수 자료! 기업 최신이슈+면접기출+답안 상세 정리! 👇기업분석 자료 바로 받기 https://bit.ly/3wp6egA'
        content = ' '.join([tags.get_text().replace("▶","\n").replace(exclude1,"").replace(exclude2,"") for tags in content_tags])
        print(content)
        print()
        print()

        driver.back()
        time.sleep(2)
        iframe()

driver.close()