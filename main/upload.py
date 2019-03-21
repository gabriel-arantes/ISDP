from selenium import webdriver
import time
from functions import *
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

openISDP(driver)
site_login("D:/csv/login.csv", driver)
chooseProject(driver)
searchLista("D:/csv/lista.csv", driver)
time.sleep(3)
milestone = driver.find_element_by_xpath("//div[@title='HOL checklist + ETC Granite + Netwin']")
scrollToElement(milestone, driver)
time.sleep(3)

elements = driver.find_elements_by_xpath(
            "//div[@class='webix_ss_center_scroll']//div[@class='webix_column dt_header_tool']"
            "//span[@class='rp-blankIcon']"
            "//a[contains(@onclick, 'isd.rp.common.upload(')]")
homepage = driver.window_handles[0]
sitewindows = []
i = 0

for element in elements:
    if i <= 0:
        element.click()
        element.click()
    else:
        element.click()
    time.sleep(8)
    element = driver.find_element_by_xpath("//*[@id='taskFileManageGrdView']//div[1]//p[1]//label")
    print(element)

    #// * [ @ id = 'taskFileManageGrdView'] // div[1] // p[4] // img
    #")

    #
    #// a[ @ onclick = 'JsTaskFileManage.TaskFileManage.uploadFileData('
    #6
    #'');'
    #scrollToElement(element, driver)
    sitewindows.append(driver.window_handles[1 + i])
    time.sleep(2)
    driver.find_element_by_xpath("//td[@_col = '1'//a[@onclick='JsTaskFileManage.TaskFileManage.uploadFileData('7');']").click()
    time.sleep(2)
    driver.switch_to.window(homepage)
    i = i + 1
