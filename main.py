import requests, os, logging
from pystyle import *
from threading import Thread
from GmailDotEmailGenerator import GmailDotEmailGenerator
os.system("cls")
os.system ("title [Vortex license] Main")
logging.basicConfig(
    level=logging.INFO,
    format="\x1b[31m[\x1b[0m%(asctime)s\x1b[31m]\x1b[0m %(message)s",
    datefmt="%H:%M:%S"
)
ascii = (""""
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~""")
print(Colorate.Horizontal(Colors.purple_to_blue,(ascii)))
basemail = input(Colorate.Horizontal(Colors.purple_to_blue,("\n\n\nEmail: ")))
os.system ("title [Vortex license] sending")
def send():
    for email in \
        (GmailDotEmailGenerator(basemail).generate())[:127240]:
        sent = requests.get (f"""http://46.101.168.188:5000/emails/{email}/619F5E1375AC225A44F656FD7AE58""")
        if sent.text == 'email address used before':
            logging.critical ("Email used before")
        elif sent.text == 'succefully joined the 7 day free trial':
            logging.critical ("Sent 7 days trial key")

            
            
for i in range(10):
    x = Thread(target=send)
    x.start()
