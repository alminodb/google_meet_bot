from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


from time import sleep


# podesavanje opcija - enabling mic and cam
opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 1
})


# stvaranje web drajvera
PATH = "C:\chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH, options=opt)

participants = 0

#https://meet.google.com/tnh-eowd-vtc
meet_link = "https://meet.google.com/lookup/gutpwcfpgh"

driver.get("https://www.gmail.com")
sleep(1)

driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys("almin.odobasic.20@size.ba", Keys.RETURN)
while True:
    sleep(3)
    try:
        driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys("pasvord4", Keys.RETURN)
        break
    except:
        pass

sleep(5)
driver.get(meet_link)

while True:
    sleep(10)
    if(len(driver.find_elements_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[3]/div[2]/div/div/div[2]/div/div')) > 0):
        participants = int(driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[3]/div[2]/div/div/div[2]/div/div').text)
        if(participants > 10):
            print("Predavanje u toku...")
        else:
            print("Predavanje zavrsilo!")
            driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[2]/div/div[6]/span/button').click()
            sleep(5)
            break;
        break;
    else:
        print("Niste usli na predavanje...")



input("> ")
driver.quit()