from functions import *
import pyperclip
from keyboard import press, release
from os import listdir
from os.path import isfile, join
from pynput.keyboard import Key, Controller



driver = webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")
keyboard = Controller()

openISDP(driver)
site_login("D:/csv/login.csv", driver)
chooseProject(driver)
searchLista("D:/csv/lista.csv", driver)

try:
    element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//div[@title='HOL checklist + ETC Granite + Netwin']"))
    )
except:
    print("Problemas de conexão")

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
extrawindows = []
sitesnames= driver.find_elements_by_xpath("//a[@class='jalor-link-btn' and contains(@onclick,'7')]")
nomesdascaralha = []
lista = []
i = 0
z = 0

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
    w = len(sitewindows)
    y = 1
    filepath = "D:\\upload\\"
    name = lista[z]
    files = [f for f in listdir(filepath + name) if isfile(join(filepath + name, f))]
    driver.switch_to.window(sitewindow)
    capiroto = driver.find_element_by_id('taskFileManageUnstructGrdOuter')
    scrollToElement(capiroto, driver)

    for file in files:
        driver.find_element_by_xpath("//a[contains(@onclick,'7')]").click()
        time.sleep(3)
        extrawindows.append(driver.window_handles[(len(sitesnames) + y)])
        driver.switch_to.window(extrawindows[y - 1])

        try:
            element = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.ID, "uploader_browse"))
            )
        except:
            print("Problemas de conexão")

        driver.find_element_by_id("uploader_browse").click()
        time.sleep(1)
        pyperclip.copy(name + "\\" + file)

        for char in filepath:
            keyboard.press(char)
            keyboard.release(char)
        press('ctrl')
        press('v')
        release('ctrl')
        release('v')
        time.sleep(1)
        press('enter')
        driver.switch_to.window(sitewindow)
        y = y + 1

    WebDriverWait(driver, 20).until(EC.number_of_windows_to_be(len(sitesnames) + 1))
    driver.switch_to.window(sitewindow)
    extrawindows.clear()
    z = z + 1

for sitewindow in sitewindows:
    buttonxpath = "//div[@class='jalor-dialog jalor-popup message-box modal onlyone share_notice_width']" \
                  "//div[@class='jalor-dialog-head unselect']" \
                  "//div[@class='jalor-dialog-close']" \
                  "//div[@class='jalor-dialog-closeimg']"
    driver.switch_to.window(sitewindow)

    try:
        element = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "callBackButton"))
        )
    except:
        print("")

    time.sleep(2)
    driver.find_element_by_id("callBackButton").click()

    try:
        element = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, buttonxpath))
        )
    except:
        print("")

    driver.find_element_by_xpath(buttonxpath).click()
    time.sleep(1)
    driver.find_element_by_id("callBackButton").click()
ctypes.windll.user32.MessageBoxW(0, "Upload Completo.", "Voilà", 0)
