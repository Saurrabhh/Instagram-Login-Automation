# Instagram-Login-Automation
 We will be using this program for automating Instagram to login .i.e We're creating a bot which takes our userID and password as input and login on instagram by itself.
 To perform this login automation we will need framework named Selenium (Selenium is an open-source tool that automates web browsers).
 
 TO INSTALL SELENIUM , first we need oue pip(python package install) working
 
 1. To check if pip is installed(usually it comes installed with python installer)-
      1. Open Command prompt window
      2. Write the following code:  
         pip
         
 2. To install selenium,write the following code on command prompt window: 
        pip install selenium
        
 3. Now we need to install the chrome web driver (we're using google chrome as our interface), To download the Chrome web driver
    go to this website and download chrome web driver for your version of google chrome (https://sites.google.com/a/chromium.org/chromedriver/downloads)
    
    NOTE - Check your version of google chrome on Help section before downloading chrome web driver
    
    Now once you've downloaded the chrome web driver extract the file named "chromedriver" move it to the directory (C:\Program Files (x86))
    
 4.Now to import the selenium on your program use the following codes
    from selenium import webdriver
    
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    
    driver.get("THE WEBSITE YOU WANT TO SCRAP") #in this case we're using instagram.com
    so the code will be
    driver.get("https://www.instagram.com")
         
 
