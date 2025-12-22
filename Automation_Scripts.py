from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

# Comunica ao codigo em qual celular ele deve "mandar"
capabilities = {
    "plataformName": "Android",
    "automationName": "UiAutomator2",
    "deviceName": "Samsung_Galaxy_S22",
    "appPackage": "com.exemplo.ecommerce",
    "appActivity": ".LoginActivity"
}

# Inicia a conexao com o servidor do Appium
driver = webdriver.Remote("http://localhost:4723/wd/hub", capabilities)

try:
    # Localiza os elementos na tela e interagi
    email_field = driver.find_element(by=AppiumBy.ID, value="com.exemplo:id/input_email")
    email_field.send_keys("marcelo.vinicius@email.com")

    pass_field = driver.find_element(by=AppiumBy.ID, value="com.exemplo:id/input_password")
    pass_field.send_keys("123456")

    login_button = driver.find_element(by=AppiumBy.ID, value="com.exemplo:id/btn_login")
    login_button.click()

    # Verificacao
    time.sleep(2)
    home_element = driver.find_element(by=AppiumBy.ID, value="com.exemplo:id/welcome_msg")

    if home_element.is_displayed():
        print("Test Result: PASS")
    else:
        print("Test Result: FAIL")

finally:
    driver.quit()