import ctypes
import string
import os
import time
from pystyle import *
from pystyle import Colorate, Colors, System, Center, Write, Anime
LICNECE = """
PlutoniumSQ  ||  2023  ||  https://discord.gg/gGmmjwx5Hx
"""


USE_WEBHOOK = True

print(LICNECE)

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')


try: 
    from discord_webhook import DiscordWebhook  
except ImportError:  
    
    input(
        f"Le Module discord_webhook n'est pas installer, pour le download, fais simplement '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nTu peus ignorer si tu veux pas utiliser de webhook\nAppuie sur entrer pour quitter")
    USE_WEBHOOK = False
try:  
    import requests  
except ImportError:  
   
    input(
        f"Le Module requests n'est pas installer, pour le download, fais simplement '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nAppuie sur entrer pour quitter")
    exit()  
try:  
    import numpy  
except ImportError:  
    
    input(
        f"Le Module numpy n'est pas installer, pour le download, fais simplement '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install numpy'\nAppuie sur entrer pour quitter")
    exit()  


class NitroGen: 
    def __init__(self): 
        self.fileName = "Codes Nitro.txt" 

    def main(self):  
        os.system('cls' if os.name == 'nt' else 'clear')  
        if os.name == "nt":  
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW(
                "Nitro Generator / Checker - Made By FullyAxyv#5815")  
        else:  
            print(f'\33]0;Nitro Generator and Checker - Made By Axyv\a',
                  end='', flush=True)  

        banner = r"""Press Enter To Continue !
    
     ____    ___             __                                           
    /\  _`\ /\_ \           /\ \__                 __                        
    \ \ \L\ \//\ \    __  __\ \ ,_\   ___     ___ /\_\  __  __    ___ ___    
     \ \ ,__/ \ \ \  /\ \/\ \\ \ \/  / __`\ /' _ `\/\ \/\ \/\ \ /' __` __`\  
      \ \ \/   \_\ \_\ \ \_\ \\ \ \_/\ \L\ \/\ \/\ \ \ \ \ \_\ \/\ \/\ \/\ \ 
       \ \_\   /\____\\ \____/ \ \__\ \____/\ \_\ \_\ \_\ \____/\ \_\ \_\ \_\
        \/_/   \/____/ \/___/   \/__/\/___/  \/_/\/_/\/_/\/___/  \/_/\/_/\/_/


                              > By Axyv <                   V1.0              """
        
        Anime.Fade(Center.Center(banner), Colors.green_to_cyan, Colorate.Vertical, enter=True)

        time.sleep(2)  

        self.slowType("Made By : FullyAxyv#5815", .02)
        time.sleep(1)  
        
        self.slowType(
            "\nHow Much Nitro Code Do You Want To Gen ? : ", .02, newLine=False)
        
        try:
            num = int(input(''))  
        except ValueError:
            input("You Didn't Write A Number\nPress Enter To Exit")
            exit()  

        if USE_WEBHOOK:
            
            self.slowType(
                "Webhook : Soon | Press Enter", .02, newLine=False)
            url = input('')  
            
            webhook = url if url != "" else None
            
            if webhook is not None:
                DiscordWebhook(  
                        url=url,
                        content=f"```Checker In Progress\nCodes Will Be Sent Here```"
                    ).execute()

        

        valide = []  
        invalide = 0  
        chars = []
        chars[:0] = string.ascii_letters + string.digits

        
        c = numpy.random.choice(chars, size=[num, 23])
        for s in c:  
            try:
                code = ''.join(x for x in s)
                url = f"https://discord.gift/{code}"  

                result = self.quickChecker(url, webhook)  

                if result:  
                    
                    valide.append(url)
                else:  
                    invalide += 1  
            except KeyboardInterrupt:
                
                print("\nInterrupted By A User !")
                break  

            except Exception as e:  
                print(f" Error | {url} ")  

            if os.name == "nt":  
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"Nitro Generator / Checker - {len(valide)} Valid | {invalide} Invalid - Made By FullyAxyv#5815")  
                print("")
            else:  
                
                print(
                    f'\33]0;Nitro Generator and Checker - {len(valid)} Valid | {invalide} Invalid - Made By Axyv\a', end='', flush=True)

        print(f"""
Resultats :
 Valid : {len(valide)}
 Invalid : {invalide}
 Codes Valide : {', '.join(valide)}""")  

        
        input("\nFinished !    Press Enter 5 Times To Close The Window, And The Program !")
        [input(i) for i in range(4, 0, -1)]  

    
    def slowType(self, text: str, speed: float, newLine=True):
        for i in text:  
            
            print(i, end="", flush=True)
            time.sleep(speed)  
        if newLine:  
            print()  

    def quickChecker(self, nitro:str, notify=None):  
        
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)  

        if response.status_code == 200:  
            
            print(f" Valid | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            with open("Codes Nitro.txt", "w") as file:  
                
                file.write(nitro)

            if notify is not None:  
                DiscordWebhook(  
                    url=url,
                    content=f"A Valid Code Is Detected ! @everyone \n{nitro}"
                ).execute()

            return True  

        
        else:
            
            print(f" Invalid | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            return False  


if __name__ == '__main__':
    Gen = NitroGen()  
    Gen.main() 
    
#Axyv Heree
