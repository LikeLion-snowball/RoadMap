import enum
import os
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import date, timedelta
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "RoadmapProject.settings")
import django
django.setup()
from info.models import Recruit
from idpw import naverid, naverpw

def fetch_recruit_latest_data():
    driver = webdriver.Chrome('/Users/yujin/sookmyung/chromedriver')

    driver.get('https://www.saramin.co.kr/zf_user/jobs/hot100')
    driver.implicitly_wait(2)

    driver.find_element_by_xpath('//*[@id="sri_header"]/div[1]/div[2]/a[1]/span').click()
    driver.implicitly_wait(2)
    driver.find_element_by_name('id').send_keys(naverid)
    driver.find_element_by_name('password').send_keys(naverpw)
    driver.find_element_by_xpath('//*[@id="login_frm"]/div[2]/div[1]/div[2]/button').click()
    driver.implicitly_wait(2)

    driver.find_element_by_xpath('//*[@id="search_panel_wrapper"]/form/fieldset/div/div[1]/div/div[1]/ul/li[4]/button').click()
    sleep(3)

    html = BeautifulSoup(driver.page_source, 'html.parser')

    banners = html.select('#content > div.recruit_hot_wrap > div.recruit_hot_list > div.careers > div > ul > li')
    result=[]
    link_root = "https://www.saramin.co.kr"

    for i, banner in enumerate(banners):
        if i == 0:
            continue
        corp = banner.select_one('div.area_rank > div.rank_company_info > a > span').text
        title = banner.select_one('div.area_detail > a.tit > span').text
        dt = banner.select_one('div.area_detail > dl > dd').text
        link = link_root + banner.select_one('div.area_detail > a.tit')["href"]
        career = banner.select_one('div.area_detail > div > span:nth-child(1)').text
        academic = banner.select_one('div.area_detail > div > span:nth-child(2)').text
        if banner.select_one('div.area_detail > div > span:nth-child(4)') :
            type = banner.select_one('div.area_detail > div > span:nth-child(3)').text
            area = banner.select_one('div.area_detail > div > span:nth-child(4)').text
        else :
            area = banner.select_one('div.area_detail > div > span:nth-child(3)').text

        # 연말에 연도 바뀌는 건 아직...?
        if "D" in dt:
                num = dt[2]
                end_date = date.today() + timedelta(int(num))
                end_date = end_date.strftime("%Y-%m-%d")
        elif "상시" in dt:
            end_date = "상시채용"
        elif "채용시" in dt:
            end_date = "채용시"
        elif "오늘마감" in dt:
            end_date = date.today()
            end_date = end_date.strftime("%Y-%m-%d")
        elif "내일마감" in dt:
            end_date = date.today() + timedelta(1)
            end_date = end_date.strftime("%Y-%m-%d")
        elif "시마감" in dt:
            end_date = date.today()
            end_date = end_date.strftime("%Y-%m-%d")

        if len(dt) > 5:
            if dt[5] == "(":
                #~ 8/2(
                end_date = str(date.today().year) + "-0" + dt[2] + "-0" + dt[4]
            elif dt[6] == "(" and dt[3] == "/":
                #~ 8/12(
                end_date = str(date.today().year) + "-0" + dt[2] + "-" + dt[4:6]
            elif dt[6] == "(" and dt[4] == "/":
                #~ 12/1(
                end_date = str(date.today().year) + "-" + dt[2:4] + "-0" + dt[5]
            elif dt[7] == "(":
                #~ 12/12(
                end_date = str(date.today().year) + "-" + dt[2:4] + "-" + dt[5:7]

        item_obj = {
            'corp': corp,
            'title': title,
            'end_date': end_date,
            'link': link,
            'career': career,
            'academic': academic,
            'type': type,
            'area': area
        }
    
        # print(item_obj)
        # print()
        result.append(item_obj)                

    driver.close()
    return result


def add_new_items(crawled_items):
    Recruit.objects.all().delete()
    # Recruit.objects.filter(end_date__lt=date.today()).delete() # 날짜 지난 거 삭제
    # 상시채용 같은 건 어떻게 업데이트 할건지...?
    for item in crawled_items:
        try:
            object = Recruit.objects.get(link=item['link']) # 링크 같은 건 제외
        except Recruit.DoesNotExist:
            if "-" in item['end_date']:
                Recruit(corp=item['corp'],
                        title=item['title'],
                        end_date=item['end_date'],
                        link=item['link'],
                        career=item['career'],
                        academic=item['academic'],
                        type=item['type'],
                        area=item['area']
                ).save()
            else:
                Recruit(corp=item['corp'],
                        title=item['title'],
                        end_date_str=item['end_date'],
                        link=item['link'],
                        career=item['career'],
                        academic=item['academic'],
                        type=item['type'],
                        area=item['area']
                ).save()



if __name__ == '__main__':
    add_new_items(fetch_recruit_latest_data())
    