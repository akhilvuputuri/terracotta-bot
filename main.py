from selenium import webdriver

def getDriver(url):

    '''
    Main logic behind creating a driver object to use FireFox web browser
    Arguments:
        url(str): Target url
    
    Returns:
        Firefox webdriver instance in python
    '''
    profile = webdriver.FirefoxProfile()
    profile.accept_untrusted_certs = True
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--headless")
    firefox_options.add_argument("--no-sandbox")
    firefox_options.add_argument("--disable-dev-shm-usage")
    firefox_options.add_argument("--disable-gpu")
    driver = webdriver.Firefox(firefox_options = firefox_options,firefox_profile = profile)
    driver.get(url)
    return driver
  
driver = getDriver("https://10.10.0.112/");
driver.get("https://10.10.0.112/")
driver.quit()
