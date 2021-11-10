from selenium import webdriver
import os
import shutil


class PythonSelenium:
    
    def __init__(self, webdriverVal):
        driver = webdriverVal
        
    def setup(self):
        print("Execute Chrome webdriver")
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(15)
        
       
    def launchWeb(self):
        print("Launch Website")
        driver.get("Enter Website Link")
        
        file = r".../pwd.txt"
        with open(file, 'r') as f:
            password = f.readline().rstrip()        
      
        username = "username"
        password = password   
        
        print("Admin Login Page")
        driver.find_element_by_id("admin_email").send_keys(username)
        driver.implicitly_wait(10)
        driver.find_element_by_id("admin_password").send_keys(password)
        driver.implicitly_wait(10)
        driver.find_element_by_name("commit").click()

    
    def mfaToken(self, MFA):
        
        print('MFA token')
        driver.find_element_by_id("admin_otp_attempt").send_keys(MFA)
        driver.implicitly_wait(10)
        driver.find_element_by_name("commit").click()

        print("Click on Admin button")
        driver.find_element_by_xpath("//a[@href='Enter href link']").click()
        driver.find_element_by_xpath("//a[@href='Enter href link']").click()
        driver.implicitly_wait(10)
        
        
    def downloadFile(self, startDate, endDate):
        
        #startDate = '2021-11-01'
        #endDate = '2021-11-02'
        
        print("Click on Download button")
        driver.find_element_by_id("q_created_at_gteq").send_keys(startDate)
        driver.find_element_by_id("q_created_at_lteq").send_keys(endDate)
        driver.find_element_by_name("commit").click()
        
        print("Click on Admin SignOut button")
        driver.find_element_by_xpath("//a[@href='Enter href link']").click()
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(20)


    def quitApp(self):
        print("Quit Application")        
        driver.quit()



def moveFiles(sourceFolder, file, destinationFolder):
    sourcePath = sourceFolder+'/'+file
    destinationPath = destinationFolder+'/'+file

    if os.listdir(destinationFolder) == file:
        print(file, 'exists in the destination folder')
        os.remove(destinationPath)
        print(file, 'deleted in', destinationFolder)
    else:
        shutil.move(sourcePath, destinationFolder)
        print(file, 'successfully moved to', destinationFolder)
        


if __name__ == '__main__':   
    driver = webdriver.Chrome("Enter chrome driver path")
    obj = PythonSelenium(driver)
    obj.setup()
    obj.launchWeb()
    print("Enter MFA token")
    MFA = int(input)
    obj.mfaToken(MFA)
    print("Enter start date in YYYY-MM-DD format")
    startDate = input()
    print("Enter end date in YYYY-MM-DD format")
    endDate = input()
    obj.downloadFile(startDate, endDate)
    obj.quitApp()
    
    print("Prepare to move downloaded excel file to the destination path")
    sourceFolder =  r"source folder"
    file = r"filename.xlsx"
    destinationFolder = r"destination folder"
    moveFiles(sourceFolder, file, destinationFolder)
    
