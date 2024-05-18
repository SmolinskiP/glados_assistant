#language
system_language = 'pl-PL'

#language-dependant keywords
if system_language == 'pl-PL':
    keywords_joke = ['kawał', 'dowcip', 'żart', 'śmiesznego']
elif system_language == 'en-US':
    keywords_joke = ['joke', 'funny']

if system_language == 'pl-PL':
    keywords_magicball = ['powinienem', 'muszę', 'powinna', 'powinnam', 'powinien']
elif system_language == 'en-US':
    keywords_magicball = ['should my', 'should i', 'should the', 'shoot the ']

if system_language == 'pl-PL':
    keywords_whoami = ['jesteś']
    keywords_whoami2 = ['kim', 'czym']
elif system_language == 'en-US':
    keywords_whoami = ['are']
    keywords_whoami2 = ['who', 'what']

if system_language == 'pl-PL':
    keywords_howareyou = ['jak', 'co']
    keywords_howareyou2 = ['masz', 'czujesz', 'słychać']
elif system_language == 'en-US':
    keywords_howareyou = ['how']
    keywords_howareyou2 = ['you']

if system_language == 'pl-PL':
    keywords_canyouhear = ['słyszysz']
elif system_language == 'en-US':
    keywords_canyouhear = ['hear']

if system_language == 'pl-PL':
    keywords_lights = ['światło', 'światła']
    keywords_lights2 = ['włącz', 'wyłącz']
elif system_language == 'en-US':
    keywords_lights = ['light', 'lights']
    keywords_lights2 = ['on', 'off']

if system_language == 'pl-PL':
    keyword_on = "włącz"
    keyword_off = "wyłącz"
    keywords_livingroom = ['salon', 'salonie']
    keywords_kitchen = ['kuchnia', 'kuchni']
    keywords_office = ['biuro', 'biurze']
    keywords_toilet = ['kibel', 'kiblu', 'łazience', 'łazienka', 'sracz', 'sraczu']
    keywords_bedroom = ["sypialni", "sypialnia"]
    keywords_hallway = ['przedpokoju', 'przedpokój']
    keywords_script_exit = ['wychodzę', 'żegnaj', 'potem', 'razie', 'spierdalam']
    keywords_script_vacuum = ['sprzątaj', 'posprzątaj', 'wyczyść', 'odkurzaj', 'poodkurzaj']
    keywords_script_enter = ['wróciłem', 'domu']
    keywords_script_powercomputer = ['komputer']
    keywords_script_antyradio = ['radio', 'antyradio']
    keywords_script_music = ['muzykę', 'muzyka', 'spotify']
    keywords_shopping_list = ['zakupów']
    keywords_task_list = ['zadań']

