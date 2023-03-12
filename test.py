from gtts import gTTS
tts = gTTS('hello', lang="en")
tts.save('hello.mp3')

# import googletrans
# from googletrans import Translator

# print(googletrans.LANGUAGES)
# text1 = "Hello welcome to my website!"
# translator = Translator()
# trans1 = translator.translate(text1, src='en', dest='ko')
# print("English to Japanese: ", trans1.text)
