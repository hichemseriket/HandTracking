import pyttsx3

# engine = pyttsx3.init()
#
# # engine.say("salut, je suis hichem")
# # engine.say("azzedine, change R, change R")
# # engine.say("ceci est mon premier programme text to speech")
# # engine.say("tu es au top")
# # engine.say("azzedine bouffeur de grosse chatte poilu, professionnel")
# # engine.say("ce que je vais ecrire ici")
# # engine.say("sera parlé")
# # engine.say("par le programme ")
# # engine.say("donc, je te propose ")
# # engine.say("de tester mon programme")
# engine.runAndWait()

import pyttsx3

engine = pyttsx3.init()  # object creation

""" RATE"""
rate = engine.getProperty('rate')  # getting details of current speaking rate
print(rate)  # printing current voice rate
engine.setProperty('rate', 180)  # setting up new voice rate

"""VOLUME"""
volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
print(volume)  # printing current volume level
engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')  # getting details of current voice
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
# engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
# engine.say("vien ici sockette!")
engine.setProperty('voice', voices[0].id)  # changing index, changes voices. 1 for female
engine.say("samooos!")
engine.say("")
# engine.say("alilou voleur de briquet!")
# engine.say('hichem est mon maitre')
# engine.say('mimoze le sang')
# engine.runAndWait()
# engine.stop()

"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.save_to_file('hichem est mon maitre', 'test.mp3')
engine.runAndWait()

# import pyttsx3
#
#
# def onStart(name):
#     print('debut', name)
#
#
# def onWord(name, location, length):
#     print('mot', name, location, length)
#     if location > 10:
#        engine.stop()
#
#
# def onEnd(name, completed):
#     print('fin', name, completed)
#
#
# engine = pyttsx3.init()
# engine.connect('debut de la conversation', onStart)
# engine.connect('debut-mot', onWord)
# engine.connect('fin de la conversation', onEnd)
# engine.say('hichem le boss.')
# engine.runAndWait()

# engine = pyttsx3.init()
# def onStart(name):
#    print('debut', name)
# def onWord(name, location, length):
#    print('mot', name, location, length)
# def onEnd(name, completed):
#    print('fin', name, completed)
#    if name == 'azzedine':
#       engine.say('quelle salaud!', 'mili')
#    elif name == 'mili':
#       engine.endLoop()
# engine = pyttsx3.init()
# engine.connect('debut de la conversation', onStart)
# engine.connect('mot de debut', onWord)
# engine.connect('fin de la conversation', onEnd)
# engine.say('hichem le boss.', 'azzedine')
# engine.startLoop()

# engine = pyttsx3.init()
# def onStart(name):
#    print ('starting', name)
# def onWord(name, location, length):
#    print ('word', name, location, length)
# def onEnd(name, completed):
#    print ('finishing', name, completed)
#    if name == 'fox':
#       engine.say('What a lazy dog!', 'dog')
#    elif name == 'dog':
#       engine.endLoop()
# engine = pyttsx3.init()
# engine.connect('started-utterance', onStart)
# engine.connect('started-word', onWord)
# engine.connect('finished-utterance', onEnd)
# engine.say('The quick brown fox jumped over the lazy dog.', 'fox')
# engine.startLoop()
