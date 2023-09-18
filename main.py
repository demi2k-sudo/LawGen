from Knowledge import knowledge
from Templates import templates
from Htmlgen import htmls
import pdfkit
from test import fillin

import Advisor
import TemplateEngine
import HtmlGen

knowledge.Develop()
templates.Develop()
htmls.Develop()
def html_to_pdf(html_string, output_pdf_path):

    try:
        # Configure pdfkit options
        options = {
            'page-size': 'A4',
            'margin-top': '20mm',
            'margin-right': '20mm',
            'margin-bottom': '20mm',
            'margin-left': '20mm',
            'encoding': 'UTF-8',
        }
        config = pdfkit.configuration(wkhtmltopdf="C:\Program Files\wkhtmltopdf\Bin\wkhtmltopdf.exe")

        # Create a PDF from the HTML string and save it to the output path
        pdfkit.from_string(html_string, output_pdf_path, options=options, configuration=config)


        print(f"PDF saved to: {output_pdf_path}")
    except Exception as e:
        print(f"Error: {e}")

query = input('Explain elaborately what do you need to document legally: ')

conversation1 = Advisor.get()
response = conversation1({'question':f'Tell me the name of a one legal document related to the need {query}. Give the name alone do not give a sentence'})

print('\n\n'+response['answer']+'\n\n')
document = response['answer']

response = conversation1({'question':f'Find the laws related to the below details\n Document : {document}\n User query: {query}'})
laws = response['answer']
print(laws)
prompt = f'''
Give a , Very long template(Details to be filled before taking print enclosed by squared brackets) for the {document} 
in simple words that a layman can understand and detailed, without any disclaimers and also consider that the user has said ' {query}' 
Include these Supporting laws : {laws}
Rules: Use a single type of place holder name for a single entity
Leave a blank space for signatures
'''

conversation2 = TemplateEngine.get()
response = conversation2({'question':prompt})
print(response['answer'])
template = response['answer']

result = fillin(template)

conversation3 = HtmlGen.get()
prompt2 = f'''
I want you to convert document into a html enclosing the appropriate field with appropriate tags based on your knowledge.
I want the first heading to be aligned centre and all the headings to be bold
here is the document
{result}
'''
response = conversation3({'question':prompt2})
htmlresult = response['answer']
print(htmlresult)

name = input('Enter the file name :')
html_to_pdf(htmlresult,f'{name}.pdf')



