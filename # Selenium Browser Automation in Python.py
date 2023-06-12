# Selenium Browser Automation in Python 

# via @NeuralNine

# pip install selenium + pip install webdriver-manager

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
			  options=options)

driver.get("https://www.neuralnine.com/")
driver.maximize_window()

links = driver.find_elements("xpath", "//a[@href]")
for link in links:
    #print(link.get_attribute("innerHTML"))
	if "Books" in link.get_attribute("innerHTML"):
		link.click()
		break 


book_links = driver.find_elements("xpath",
				  				  "//div[contains(@class, 'elementor-column-wrap')][.//h2[text()[contains(., '7 IN 1')]]][count(.//a)=2]//a")

book_links[0].click()

driver.switch_to.window(driver.window_handles[1])

time.sleep(3)
buttons = driver.find_elements("xpath", "//a[.//span[text()[contains(.,	'Paperback')]]]//span[text()[contains(., '$')]]")

for button in buttons:
	print('-=-'*30)
	print("O preço do livro em dólar é:\n")
	print(button.get_attribute("innerHTML"))
	print('-=-'*30)



