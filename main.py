from Knowledge import knowledge
from Templates import templates


import Advisor
import TemplateEngine

knowledge.Develop()
templates.Develop()

query = input('Enter your use case : ')

conversation1 = Advisor.get()
response = conversation1({'question':f'Tell me the name of a one legal document related to the need {query}'})

print('\n\n'+response['answer']+'\n\n')
document = response['answer']

conversation2 = TemplateEngine.get()
response = conversation2({'question':f"Give a template for the described document in simple words and without any disclaimers : {response['answer']} "})
print(response['answer'])
template = response['answer']

response = conversation2({'question':"frame questions that should be asked to the user to fill in all the place holders given in this template :\n{template}"})
print(response['answer'])

user_answers = input('Answer these : ')

response = conversation1({'question':"Using this template ({template}) make a document with random values in place holders"})

print(response['answer'])
