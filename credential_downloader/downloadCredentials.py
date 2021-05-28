import time 
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import os.path
from os import path
import shutil
import getpass

credentialsFile = os.path.expanduser('~') + os.sep + "Downloads" + os.sep + "credentials"
allKeysFile = os.path.expanduser('~') + os.sep + "Downloads" + os.sep + "allCredentials"
awsCredentials = os.path.expanduser('~') + os.sep + ".aws" + os.sep + "credentials"
myNetworkDir = "H:" + os.sep + getpass.getuser() + os.sep

def isFileDownloaded(driver):
   if path.isfile(credentialsFile):
      return True
   else:
      return False

def isDuoScreenLoaded(driver):
   try:
      if driver.find_element_by_id("duo_iframe"):
         return True
   except:
      return False

def isAWSAccountDropdownAvailable(driver):
   try:
      if driver.find_element_by_id("aws-name"):
         return True
   except:
      return False

def getCredentials(awsNameBox, envName):
    tokens = envName.split("_")
    #env = "[" + tokens[4]+"_"+tokens[3] + "]\n"
    env = "[" + tokens[4]+"-"+tokens[3] + "]\n"
    env = env.lower()
    awsNameBox.select_by_visible_text(envName)
    selectRoleBoxElement = driver.find_element_by_id("aws-role")
    selectRoleBox = webdriver.support.select.Select(selectRoleBoxElement)

    try:
      selectRoleBox.select_by_visible_text("LZ_DevOps")
      # Locate Get Credentials button
      getCredsButton = driver.find_element_by_xpath("/html/body/div/div/div[2]/form/button")
      getCredsButton.click()

      ## Click Download Credentials button
      downloadCreds = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/a[2]")
      downloadCreds.click()
      WebDriverWait(driver,25).until(isFileDownloaded)
      with open(credentialsFile) as f:
         lines = f.readlines()
      os.remove(credentialsFile)
      lines = [env if line.strip('\n')=='[default]' else line for line in lines]
    except NoSuchElementException as e:
       print("Looks like Role (LZ_DevOps) not found!",e)
       return ''

    return lines

if __name__ == "__main__":
   driver = webdriver.Chrome()
   driver.get('https://sso.centene.com/AWSPortal-LZ');
   WebDriverWait(driver,90).until(isDuoScreenLoaded)
   driver.switch_to.frame("duo_iframe")
   #auth_buttons = driver.find_element_by_xpath("//*[@id='auth_methods']/fieldset/div[1]/button")

   ActionChains(driver).click(driver.find_element_by_xpath("//*[@id='auth_methods']/fieldset/div[1]/button")).perform()
   #auth_buttons.click()
   driver.implicitly_wait(5)
   driver.switch_to.default_content()
   WebDriverWait(driver,90).until(isAWSAccountDropdownAvailable)
   selectBoxElement = driver.find_element_by_id("aws-name")
   selectBox = webdriver.support.select.Select(selectBoxElement)
   values = []
   for option in selectBox.options:
      values.append(option.text)

   with open(allKeysFile, "w") as f1:
      for value in values:
         if value :
            print("Downloading for :",value)
            lines = getCredentials(selectBox,value)
            if lines :
               for line in lines:
                  line = line.replace("AWS_ACCESS_KEY_ID=","aws_access_key_id=")
                  line = line.replace("AWS_SECRET_ACCESS_KEY=","aws_secret_access_key=")
                  line = line.replace("AWS_SESSION_TOKEN=","aws_session_token=")
                  f1.writelines(line)
               f1.write("\n")
               f1.write("region=us-east-1\n")
            selectBoxElement = driver.find_element_by_id("aws-name")
            selectBox = webdriver.support.select.Select(selectBoxElement)
   ## All done now move the file to .aws folder
   shutil.move(allKeysFile,awsCredentials)
   shutil.copy(awsCredentials,myNetworkDir)
   print("All done.")
   driver.quit()
