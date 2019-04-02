from functions import *

driver = webdriver.Chrome(executable_path="D:\ISDP\chromedriver.exe")

driver.get('http://app-br.huawei.com/sdcp/esurvey/esurvey')
driver.maximize_window()
time.sleep(2)
site_login("D:/ISDP/csv/login.csv", driver)
chooseProject(driver)
time.sleep(3)
driver.find_element_by_class_name("allTaskTotal").click()
searchLista("D:/ISDP/csv/lista.csv", driver, "taskManager_number_id", "taskManager_table_search_btn")
time.sleep(3)
select = driver.find_element_by_class_name("jalor-pager-pagesize")
scrollToElement(select, driver)
select.click()
time.sleep(2)
driver.find_element_by_xpath("//option[@value='500']").click()
time.sleep(2)

try:
    element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jalor-link-btn"))
    )
except:
    print("Problemas de conexão")

siteslinks = driver.find_elements_by_xpath('//a[contains(@onclick, "indexRenderTable.dataUrlOnClickView(")]')
homepage = driver.window_handles[0]
sitewindows = []
i = 1

for sitelink in siteslinks:
    scrollToElement(sitelink, driver)
    sitelink.click()
    sitewindows.append(driver.window_handles[i])
    driver.switch_to.window(homepage)
    time.sleep(1)
    i = i + 1

for sitewindow in sitewindows:
    driver.switch_to.window(sitewindow)
    try:
        element = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//li[@tabid='attachmentModelTab']"))
        )
    except:
        print("")

    driver.find_element_by_xpath("//li[@tabid='attachmentModelTab']").click()
    time.sleep(2)
    wtf = driver.find_elements_by_class_name("oneAttachmentDiv")
    wtf[2].click()
    try:
        element = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//img[contains(@onclick, ".zip")]'))
        )
    except:
        print("")
    driver.find_element_by_xpath('//img[contains(@onclick, ".zip")]').click()
    time.sleep(5)
    driver.close()
ctypes.windll.user32.MessageBoxW(0, "Download Completo.", "Voilà", 0)
