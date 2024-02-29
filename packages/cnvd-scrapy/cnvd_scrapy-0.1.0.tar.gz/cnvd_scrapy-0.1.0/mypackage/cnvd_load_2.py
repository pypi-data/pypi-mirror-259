# coding = utf-8
# @author :ylc
# @Time :2021.08.10 09:22
# @file :main2.py
# @software :PyCharm

import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import pymysql
import random
import datetime
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait

headers = [
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; pt-BR; rv:1.9.1.11) Gecko/20100701 Firefox/3.5.11 ( .NET CLR 3.5.30729)'
    , 'Mozilla/5.0 (Windows; U; Windows NT 6.0; ru; rv:1.9.2) Gecko/20100115 Firefox/3.6'
    , 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
    , 'Mozilla/5.0 (Windows; U; Windows NT 6.0; it; rv:1.8.1.9) Gecko/20071025 Firefox/2.0.0.9'
    , 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.2.17) Gecko/20110420 Firefox/3.6.17'
    , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a1) Gecko/20060323 Firefox/1.6a1'
    , 'Mozilla/5.0 (Windows; U; Windows NT 6.0; id; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 (.NET CLR 3.5.30729)'
    , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.0.8) Gecko/2009032609 Firefox/3.07'
    , 'Mozilla/5.0 (Windows; U; Windows NT 6.0; es-ES; rv:1.8.1.16) Gecko/20080702 Firefox/2.0.0.16'
    , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; rv:1.7.3) Gecko/20040911 Firefox/0.10.1'
    , 'Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.7) Gecko/20040803 Firefox/0.9.3'
    , 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.7.9) Gecko/20050711 Firefox/1.0.5'
    , 'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.0) Gecko/20060728 Firefox/1.5.0'
    , 'Mozilla/5.0 (Windows; U; Windows NT 6.1; nl; rv:1.9.0.9) Gecko/2009040821 Firefox/3.0.9 FirePHP/0.3'
    , 'Mozilla/5.0(Windows; U; Windows NT 5.2; rv:1.9.2) Gecko/20100101 Firefox/3.6'
    , 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20120101 Firefox/29.0'
    , 'Mozilla/5.0 (Windows; U; Windows NT 5.0; ; rv:1.8.0.10) Gecko/20070216 Firefox/1.9.0.1'
    , 'Mozilla/5.0 (Windows; U; Windows NT 6.1; pt-BR; rv:1.9.2.18) Gecko/20110614 Firefox/3.6.18 (.NET CLR 3.5.30729)'
    , 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b11pre) Gecko/20110129 Firefox/4.0b11pre'
    , 'Mozilla/5.0 (Windows NT 5.1; U; de; rv:1.8.0) Gecko/20060728 Firefox/1.5.0'
    , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; cs; rv:1.8.1.18) Gecko/20081029 Firefox/2.0.0.18'
    , 'Mozilla/5.0 (Windows; U; Windows NT 6.0; ru; rv:1.8.1.12) Gecko/20080201 Firefox/2.0.0.12; MEGAUPLOAD 2.0'
    , 'Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/7.0'
    , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; hu; rv:1.9.1.11) Gecko/20100701 Firefox/3.5.11'
    , 'Mozilla/5.0 (Windows; U; Windows NT 6.0; de; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2 (.NET CLR 3.5.30729)'
    , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU; rv:1.9.1.4) Gecko/20091016 Firefox/3.5.4 (.NET CLR 3.5.30729)'
    ,
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.13) Gecko/2009073022 Firefox/3.0.13 (.NET CLR 3.5.30729) FBSMTWB'
    , 'Mozilla/5.0 (U; Windows NT 5.1; en-GB; rv:1.8.1.17) Gecko/20080808 Firefox/2.0.0.17'
    ,
    'Mozilla/5.0 (Windows; U; Windows NT 6.0; zh-CN; rv:1.9.0.19) Gecko/2010031422 Firefox/3.0.19 ( .NET CLR 3.5.30729)'
    , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.7.7) Gecko/20050414 Firefox/1.0.3']
finsh = 0


