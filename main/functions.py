import csv
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import ctypes  # An included library with Python install.

def openISDP(driver):
    driver.get('http://app-br.huawei.com/sdcp/portalNew#!isd/webix/rolloutPlanManagment.html')
    driver.maximize_window()
    time.sleep(2)

def site_login(filepath,driver):
    try:
        element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.NAME, "Submit"))
        )
    except:
        print("Problemas de conexão")

    with open(filepath, "r") as th:
        lines = csv.reader(th)
        for line in lines:
            username = line[0]
            password = next(lines)
            driver.find_element_by_id("uid").send_keys(username)
            driver.find_element_by_id("password").send_keys(password)
            driver.find_element_by_name("Submit").click()


def chooseProject(driver):
    try:
        element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='project']"))
        )
    except:
        print("Problemas de conexão")

    driver.find_element_by_xpath("//div[@class='project']").click()
    try:
        element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//ul[@id='project-list']//li//strong[.='56A02A1']"))
        )
    except:
        print("Problemas de conexão")

    driver.find_element_by_xpath("//ul[@id='project-list']//li//strong[.='56A02A1']").click()


def readCSV(filepath):
    with open(filepath, "r") as fh:
        lines = csv.reader(fh)
        i = 0
        sites = []
        for line in lines:
            site = line[i] + ","
            sites.append(site)
    return sites


def searchLista(filepath, driver):
    sitesCSV = readCSV(filepath)
    try:
        element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "aGlobalSearch"))
        )
    except:
        print("Problemas de conexão")
    time.sleep(2)
    driver.find_element_by_id("rpSearchKey").send_keys(sitesCSV)
    time.sleep(2)
    driver.find_element_by_id("aGlobalSearch").click()


def scrollToElement(element, driver):
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
