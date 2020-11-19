from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from textblob import TextBlob
root = Tk ()

root.title('Translator')
root.geometry('700x300+800+250')
root.resizable(False, False)
root.config(bg = '#1A1A1A')

######## Creating the function #######
LaNG_pick = {'Afrikaans': 'af', 'Albanian': 'sq', 'Amharic': 'am', 'Arabic': 'ar', 'Armenian': 'hy', 'Azerbaijani': 'az', 'Basque': 'eu', 'Belarusian': 'be', 'Bengali': 'bn', 'Bosnian': 'bs', 'Bulgarian': 'bg', 'Catalan': 'ca', 'Cebuano': 'ceb', 'Chichewa': 'ny', 'Chinese (simplified)': 'zh-cn', 'Chinese (traditional)': 'zh-tw', 'Corsican': 'co', 'Croatian': 'hr', 'Czech': 'cs', 'Danish': 'da', 'Dutch': 'nl', 'English': 'en', 'Esperanto': 'eo', 'Estonian': 'et', 'Filipino': 'tl', 'Finnish': 'fi', 'French': 'fr', 'Frisian': 'fy', 'Galician': 'gl', 'Georgian': 'ka', 'German': 'de', 'Greek': 'el', 'Gujarati': 'gu', 'Gaitian creole': 'ht', 'Hausa': 'ha', 'Hawaiian': 'haw', 'Hebrew': 'he', 'Hindi': 'hi', 'Hmong': 'hmn', 'Hungarian': 'hu', 'Icelandic': 'is', 'Igbo': 'ig', 'Indonesian': 'id', 'Irish': 'ga', 'Italian': 'it', 'Japanese': 'ja', 'Javanese': 'jw', 'Kannada': 'kn', 'Kazakh': 'kk', 'Khmer': 'km', 'Korean': 'ko', 'Kurdish (kurmanji)': 'ku', 'Kyrgyz': 'ky', 'Lao': 'lo', 'Latin': 'la', 'Latvian': 'lv', 'Lithuanian': 'lt', 'Luxembourgish': 'lb', 'Macedonian': 'mk', 'Malagasy': 'mg', 'Malay': 'ms', 'Malayalam': 'ml', 'Maltese': 'mt', 'Maori': 'mi', 'Marathi': 'mr', 'Mongolian': 'mn', 'Myanmar (burmese)': 'my', 'Nepali': 'ne', 'Norwegian': 'no', 'Odia': 'or', 'Pashto': 'ps', 'Persian': 'fa', 'Polish': 'pl', 'Portuguese': 'pt', 'Punjabi': 'pa', 'Romanian': 'ro', 'Russian': 'ru', 'Samoan': 'sm', 'Scots gaelic': 'gd', 'Serbian': 'sr', 'Sesotho': 'st', 'Shona': 'sn', 'Sindhi': 'sd', 'Sinhala': 'si', 'Slovak': 'sk', 'Slovenian': 'sl', 'Somali': 'so', 'Spanish': 'es', 'Sundanese': 'su', 'Swahili': 'sw', 'Swedish': 'sv', 'Tajik': 'tg', 'Tamil': 'ta', 'Telugu': 'te', 'Thai': 'th', 'Turkish': 'tr', 'Ukrainian': 'uk', 'Urdu': 'ur', 'Uyghur': 'ug', 'Uzbek': 'uz', 'Vietnamese': 'vi', 'Welsh': 'cy', 'Xhosa': 'xh', 'Yiddish': 'yi', 'Yoruba': 'yo', 'Zulu': 'zu'}

def getLanguage():
    word3 = TextBlob(Redacted.get())
    lan = word3.detect_language()
    lan_topick = select.get()
    lan_to = LaNG_pick[lan_topick]
    word3 = word3.translate(from_lang= lan, to=lan_to)
    label3.configure(text=word3)
    Redacted2.set(word3)




######## Langauage Selection ######


select = StringVar()
font_box = Combobox(root, width= 30, textvariable = select, state= 'readonly')
font_box['values'] = [ i for i in LaNG_pick.keys()]
font_box.current(21)
font_box.place(x = 400, y=90)

######## GUI BOX ######

Redacted = StringVar()
entryENG = Entry(root, width= 50 , textvariable = Redacted, bg = '#CCCCCC')
entryENG.place(x = 10 , y= 90 )
Redacted2 = StringVar()
entryForeign = Entry(root, width= 50 , textvariable = Redacted2, bg = '#CCCCCC')
entryForeign.place(x = 10 , y= 160 )

######## Entry BOXES REDACTED CAN IS JUST VAR NAME + entryENG IS FIRST/ entryForeig IS SECOND BOX    ######

label0 = Label( root, text = 'Phraser V2' , foreground = ('white'), bg ='#1A1A1A', font= ('bold', 22 ) )
label0.place(x = 300, y=10)


label1 = Label(root, text = 'Enter a sentence : ' , foreground = ('white'), bg = '#1A1A1A', font = ('bold'))
label1.place(x = 10, y=65)


label2 = Label(root, text = 'Translation : ' , foreground = ('white'), bg = '#1A1A1A', font = ('bold'))
label2.place(x = 10, y=135)

label3 = Label()
####### FUNCTIONS WHERE TRANSLATIONS WILL BE AND COOL RADICAL BUTTONS OWO   ###########
butt = Button(root, text = 'Translate ', bd = 10, bg = '#940000' , fg = 'white', activebackground = 'blue', width = 10, font = 'bold', foreground= 'white', command = getLanguage )
butt.place(x= 10, y = 200)
#### Logo ##############
ima = PhotoImage(file = 'Logo.png')








root.mainloop()
