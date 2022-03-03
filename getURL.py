from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="D:/chromedriver/chromedriver.exe")

def geturl(url,class_name):
    # Handle infinitive load
    driver.get(url)
    for i in range(10000):
        driver.execute_script("""$('div[class="more"]').click()""") #xpage-more-btn
    time.sleep(0.2)
    links = driver.find_elements_by_xpath(class_name)
    url = {}
    for link in links:
        key = hash(link)
        value = link.get_attribute("href")
        url[key] = value
        print("URL : ",value)
    print(len(url))
    return url

#geturl('https://www.epochtimes.com/gb/nsc413_{}.htm'.format(i),'//div[@class="text"]//a') 
# geturl("http://www.xinhuanet.com/sikepro/",'//div[@class="mod-tit"]//a') 
