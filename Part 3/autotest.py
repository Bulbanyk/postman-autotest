from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

def test_success_login():
    # Открытие браузера
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")

    # Ввод логина
    driver.find_element(By.ID, "user-name").send_keys("standard_user")

    # Ввод пароля
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # Нажатие на кнопку логина
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)  # Ждём переход

    # Проверка, что пользователь попал на страницу с товарами
    assert "inventory" in driver.current_url

    # Закрытие браузера
    driver.quit()
