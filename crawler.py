from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from getURL import geturl
from preprocess import tokenize_sentence,append_dot,remove_special_character,remove_duplicate,remove_special_senc
import time
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1280x720")

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="D:/chromedriver/chromedriver.exe")
lnk = "https://www.epochtimes.com/gb/nsc413_2.htm"
class_name = '//div[@class="text"]//a'
file = "data/clean_data/data_ch_clean.txt"
url = geturl(lnk,class_name)  
f = open(file,'a',encoding='utf-8')
f0 = open('URL_crawled.txt','w+',encoding="utf-8")
crawled = f0.readlines()
try:
    for i in url.values():
        if i in crawled:
            continue
        else:
            driver.get(i)
            time.sleep(0.2)
            contents = driver.find_elements_by_xpath('//div[@id="artbody"]//p')                   
            for content in contents:
                result = content.text
                a = f.write(result + "\n") 
                print(result)
            crawled.append(i)  
        
except:
    
    for element in crawled:
        f0.write(element + "\n")

# output_file = "data/clean_data/data_ch_clean2.txt"
# tokenize_sentence(file)
# append_dot(file)
# remove_special_senc(file)
# remove_special_character(file)
# remove_duplicate(file,output_file)







