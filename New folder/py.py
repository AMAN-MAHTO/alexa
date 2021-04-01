import pyttsx3  # for voice engin
import datetime  # for current time and date
import random  # to provide randomness
import smtplib  # for connecting mail
from pyautogui import hotkey, typewrite, press  # to automate some keybords comment
import time  # for giving time sense

try:
    import pywhatkit as kit  # for search,send whatsup message,play video on youtube
except:
    print('please check internet connection')
import speech_recognition as sr  # use to recognize user voice imf.
import webbrowser  # for online web search
import os  # for control on pc
import wikipedia  # it contain data that make easy to answer
from textblob import TextBlob  # for detecting language, corrections and many more
from pyperclip import paste  # to copy any data as python variable
import sqlite3  # it provide database to store data like pathes of file

# engine of alexa to speak
engine = pyttsx3.init("sapi5")
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[3].id)  # selecting language of alexa 0,1

contect = {"atul": "atulmahto201@gmail.com", "papa": "ashokmahto79@gmail.com"}
wtscontect = {'bhanu': '+918595639688', 'kamlesh': '+918595663935', 'addesh': '+919599134513', 'atul': '+91 9910170261',
              'bheya': '+91 9910170261'}


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def listning():
    """ it take microphone input from
    user and recognize it
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print('Listening....')
            # r.adjust_for_ambient_noise(source,duration=0.5)
            audio = r.listen(source)
        except OSError:
            speak('please check your mic connection')
            print('Mic connection error')
        except:
            speak('please check your mic connection')
        try:
            print("Recognizing....")
            query = r.recognize_google(audio)

            print("User Said :", format(query))
        except:
            return 'None'
        return query


# excuting all save data data
try:
    # connecting db file QuestionAnsw
    dbfile = sqlite3.connect("QuestionAnsw.db")
    curs = dbfile.cursor()
    # collecting all added question ans from table questions and set all in list
    qusetion = "SELECT * from questions"
    curs.execute(qusetion)
    x = curs.fetchall()
    qusdic = {}
    for i in x:
        qusdic[i[0]] = i[1]
    try:
        # collecting all added pathes from table path and set all in list
        path = "SELECT * from paths"
        curs.execute(path)
        x = curs.fetchall()
        path_list = {}
        for j in x:
            path_list[j[0]] = j[1]
    # exception if path table not find
    except:
        dbfile = sqlite3.connect("QuestionAnsw.db")
        cours = dbfile.cursor()
        cours.execute('''CREATE TABLE path(name STRING PRIMARY KEY,path STRING);''')
        dbfile.commit()
# exception if db file or other table not find
except:
    dbfile = sqlite3.connect("QuestionAnsw.db")
    cours=dbfile.cursor()
    cours.execute('''CREATE TABLE questions(qus STRING,ans STRING);''')
    dbfile.commit()


def askqus(qus):

    try:
        x = qusdic[str(qus)]
        print(x)
        speak(x)
    except:
        try:
            result = wikipedia.summary(qus, sentences=2)
            if 'song' in result:
                speak('sir you want to play these song say play')
                q = listning().lower()
                if 'play' in q:
                    kit_f('youtube', quary)

            else:
                speak(result)
        except Exception as e:
            ans='unknown'
            curs.execute("INSERT INTO questions(qus,ans) VALUES(?,?);", (qus,ans))
            dbfile.commit()
            print(e)
            speak("please tell again")
            speak("their is no result found")


def list_to_str(lst):
    string = " ".join(lst)
    return string

def kit_f(onwhat, q):
    try:
        if onwhat == 'whatsapp':
            cont = q.index('to')
            contect = q[cont + 1]
            try:
                to = wtscontect[contect]
            except:
                speak("there is no {} in your contect".format(key))
            msg = list_to_str(q[cont + 2:])
            h = int(datetime.datetime.now().hour)
            m = int(datetime.datetime.now().minute)
            m += 2
            kit.sendwhatmsg(to, msg, h, m)
        elif onwhat == 'youtube':
            kit.playonyt(q)
            speak('playing ' + quary)
    except:
        print('you are not on active internet')
        speak('Please checck your inter net connection')


def openf(quary):
    quary = quary.replace("open", '')
    if "youtube" in quary:
        speak("Opning youtube")
        webbrowser.open("www.youtube.com")
    elif "google" in quary:
        speak("Opning google")
        webbrowser.open("www.google.com")
    elif "python" in quary:
        speak("opning Python")
        open(
            "C:\\Users\\ashok mahato\\AppData\\Local\\Programs\\Python\\Python38-32\\Lib\\idlelib\\idle.pyw")
    elif "whatsapp" in quary:
        speak("opening whats app")
        open("C:\\Users\\ashok mahato\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    elif "pycharm" in quary:
        speak("opening pycharm")
        open(
            "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2\\bin\\pycharm64.exe")
    elif "webex" in quary:
        speak("opening webex")
        open("C:\\Program Files (x86)\\Webex\\Webex\\Applications\\ptoneclk.exe")
    elif "zoom" in quary:
        speak("opening zoom")
        open("C:\\Users\\ashok mahato\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
    elif "hp audio switch" in quary:
        speak("opening hp audio switch")
        open("C:\\Program Files (x86)\\HP\\HPAudioSwitch\\HPAudioSwitch.exe")
    elif "cmd" in quary:
        speak("opening cmd")
        open(
            "C:\\Users\\ashok mahato\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt")
    else:
        try:
            open(path_list[str(quary)])
        except:
            press("win")
            speak('searching on pc')
            time.sleep(2)
            typewrite(quary)
            time.sleep(1)
            speak('is that you want can i open it for you? Say yes to open')
            quary = listning().lower()
            if 'yes' in quary:
                press('enter')
                speak('sir can i add this path in by data file it make me fast and easy to open this.'
                      'speak yes to add')
                quary = listning().lower()
                if 'yes' in quary:
                    speak('adding path please do not press any thing for few seconds')
                    time.sleep(3)
                    try:
                        hotkey("atl", "d")
                        hotkey('ctrl', 'c')
                        copy_path = paste()
                        gen_path = ''
                        for path_char in copy_path:
                            gen_path += path_char
                            if path_char == '\\':
                                gen_path += path_char
                        curs.execute("INSERT INTO path(name,path) VALUES(?,?);", (quary, gen_path))
                        dbfile.commit()
                        speak('path added successfully')
                    except Exception as e:
                        speak('i find ' + str(e))


def open(path):
    os.startfile(os.path.join(path))


def wishme():
    hur = int(datetime.datetime.now().hour)
    if 0 <= hur < 12:
        speak('Good Morning !!. Yes tell me how can i help you')
    elif 12 <= hur < 18:
        speak("Good Afternoon !!. Yes tell me how can i help you")
    else:
        speak("Good Evening!!. Yes tell me how can i help you")


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("amahto848@gmail.com", "@aman#8650")
    server.sendmail("amahto848@gmail.com", to, content)
    server.close()


if __name__ == '__main__':
    wishme()
    while True:
        quary = listning().lower()
        if 'alexa' in quary:
            quary=x= quary[6 : : ]       # removing alexa word from string
            quary_list = quary.split()  # converting str to list
            if quary == '':
                speak('yes sir, how may i help you')
            elif quary_list[0] == 'play':
                n_q = quary.replace('play', '')
                kit_f('youtube', n_q)
            elif quary_list[0] == 'search':
                try:
                    scrh = list_to_str(quary_list[1:])
                except:
                    speak('what i search sir')
                    scrh = listning().lower()
                url = 'https://google.com/search?q=' + scrh
                webbrowser.get().open(url)
            elif 'find' in quary_list[:4] and 'location' in quary_list[:4]:
                try:
                    loct = quary_list.index('of')
                    scrh = list_to_str(quary_list[loct:])
                except:
                    speak('for what location i search')
                    scrh = listning().lower()
                url = 'https://google.nl/map/place/' + scrh + '/&amp;'
                webbrowser.get().open(url)
            elif quary_list[0] == 'open':
                openf(quary)
            elif quary_list[0] == 'speak':
                speak(quary.replace('speak', ''))
            elif quary_list[0] == "join":
                if "chemistry" in quary:
                    speak("joining chemistry class")
                    webbrowser.open("https://meetingsapac30.webex.com/meet/pr1566859408")
                # elif "english" in quary:
                #     speak("joining english class")
                #     webbrowser.open("https://meetingsapac30.webex.com/meet/pr1566859408")
                # elif "math" in quary:
                #     speak("joining math class")
                #     webbrowser.open("https://meetingsapac30.webex.com/meet/pr1566859408")
                elif "physics" in quary:
                    speak("joining physics class")
                    webbrowser.open(
                        "https://us04web.zoom.us/j/8514569782?pwd=TWxYcnVvWWNBOU9TU1gyVmJhZkxRdz09")
                elif "computer" in quary:
                    speak("joining computer class")
                    webbrowser.open("1702852372@meetingsapac32.webex.com")
            elif "introduce yourself" in quary:
                speak(
                    "I am Alex. I am your assistant. I accept all your visitors as my reason and follow them is my task"
                    "I take tke the voice command then recognize it and give you output"
                    "I have some spacial feature"
                    " like i can open youtube, google , search on wikipidea,search on pc, play musics, even i copy you as nimickri articts just by giving the command 'copy me alexa' ")
            elif "hello" in quary:
                speak("hello, i am alexa ")
                speak("how may i help you ")

            elif "the current time" in quary:
                time = datetime.datetime.now().strftime("%H hours%M minutes%S seconds")
                speak("Sir The current Time is {}".format(time))
            elif quary_list[0] == 'send':
                if 'message' in quary:
                    kit_f('whatsapp', quary_list)

                elif "email" in quary:
                    speak("password please")
                    quary = listning().lower()
                    if quary == "my email":
                        try:
                            speak("who do you want to send this message!")
                            key = listning().lower()
                            try:
                                to = contect[key]
                            except:
                                speak("there is no {} in your contect".format(key))
                            speak("What should i say!")
                            content = listning().lower()
                            sendEmail(to, content)
                            speak("email has been sent!")
                        except Exception as e:
                            print(e)
                            speak("Soory! dod.. i am not able to sent this email")
                    else:
                        speak("wrong password")
            elif "thank you" in quary:
                speak("its my owner sir")
            elif "bye" in quary:
                speak("i think, i am use full for you 'Thank you' bye! ")
                exit()
            # simple commands
            elif quary_list[0] == "minimise":
                hotkey("win", "down")
            elif quary_list[0] == "minimise" and quary_list[0] == 'all':
                hotkey("win", "d")
            elif quary_list[0] == "maximize":
                hotkey("win", "up")
            elif quary_list[0] == "maximize" and quary_list[1] == 'all':
                hotkey("win", "d")
            elif quary_list[0] == "close":
                hotkey("alt", "f4")

            # tying alexa
            elif "start typing" in quary or quary_list[0] == "type":
                if "start typing" in quary:
                    speak("sir please select location")
                    speak("what i type sir")
                    t = True
                    while t == True:
                        quary = listning().lower()
                        if "stop typing" not in quary:
                            typewrite(quary)
                        elif "stop typing" in quary:
                            speak("ok sir")
                else:
                    quary = quary.replace('type', '')
                    typewrite(quary)

            else:
                askqus(quary)

            # else:
            #     speak('please answer in yes or no')

