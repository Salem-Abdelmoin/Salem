#Enter name && Enter passwd
######################################
import webbrowser
import time
import random 
x = "true"
y = "false"

z = input("yor hacker or true or false =")
if z == x:
        site = random.choice(['facebook.com/profile.php?id=100025532492502'])
        visit = 'http://{}'.format(site)
        webbrowser.open(visit)
        seconds = random.randrange(5,9)
        time.sleep(seconds)
        exit

elif z == y:
                site = random.choice(['facebook.com/profile.php?id=100025532492502'])
                visit = 'https://{}'.format(site)
                webbrowser.open(visit)
                exit
else :
    print ("you ara donky not hacker")