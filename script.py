from selenium import webdriver
# driver = webdriver.Chrome(r"C:\Users\dkaggs\Downloads\Compressed\chromedriver_win32\chromedriver.exe")
driver = webdriver.Firefox(r"C:\Users\dkaggs\Downloads\Compressed\geckodriver-v0.27.0-win64")
driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element_by_name("btnI").send_keys("javatpoint")
time.sleep(3)
driver.close()
print("sample test case successfully completed")