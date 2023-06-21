# PEDRO LUC LEANDRO
# TURMA: 1TDCA
# RM: 96036
# CHECKPOINT - CODE FOR SECURITY

import requests
from pyfiglet import Figlet
from termcolor import colored

Titulo = Figlet(font='slant')
print(colored(Titulo.renderText("INSTAGRAM COPY"), ("blue")))

pageID = "101926902693609"
access_token = "EAARZCRrjye0MBABPZCryYdmO4noBIIRrN7DfUSJA9aq1TGSxIxMRCtHjf4qHHrV2TGBpPWFeOuytZBdmdRcOYrf9XE4ItIyaKbKCp5MRAyPBvxiA3UajF7CvYoeeSVXiFeGz9am2CXF8aeVDkZAM53G5kESiZChbxVvGwtRyKLYxiMmzB7YyO1dVnZBPmnF2rUQEsAL5dInnTUQ4yZAWmM6"
link_foto = str(input("Digite o link da foto: "))
legenda = str(input("Digite a legenda da foto: "))

# USANDO A API PARA PEGAR A PÁGINA DO FACEBOOK
request = requests.get(f"https://graph.facebook.com/v15.0/{pageID}?fields=instagram_business_account&access_token={access_token}")

# USANDO A API PARA PEGAR O ID E A PAGINA DO INSTAGRAM
instagramID = request.json()["instagram_business_account"]["id"]

# FAZENDO O GET PARA ACESSAR A CONTA DO INSTAGRAM
request = requests.get(f"https://graph.facebook.com/v14.0/{instagramID}?fields=media%2Cfollowers_count%2Cfollows_count%2Cusername%2Cname&access_token={access_token}")

resposta = request.json()
if request.status_code == 200:
    nome = resposta["name"]
    nomeusuario = resposta["username"]
    seguidores = resposta["followers_count"]
    seguindo = resposta["follows_count"]

    print("\033[1m DADOS DO USUÁRIO \033[m")
    print(F"NOME DE USUÁRIO: \033[1m{nome}\033[m")
    print(F"NOME DA CONTA: \033[1m{nomeusuario}\033[m")
    print(F"SEGUIDORES: \033[1m{seguidores}\033[m")
    print(F"SEGUINDO: \033[1m{seguindo}\033[m")
else:
    print(f" ERRO - STATUS CODE: {request.status_code} " )

# FUNÇÃO DE POSTAR

request = requests.post(f"https://graph.facebook.com/v14.0/{instagramID}/media?image_url={link_foto}&caption={legenda}&access_token={access_token}")
imageID = request.json()["id"]
request2 = requests.post(f"https://graph.facebook.com/v14.0/{instagramID}/media_publish?creation_id={imageID}&access_token={access_token}")
resposta2 = request2.json()


















