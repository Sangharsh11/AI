import datetime
import smtplib
import webbrowser as wb
import pyttsx3
#import speech_recognition as sr
#import wikipedia as wikipedia
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)
newVoiceRate = 170
engine.setProperty('rate', newVoiceRate)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    if (month == 1):
        str_mon = "january"
    elif (month == 2):
        str_mon = "February"
    elif (month == 3):
        str_mon = "march"
    elif (month == 4):
        str_mon = "april"
    elif (month == 5):
        str_mon = "may"
    elif (month == 6):
        str_mon = "june"
    elif (month == 7):
        str_mon = "july"
    elif (month == 8):
        str_mon = "august"
    elif (month == 9):
        str_mon = "september"
    elif (month == 10):
        str_mon = "october"
    elif (month == 11):
        str_mon = "november"
    else:
        str_mon = "December"

    speak(" the current date is")
    speak(date)
    speak(str_mon)
    speak(year)


def wishme():
    speak("Welcome back sir.....Jarvis at your service...How can I help you?")


# def takecommand():
#     r = sr.Recognizer
#     with sr.Microphone() as source:
#         print("Listening....")
#         r.pause_threshold = 1
#         audio = r.listen(source)
#
#     try:
#         print("Recognizing....")
#         query = r.recognize_google(audio , 'en=US')
#         print(query)
#
#     except Exception as e:
#         print(e)
#         speak("say that again please...")
#
#         return "None"
#     return query

def exit():
    speak("Wake me up when you need something...")

def sendmail(to, content):
    server=smtplib.SMTP('patilsangharsh11@gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('test@gmail.com','123456')
    server.sendmail('test@gmail.com',to,content)
    server.close()


def screenshot():
    img=pyautogui.screenshot()
    img.save("D:\screenshots\ss.png")


def cpu():
    usage=str(psutil.cpu_percent())
    speak("CPU is at" + usage)
    battery=psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

#takecommand()
wishme()
while(True):

    print("""
    1--> for Greeting
    2--> for Date
    3-->for Time
    4--> wikipedia Search
    5--> Search on Chrome
    6--> Record to do list
    7--> Remind the to do list
    8--> CPU and battery percentage
    9--> Jokes
    anything--> Exit
    """)

    i=int(input("enter your choice: "))
    if i == 1:
        print("wishing again")
        wishme()
    elif i == 2:
        print("Here is date")
        date()
    elif i == 3:
        print("Here is time")
        time()
    elif i == 4:
        #search=input("What do you want to search? : ")

        #result=wikipedia.summary(search)
        speak("Sorry for the inconvenience...currently I am under working condition....Try other options... ")

    elif i == 5:
        speak("What should I search?")
        search=str(input("What should I search? : "))
        chromepath="C:\Program Files\Google\Chrome\Application"
        #wb.get(chromepath).open_new(search+".com")
        wb.open(search+".com")

    elif i == 6:
        speak("What is your Today's task")
        data = input(" write your to do list ")
        speak("you said me your task are" + data)
        remember = open("data.txt", "w")
        remember.write(data)
        remember.close()

    elif i == 7:
        remember = open("data.txt", "r")
        speak("your today's to do list is" + remember.read())

    elif i == 8:
        #speak("I am taking Screenshot")
        cpu()

    elif i == 9:
        jokes()

    # elif i ==10:
    #     takecommand()

    else:
        quit()


