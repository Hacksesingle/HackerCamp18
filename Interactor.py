import speech_recognition as sr  
   
# obtain audio from the microphone  
r = sr.Recognizer()  
with sr.Microphone() as source:  
  print("Please wait. Calibrating microphone...")  
  # listen for 5 seconds and create the ambient noise energy level  
  r.adjust_for_ambient_noise(source, duration=5)  
  print("Say something!")  
  audio = r.listen(source)  
   
# recognize speech using Sphinx  
try:  
  print("Sphinx thinks you said '" + r.recognize_sphinx(audio) + "'")  
except sr.UnknownValueError:  
  print("Sphinx could not understand audio")  
except sr.RequestError as e:  
  print("Sphinx error; {0}".format(e)) 

from gtts import gTTS 

# This module is imported so that we can 
# play the converted audio 
import os 
 
mytext = r.recognize_sphinx(audio) 
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("welcome.mp3") 
os.system("mpg321 welcome.mp3")
