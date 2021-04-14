from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

browser = webdriver.Chrome(
    executable_path=r'/Users/romeo/Documents/chromedriver')
cookie = [
    {"name": "language", "value": "th"},
    {"name": "SPC_T_ID", "value": '"enKhR8ryz5sSZGevH98GFAj3v26cY+HJrhNe0sdYdfliGmAcqquHZVipW008e7fvn0RptQ2AJki0VLUQlFahbcbr+gPSJ3YirszRk5YnztA="'},
    {"name": "_fbp", "value": "fb.2.1617800706535.1524182412"},
    {"name": "SPC_F", "value": "gcWOR9zwmWt9EInuSymGXwgCpZ3qJKbu"},
    {"name": "SPC_R_T_ID", "value": '"enKhR8ryz5sSZGevH98GFAj3v26cY+HJrhNe0sdYdfliGmAcqquHZVipW008e7fvn0RptQ2AJki0VLUQlFahbcbr+gPSJ3YirszRk5YnztA="'},
    {"name": "SPC_SI", "value": "mall.rT7Pw8frB9zH63EOgRWUD0RlnrzxpsxL"},
    {"name": "SPC_IA", "value": "-1"},
]
# nintendo
link = sys.argv[3]
price = 100
# test
# link = "https://shopee.co.th/%F0%9F%92%A6%E0%B8%81%E0%B8%A5%E0%B8%B4%E0%B9%88%E0%B8%99%E0%B9%83%E0%B8%AB%E0%B8%A1%E0%B9%88%F0%9F%92%A6%E0%B8%AA%E0%B9%80%E0%B8%9B%E0%B8%A3%E0%B8%A2%E0%B9%8C%E0%B9%81%E0%B8%AD%E0%B8%A5%E0%B8%81%E0%B8%AD%E0%B8%AE%E0%B8%AD%E0%B8%A5%E0%B9%8C-75-v-v-30-60-110-ml-i.71181048.5629767187"


class CheckOut():
    def __init__(self):
        print("text")
        browser.get(link)
        for c in cookie:
            browser.add_cookie(c)
            time.sleep(2);

    def login(self, email, password):
        try:
            username = (browser.find_element_by_name("navbar__username").text)
            print("username")
            pass
        except Exception as e:
            print("fuck")
            browser.get('https://shopee.co.th/buyer/login')
            time.sleep(3)
            username = browser.find_element_by_name("loginKey")
            username.send_keys(email)
            passElement = browser.find_element_by_name("password")
            passElement.send_keys(password)
            time.sleep(2)
            browser.find_elements_by_xpath(
                '//*[@id="main"]/div/div[2]/div/div/form/div/div[2]/button')[0].click()
            time.sleep(3)
        else:
            pass
        finally:
            pass
        pass

    def buy(self):
        browser.get(link);
        time.sleep(2);
        # check price
        price = browser.find_elements_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[3]/div/div/div[1]/div/div[2]/div[1]')
        if(len(price) <= 0):
            print("wait for flash sale")
            return self.buy()
        price = price[0].text
        print(price)
        if price.find('-') >= 0:
            print('have -')
            browser.find_element_by_css_selector('.product-variation').click()
            price = browser.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[3]/div/div/div[1]/div/div[2]/div[1]')[0].text
            time.sleep(1)
            if price.find('-') >= 0:
                return self.buy()
            print('not have')
        calPrice = price.replace('฿','').replace(',','')
        print(calPrice)
        # if price < 100
        if(int(calPrice) < price):
            print("checkout")
            return self.checkout()
        else:
            print("price more than "+price)
            return self.buy();

    def checkout(self):
        # time.sleep(10)
        # buy
        browser.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[5]/div/div/button[2]').click()
        time.sleep(2)
        # buy
        print("buying..")
        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/div[7]/div[5]/button').click()
        time.sleep(2)

        # select checkout by cradit card
        print("checkout by cradit card")
        browser.find_elements_by_class_name('product-variation')[1].click()

        # change delivery
        print("change delivery..")
        browser.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[3]/div[2]/div[2]/div/div[2]/div[2]/div[3]').click()
        browser.find_element_by_xpath('//*[@id="modal"]/div[2]/div[1]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]').click()
        browser.find_element_by_xpath('//*[@id="modal"]/div[2]/div[1]/div[2]/div/button[2]').click()
        time.sleep(2)



        # check money again
        print("check money again")
        lastcheckPrice = browser.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[3]/div[4]/div[2]/div[6]').text
        lastcheckPrice = lastcheckPrice.replace('฿','')
        print(lastcheckPrice)
        if(int(lastcheckPrice) < price):
            print("checkout success")
            browser.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[3]/div[4]/div[2]/div[7]/button').click()
        else:
            print("fail checkout")


if __name__ == '__main__':
    checkOut = CheckOut();
    checkOut.login(sys.argv[1],sys.argv[2])
    checkOut.buy()
