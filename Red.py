from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
data = []
driver = Chrome('/PycharmProjects/RedNotices/chromedriver')
url = 'https://www.interpol.int/How-we-work/Notices/View-Red-Notices'
driver.get(url)
for i in range(8):
    soup = BeautifulSoup(driver.page_source, 'lxml')
    notices = soup.findAll('div', class_='redNoticesList__item notice_red')[:20]
    for file in notices:
        photo = file.find('div', class_='redNoticeItem__responsiveImageContainer').find('img', class_='redNoticeItem__img').get('src')
        link = 'https://www.interpol.int/How-we-work/Notices/View-Red-Notices/'+file.find('div', class_='redNoticeItem__labelText').find('a', class_='redNoticeItem__labelLink').get('href')
        name = file.find('a', class_='redNoticeItem__labelLink').text
        age = file.find('div', class_= 'redNoticeItem__text').find('p', class_='redNoticeItem__standardText').find('span', class_='age').text.strip()
        country = file.find('div', class_= 'redNoticeItem__text').find('p', class_='redNoticeItem__standardText').find('span', class_='nationalities').text
        data.append([photo, link, name, age, country])
    if len(soup.find('a', class_='nextIndex').get('href')) > 1:
        driver.find_element(By.CLASS_NAME, 'nextIndex').click()
    else:
        break
    sleep(10)
header = ['Photo', 'Link', 'Name', 'Age', 'Country']
df = pd.DataFrame(data, columns=header)
df.to_csv('/PycharmProjects/RedNotices/RedNotices_data.csv', sep=':', encoding='utf8')
print(data)