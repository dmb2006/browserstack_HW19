import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be, have


@allure.tag('mobile android')
@allure.title('открытие странице через моб браезер')
@allure.story('TEST-001')
class AppAndroid:
    def open_app_android(self):
        with allure.step('Открытие страницы wikipedia'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).should(be.visible).click()
        with allure.step('Поиск через поисковую строку наименования: BrowserStack'):
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).should(be.visible).send_keys(
                "BrowserStack")
        with allure.step('Проверка с найденными результатами'):
            browser.all(
                (AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')
            ).should(have.size_greater_than(0))

    def open_app_android_search(self):
        with allure.step('Открытие страницы wikipedia'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).should(be.visible).click()
        with allure.step('Поиск через поисковую строку наименования: Python'):
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).should(be.visible).send_keys('Python')
        with allure.step('Проверка с найденными результатами'):
            results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
            results.should(have.size_greater_than(0))
            results.first.should(have.text('Python'))
        with allure.step('Клик по первому элементу'):
            results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
            results.first.click()