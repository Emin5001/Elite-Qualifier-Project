# needs pip install chatterbot, but that can't be done in repl.it to my knowledge. otherwise, the code should be working fine, but that is why it cannot run. If I did it on PyCharm or VSC, then it wouldn't have this error.

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new instant of the ChatBot

bot = ChatBot(
  'Bob',
  silence_performance_warning=True,
  logic_adapters = [
    'chatterbot.logic.MathematicalEvaluation',
    'chatterbot.logic.TimeLogicAdapter',
    'chatterbot.logic.BestMatch'
  ],
)

# Trains the bot

trainer = ListTrainer(bot)

trainer.train([
  "How are you?",
  "I am good.",
  "LeBron is the GOAT.",
  "No he isn't.",
  "Jordan is the GOAT",
  "Yes he is.",
  "Who will win the NBA Championship this year?",
  "The Los Angeles Lakers have my vote.",
  "Who won the NBA Championship last year?",
  "The Los Angeles Lakers won the NBA championship last year.",
  "How many points is a dunk worth?",
  "A dunk is worth 2 points.",
  "What is your favorite team?",
  "My favorite NBA Team is the New York Knicks... Yeah, it's been a rough few years for me.",
  "Bye",
  "Bye, it was nice talking about basketball with you."
])


name = input("Enter your name: ")
print("Hello " + name + "! Welcome to the Bot Basketball Service! Ask me a question, and we can have a small conversation about basketball! If you want to leave the bot, just say Bye or bye, and I'll disconnect!")
print("hello")

while True:
  request = input(name+ ": ")
  if request=='Bye' or request=='bye':
    print('Bot: Bye')
    break
  else:
    response = bot.get_response(request)
    print('Bot: ', response) 

