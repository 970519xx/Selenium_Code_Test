from selenium import webdriver


chrome_path = r"C:\Users\SUNMOON\OneDrive\Images\Documents\Selenium Codes\chromedriver.exe"


driver = webdriver.Chrome(chrome_path)

driver.get("https://www.google.com")


search_box = driver.find_element_by_name("q")
search_box.send_keys("voiture")


search_box.submit()

first_image = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img')


image_url = first_image.get_attribute("src")

driver.quit()