def main():
    try:
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('blink-settings=imagesEnabled=false')
        chrome_options.add_argument('--proxy-server=socks5://c883.kdltps.com:20818')
        chrome_options.add_argument('User-Agent={}'.format(headers[random.randint(0, 29)]))  # 配置为自己设置的UA
        # chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(chrome_options=chrome_options,
                                  executable_path='/Users/yangluchao/Downloads/chromedriver')
        # wait = WebDriverWait(driver, 10)  # 后面可以使用wait对特定元素进行等待
        # driver.implicitly_wait(10)
        driver.set_page_load_timeout(15)  # 设置页面加载超时
        driver.set_script_timeout(15)  # 设置页面异步js执行超时
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
             Object.defineProperty(navigator, 'webdriver', {
               get: () => undefined
             })
           """
        })
        db = pymysql.connect(user='root', password='ajiswu@qw1234uejUssa&F', host='43.139.42.28', database='vul_store',
                             port=3306)
        cursor = db.cursor()
        cursor.execute("select link from cnvd_copy1 where status = 0 order by id")
        links = cursor.fetchall()
        cursor.close()
        db.cursor()
        i = 0
        global finsh;
        print("捞到数据")

        while i < len(links):
            start = int(round(time.time() * 1000))
            driver.get(links[i][0])
            html = driver.page_source
            while True:
                if len(html) > 16975:
                    break
                time.sleep(3)
                driver.refresh()
                html = driver.page_source
                if breakW(driver, html):
                    return True
            if flush(driver, html, links[i][0]):
                return True
            i += 1
            finsh += 1
            end = int(round(time.time() * 1000))
            timestamp = (((end - start) * (len(links) - i)) + end)
            d = datetime.datetime.fromtimestamp(timestamp / 1000)
            ds = d.strftime("%Y-%m-%d %H:%M:%S")
            print("一共%s条，当次耗时：%s毫秒，还剩%s条，预计%s完成"
                  % (len(links), (end - start), (len(links) - i), ds))
    except:
        driver.close()
        main()
        return True
    return False


def breakW(driver, html):
    if "访问频率" in BeautifulSoup(html, "html.parser").text:
        driver.close()
        return True
    if "验证码保护" in BeautifulSoup(html, "html.parser").text:
        driver.close()
        return True


def flush(driver, html, link):
    dat = Parse(html)
    if len(dat) == 0:
        driver.refresh()
        time.sleep(2)
        html = driver.page_source
        if breakW(driver, html):
            return True
        flush(driver, html, link)
    else:
        return update(dat, link, html, driver)


def Parse(html):
    dat = []
    soup = BeautifulSoup(html, "html.parser")  # 指定Beautiful的解析器为“html.parser”
    for item in soup.find_all('tr'):
        temp = item.text
        temp = temp.replace("\n", "").replace("\t", "").replace(" ", "").replace("'", "")
        dat.append(temp)
    return dat


def update(dat, url, html, driver):
    try:
        Affectproduct = dat[3].split("影响产品")[1]  # 影响产品
    except:
        if flush(driver, html, url):
            return True
        return False
    db = pymysql.connect(user='root', password='ajiswu@qw1234uejUssa&F', host='43.139.42.28', database='vul_store',
                         port=3306)
    cursor = db.cursor()
    if len(dat) == 19:
        try:
            CVEID = dat[4].split("CVEID")[1]  # CVEID
        except:
            CVEID = dat[4]
        VulnerabilityDescribes = dat[5].split("漏洞描述")[1]  # 漏洞描述
        HoleType = dat[6].split("漏洞类型")[1]  # 漏洞类型
        referenceLinking = dat[7].split("参考链接")[1]  # 参考链接
        solution = dat[8].split("漏洞解决方案")[1]  # 解决方案
        ManufacturersPatch = dat[9].split("厂商补丁")[1]  # 产品补丁
        VerificationInformation = dat[10].split("验证信息")[1]  # 验证信息
        Vulnerabilityaccessories = dat[14].split("漏洞附件")[1]  # 漏洞附件
    elif len(dat) == 18:
        CVEID = ""
        VulnerabilityDescribes = dat[4].split("漏洞描述")[1]  # 漏洞描述
        HoleType = dat[5].split("漏洞类型")[1]  # 漏洞类型
        referenceLinking = dat[6].split("参考链接")[1]  # 参考链接
        solution = dat[7].split("漏洞解决方案")[1]  # 解决方案
        ManufacturersPatch = dat[8].split("厂商补丁")[1]  # 产品补丁
        VerificationInformation = dat[9].split("验证信息")[1]  # 验证信息
        Vulnerabilityaccessories = dat[13].split("漏洞附件")[1]  # 漏洞附件
    else:
        CVEID = dat[5].split("CVEID")[1]  # CVEID
        VulnerabilityDescribes = dat[6].split("漏洞描述")[1]  # 漏洞描述
        HoleType = dat[7].split("漏洞类型")[1]  # 漏洞类型
        referenceLinking = dat[8].split("参考链接")[1]  # 参考链接
        solution = dat[9].split("漏洞解决方案")[1]  # 解决方案
        ManufacturersPatch = dat[10].split("厂商补丁")[1]  # 产品补丁
        VerificationInformation = dat[11].split("验证信息")[1]  # 验证信息
        Vulnerabilityaccessories = dat[15].split("漏洞附件")[1]  # 漏洞附件
    sql = "update cnvd_copy1 set Affectproduct='%s',CVEID='%s',VulnerabilityDescribes='%s',HoleType='%s'," \
          "referenceLinking='%s',solution='%s',ManufacturersPatch='%s',VerificationInformation='%s'," \
          "Vulnerabilityaccessories='%s',status='%s' where link='%s'" % \
          (Affectproduct, CVEID, VulnerabilityDescribes, HoleType, referenceLinking, solution, ManufacturersPatch,
           VerificationInformation, Vulnerabilityaccessories, 1, url)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.cursor()
    time.sleep(2)


if __name__ == '__main__':
    while main():
        main()
    print("爬取完成")
