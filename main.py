from Knowledge import knowledge
from Templates import templates

from test import fillin

import Advisor
import TemplateEngine

knowledge.Develop()
templates.Develop()

query = input('Explain elaborately what do you need to document legally: ')

conversation1 = Advisor.get()
response = conversation1({'question':f'Tell me the name of a one legal document related to the need {query}. Give the name alone do not give a sentence'})

print('\n\n'+response['answer']+'\n\n')
document = response['answer']

conversation2 = TemplateEngine.get()
response = conversation2({'question':f"Give a , Very long template for the {document} in simple words and detailed and without any disclaimers and also consider that the user has said ' {query}'"})
print(response['answer'])
template = response['answer']

result = fillin(template)
