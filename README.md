# Legal Documentation Assistant

Demo - 1 : https://drive.google.com/file/d/1K8KQl9LV2TSjW2_hioFujagFmuPQEvh3/view?usp=sharing
Demo - 2 : https://drive.google.com/file/d/1cIdk7ZBZfXh3ZLznmRMBgXJhicIYgrEF/view?usp=sharing


Legal documentation can be a complicated and time-consuming process, especially for individuals and small businesses who may not have access to legal resources. 
In addition, the language and jargon used in legal documents can be difficult for non-lawyers to understand, which can lead to errors and misunderstandings. 
So I managed to bring up a solution that involves using LLMs that both find the appropriate document needed to address the issue and also generate a 
document in pdf format. 

For Embedding I have used ada-embeddings and so in the folders "htmlgen", "templates" and "knowledge" You have to add the .env file information in the format
"OPENAI_API_BASE = "https://openai-dxxx.openai.azure.com/"
OPENAI_API_KEY = "58cccbeeb49a4xxxxxxxxxx77765f16"
OPENAI_API_TYPE = "azure"
OPENAI_DEPLOYMENT_NAME = "SIH"
OPENAI_DEPLOYMENT_VERSION = "2"
OPENAI_MODEL_NAME="text-embedding-ada-002""

in the .env file in the root folder you hafta make an .env file that contains the openai api key that you can avail from platform.openai.com

I have used 3 LLMs which is created and returned as a conversational chain from the three python files : Advisor,Templategen and Htmlgen.

The streamlitapp.py is the file to be run and since streamlit is used, "streamlit run streamlitapp.py" is to be used.

Thanks.

You can check the sample generations here : https://lnkd.in/geipKPqH
