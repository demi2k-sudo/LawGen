import streamlit as st
import pdfkit
import Advisor
import TemplateEngine
import HtmlGen

# Define a function to convert HTML to PDF
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
        config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")

        # Create a PDF from the HTML string and save it to the output path
        pdfkit.from_string(html_string, output_pdf_path, options=options, configuration=config)

        st.write(f"PDF saved to: {output_pdf_path}")
    except Exception as e:
        st.error(f"Error: {e}")

# Streamlit app
def main():
    st.title('Legal Documentation Assistant')

    if 'conversation1' not in st.session_state:
        st.session_state.conversation1 = None
    if 'conversation2' not in st.session_state:
        st.session_state.conversation2 = None
    if 'conversation3' not in st.session_state:
        st.session_state.conversation3 = None
    if 'advisor_response' not in st.session_state:
        st.session_state.advisor_response = None  # Initialize the session state variable
    if 'template' not in st.session_state:
        st.session_state.template = None
    if 'generate_pdf' not in st.session_state:
        st.session_state.generate_pdf = False  # Initialize the generate PDF flag

    # with st.spinner("Loading..."):
        # Your code for loading modules...

    query = st.text_input('Explain elaborately what do you need to document legally: ')

    if query:
        if st.session_state.advisor_response is None:
            with st.spinner('Processing Advisor...'):
                st.session_state.conversation1 = Advisor.get()
                response = st.session_state.conversation1({'question':f'Tell me the name of one legal document related to the need {query}. Give the name alone, do not give a sentence'})
                st.session_state.advisor_response = response  # Store the advisor's response

        st.write(st.session_state.advisor_response['answer'])
        document = st.session_state.advisor_response['answer']

        response = st.session_state.conversation1({'question':f'Find the laws related to the below details\n Document : {document}\n User query: {query}'})
        laws = response['answer']
        st.write(laws)

        prompt = f'''
        Give a very long template (details to be filled before taking print enclosed by squared brackets) for the {document} 
        in simple words that a layman can understand and detailed, without any disclaimers, and also consider that the user has said '{query}' 
        Include these Supporting laws: {laws}
        Rules: Use a single type of placeholder name for a single entity
        Leave a blank space for signatures
        '''

        st.session_state.conversation2 = TemplateEngine.get()
        response = st.session_state.conversation2({'question':prompt})
        template = response['answer']
        st.session_state.template = template
        st.write(template)

    # Check if template is available
    if st.session_state.template:
        with st.form(key='template_form'):
            filled_template = ""
            lines = st.session_state.template.split('\n')
            for line in lines:
                if '[' in line and ']' in line:
                    placeholder = line[line.find('[')+1:line.find(']')]
                    # Use a unique key based on the placeholder
                    user_input = st.text_input(f"Enter value for '{placeholder}':", key=f"{placeholder}_input")
                    line = line.replace(f"[{placeholder}]", user_input)
                filled_template += line + '\n'

            if st.form_submit_button("Generate PDF") and not st.session_state.generate_pdf:
                st.session_state.generate_pdf = True  # Set the flag to generate PDF
                st.experimental_rerun()  # Rerun the app to generate the PDF

    if st.session_state.generate_pdf:
        st.session_state.conversation3 = HtmlGen.get()
        prompt2 = f'''
        I want you to convert the document as it is into HTML enclosing the appropriate field with appropriate tags based on your knowledge.
        I want the first heading to be aligned center and all the headings to be bold, and all the fonts must be Times New Roman and formally spaced.
        Here is the document:
        {filled_template}
        '''
        st.write(prompt2)
        response = st.session_state.conversation3({'question': prompt2})
        htmlresult = response['answer']
        st.write(htmlresult)

        # Generate the PDF with the filled template
        pdf_filename = f'{document}_filled.pdf'
        html_to_pdf(htmlresult, pdf_filename)
        st.write(f"PDF saved to: {pdf_filename}")

if __name__=='__main__':
    main()
