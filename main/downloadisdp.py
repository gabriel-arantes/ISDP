from functions import *

driver = webdriver.Chrome(executable_path="D:\\ISDP\\chromedriver.exe")

openISDP(driver)
time.sleep(2)
site_login("D:/ISDP/csv/login.csv", driver)
chooseProject(driver)
searchLista("D:/ISDP/csv/lista.csv", driver, "rpSearchKey", "aGlobalSearch")
milestone = driver.find_element_by_xpath("//div[@title='HOL DOCUMENTAÇÃO CHECKLIST  WL']")
try:
    element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//div[@title='HOL DOCUMENTAÇÃO CHECKLIST  WL']"))
    )
except:
    print("Problemas de conexão")

actions = ActionChains(driver)
actions.move_to_element(milestone).perform()

try:
    element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='webix_ss_center_scroll']//div[@class='webix_column dt_header_tool']"
            "//span[@class='rp-blankIcon']"
            "//a[contains(@onclick, 'isd.rp.common.viewAttachment(')]"))
    )
except:
    print("Problemas de conexão")

elements = driver.find_elements_by_xpath(
            "//div[@class='webix_ss_center_scroll']//div[@class='webix_column dt_header_tool']"
            "//span[@class='rp-blankIcon']"
            "//a[contains(@onclick, 'isd.rp.common.viewAttachment(')]")

homepage = driver.window_handles[0]
sitewindows = []
i = 1

for element in elements:
    if i <= 1:
        element.click()
        element.click()
    else:
        element.click()
    try:
        element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Checklist"))
        )
    except:
        print("Problemas de conexão")


    driver.find_element_by_partial_link_text("Checklist").click()
    time.sleep(3)
    sitewindows.append(driver.window_handles[i])
    driver.switch_to.window(homepage)
    try:
        element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "close"))
        )
    except:
        print("Problemas de conexão")

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
ctypes.windll.user32.MessageBoxW(0, "Download Completo.", "Voilà", 0)
