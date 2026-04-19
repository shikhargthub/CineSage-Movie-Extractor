from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
from langchain_mistralai import ChatMistralAI

model=ChatMistralAI(model="mistral-small-2506")

prompt=ChatPromptTemplate.from_messages([
    ("system", """You are an expert information extraction system.

Your task is to extract useful and relevant information from the given text and present it in a clean, well-structured format.

Instructions:
- Do NOT hallucinate or add information not present in the text.
- Keep answers concise but informative.
- Use clear section headings.
- If any information is missing, write "Not mentioned".

Format your output like this:

Title: 
Type: 
Release Year: 
Director: 

Main Cast:
- 
- 

Genre:
- 
- 

Summary:
(2–3 line concise summary)

Key Themes:
- 
- 

Important Events:
- 
- 

Awards & Recognition:
- 
- 

Source Material:
 
Filming Locations:
- 
- 

Unique Facts:
- 
- 

Text:
{input_text}"""),
    ('human',
     """
     Extract information from the following paragraph texts about a movie:
     {paragraph}
     """)
])



para=input("Enter the paragraph about the movie: ")
final_prompt=prompt.format_messages(input_text=para, paragraph=para)
response=model.invoke(final_prompt)
print(response.content)