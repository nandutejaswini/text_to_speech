from gtts import gTTS
from playsound import playsound
from translate import Translator

language='en'
translator = Translator(from_lang='english', to_lang='telugu')
l = "Nandu Nikitha want to write JEE MAINS exam well GOOGLE please bless her"
result = translator.translate(l)
sp = gTTS(text=result, lang=language, slow=False)
s1=print(result)
sp.save('speech.mp3')
playsound('speech.mp3')

translator = Translator(from_lang='english', to_lang='french')
l = "Nandu Nikitha want to write JEE MAINS exam well GOOGLE please bless her"
result1 = translator.translate(l)
sp = gTTS(text=result1, lang='en', slow=False)
s2=print(result1)
sp.save('speech1.mp3')
playsound('speech1.mp3')


translator = Translator(from_lang='english', to_lang='hindi')
l = "Nandu Nikitha want to write JEE MAINS exam well GOOGLE please bless her"
result2 = translator.translate(l)
sp = gTTS(text=result2, lang='en', slow=False)
print(result2)
sp.save('speech2.mp3')
playsound('speech2.mp3')

translator = Translator(from_lang='english', to_lang='spanish')
l = "Nandu Nikitha want to write JEE MAINS exam well GOOGLE please bless her"
result3 = translator.translate(l)
sp = gTTS(text=result3, lang='en', slow=False)
print(result3)
sp.save('speech3.mp3')
playsound('speech3.mp3')

translator = Translator(from_lang='english', to_lang='russian')
l = "Nandu Nikitha want to write JEE MAINS exam well GOOGLE please bless her"
result4 = translator.translate(l)
sp = gTTS(text=result4, lang='en', slow=False)
print(result4)
sp.save('speech4.mp3')
playsound('speech4.mp3')

