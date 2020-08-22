import pyttsx3
import os
from googlesearch import *
import webbrowser
import datetime
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

os.system("cls")
print("\tWELCOME!")
pyttsx3.speak("WELCOME!")

while True:
 
 print("\nHow can I help you? " , end='')
 pyttsx3.speak(" How can I help you?")
 
 y=input()
 x=y.lower()
 
 if((("add" in x) or ("multiply" in x) or ("divide" in x) or ("subtract" in x)) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  from operator import pow, truediv, mul, add, sub  

  operators = {
   '+': add,
   '-': sub,
   '*': mul,
   '/': truediv
  }

  def calculate(s):
      if s.isdigit():
          return float(s)
      for c in operators.keys():
          left, operator, right = s.partition(c)
          if operator in operators:
              return operators[operator](calculate(left), calculate(right))
  pyttsx3.speak("Type calculation")
  calc = input("Type calculation:\n")
  
  print("Answer: " + str(calculate(calc)))
  pyttsx3.speak("The answer is")
  z=str(calculate(calc))
  pyttsx3.speak(z)

 elif (("why" in x) or ("tell" in x) or ("show" in x) or ("what" in x) or ("display" in x)) and ("news" in x) and (not (("don't" in x) or ("dont" in x) or ("do not" in x))):
  pyttsx3.speak("Here is the news")
  news_url="https://news.google.com/news/rss"
  Client=urlopen(news_url)
  xml_page=Client.read()
  Client.close()

  soup_page=soup(xml_page,"xml")
  news_list=soup_page.findAll("item")
  # Print news title, url and publish date
  for news in news_list:
   print(news.title.text)
   print(news.link.text)
   print(news.pubDate.text)
   print("-"*60)

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x) or ("display" in x) or ("show" in x))and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x))) and (("youtube" in x) or ("utube" in x))):
  webbrowser.open("https://www.youtube.com/")
  pyttsx3.speak("okay!starting youtube")
  print("Opening...")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x) or ("display" in x) or ("show" in x))and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x))) and (("linkedin" in x) or ("linkdin" in x))):
  webbrowser.open("https://www.linkedin.com/")
  pyttsx3.speak("okay!starting LinkedIn")
  print("Opening...")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x) or ("display" in x) or ("show" in x))and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x))) and (("gmail" in x) or ("google mail" in x))):
  webbrowser.open("https://accounts.google.com/")
  pyttsx3.speak("okay!starting G-mail")
  print("Opening...")

 elif (("search" in x) and ("google" in x)) and (not(("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x))):
  pyttsx3.speak("Okay!Type your Query")
  query = input("Type your query: ")
  
  chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
  pyttsx3.speak("okay!here is your information")
  for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
   webbrowser.open("https://google.com/search?q=%s" % query) 
  
 elif ((("why" in x) or ("tell" in x) or ("show" in x) or("what" in x)or ("which" in x)) and (("clock" in x) or ("time" in x)) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  d=datetime.datetime.now()
  print("The Time is",d.strftime("%X"))
  pyttsx3.speak("The time is")
  pyttsx3.speak(d.strftime("%X"))

 elif ((("why" in x) or ("tell" in x) or ("show" in x) or("what" in x) or ("which" in x)) and (("date" in x)) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  d=datetime.datetime.now()
  print("The Date is",d.strftime("%x"))
  pyttsx3.speak("The date is")
  pyttsx3.speak(d.strftime("%x"))

 elif ((("why" in x) or ("tell" in x) or ("show" in x) or("what" in x) or ("which" in x)) and (("day" in x)) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  d=datetime.datetime.now()
  print("The Day is",d.strftime("%A"))
  pyttsx3.speak("The day is")
  pyttsx3.speak(d.strftime("%A"))

 elif ((("why" in x) or ("tell" in x) or ("show" in x) or("what" in x) or ("which" in x)) and (("month" in x)) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  d=datetime.datetime.now()
  print("The Month is",d.strftime("%B"))
  pyttsx3.speak("The month is")
  pyttsx3.speak(d.strftime("%B"))

 elif ((("why" in x) or ("tell" in x) or ("show" in x) or("what" in x)or ("which" in x)) and (("year" in x)) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  d=datetime.datetime.now()
  print("The Year is",d.strftime("%Y"))
  pyttsx3.speak("The year is")
  pyttsx3.speak(d.strftime("%Y"))

 elif ((("why" in x) or ("tell" in x) or ("show" in x) or("what" in x)or ("which" in x)) and (("week" in x)) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  d=datetime.datetime.now()
  print("The current week number is",d.strftime("%U"))
  pyttsx3.speak("The current week number is")
  pyttsx3.speak(d.strftime("%U"))

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and ("excel" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x))):
  os.system("start excel")
  print("Okay! Starting excel..")
  pyttsx3.speak("starting excel")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("whatsapp" in x) or ("what's app" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("https://web.whatsapp.com/")
  print("Okay! Starting whatsapp..")
  pyttsx3.speak("starting whatsapp")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("clock" in x) or ("time" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start ms-clock:")
  print("Okay! Starting ms-clock:..")
  pyttsx3.speak("starting clock:")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("calc" in x) or ("calculator" in x) or ("calci" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start calculator:")
  print("Okay! Starting calculator..")
  pyttsx3.speak("starting calculator")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("available network" in x) or ("wifi network" in x) or ("wifi devices" in x) or ("wifi connection" in x) or ("available wifi" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start ms-availablenetworks:")
  print("Okay! Showing available networks:..")
  pyttsx3.speak("Showing available networks")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("date" in x) or ("day" in x) or ("calender" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start outlookcal:")
  print("Okay! Starting calendar:..")
  pyttsx3.speak("starting calendar")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("action center" in x) or ("notification" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start ms-actioncenter:")
  print("Okay! Showing notifications:..")
  pyttsx3.speak("starting notifications")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("webcam" in x) or ("camera" in x) or ("cam" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start microsoft.windows.camera:")
  print("Okay! Starting camera:..")
  pyttsx3.speak("starting camera")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("connect" in x) or ("wireless connection" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start ms-projection:")
  print("Okay! Starting connect:..")
  pyttsx3.speak("starting connect")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("device discovery" in x) or ("discover device" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start ms-settings-connectabledevices:devicediscovery")
  print("Okay! Turning on device discovery..")
  pyttsx3.speak("Turning on device discovery")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("cortana" in x) or ("voice assistant" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start ms-cortana:")
  print("Okay! Starting ms-cortana:..")
  pyttsx3.speak("starting ms-cortana")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("feedback hub" in x) or ("feedback" in x)) and(not (("why" in x) or ("tell" in x) or ("what" in x))) and  (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start feedback-hub:")
  print("Okay! Starting feedback-hub:..")
  pyttsx3.speak("starting feedback-hub")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("get help" in x) or ("help"in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start ms-contact-support:")
  print("Okay! Starting ms-contact-support:..")
  pyttsx3.speak("starting ms-contact-support")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("music" in x) or ("songs" in x) or ("tracks" in x) or ("groove music" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start mswindowsmusic:")
  print("Okay! Starting mswindowsmusic:..")
  pyttsx3.speak("starting mswindowsmusic")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and ("mail" in x)and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start outlookmail:")
  print("Okay! Starting outlookmail:..")
  pyttsx3.speak("starting outlookmail")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and ("map" in x) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start bingmaps:")
  print("Okay! Starting bingmaps:..")
  pyttsx3.speak("starting bingmaps")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and ("message" in x) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start ms-chat:")
  print("Okay! Starting ms-chat:..")
  pyttsx3("starting ms-chat")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("microsoft explorer" in x) or ("edge" in x))and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start microsoft-edge:")
  print("Okay! microsoft-edge:..")
  pyttsx3.speak("starting microsoft-edge")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and ("news" in x) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start bingnews:")
  print("Okay! Starting bingnews:..")
  pyttsx3.speak("starting bingnews")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("Solitaire" in x) or ("card game" in x) or ("game" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start xboxliveapp-1297287741:")
  print("Okay! Starting Solitaire:..")
  pyttsx3.speak("starting Solitaire")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("Microsoft Store" in x) or ("ms store" in x) or ("app download" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start ms-windows-store:")
  print("Okay! Starting ms-windows-store:..")
  pyttsx3.speak("starting ms-windows-store")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and ("hololens cam" in x)and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start ms-holocamera:")
  print("Okay! Starting ms-holocamera:..")
  pyttsx3.speak("starting ms-holocamera")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and ("ms video" in x) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start mswindowsvideo:")
  print("Okay! Starting mswindowsvideo:..")
  pyttsx3.speak("starting mswindowsvideo")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("one note" in x) or ("onenote" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start onenote:")
  print("Okay! Starting onenote:..")
  pyttsx3.speak("starting onenote")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("paint" in x) or ("draw" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start ms-paint:")
  print("Okay! Starting ms-paint:..")
  pyttsx3.speak("starting ms-paint")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and ("People" in x) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start ms-people:")
  print("Okay! Starting ms-people:..")
  pyttsx3.speak("starting ms-people")
 
 elif("clear screen" in x) or ("clear window" in x):
  os.system("cls")
  pyttsx3.speak("Screen cleared")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("Project Display" in x) or ("project" in x))and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start ms-settings-displays-topology:projection")
  print("Okay! Starting Project Display..")
  pyttsx3.speak("starting Project Display")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("Screen Snip" in x) or ("snipping tool" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start ms-screenclip:")
  print("Okay! Starting snipping tool..")
  pyttsx3.speak("starting snipping tool")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and ("settings" in x)and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start ms-settings:")
  print("Okay! Starting settings..")
  pyttsx3("starting settings")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and ("tips" in x) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start ms-get-started:")
  print("Okay! Starting tips..")
  pyttsx3.speak("starting tips")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and ("View Preview" in x) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start com.microsoft.3dviewer:")
  print("Okay! Starting microsoft 3dviewer:..")
  pyttsx3.speak("starting microsoft 3dviewer")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and ("Voice Recorder" in x)and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start ms-callrecording:")
  print("Okay! Starting ms-callrecording:..")
  pyttsx3.speak("starting ms-callrecording:")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and ("Weather" in x) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start bingweather:")
  print("Okay! Starting bingweather:..")
  pyttsx3.speak("starting bingweather:")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("Windows Security" in x) or ("security" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start windowsdefender:")
  print("Okay! Starting windowsdefender:..")
  pyttsx3.speak("starting windowsdefender:")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("Disk Cleanup" in x) or ("clean disk" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start cleanmgr")
  print("Okay! Starting clean manager..")
  pyttsx3("starting cleanmanager")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("manage computer" in x) or ("manage pc" in x) or ("computer management" in x) ) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start compmgmt")
  print("Okay! Starting computer management..")
  pyttsx3.speak("starting computer management")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and ("user folder" in x) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start ..")
  print("Okay! Opening users folder..")
  pyttsx3.speak("Opening users folder")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and ("configure" in x) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start msconfig")
  print("Okay! Starting system configuration..")
  pyttsx3.speak("starting system configuration")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and ("troubleshoot" in x) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start resmon")
  print("Okay! Starting resource monitor..")
  pyttsx3.speak("starting resource monitor")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("mouse setting" in x) or ("arrow setting" in x))and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start main.cpl")
  print("Okay! Opening mouse settings..")
  pyttsx3.speak("Opening mouse settings")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and ("screen keyboard" in x)and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start osk")
  print("Okay! Starting Screen keyboard..")
  pyttsx3.speak("starting Screen keyboard")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("system info" in x) or ("pc info" in x) or ("laptop info" in x) or ("software environment" in x) or ("hardware resources" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start msinfo32")
  print("Okay! Starting System information..")
  pyttsx3.speak("starting System information")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("change office lang" in x) or ("microsoft lang" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start setlang")
  print("Okay! Starting office setlang..")
  pyttsx3.speak("starting office setlang")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("virtual box" in x) or ("virtualization program" in x) or ("virtualisation program" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start virtualbox")
  print("Okay! Starting virtual box..")
  pyttsx3.speak("starting virtual box")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and ("character map" in x) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start charmap")
  print("Okay! Starting character map..")
  pyttsx3.speak("starting character map")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("net explorer" in x) or ("browser" in x) or ("internet" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start iexplore")
  print("Okay! Starting iexplore..")
  pyttsx3.speak("starting iexplore")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("math input" in x) or ("math panel" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start math input panel")
  print("Okay! Starting math input panel..")
  pyttsx3.speak("starting math input panel")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("Intel driver support assistant" in x) or ("Intel assistant" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start dsaservicehelper")
  print("Okay! Starting Intel driver support assistant..")
  pyttsx3.speak("starting Intel driver support assistant")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("quick assist" in x) or ("control computer" in x) or ("connect computer" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start quickassist")
  print("Okay! Starting quick assist..")
  pyttsx3.speak("starting quick assist")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and ("remote desktop connection" in x)and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start mstc")
  print("Okay! Starting remote desktop connection..")
  pyttsx3.speak("starting remote desktop connection")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("step record" in x) or ("record step" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start psr")
  print("Okay! Starting steps recorder..")
  pyttsx3.speak("Okay! starting steps record")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("fax" in x) or ("scan" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start wfs")
  print("Okay! Starting windows fax and scan..")
  pyttsx3.speak("Starting windows fax and scan")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("wordpad" in x) or ("word pad" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start wordpad")
  print("Okay! Starting wordpad..")
  pyttsx3("starting wordpad")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and ("component service" in x) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start comexp")
  print("Okay! Starting ccomponent service..")
  pyttsx3.speak("starting component service")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("performance monitor" in x) or ("monitoring tool" in x) or ("data collector sets" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start perfmon")
  print("Okay! Opening performance monitor..")
  pyttsx3.speak("Okay! Opening performance monitor")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("recovery drive" in x) or ("configure system restore" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start recoverydrive")
  print("Okay! Starting recovery drive..")
  pyttsx3.speak("starting recovery drive")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and ("service" in x) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start services")
  print("Okay! Starting services..")
  pyttsx3("starting services")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and ("event view" in x) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start devenv")
  print("Okay! Starting event viewer..")
  pyttsx3.speak("starting event viewer")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("command prompt" in x) or ("cmd" in x) or ("command line" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start cmd")
  print("Okay! Starting command prompt..")
  pyttsx3.speak("starting command prompt")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("learn feature" in x) or ("narrator" in x) or ("feature information" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start narrator")
  print("Okay! Starting narrator..")
  pyttsx3.speak("starting narrator")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("memory diagnostic" in x) or ("detect problem" in x) or ("check for problem" in x) or ("check problem" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start mdsched")
  print("Okay! Starting windows memory diagnostic...")
  pyttsx3.speak("starting windows memory diagnostic")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("event manager" in x) or ("manage event" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start eventvwr")
  print("Okay !Starting event manager..")
  pyttsx3.speak("starting event manager")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and ("administrative tools" in x) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start control")
  print("Okay! Starting control..")
  pyttsx3.speak("starting control")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("notepad" in x) or ("notebook" in x) or ("editor" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start notepad")
  print("Okay! Starting notepad..")
  pyttsx3.speak("starting notepad")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("control" in x) or ("panel" in  x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start control panel")
  print("Okay! Starting control panel..")
  pyttsx3.speak("starting control panel")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("word" in x) or ("msword" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start winword")
  print("Okay! Starting ms-word..")
  pyttsx3.speak("starting ms nword")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x) or ("display" in x)) and (("chrome" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start chrome")
  print("Okay! Starting chrome..")
  pyttsx3.speak("starting chrome")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("power" in x) or("point" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start powerpnt")
  print("Okay! Starting powerpnt..")
  pyttsx3.speak("starting powerpnt")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("magnifier" in x) or ("magnify" in x) or ("scale" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start magnify")
  print("Okay! Starting magnify..")
  pyttsx3.speak("starting magnify")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("taskmgr" in x) or ("task manager" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start taskmgr")
  print("Okay! Starting task manager..")
  pyttsx3.speak("starting task manager")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("wmplayer" in x) or ("media player" in x) or ("player" in x) or ("track player" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start wmplayer")
  print("Okay! Starting windows media player..")
  pyttsx3.speak("starting windows media player")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("zoom" in x) or ("meeting" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start zoom")
  print("Okay! Starting zoom..")
  pyttsx3.speak("starting zoom")

 elif ((("launch" in x) or ("open" in x) or ("start" in x) or ("execute" in x) or ("run" in x)) and (("task schedule" in x) or ("scheduler" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  os.system("start taskschd")
  print("Okay! Starting task scheduler..")
  pyttsx3.speak("starting task scheduler")

 elif ((("speak" in x) or ("say" in x)) and (not (("why" in x) or ("tell" in x) or ("what" in x))) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  print("What to speak?",end='')
  a=input()
  pyttsx3.speak(a)

 elif ((("exit" in x) or ("stop" in x)) or (("escape" in x) or ("quit" in x)) and (not (("don't" in x) or ("dont" in x) or ("do not" in x)))):
  print("Exiting! Thank you..")
  pyttsx3.speak("Exiting! Thank you")
  break

 elif (("don't" in x) or ("dont" in x) or ("do not" in x)):
  print("Okay! Won't open") 
  pyttsx3.speak("Okay! Won't open")

 else:
  print("ERROR!An exception occurred") 
  pyttsx3.speak("Error!An exception occurred") 