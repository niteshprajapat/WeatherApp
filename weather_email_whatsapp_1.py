
# ============================= import required modules  =========================================

import smtplib
import time
import requests
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



# ============================ using API to fetch data (openweathermap.org) ======================

user_api = pyautogui.prompt("Enter API token")
location = pyautogui.prompt("Enter Location Here ")
api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + user_api


# ============================= sending information via email ID & whatsapp ======================

your_email = pyautogui.prompt("Enter Your Email Address")
your_pwd = pyautogui.prompt("Enter Your Password")
target_email = ['target_email-1', 'ptarget_email-2','........']

whats_no = [911234567890, 912131415161, 919089786756]   # number should be in int


# ============================== retrieving data ================================================

api = requests.get(api_link)
api_json_data = api.json()

#===================================== WEATHER ================================================

def weather():
    try:
        if not(api_json_data['cod'] == '404'):
            city_temp = (api_json_data['main']['temp']) - 273 
            weather_desc = api_json_data['weather'][0]['description']
            humidity = api_json_data['main']['humidity']
            pressure = api_json_data['main']['pressure']
            # sea_level = api_data['main']['sea_level']   This is optional because some location showing error while retrieving data . 
            wind_speed = api_json_data['wind']['speed']

            output = (f"\n\t\t Location = {location}\n\nCity Temperature is ==>> {city_temp} deg C \nWeathe Description ==>> {weather_desc} \nHumidity is ==>> {humidity}% \nCurrent Pressure is ==>> {pressure} pa \nCurrent Wind Speed is ==>> {wind_speed} m/s")

            return output

            
    except Exception as e:
        print(f"Error >> {e}")


# ======================================== EMAIL =================================================

def email():
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(your_email,your_pwd)
        time.sleep(2)
        server.sendmail(your_email,target_email, f"Subject : Weather Information\n{output_data}")
        server.close()

    except Exception as ex:
        print(f"Email error >> {ex}")


# ========================================= WHATSAPP ===========================================

def whtsapp():
    try:
        driver = webdriver.Firefox()
        for i in whats_no:
            driver.maximize_window()
            driver.get("https://web.whatsapp.com/send?phone=" + str(i))
            time.sleep(5)
            driver.get("https://web.whatsapp.com/send?phone=" + str(i))
            time.sleep(5)
            msg = driver.find_element_by_css_selector("html.js.serviceworker.adownload.cssanimations.csstransitions.webp.webp-alpha.webp-animation.webp-lossless body.web div#app div._347-w._2UMYL.app-wrapper-web.os-win div.h70RQ.two div._1-iDe.Wu52Z div#main._2BuJM footer._2vJ01 div._3ee1T._1LkpH.copyable-area div._3uMse div._2FVVk._2UL8j div._3FRCZ.copyable-text.selectable-text")
            msg.send_keys(output_data)
            msg.send_keys(Keys.ENTER)
            time.sleep(5)


    except Exception as whts_ex:
        print(f"Whatsapp error >> {whts_ex}")


output = weather()
output_data = output


# ==========================================================================================================#

while True:
    email()
    print("Email Sent. Please Checkout!!")
    time.sleep(2)
    whtsapp()
    print("Whatsapp Message Sent. Please Checkout!!")
    time.sleep(2)


    