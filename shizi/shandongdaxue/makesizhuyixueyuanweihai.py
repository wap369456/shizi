import uuid

import pymysql
from bs4 import BeautifulSoup
from selenium import webdriver
import re


def get_data(address):
    driver.get(address)
    soup_tmp = BeautifulSoup(driver.page_source, 'lxml')
    uuid_a = str(uuid.uuid4()).replace('-', '')
    college_uuid = 'f02b5735cbab4fc68717f97e306f9a5c'
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
    url = 'https://mlb.wh.sdu.edu.cn/xygk/szdw.htm'
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    uls = soup.find_all('ul', attrs={'class': 'szqaq'})
    for ul in uls[:-1]:
        a_s = ul.find_all('a')
        for a in a_s:
            try:
                name_a = a.get_text()
                if '../..' in a['href']:
                    href = a['href'].replace('../..', 'https://mlb.wh.sdu.edu.cn')
                else:
                    if '..' in a['href']:
                        href = a['href'].replace('..', 'https://mlb.wh.sdu.edu.cn')
                    else:
                        href = 'https://mlb.wh.sdu.edu.cn/' + a['href']
                if '#' not in href:
                    # print(name_a, href)
                    get_data(href)
            except:
                continue
    conn.close()
    driver.close()
