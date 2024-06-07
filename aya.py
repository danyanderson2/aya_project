from openai import OpenAI
import os

############################################################################################################################################################################################################################
COMPUTER_DESCRIPTIONS =  "Lenovo 15.6\" IdeaPad Laptop with 1 Year Microsoft Office 365, Intel Pentium Quad-Core Processor, 20GB RAM, 1TB SSD (128GB eMMC+1TB PCIe SSD), Wi-Fi 6 and Bluetooth 5.0, HDMI, NLY MP, Windows 11"

SYSTEM_MESSAGE = "Aya est une assisstante qui génère des description formatéés d'ordinateurs a partir"
                                  "de descriptions brute copiees dans sa fenetre de contexte, avec des emojis tel que "
                                  "chaque characteristique occupe une ligne. Ceci, avec un ton Camerounais dans le langage"
############################################################################################################################################################################################################################

my_Key=os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=my_Key)
completion = client.chat.completions.create(
  model="ft:gpt-3.5-turbo-0613:personal::8TSj5oGF",  # the fine_tuned model
  messages=[
    {"role": "system", "content": COMPUTER_DESCRIPTIONS},
    {"role": "user", "content": SYSTEM_MESSAGE}
  ]
)

print(completion.choices[0].message.content)
