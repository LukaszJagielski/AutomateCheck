import requests
import whois
import time
import re


score = 0
VT_Score = 1
count = 0
response = 0



def get_status_code(response_site):
	if response_site.status_code == 200:
		print("- Status zadania: 200 - OK")
		s()
	elif response_site.status_code == 404:
		print("- Status zadania: 404 - Not Found")
	elif response_site.status_code == 301:
		print("- Status zadania: 301 - Moved Permanently")
		s()
	elif response_site.status_code == 502:
		print("- Status zadania: 502 - Bad Gateway")
	else:
		print("Nieznane zadanie")

def redirect(response_site):
	if response_site.is_redirect == False:
		print("- Brak przekierowania na stronie internetowej")
	else:
		print("- Istnieja przekierowania na stronie internetowej")
		s()

def s():
	global score
	score += 1
def d():
	global VT_Score
	VT_Score += 1

def how_many(response_site):
	print("How much .vbs extension: ", response_site.text.count('.vbs'))
	print("How much .vbe extension: ", response_site.text.count('.vbe'))
	print("How much .exe extension: ", response_site.text.count('.exe'))
	print("How much .iso extension: ", response_site.text.count('.iso'))
	print("How much .js extension: ", response_site.text.count('.js'))
	print("How much .jar extension: ", response_site.text.count('.jar'))
	print("How much .zip extension: ", response_site.text.count('.zip'))
	print("How much .py extension: ", response_site.text.count('.py'))

	print("Score is: ", score)

def VT_URL(d3):
	global VT_Score
	config_read = open("config.txt","r")
	apikey = config_read
	url = 'https://www.virustotal.com/vtapi/v2/url/report'

	d4 = 'http://'
	site = d4 + d3

	print('Which URLs I check:', site)
	print('\n')

	if site:
		
		params = {'apikey': apikey,'resource': site }
		response = requests.get(url, params=params)
		response_site = requests.get(site)
		response_site_txt = response_site.text
		response_json = response.json()
		site_whois = site.replace('http://', '')
		url_whois = whois.query(site_whois)

		if response_json['positives'] >= 2:
			print('Domain name: ', url_whois.name)
			print('Domain was registered: ', url_whois.creation_date)
			print('Registered name: ', url_whois.registrar)
			print("- Webstie is categorize as malicious by more than 2 AV in VirusTotal")
			print('Numbers of AV which recognize file as malicious: ', response_json['positives'])
			d()
			print("Last scan of VirusTotal: ", response_json['scan_date'])
			get_status_code(response_site)
			redirect(response_site)
			parse_all_links(response_site_txt)
			how_many(response_site)

		else:
			print('Domain name: ', url_whois.name)
			print('Domain was registered: ', url_whois.creation_date)
			print('Registered name: ', url_whois.registrar)
			print("- Website is not categorize as malicious\n")
			print('Numbers of AV which recognize file as malicious: ', response_json['positives'])
			print("Last scan of VirusTotal: ", response_json['scan_date'])
			get_status_code(response_site)
			redirect(response_site)
			parse_all_links(response_site_txt)
			how_many(response_site)


def VT_MD5(d3):
	global VT_Score
	config_read = open("config.txt","r")
	apikey = config_read
	url = 'https://www.virustotal.com/vtapi/v2/file/report'

	file = d3

	print('Which MD5 I check: ', file)
	print('\n')


	if file:

		params = {'apikey': apikey,'resource': file }
		response = requests.get(url, params=params)
		response_json = response.json()
		if response_json['response_code'] == 1:
			if response_json['positives'] >= 2:
				print('md5: ', response_json['md5'])
				print('sha256: ', response_json['sha256'])
				print('Last scan of VirusTotal: ', response_json['scan_date'])
				print('Numbers of AV which recognize file as malicious: ', response_json['positives'])
				print('\n')
				d()
				print("Analyze by VirustTotal: ", response_json['permalink'])
				print("File is categorize as malicious by more than 2 AV in VirusTotal")
			else:
				print('md5: ', response_json['md5'])
				print('sha256: ', response_json['sha256'])
				print('Last scan of VirusTotal: ', response_json['scan_date'])
				print('Numbers of AV which recognize file as malicious: ', response_json['positives'])
				print('\n')
				d()
				print("File is not categorize as malicious")
		elif response_json['response_code'] == 0:
			print('I check file:', response_json['resource'])
			print('File is not recognize by VirusTotal')


def parse_all_links(response_site_txt):

    links = re.findall(r"a href", response_site_txt)

    if len(links) == 0:
        print("- No links found")
        count = 0
    else:
        count = 0  
        for e in links:
            count += 1

    print('- Counts of links: {} '.format(count))