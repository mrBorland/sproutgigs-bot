import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from telegram import Bot
from telegram.ext import Updater, CommandHandler

# Твій токен телеграм-бота
TELEGRAM_API_TOKEN = "встав сюди токен"
CHAT_ID = "встав сюди chat_id"

# Логін від SproutGigs
SPROUT_EMAIL = "email@example.com"
SPROUT_PASSWORD = "password"

bot = Bot(token=TELEGRAM_API_TOKEN)

def send_telegram(msg):
    bot.send_message(chat_id=CHAT_ID, text=msg)

def sproutgigs_login():
    driver = webdriver.Chrome()
    driver.get("https://sproutgigs.com")
    time.sleep(3)

    email_input = driver.find_element(By.NAME, 'email')
    pass_input = driver.find_element(By.NAME, 'password')

    email_input.send_keys(SPROUT_EMAIL)
    pass_input.send_keys(SPROUT_PASSWORD)
    pass_input.send_keys(Keys.RETURN)

    time.sleep(5)
    return driver

def run_tasks(driver):
    # Тут буде логіка кліків
    send_telegram("Виконую завдання...")
    time.sleep(2)

def start_bot():
    send_telegram("Бот SproutGigs запущено!")
    driver = sproutgigs_login()
    while True:
        run_tasks(driver)
        time.sleep(60)

if __name__ == "__main__":
    start_bot()
