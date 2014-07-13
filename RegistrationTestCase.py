# -*- coding: utf-8 -*- 

from selenium import webdriver
import unittest

class RegistrationTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://anketolog.ru/user/account/registration')


    # registration with empty fields
    # Если нажать кнопку регистрации с пустыми полями, должны свалидироваться пустые поля
    def test_empty_fields(self):
        self.driver.find_element_by_xpath("//button [@type = 'submit']").click()
        elements = self.driver.find_elements_by_class_name('help-block')

        errors = []
        for item in elements:
            errors.append(item.text)

        condition = [u'Необходимо заполнить поле Email.',
                     u'Необходимо заполнить поле Пароль.',
                     u'Необходимо заполнить поле Повтор пароля.',
                     u'Неправильный код проверки.']
        
        self.assertEqual(errors, condition)


    # if email is not valid
    # Если ввести невалидный email, должно вывестись сообщение 'Email не является правильным E-Mail адресом.'
    def test_notvalid_email(self):
        self.driver.find_element_by_xpath("//input [@id = 'id-f1404089628-email']").send_keys('testgmail.com')
        self.driver.find_element_by_xpath("//button [@type = 'submit']").click()

        element = self.driver.find_element_by_xpath("//div[@class = 'help-block']")
        self.assertEqual(element.text, u'Email не является правильным E-Mail адресом.')


    # passwords do not match
    # Если пароль и повторенный пароль не совпадают, должно вывестись сообщение 'Пароль должен быть повторен в точности'
    def test_password_comparison(self):
        self.driver.find_element_by_xpath("//input [@id = 'id-f1404089628-email']").send_keys('test@gmail.com')
        self.driver.find_element_by_xpath("//input [@id = 'id-f1404089628-password']").send_keys('123455')
        self.driver.find_element_by_xpath("//input [@id = 'id-f1404089628-confirm']").send_keys('123456')
        self.driver.find_element_by_xpath("//button [@type = 'submit']").click()

        element = self.driver.find_element_by_xpath("//div[@class = 'help-block']")
        self.assertEqual(element.text, u'Пароль должен быть повторен в точности')


    # short password
    # Если введен короткий пароль, должно вывестись сообщение 'Минимальная длина пароля - 6 символов'
    def test_short_password(self):
        self.driver.find_element_by_xpath("//input [@id = 'id-f1404089628-email']").send_keys('test@gmail.com')
        self.driver.find_element_by_xpath("//input [@id = 'id-f1404089628-password']").send_keys('123')
        self.driver.find_element_by_xpath("//button [@type = 'submit']").click()

        element = self.driver.find_element_by_xpath("//div[@class = 'help-block']")
        self.assertEqual(element.text, u'Минимальная длина пароля - 6 символов')


     # incorrect captcha
     # Если неправильно введена капча, должно вывестись сообщение 'Неправильный код проверки.'
    def test_incorrect_captcha(self):
         self.driver.find_element_by_xpath("//input [@id = 'id-f1404089628-email']").send_keys('test@gmail.com')
         self.driver.find_element_by_xpath("//input [@id = 'id-f1404089628-password']").send_keys('123456')
         self.driver.find_element_by_xpath("//input [@id = 'id-f1404089628-confirm']").send_keys('123456')
         self.driver.find_element_by_xpath("//input [@id = 'id-f1404089628-captcha']").send_keys('123')
         self.driver.find_element_by_xpath("//button [@type = 'submit']").click()

         element = self.driver.find_element_by_xpath("//div[@class = 'help-block']")
         self.assertEqual(element.text, u'Неправильный код проверки.')


    # Email already exists
    # Если введеный email уже используется, должно выводиться сообщение, что данный email уже занят
    def test_email_exists(self):
         self.driver.find_element_by_xpath("//input [@id = 'id-f1404089628-email']").send_keys('kate22test@gmail.com')
         self.driver.find_element_by_xpath("//input [@id = 'id-f1404089628-password']").send_keys('123456')
         self.driver.find_element_by_xpath("//input [@id = 'id-f1404089628-confirm']").send_keys('123456')
         self.driver.find_element_by_xpath("//button [@type = 'submit']").click()

         element = self.driver.find_element_by_xpath("//div[@class = 'help-block']")
         self.assertEqual(element.text, u'Email "kate22test@gmail.com" уже занят.')


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
