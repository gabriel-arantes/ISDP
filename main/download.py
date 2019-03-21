from functions import *

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

openISDP(driver)
site_login("D:/csv/login.csv", driver)
chooseProject(driver)
searchLista("D:/csv/lista.csv", driver)
milestone = driver.find_element_by_xpath("//div[@title='HOL DOCUMENTAÇÃO CHECKLIST  WL']")
scrollToElement(milestone, driver)

elements = driver.find_elements_by_xpath(
            "//div[@class='webix_ss_center_scroll']//div[@class='webix_column dt_header_tool']"
            "//span[@class='rp-blankIcon']"
            "//a[contains(@onclick, 'isd.rp.common.viewAttachment(')]")

homepage = driver.window_handles[0]
sitewindows = []
i = 0

for element in elements:
    if i <= 0:
        element.click()
        element.click()
    else:
        element.click()
    time.sleep(3)
    driver.find_element_by_partial_link_text("Checklist").click()
    time.sleep(2)
    sitewindows.append(driver.window_handles[1 + i])
    driver.switch_to.window(homepage)
    driver.find_element_by_id("close").click()
    i = i + 1

for sitewindow in sitewindows:
    driver.switch_to.window(sitewindow)
    janfdp = driver.find_element_by_class_name("closeicoimg")
    if janfdp.is_displayed():
        janfdp.click()

    driver.find_element_by_xpath("//label[contains(@onclick, 'downloadDocumentSubmit(')]").click()
    time.sleep(2)
    driver.close()
