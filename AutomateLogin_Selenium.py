from selenium import webdriver
import os
import shutil
import time

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
        driver.implicitly_wait(600) # 10 minutes
        time.sleep(600) # 10 minutes


    def quitApp(self):
        print("Quit Application")        
        driver.quit()


class UserInput:

    def MFA_UserInput(self):
        n =  input("Enter MFA token: " )
        check = str(input("Confirm MFA token (y/n): ")).lower().strip()
        try: 
            if check[0] == 'y':
                return n
            elif check[0] == 'n':
                return UserInput.MFA_UserInput(self)
            else: 
                return UserInput.MFA_UserInput(self)
        except Exception as error:
            print("Please enter valid inputs")
            print(error)
            return UserInput.MFA_UserInput(self)
        
        
    def DateInput(self):
        dd = input("Enter date in YYYY-MM-DD format: " )
        check = str(input("Confirm date entered (y/n): ")).lower().strip()
        try: 
            if check[0] == 'y':
                return dd
            elif check[0] == 'n':
                return UserInput.DateInput(self)
            else: 
                return UserInput.DateInput(self)
        except Exception as error:
            print("Please enter valid inputs")
            print(error)
            return UserInput.DateInput(self)
        
        

def moveFiles(sourceFolder, file, destinationFolder):
        
    sourcePath = sourceFolder+'/'+file
    destinationPath = destinationFolder+'/'+file

    if os.path.exists(destinationPath):
        print(file, 'exists in the destination folder')
        os.remove(destinationPath)
        print(file, 'deleted in', destinationFolder)
        shutil.move(sourcePath, destinationFolder)
        print(file, 'successfully moved to', destinationFolder)
    else:
        shutil.move(sourcePath, destinationFolder)
        print(file, 'successfully moved to', destinationFolder)
        


if __name__ == '__main__':   
    driver = webdriver.Chrome("Enter chrome driver path")
    obj = PythonSelenium(driver)
    obj.setup()
    obj.launchWeb()
    
    print("====MFA token required====")
    usr = UserInput()
    MFA = usr.MFA_UserInput()
    obj.mfaToken(MFA)
    
    print("====Start date required in YYYY-MM-DD format====")    
    startDate = usr.DateInput()
    print("====End date required in YYYY-MM-DD format====")
    endDate = usr.DateInput()
    obj.downloadFile(startDate, endDate)
    
    obj.quitApp()
    
    print("====Prepare to move downloaded excel file to the destination path====")
    sourceFolder =  r"source Folder"
    file = r"filename.xlsx"
    destinationFolder = r"dest folder"
    moveFiles(sourceFolder, file, destinationFolder)
