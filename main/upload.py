from functions import *

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
uploadwindows = []
i = 0
sitesnames= driver.find_elements_by_xpath("//a[@class='jalor-link-btn' and contains(@onclick,'7')]")
nomesdascaralha = []
lista = []

for sitename in sitesnames:
    nomedacaralha = sitename.text
    nomesdascaralha.append(nomedacaralha)
    lista = [e[2:] for e in nomesdascaralha]

for element in elements:
    if i <= 0:
        element.click()
        element.click()
    else:
        element.click()
    time.sleep(2)
    sitewindows.append(driver.window_handles[1 + i])
    driver.switch_to.window(homepage)
    i = i + 1

for sitewindow in sitewindows:
    driver.switch_to.window(sitewindow)
    capiroto = driver.find_element_by_id('taskFileManageUnstructGrdOuter')
    scrollToElement(capiroto, driver)
    FDP = driver.find_element_by_xpath("//a[contains(@onclick,'7')]")
    FDP.click()
    uploadwindows.append(driver.window_handles[1 + i])
    i = i + 1
    time.sleep(2)

for uploadwindow in uploadwindows:
    driver.switch_to.window(uploadwindow)
driver.find_element_by_class_name("plupload_droptext").sendKeys("D://upload/*" + lista[i] + "*")
