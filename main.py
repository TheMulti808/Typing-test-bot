from cmd import IDENTCHARS
from tkinter import W
from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys, time, pydirectinput

PATH = "C:\Program Files (x86)\chromedriver.exe" #selenium chrome driver path
driver = webdriver.Chrome(PATH)
sleepDelay = 0
siteLink = "https://www.typing.academy/typing-tutor/typing-test"


def wfe(driver, byWhat, arg): #wait for element, function because im lazy
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((byWhat, arg)))
    return element


def main():
    try: #login
        driver.get(siteLink)
        wfe(driver, By.CLASS_NAME, "dialog_confirm").click()
        wfe(driver, By.CLASS_NAME, "startcompare").click() 
        fingersContainer = wfe(driver, By.CLASS_NAME,'text-center')
        fingersContainer.find_element(by=By.TAG_NAME, value = "a").click()
        time.sleep(1)
        wfe(driver, By.ID, "reminder_local").click() 
        time.sleep(1)
        writerelement = wfe(driver, By.ID, "writer_text")
        while True:
            #time.sleep(sleepDelay)
            currentLetter = writerelement.find_element(by=By.CLASS_NAME, value='current').text
            pydirectinput.keyDown(currentLetter)
            pydirectinput.keyUp(currentLetter)
            try:
                tempElement = driver.find_element(by=By.ID, value='finished').text
                if tempElement: break
            except:
                pass
        
        wordsPerMin = wfe(driver, By.CLASS_NAME, "signs").text
        totalTime = wfe(driver, By.CLASS_NAME, "time").text
        print('Finished!', f"Words per min: {wordsPerMin}",f"Total time: {totalTime}")
        driver.quit()
        sys.exit()
    except Exception as e:
        print('Error, quiting application\n', e)
        driver.quit()


if __name__ == "__main__":
    main()