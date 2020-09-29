# AutomateCheck
Check domain, URL, MD5

Script using simple os.system commands and two APIs website. Virus Total and Hackertarget. For option 1,2,3,5,6 there is a limit of 100 API calls per day from a single IP address and for 7,8,9,0 option depends on the subscription plan on Virus Total

Remember to paste your Virus Total API Key to config.txt !

The core of script is checking domain or URL, also counting extension (vbs, vbe, exe, iso, js, jar, zip, py), links and give you a screenshot of website. This may help to do quick analysis.

[![VT-Check.png](https://i.postimg.cc/KctbhQrZ/VT-Check.png)](https://postimg.cc/yW6tFmb5)

Also there is scoring point in code, but it's still in build progress.

# What can i do?

[![Screenshot-2020-09-29-04-10-48.png](https://i.postimg.cc/Hxmynqbz/Screenshot-2020-09-29-04-10-48.png)](https://postimg.cc/8Fy5nnKf)


{1} - Determine the registered owner of a domain or IP address block with the whois tool.\
{2} - Using mtr an advanced traceroute tool trace the path of an Internet connection.\
{3} - Find DNS records for a domain, results are determined using the dig DNS tool.\
{4} - Download index of webiste using wget.\
{5} - Determine the status of an Internet facing service or firewall.\
{6} - Discover web hosts sharing an IP address with a reverse IP lookup.\
{7} - Checking domain or URL, also count extension (vbs, vbe, exe, iso, js, jar, zip, py), links and can give you a screenshot of website.\
{8} - Show how many numbers of AV recognize file as malicious and when was last scan of Virust Total.\
{99} - Exit from script

-------------------------------------------------------------------------------------------------------------------------------------------
{9} - Same as number 7 but you can check many URL. Copy and paste URL to search.txt, save and run script.\
{0} - Same as number 8 but you can check many MD5. Copy and paste MD5 to search.txt, save and run script.

-------------------------------------------------------------------------------------------------------------------------------------------
{10} - This option give you 1,2,3,5,7 options for single URL.

# Requirements:

1. Firefox 68.7 or less
2. pip module from (pip is already installed if you are using Python 2 >=2.7.9 or Python 3 >=3.4) https://pip.pypa.io/en/stable/installing/ 
3. geckodriver-v0.26.0-linux64.tar.gz - https://github.com/mozilla/geckodriver/releases
4. Modules from install.py
5. Virus total API KEY

# Installation:
1. Run in terminal "python3 Install.py"
2. Download geckodriver-v0.26.0-linux64.tar.gz from https://github.com/mozilla/geckodriver/releases copy driver to your PATH, e. g., place it in /usr/bin or /usr/local/bin.
3. Run script using "python3 AutomateCheck.py"

