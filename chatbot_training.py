from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)

for files in os.listdir('C:/python/chatterbot-corpus-master\chatterbot_corpus\data\english/'):
	data = open('C:/python/chatterbot-corpus-master\chatterbot_corpus\data\english/' + files, 'r').readlines()
	bot.train(data)

while True:
	message = imput('You: ')
	if message.strip() != 'Bye':
	   reply = bot.get_response(message)
	   print('ChatBot: ', reply)
	if messgae.strip() == 'Bye':
	   print('ChatBot : Bye')
	   break