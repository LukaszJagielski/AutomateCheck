from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time


# For Forcepoint check
"""
def FP_check():
	options = FirefoxOptions()
	options.add_argument("--headless")
	driver = webdriver.Firefox(options=options)
	driver.get('https://csi.forcepoint.com')
	reports = driver.find_element_by_xpath('/html/body/section[1]/div[1]/div[1]/div/div[1]/div/form/span[4]/a')
	print(reports.text)


def FP_analysis(domain_name):
	options = FirefoxOptions()
	options.add_argument("--headless")
	driver = webdriver.Firefox(options=options)
	driver.get('https://csi.forcepoint.com')
	search = driver.find_element_by_name('LookupUrl')
	search.send_keys(domain_name)
	element = driver.find_element_by_xpath('//*[@id="btnAnalyze"]')
	element.click()
	time.sleep(5)

	Total_links = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[6]/div[2]/table[1]/tbody/tr/td[1]/p')
	Malicious_links = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[6]/div[2]/table[1]/tbody/tr/td[2]/p/span')
	Severity = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/table/tbody/tr[1]/td/p')
	Vul = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[4]/div[2]/table[2]/tbody/tr[4]/td[2]/p/span')
	RTCA = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[6]/div[2]/table[2]/tbody/tr/td[1]/p')
	IP = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[6]/div[2]/table[2]/tbody/tr/td[1]/p')


	ML_text = Malicious_links.text
	Severity_text = Severity.text
	Vul_text = Vul.text

	print('I check: ', domain_name)
	print('IP Address: ', IP.text)
	print('Real-time Content Analysis', RTCA.text)
	print('Total Number of Links: ', Total_links.text)
	print('Malicious Links: ', ML_text)
	print('Heartbleed Vulnerability: ', Vul_text)
	print(Severity_text)
"""

def Screenshot():
	indicators = open('search.txt')	
	sites = indicators.readlines()
	i = 1

	for site in sites:
		site_whois = site.replace('http://', '')
		options = FirefoxOptions()
		options.add_argument("--headless")
		driver = webdriver.Firefox(options=options)
		driver.get(site)

		S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
		driver.set_window_size(S('Width'),S('Height'))  
		time.sleep(5)                                                                                                           
		driver.find_element_by_tag_name('body').screenshot("screenshot_of_{}.png".format(site_whois))
		time.sleep(1)


		driver.quit()
		print("\nScreenshots is complete\n")

def SingleScreenshot(d3):

	d4 = 'http://'
	site = d4 + d3
	print(site)

	if site:
		site_whois = site.replace('http://', '')
		options = FirefoxOptions()
		options.add_argument("--headless")
		driver = webdriver.Firefox(options=options)
		driver.get(site)

		S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
		driver.set_window_size(S('Width'),S('Height'))  
		time.sleep(5)                                                                                                           
		driver.find_element_by_tag_name('body').screenshot("screenshot_of_{}.png".format(site_whois))
		time.sleep(1)


		driver.quit()
		print("\nScreenshots is complete\n")
