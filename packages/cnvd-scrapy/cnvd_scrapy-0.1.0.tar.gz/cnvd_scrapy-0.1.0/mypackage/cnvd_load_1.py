# coding = utf-8
# @author :ylc
# @file :mian.py
# @software :PyCharm
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import pymysql
import random
from selenium.webdriver.chrome.options import Options

# 应用漏洞获取
list = [27, 28, 29, 30, 31, 32, 33, 34, 35, 38]
breakDate = "2020-01-01"


def main():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    # chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/Users/yangluchao/Downloads/chromedriver')
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
      Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
      })
    """
    })
    i = 0
    while i < len(list):
        leng = 0
        while True:
            url = "https://www.cnvd.org.cn/flaw/typeResult?typeId=%d&max=100&offset=%d" % (list[i], leng)
            driver.get(url)
            driver.refresh()  # 刷新页面
            html = driver.page_source
            print("数据包长度：" + str(len(html)))
            if len(html) < 20000:
                print("休眠120秒")
                time.sleep(120)
                print("休眠结束")
                driver.refresh()  # 刷新页面
                html = driver.page_source
            result = parseHtml(html, list[i])
            if result[0] is not None:
                datasize = len(result[0])
                if datasize != 0:
                    leng = leng + 100
                save(result[0])
                driver.refresh()
                print("当前i=%d,leng=%d,datasize=%d,currentDate=%s" % (list[i], leng, datasize, result[2]))
            if result[1]:
                break
        i = i + 1
    driver.close()


def parseHtml(html, vulType):
    datlist = []  # 存一页漏洞基本信息
    soup = BeautifulSoup(html, "html.parser")  # 指定Beautiful的解析器为“html.parser”
    if "对不起" in soup.text:
        return [None, True]
    findLevel = re.compile(r'</span>(.*?)</td>', re.S)  # 危害级别匹配规则
    findDate = re.compile(r'<td width="13%">(.*?)</td>', re.S)  # 时间匹配规则
    k = 0
    items = soup.find_all('tr')
    if vulType == 27:
        vulType = "操作系统"
    elif vulType == 28:
        vulType = "应用程序"
    elif vulType == 29:
        vulType = "WEB应用"
    elif vulType == 30:
        vulType = "数据库"
    elif vulType == 31:
        vulType = "网络设备（交换机，路由器等网络终端设备）"
    elif vulType == 32:
        vulType = "安全产品"
    elif vulType == 33:
        vulType = "智能设备（物联网终端设备）"
    elif vulType == 34:
        vulType = "区块链公链"
    elif vulType == 35:
        vulType = "区块链联盟链"
    elif vulType == 38:
        vulType = "工业控制系统"
    currentDate = ""

    while k < len(items):
        dat = []  # 存一个漏洞基本信息
        item = items[k]
        link = "https://www.cnvd.org.cn" + item.a["href"]  # 获取漏洞详细信息链接
        title = item.a["title"]  # 获取漏洞标题
        item = str(item)  # 转换为字符串
        level = re.findall(findLevel, item)[0]
        date = re.findall(findDate, item)[0]
        dat.append(title)
        dat.append(level.strip())
        currentDate = date
        if date < breakDate:
            return [datlist, True, currentDate]
        dat.append(date)
        dat.append(link)
        dat.append(vulType)
        datlist.append(dat)
        k += 1
    return [datlist, False, currentDate]


def save(datlist):
    if datlist is None:
        return
    db = pymysql.connect(user='root', password='ajiswu@qw1234uejUssa&F', host='43.139.42.28', database='vul_store',
                         port=3306)
    cursor = db.cursor()
    for dat in datlist:
        try:
            data = "'" + dat[0].replace("'", "") + "'" + "," + "'" + dat[1].replace(" ", "").replace("\n", "").replace(
                "\t", "") + "'" + "," + "'" + dat[2] + "'" + "," + "'" + dat[3] + "'" + "," + "'" + dat[4] + "'"
            sql = "insert into cnvd (title,level,date,link,type) values(%s)" % data
            cursor.execute(sql)  # 提交数据库操作
            db.commit()  # 提交事务
        except:
            print("有数据错误")
    cursor.close()
    db.close()
    t = random.randint(1, 6)  # 取随机数
    print("等待%d秒" % t)
    time.sleep(t)  # 休眠t秒


# 输入selenium 搜索
# element = driver.find_element_by_name('a')
# ActionChains(driver).move_to_element(element).perform()
# 单击，弹出的Ajax元素，根据链接节点的文本内容查找

if __name__ == '__main__':
    main()
    print("爬取完成")
