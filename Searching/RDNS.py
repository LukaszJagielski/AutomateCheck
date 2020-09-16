import os
import sys
from Searching import Requests
from Searching import FromFile
from Selen import Selenium


def menu():

    logo = '''\033[0m 
                 _                        _        _____ _               _    
      /\        | |                      | |      / ____| |             | |   
     /  \  _   _| |_ ___  _ __ ___   __ _| |_ ___| |    | |__   ___  ___| | __
    / /\ \| | | | __/ _ \| '_ ` _ \ / _` | __/ _ \ |    | '_ \ / _ \/ __| |/ /
   / ____ \ |_| | || (_) | | | | | | (_| | ||  __/ |____| | | |  __/ (__|   < 
  /_/    \_\__,_|\__\___/|_| |_| |_|\__,_|\__\___|\_____|_| |_|\___|\___|_|\_\

  
  URL and MD5 Edition 1.2                                                                                                                                                                                                                                                                                                                          
    '''
    menu = '''\033[0m
      Single check from input

      {1}--Whois lookup
      {2}--Traceroute
      {3}--DNS Lookup
      {4}--Download Index
      {5}--Port Scan
      {6}--Reverse IP Lookup
      {7}--VirusTotal URL check
      {8}--VirusTotal MD5 check
      {99}-Exit
      ---------------------------------------
      Multiple check from file

      {9}--VirusTotal URL check
      {0}--VirusTotal MD5 check
      ---------------------------------------
      Reports

      {10}-- Full report URL
                                                                                                                         
   '''

    print(logo)
    print(menu)


def quit():
    con = input('Continue [Y/n] -> ')
    if con[0].upper() == 'N':
        exit()
    else:
        os.system("clear")
        menu()
        select()


def questionMulti():
    con = input('Do you want to take Screenshot [Y/n] -> ')
    if con[0].upper() == 'N':
        quit()
    else:
        os.system("clear")
        Selenium.Screenshot()
        quit()


def questionSingle(d3):
    con = input('Do you want to take Screenshot [Y/n] -> ')
    if con[0].upper() == 'N':
        quit()
    else:
        os.system("clear")
        Selenium.SingleScreenshot(d3)
        quit()


