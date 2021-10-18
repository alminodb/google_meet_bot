from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


from time import sleep, gmtime

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

email = ""
password = ""

#meet_link = "https://meet.google.com/tnh-eowd-vtc"             #telekomunikacije i prijenos podataka
#meet_link = "https://meet.google.com/lookup/gutpwcfpgh"
#meet_link = "https://meet.google.com/ffb-tdpi-mog?hs=224"
#meet_link = "https://meet.google.com/cms-abxw-ciu"
#meet_link = "https://meet.google.com/nth-kekq-jfs"              #tehnicki engleski jezik

driver.get("https://www.gmail.com")
sleep(1)

driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(email, Keys.RETURN)
while True:
    sleep(3)
    try:
        driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password, Keys.RETURN)
        break
    except:
        pass

sleep(5)
driver.get(meet_link)

meetStarted = False
while True:
    sleep(10)
    if(len(driver.find_elements_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[3]/div[2]/div/div/div[2]/div/div')) > 0):
        participants = int(driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[3]/div[2]/div/div/div[2]/div/div').text)
        if(meetStarted and participants > 15):
            print("Predavanje u toku...")
        elif(not meetStarted and participants >= 25):
            meetStarted = True
        elif(meetStarted and participants < 15):
            print("Predavanje zavrsilo!")
            driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[2]/div/div[6]/span/button').click()
            sleep(5)
            break
        else:
            print("Ceka se pocetak predavanja..")
    else:
        print("Niste usli na predavanje...")



sleep(1)
driver.quit()
