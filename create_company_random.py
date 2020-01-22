from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import string
import random

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://dev.local.hrketing.ru/auth/signin")
        driver.maximize_window()
        driver.find_element_by_name("email").send_keys("HrkViktorov@yandex.ru")
        driver.find_element_by_name("password").send_keys("Sa2589NS")
        driver.find_element_by_css_selector('button[type="submit"]').click()
        driver.find_element_by_xpath('//*[@id="react-app"]/div/div/div[1]/div/div/div[3]/nav/ul/li/span').click()
        driver.find_element_by_xpath('//*[@id="react-app"]/div/div/div[1]/div/div/div[3]/nav/ul/li/ul/li[1]/a').click()

        driver.find_element_by_link_text(u"Компании").click()
        actions = ActionChains(driver)
        actions.move_by_offset(100, 100).perform()
        time.sleep(1)
        actions.click().perform()
        driver.refresh()
        driver.find_element_by_css_selector(
            '#react-app > div > div > div.viewControls__StretchWrapper-sc-18h7ht4-2.DvXOO > div > div.viewControls__Header-sc-18h7ht4-6.jLQYqQ > div.viewControls__Favorites-sc-18h7ht4-37.evfGnl > div > a').click()

        try:
            element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "name"))
    )

        finally:
            company_name = driver.find_element_by_css_selector('[name=name]')
        N = random.randint(5,12)
        company_name_random = (''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(N)))
        company_name_random = company_name_random.capitalize()
        company_name.send_keys('Компания ' + company_name_random)

        rus = ord('а')
        random_rus = (''.join([chr(i) for i in range(rus, rus + 32)]))
        N = random.randint(5, 14)
        juridical_name_random = (''.join(random.choice(random_rus) for _ in range(N)))

        juridical_name = driver.find_element_by_name('juridical.name')
        juridical_name_random = juridical_name_random.capitalize()
        juridical_name.send_keys(juridical_name_random)

        N = random.randint(5, 14)
        juridical_fullName_random = (''.join(random.choice(random_rus) for _ in range(N)))
        juridical_fullName = driver.find_element_by_name('juridical.fullName')
        juridical_fullName_random = juridical_fullName_random.capitalize()
        juridical_fullName.send_keys(juridical_fullName_random)

        juridical_ogrn_random = random.randint(100000000, 999999999)
        juridical_ogrn = driver.find_element_by_name('juridical.ogrn')
        juridical_ogrn.send_keys(juridical_ogrn_random)

        juridical_inn_rangom = random.randint(100000000, 999999999)
        juridical_inn = driver.find_element_by_name('juridical.inn')
        juridical_inn.send_keys(juridical_inn_rangom)

        N = random.randint(5, 14)
        department_name_random = (''.join(random.choice(random_rus) for _ in range(N)))
        department_name = driver.find_element_by_name('defaultDepartmentName')
        department_name_random = department_name_random.capitalize()
        department_name.send_keys('Департамент ' + department_name_random)

        N = random.randint(5, 14)
        project_name_random = (''.join(random.choice(random_rus) for _ in range(N)))
        project_name = driver.find_element_by_name('defaultProjectName')
        project_name_random = project_name_random.capitalize()
        project_name.send_keys('Проект ' + project_name_random )

        phone_number_random = random.randint(1000000000, 9999999999)
        phone_number = driver.find_element_by_css_selector('[name=defaultPhoneNumber')
        phone_number.send_keys('+7' + str(phone_number_random))

        N = random.randint(5, 12)
        user_email_random = (''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(N)))
        user_email = driver.find_element_by_name('defaultUserEmail')
        user_email.send_keys(user_email_random+'@email.ru')

        N = random.randint(1, 999)
        avia_purchase_commission = driver.find_element_by_name('companySettings.commissions.aviaPurchaseCommission')
        avia_purchase_commission.send_keys('\b')
        avia_purchase_commission.send_keys(N)

        N = random.randint(100, 999)
        avia_cancel_commission = driver.find_element_by_name('companySettings.commissions.aviaCancelCommission')
        avia_cancel_commission.send_keys('\b')
        avia_cancel_commission.send_keys(N)

        N = random.randint(100, 999)
        rails_purchase_commission = driver.find_element_by_name('companySettings.commissions.railsPurchaseCommission')
        rails_purchase_commission.send_keys('\b')
        rails_purchase_commission.send_keys(N)

        N = random.randint(100, 999)
        rails_cancel_commission = driver.find_element_by_name('companySettings.commissions.railsCancelCommission')
        rails_cancel_commission.send_keys('\b')
        rails_cancel_commission.send_keys(N)

        N = random.randint(100, 999)
        hotels_purchase_commission = driver.find_element_by_name('companySettings.commissions.hotelsPurchaseCommission')
        hotels_purchase_commission.send_keys('\b')
        hotels_purchase_commission.send_keys(N)

        N = random.randint(100, 999)
        hotels_cancel_commission = driver.find_element_by_name('companySettings.commissions.hotelsCancelCommission')
        hotels_cancel_commission.send_keys('\b')
        hotels_cancel_commission.send_keys(N)

        driver.find_element_by_css_selector(
            '#react-app > div > div > div.viewControls__StretchWrapper-sc-18h7ht4-2.DvXOO > form > div > div.controls__WrapperContent-sc-19fe775-2.hkWxqr > div.viewControls__Div-sc-18h7ht4-12.bzLNqz.row > div:nth-child(4) > div.tableControls__Table-sc-13ab6q9-4.jMlmFE > div:nth-child(1) > div.tableControls__TD-sc-13ab6q9-1.fAJjic > div > div:nth-child(1) > div > label > span.controls__LabelText-sc-1x0p6yk-2.faRSxS'
        ).click()

        time.sleep(20)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()