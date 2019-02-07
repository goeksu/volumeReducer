import os
from pydub import AudioSegment

form = raw_input("format:")
liste = os.listdir(os.getcwd())
print "asagidaki dosyalar kisiliyor"
for ses in liste:
  if ses.endswith(form):
    print ses;
    sarki = AudioSegment.from_mp3(ses)
    azaltildi = sarki -  100
    azaltildi.export(ses, format="mp3")
        #azaltildi.export(ses, format="mp3")
		
print"BITTI"







