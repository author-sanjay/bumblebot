import os,random,sys,time
from selenium import  webdriver
from urllib.parse import urlparse
from selenium.webdriver.chrome.service import Service

baseurl="https://bumble.com/get-started"

driverlink="/home/sanju/Downloads/chromedriver"

configfile="/home/sanju/PycharmProjects/bumblebot/config.txt"
file=open(configfile)
line=file.readlines()
myphonenumber=line[0]

# website=baseurl+"/uas/login?fromSignIn=true&trk=cold_join_sign_in"
service=Service(executable_path=driverlink)
driver=webdriver.Chrome(service=service)
driver.get(baseurl)

login=driver.find_element(by="xpath",value='/html/body/div/div/div[1]/div[2]/main/div/div[3]/form/div[3]/div')
driver.execute_script("arguments[0].click();", login)
enternumber=driver.find_element(by="xpath",value='//*[@id="phone"]')
driver.execute_script("arguments[0].click();", enternumber)
time.sleep(2)
enternumber.send_keys(myphonenumber)
time.sleep(3)
print("Done")
clicktologin=driver.find_element(by="xpath",value='//*[@id="main"]/div/div[1]/div[2]/main/div/div[3]/form/div[4]/button')
driver.execute_script("arguments[0].click();", clicktologin)
time.sleep(60)
print("Done")

for i in range(0,100):
    like=driver.find_element(by="xpath",value='//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div/div[1]/span').click();
    # driver.execute_script("arguments[0].click();", like)
    time.sleep(5)
    print("Hello")
    i=i+1
