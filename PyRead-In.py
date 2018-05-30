from gtts import gTTS
import textract as tx
import re
import os.path

filepath = raw_input("Paste File: ")
if os.path.exists(filepath):
    print("File found")
    k = raw_input("Speed slow/fast [S/f]?")
    format = raw_input("Enter desired output format mp3/wav[M/w]?")
    if(k == 's' or k == 'S'):
        k = True
    else:
        k = False
    raw_text = tx.process(filepath)
    if(format == 'mp3' or format == 'M' or format == 'm'):
        format = '.mp3'
    else:
        format = '.wav'
    print("File converted to text")
    text = re.sub(r'[^\x00-\x7F]+', ' ', raw_text)
    print("Processed text")
    tts = gTTS(text=text, lang='en', slow=k)
    tts.save(os.path.splitext(filepath)[0]+format)
    print("Audio file is ready!!!")
else:
    print("File Not Found")
