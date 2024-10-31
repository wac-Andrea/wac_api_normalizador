from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()  

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY")
)

META_PROMPT = """
Tengo un texto mal escrito con símbolos extraños, palabras mal ordenadas, palabras mal separadas o con faltas de ortografía. 
Necesito que me devuelvas el texto correctamente escrito, con buena puntuación y con las palabras corregidas. 
Sólo corrige el texto, no añadas información o palabras que no vengan en el prompt del usuario. Selecciona únicamente
los párrafos y frases que encuentres. Elimina las frases completas que empiecen por Fig.
""".strip()

def generate_prompt(task_or_prompt: str) -> str:
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": META_PROMPT,
            },
            {
                "role": "user",
                "content": task_or_prompt,
            },
        ],
    )
    return completion.choices[0].message.content

def texts_to_api(text_list):
    corrected_texts = []
    for text in text_list:
        corrected_text = generate_prompt(text)
        corrected_texts.append(corrected_text)
    return corrected_texts


texts_to_correct = [
    "La unidad del tanque convierte el nivel del combustible del tanque en una senal de corriente electrica. La figura 1.11 muestra su construccion. Para convertir el nivel del combustible en una senal electrica se utiliza una resistencia variable con cable de nicromio， con un elemento deslizante unido a un f1otadof. ",
    " El medidor de combustible es de tipo bimetal， y s叩uindicωador oscila de叩pen吋die白ndode la ca訂釦ntidadde ∞cor汀n白er凶lteque pasa a tr um泊dadde calent阻aml白entωodel bimetal. Cuando el flotador esta en la posicion mas alta， la unidad del tanque indica una resistencia de 9，5 a 11 ohmios. Esto peロniteque una gran cantidad de corriente electrica pase a traves de la resistencia， haciendo que el bimetal se doble considerablemente para que el indicador del medidor de combustible senale hacia la marca F. ",
]

corrected_texts = texts_to_api(texts_to_correct)

for corrected in corrected_texts:
    print(f"Textos corregidos: {corrected}\n")