def select():
    try:
        choice = input("AutomateCheck~# ")
        choice = int(choice)
        print(choice)
        if choice == 1:
            d3 = input('Enter IP Or Domain : ')
            os.system("clear")
            print("""
 _       ____  ______  _________
| |     / / / / / __ \/  _/ ___/
| | /| / / /_/ / / / // / \__ \ 
| |/ |/ / __  / /_/ _/ / ___/ / 
|__/|__/_/ /_/\____/___//____/                                  
      """)
            os.system("curl http://api.hackertarget.com/whois/?q=" + d3)
            print("")
            quit()
        elif choice == 2:
            d3 = input('Enter IP Or Domain : ')
            os.system("clear")
            print("""
  _____                                   _       
 |_   _| __ __ _  ___ ___ _ __ ___  _   _| |_ ___ 
   | || '__/ _` |/ __/ _ \ '__/ _ \| | | | __/ _ \
   | || | | (_| | (_|  __/ | | (_) | |_| | ||  __/
   |_||_|  \__,_|\___\___|_|  \___/ \__,_|\__\___|
                                                  
""")
            os.system("curl https://api.hackertarget.com/mtr/?q=" + d3)
            print("")
            quit()
        elif choice == 3:
            d3 = input('Enter Domain : ')
            os.system("clear")
            print("""
______ _   _ _____   _                 _                
|  _  | \ | /  ___| | |               | |               
| | | |  \| \ `--.  | |     ___   ___ | | ___   _ _ __  
| | | | . ` |`--. \ | |    / _ \ / _ \| |/ | | | | '_ \ 
| |/ /| |\  /\__/ / | |___| (_) | (_) |   <| |_| | |_) |
|___/ \_| \_\____/  \_____/\___/ \___/|_|\_\\__,_| .__ / 
                                                 | |    
                                                 |_|     
""")
            os.system("curl http://api.hackertarget.com/dnslookup/?q=" + d3)
            print("")
            quit()
        elif choice == 4:

            d3 = input('Enter URL or Domain: ')
            os.system("clear")
            print("""
  ____                      _                 _    _           _           
 |  _ \  _____      ___ __ | | ___   __ _  __| |  (_)_ __   __| | _____  __
 | | | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |  | | '_ \ / _` |/ _ \ \/ /
 | |_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  | | | | | (_| |  __/>  < 
 |____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|  |_|_| |_|\__,_|\___/_/\_\
                                                                           
	  """)
            os.system("wget -p " + d3)
            print("")
            quit()
        elif choice == 5:
            d3 = input('Enter IP Or Domain : ')
            os.system("clear")
            print("""
     __                         __                 
  /\ \ \_ __ ___   __ _ _ __   / _\ ___ __ _ _ __  
 /  \/ | '_ ` _ \ / _` | '_ \  \ \ / __/ _` | '_ \ 
/ /\  /| | | | | | (_| | |_) | _\ | (_| (_| | | | |
\_\ \/ |_| |_| |_|\__,_| .__/  \__/\___\__,_|_| |_|
                       |_|                         
      """)
            os.system("curl http://api.hackertarget.com/nmap/?q=" + d3)
            print("")
            quit()
        elif choice == 6:
            d3 = input('Enter IP Or Domain : ')
            os.system("clear")
            print("""
 (   (      (                             
 )\ ))\ )   )\ )            )             
(()/(()/(  (()/(         ( /(   (         
 /(_)/(_))  /(_)) (   (  )\()) ))\ `  )   
(_))(_))   (_))   )\  )\((_)\ /((_)/(/(   
|_ _| _ \  | |   ((_)((_| |(_(_))(((_)_\  
 | ||  _/  | |__/ _ / _ | / /| || | '_ \) 
|___|_|    |____\___\___|_\_\ \_,_| .__/  
                                  |_|     
    """)
            os.system("wget http://api.hackertarget.com/reverseiplookup/?q=" + d3)
            os.system("clear")
            os.system("curl http://api.hackertarget.com/reverseiplookup/?q=" + d3)
            print("")
            print("\033[91m\033[1mFile Saved On : ")
            os.system("pwd")
            print("File : index.html?q=" + d3)
            print("\033[0m")
            quit()

        elif choice == 7:
            d3 = input('Enter URL Or Domain : ')
            os.system("clear")
            print("""
__      _________    _    _ _____  _          _____ _               _    
\ \    / /__   __|  | |  | |  __ \| |        / ____| |             | |   
 \ \  / /   | |     | |  | | |__) | |       | |    | |__   ___  ___| | __
  \ \/ /    | |     | |  | |  _  /| |       | |    | '_ \ / _ \/ __| |/ /
   \  /     | |     | |__| | | \ \| |____   | |____| | | |  __/ (__|   < 
    \/      |_|      \____/|_|  \_\______|   \_____|_| |_|\___|\___|_|\_\    
                                  
  """)
            Requests.VT_URL(d3)
            questionSingle(d3)
            print("")
            print("")
            quit()
        elif choice == 8:
            d3 = input('Enter MD5 : ')
            os.system("clear")
            print("""
 __      _________    __  __ _____  _____     _____ _               _    
 \ \    / /__   __|  |  \/  |  __ \| ____|   / ____| |             | |   
  \ \  / /   | |     | \  / | |  | | |__    | |    | |__   ___  ___| | __
   \ \/ /    | |     | |\/| | |  | |___ \   | |    | '_ \ / _ \/ __| |/ /
    \  /     | |     | |  | | |__| |___) |  | |____| | | |  __/ (__|   < 
     \/      |_|     |_|  |_|_____/|____/    \_____|_| |_|\___|\___|_|\_\
                                                                         
                                                                                                   
  """)
            Requests.VT_MD5(d3)
            print("")
            print("")
            quit()

        elif choice == 9:
            os.system("clear")
            print("""
__      _________    _    _ _____  _          _____ _               _    
\ \    / /__   __|  | |  | |  __ \| |        / ____| |             | |   
 \ \  / /   | |     | |  | | |__) | |       | |    | |__   ___  ___| | __
  \ \/ /    | |     | |  | |  _  /| |       | |    | '_ \ / _ \/ __| |/ /
   \  /     | |     | |__| | | \ \| |____   | |____| | | |  __/ (__|   < 
    \/      |_|      \____/|_|  \_\______|   \_____|_| |_|\___|\___|_|\_\   

    From file 
                                  
  """)
            FromFile.VT_URL()
            questionMulti()
            print("")
            print("")
            quit()
        elif choice == 0:
            os.system("clear")
            print("""
 __      _________    __  __ _____  _____     _____ _               _    
 \ \    / /__   __|  |  \/  |  __ \| ____|   / ____| |             | |   
  \ \  / /   | |     | \  / | |  | | |__    | |    | |__   ___  ___| | __
   \ \/ /    | |     | |\/| | |  | |___ \   | |    | '_ \ / _ \/ __| |/ /
    \  /     | |     | |  | | |__| |___) |  | |____| | | |  __/ (__|   < 
     \/      |_|     |_|  |_|_____/|____/    \_____|_| |_|\___|\___|_|\_\

     From file
                                                                         
                                                                                                   
  """)
            FromFile.VT_MD5()
            print("")
            print("")
            quit()

        elif choice == 10:
            d3 = input('Enter URL : ')
            os.system("clear")
            print("""

  ______     _ _                              _      _    _ _____  _      
 |  ____|   | | |                            | |    | |  | |  __ \| |     
 | |__ _   _| | |   _ __ ___ _ __   ___  _ __| |_   | |  | | |__) | |     
 |  __| | | | | |  | '__/ _ \ '_ \ / _ \| '__| __|  | |  | |  _  /| |     
 | |  | |_| | | |  | | |  __/ |_) | (_) | |  | |_   | |__| | | \ \| |____ 
 |_|   \__,_|_|_|  |_|  \___| .__/ \___/|_|   \__|   \____/|_|  \_\______|
                            | |                                           
                            |_|                                           
                                                                                                   
  """)

            whois = os.system("curl http://api.hackertarget.com/whois/?q=" + d3)
            print(35*"#")
            traceroute = os.system("curl https://api.hackertarget.com/mtr/?q=" + d3)
            print(35*"#")
            dnslookup = os.system("curl http://api.hackertarget.com/dnslookup/?q=" + d3)
            print(35*"#")
            scan = os.system("curl http://api.hackertarget.com/nmap/?q=" + d3)
            print(35*"#")
            VT = Requests.VT_URL(d3)
            print(35*"#")

            print("")
            print("")
            quit()
        else:
            print("Not valid number")
            exit()

    except(KeyboardInterrupt):
        print ("")

    except ValueError:
      print("This is not a number. Please enter a valid number")
      quit()

    except NameError:
      print("\nThis is not a number. Please enter a valid number")
      quit()
