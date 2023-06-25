import os
import pyttsx3
import subprocess as sp
import speech_recognition as speech
import webbrowser
os.system("python assistant_corner.py")
import assistant_corner
engine = pyttsx3.init()
engine.setProperty('voice', "english")
engine.setProperty('rate', 170)
engine.setProperty('volume', 1)
engine.say(assistant_corner.greet())
engine.runAndWait()
r = speech.Recognizer()
mic = speech.Microphone(device_index=1)
f = open('log.txt', 'a')
tmp_text = ''
with mic as source:
    print('[*] Speak Anything')
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    print(r.recognize_google(audio)) 
    try:
        tmp_text = r.recognize_google(audio)
        content = f.write(f'[+] {tmp_text}\n')
    except:
       print("Sorry could not recognize you voice")
       pass
text = str.lower(tmp_text.split(' ')[-1])
engine.say(f'running command {text}. Please have patience.')
engine.runAndWait()
print(f'You said {text}')
map_command = {
	'shutdown' : 0,											# this no is the process id assigned by us
	'powershell' : 1,
	'dialer' : 2,
	'dvdplay' : 3,
	'calculator' : 4,
	'edge' : 5,
	'bluetooth' : 6,
	'panel' : 7,
	'explorer' : 8,
	'prompt' : 9,
	'plus' : 10,
	'text' : 11,
	'word' : 12,
	'powerPoint' : 13,
	'excel' : 14,
	'access' : 15,
	'chrome' : 16,
	'firefox' : 17,
	'paint' : 18,
	'news' : 19,
	'clock' : 20,
	'camera' : 21,
	'calendar' : 22,
	'notepad' : 23,
	'youtube' : 24,
	'google' : 25,
	'joke' : 26,
}
try:
	choice = str(map_command[text])
	if choice == '0':
			os.system("shutdown /s /t 1")

	elif choice == '1':
			sp.Popen(['powershell'])

	elif choice =='2':
			sp.Popen(['dialer'])

	elif choice =='3':
			sp.Popen(['dvdplay'])

	elif choice =='4':
			sp.Popen(['calc'])

	elif choice =='5':
			sp.Popen(['MicrosoftEdge'])

	elif choice =='6':
			sp.Popen(['fsquirt'])

	elif choice =='7':
			sp.Popen(['control'])

	elif choice =='8':
			sp.Popen(['explorer'])

	elif choice =='9':
			sp.Popen(['cmd'])

	elif choice =='10':
		lnk_path = 'C:\\Users\\Public\\Desktop\\Turbo C++.lnk'
		sp.Popen(lnk_path,shell=True)

	elif choice =='11':
		lnk_path = 'C:\\Users\\Hp\\Downloads\\sublime_text_build_4126_x64\\subl.exe'
		sp.Popen(lnk_path,shell=True)

	elif choice =='12':
		lnk_path = 'C:\\Users\\Hp\\Desktop\\Microsoft Office Word 2007.lnk'
		sp.Popen(lnk_path,shell=True)

	elif choice =='13':
		lnk_path = 'C:\\Users\\Hp\\Desktop\\Microsoft Office PowerPoint 2007.lnk'
		sp.Popen(lnk_path,shell=True)

	elif choice =='14':
		lnk_path = 'C:\\Users\\Hp\\Desktop\\Microsoft Office Excel 2007.lnk'
		sp.Popen(lnk_path,shell=True)

	elif choice =='15':
		lnk_path = 'C:\\Users\\Hp\\Desktop\\Access.lnk'
		sp.Popen(lnk_path,shell=True)

	elif choice =='16':
		lnk_path = 'C:\\Users\\STUDENT\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Chrome.lnk'
		sp.Popen(lnk_path,shell=True)

	elif choice =='17':
		lnk_path = 'C:\\Program Files (x86)\\Mozilla Firefox\\Firefox.lnk'
		sp.Popen(lnk_path,shell=True)

	elif choice =='18':
		lnk_path = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Paint.lnk'
		sp.Popen(lnk_path,shell=True)

	elif choice =='19':
		lnk_path = 'C:\\Users\\Hp\\Desktop\\Microsoft News.lnk'
		sp.Popen(lnk_path,shell=True)

	elif choice =='20':
		lnk_path = 'C:\\Users\\Hp\\Desktop\\Alarms & Clock.lnk'
		sp.Popen(lnk_path,shell=True)

	elif choice =='21':
		lnk_path = 'C:\\Users\\Hp\\Desktop\\Camera.lnk'
		sp.Popen(lnk_path,shell=True)

	elif choice =='22':
		lnk_path = 'C:\\Users\\Hp\\Desktop\\Calendar.lnk'
		sp.Popen(lnk_path,shell=True)

	elif choice == '23':
			sp.Popen(['notepad'])

	elif choice == '24':
		to_search = input('What do you want me to search?')
		webbrowser.open(f'https://youtube.com/results?search_query={to_search}')

	elif choice == '25':
		to_search = input('What do you want to search?')
		webbrowser.open(f'https://google.com/search?q={to_search}')

	elif choice == '26':
		print(assistant_corner.jokes())
		say.engine(assistant_corner.jokes())
		say.runAndWait()

except Exception as e:
	engine.say(f' Nai Mila')
	engine.runAndWait()

