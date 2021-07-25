import os
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

def fetch_recruit_latest_data():
    driver = webdriver.Chrome('/Users/yujin/sookmyung/chromedriver')

    driver.get('https://www.saramin.co.kr/zf_user/jobs/list/job-category?cat_cd=404%2C407%2C408%2C402%2C409%2C405%2C417%2C403%2C411%2C416&panel_type=&search_optional_item=n&search_done=y&panel_count=y')
    driver.implicitly_wait(2)

    html = BeautifulSoup(driver.page_source, 'html.parser')

    titles = html.select('#banner_list > div:nth-child(1) > ul > li')
    result = []
    link_root = "https://www.saramin.co.kr"

    for title in titles:
        if title.select_one('a > span.corp') :
            corp = title.select_one('a > span.corp').text
            tit = title.select_one('a > strong.tit').text
            dt = title.select_one('span.date').text
            link = link_root + title.select_one('a')["href"]
            logo = title.select_one('a.link > span.logo > img')['src']
            career = title.select_one('a > ul > li:nth-child(1)').text
            academic = title.select_one('a > ul > li:nth-child(2)').text
            area = title.select_one('a > ul > li:nth-child(3)').text

            # 연말에 연도 바뀌는 건 아직...
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
                'tit': tit,
                'end_date': end_date,
                'link': link,
                'logo': logo,
                'career': career,
                'academic': academic,
                'area': area
            }
        
            # print(item_obj)
            # print()
            result.append(item_obj)

    driver.close()
    return result

def add_new_items(crawled_items):
    for item in crawled_items:
        try:
            object = Recruit.objects.get(link=item['link'])
        except Recruit.DoesNotExist:
            if "-" in item['end_date']:
                Recruit(corp=item['corp'],
                        title=item['tit'],
                        end_date=item['end_date'],
                        link=item['link'],
                        logo=item['logo'],
                        career=item['career'],
                        academic=item['academic'],
                        area=item['area']
                ).save()
            else:
                Recruit(corp=item['corp'],
                        title=item['tit'],
                        end_date_str=item['end_date'],
                        link=item['link'],
                        logo=item['logo'],
                        career=item['career'],
                        academic=item['academic'],
                        area=item['area']
                ).save()



if __name__ == '__main__':
    add_new_items(fetch_recruit_latest_data())
    