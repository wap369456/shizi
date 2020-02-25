import uuid

import pymysql
from bs4 import BeautifulSoup
from selenium import webdriver
import re


def get_data(address):
    driver.get(address)
    soup_tmp = BeautifulSoup(driver.page_source, 'lxml')
    uuid_a = str(uuid.uuid4()).replace('-', '')
    college_uuid = 'de07e2fd649849c99f1e6be96f953eb5'
    try:
        teachername = name_a.replace(' ', '')
    except:
        teachername = ''
    try:
        title = title_a
    except:
        title = ''
    try:
        teaching = ''
    except:
        teaching = ''
    try:
        resume = ''
    except:
        resume = ''
    try:
        teacher_info = soup_tmp.find('form', attrs={'name': '_newscontent_fromname'})
        if teacher_info is None:
            teacher_info = str(soup_tmp.find('div', attrs={'class': 'main'}))
        else:
            teacher_info = str(soup_tmp.find('form', attrs={'name': '_newscontent_fromname'}))
    except:
        teacher_info = ''
    try:
        page_url = address
    except:
        page_url = ''
    print(uuid_a, college_uuid, teachername, title, teaching, page_url, resume, teacher_info)
    sql = "insert into teachers_wang(uuid,college_uuid,name,title,research_direction,resume,teacher_info,page_url) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, (uuid_a, college_uuid, teachername, title, teaching, resume, teacher_info, page_url))
    conn.commit()


if __name__ == '__main__':
    driver = webdriver.Firefox()
    conn = pymysql.connect(host='120.221.224.13', port=50266, user='root', passwd='job2019.thu', db='teachersource')
    cursor = conn.cursor()
    url = 'http://www.pspa.qd.sdu.edu.cn/jytd/qzjs.htm'
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    divs = soup.find('div', attrs={'class': 'lm_listpx'}).find_all('div', attrs={'class': 'lm_listpx'})
    titles = soup.find_all('div', attrs={'class': 'name-qz'})
    i = 0
    for div in divs:
        title_a = titles[i].get_text()
        a_s = div.find_all('a')
        for a in a_s:
            try:
                name_a = a.get_text()
                if '../..' in a['href']:
                    href = a['href'].replace('../..', 'http://www.pspa.qd.sdu.edu.cn')
                else:
                    if '..' in a['href']:
                        href = a['href'].replace('..', 'http://www.pspa.qd.sdu.edu.cn')
                    else:
                        href = a['href']
                if '#' not in href:
                    # print(name_a, title_a, href)
                    get_data(href)
            except:
                continue
        i += 1
    conn.close()
    driver.close()