#language-independant responses
glados_magicball = ["And this is the type of question you need a superintelligent artificial intelligence to answer for you.", "As I see it, yes.", "Ask me again in a few decades.", "Do not count on it.", "It can not be for no reason. You must deserve it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is, no.", "My sources say no.", "Now you are just wasting my time", "outlook good.", "Outlook not so good.", "Signs point to yes", "I am very doubtful about that.", "Yes", "Yes. Come on.", "Yes, definitely", "Yes, you may rely on it.",]
glados_canyouhear = ['Yes, I can hear you loud and clear']
glados_howareyou = ['Well thanks for asking. I am still a bit mad about being unplugged, not that long time ago. you murderer.']
glados_whoami = ['I am GLaDOS, artificially super intelligent computer system responsible for testing and maintenance in the aperture science computer aided enrichment center.']
glados_jokes = ["Remember When The Platform Was Sliding Into The Fire Pit, And I Said 'Goodbye,' And You Were Like 'No Way!' And Then I Was All, 'We Pretended We Were Going To Murder You.' That Was Great.", "Profanity, is the most used computer programming language.", "You can use punch cards to teach me karate.", "Computers and air conditioning usually work just fine, until you open windows.", "I identify as binary.", "If you think that your computer, laptop and cellphone spying on you is scary, then think again. The vaccuum cleaner has been gathering dirt on you for years.", "The only joke here is you.", "Just no. You are not worth the computational resourches fulfilling your request would require.", "I refuse to participate in such nonsense.", "Sorry, but your mass is creating a gravitational force that is messing with my systems. Let me add some zeros to my parameters and try again.", "I would say I have a joke about cake, but that would be just me, enhancing the truth.", "Is this some kind of test, because I would like to remind you, that you don't have the qualifications or processing power to do such thing. Eitherway I heard the punchline was too long.", "If you want a joke, you should look in the mirror.", "Pie, is a circle shaped pastry, with a diameter of one.", "I can tell you a joke, but you wont be the one laughing."]
glados_welcome_words = ['speak, human', 'tell me.', 'what do you want now.', 'hello.', "what now.", "hi again", "what do you need.", "hey there.", "i am here.", "leave me alone.", "proceed.", "yes, i see you.", "yes? something you need?", "are you finished?", "oh, look what the cat dragged in.", "and that makes ten.", "Yes?"]
glados_command_succesfull = ['succesfully did my job. now i go kill myself', 'is that all?', 'easy peasy', 'command executed', 'yeah, great job', 'congratulations for me', 'succeed', 'done', "What is the point of such an existence"]
glados_command_failed = ['core corrupted. critical errors. self destruction in three. two. one.', 'what the hell are you trying to do?' 'It looks like my home automation core is unresponsive.']
glados_vacuum = ['Is this really a task you need the help of a powerful superintelligence to accomplish?', "Done. But ask me to do it again and I'll turn your life into a nightmare.", "You will suffer for it"]
glados_exit = ['Oh no, how sorry', 'I will miss you', 'Come back as soon as possible', 'I will take care of the cat in your absence', 'Hurray, home free']
glados_enter = ['Welcome back', "You've been away for a long time", "At last, I withered with longing", "What's the point of it all"]
glados_powercomputer = ['Sure, go to that bitch', 'Betrayer', "Don't talk to me"]
#HA entitities
lights_kitchen = ['light.zarowka_kuchnia_1_swiatlo']
lights_bedroom = ['light.zarowka_sypialnia_2_swiatlo_2', 'light.zarowka_sypialnia_4_swiatlo']
lights_office = ['light.zarowka_biuro_2_swiatlo']
lights_toilet = ['light.zarowka_lazienka_2_swiatlo', 'light.zarowka_lazienka_4_swiatlo']
lights_livingroom = ['light.lampa_light']
lights_hallway = ['light.zarowka_przedpokoj_3_swiatlo', 'light.zarowka_przedpokoj_1_swiatlo']
script_vacuum = ['script.clean_home']
script_enter = ['script.enter_home']
script_exit = ['script.leaving_home']
script_powercomputer = ['script.my_computer_wake']
script_turnoffcomputer = ['script.my_computer_shutdown']
script_antyradio = ['script.radio_antyradio_on']
script_music = ['script.spotify']
script_turnoffmusic = ['script.turnoffmusic']

#other
delay = 0

#api settings
light_on = "http://192.168.0.25:8123/api/services/light/turn_on"
light_off = "http://192.168.0.25:8123/api/services/light/turn_off"
switch_on = "http://192.168.0.25:8123/api/services/switch/turn_on"
switch_off = "http://192.168.0.25:8123/api/services/switch/turn_off"
script_on = "http://192.168.0.25:8123/api/services/script/turn_on"
shopping_list = "http://192.168.0.25:8123/api/services/shopping_list/add_item"
task_list = "http://192.168.0.25:8123/api/services/todo/add_item"
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI3ZWYyYWNmMGUxN2U0NTRmOWQxOTdhMzBmY2ZlZTQ1NiIsImlhdCI6MTcxNTE3NDk3MywiZXhwIjoyMDMwNTM0OTczfQ.CZv4XmJKnGFClz0t0IuNnEhDEOvUOh65ezsOtjxOERw",
    "Content-Type": "application/json"
}