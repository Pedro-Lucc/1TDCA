import requests

# Pegando manualmente o ID da página do Facebook para conectar com o API graph
pageID = "101062742775873"
access_token = 'EAAHWiUWdxy0BAPdAPZClgJHUrZBk5x9pFxlEqmuUawqX9s3klRraHQA7FRlpZCLUntVDlCeUt3hcxZAuCH84rrhTFZCxHXRkmd8cXAeJPbdR2NmBJz2PcO3ZBtAW8DDS94koCC0dOqoW4PeZBTXE11D9NuFkuXZCSQ0ZBSwLF0p8KHhb7f1lYvY1K5vyILGHPGYpTjmppiplECWsbDOPZCHtAL'

# Pedindo para o usuário inputar o link da foto a sua legenda
link_da_foto = str(input("\033[1;32mLink da foto:\033[m "))
legenda_da_foto = str(input("\033[1;32mLegenda da foto:\033[m "))
print("\n")
# Fazendo um GET da pagina do Facebook
request = requests.get(
    f"https://graph.facebook.com/v15.0/{pageID}?fields=instagram_business_account&access_token={access_token}")

# Fazendo um JSon com as informações da conta do Instagram
instagramID = request.json()["instagram_business_account"]["id"]

# Fazendo um GET do perfil do Instagram
request = requests.get(
    f"https://graph.facebook.com/v14.0/{instagramID}?fields=media%2Cfollowers_count%2Cfollows_count%2Cusername%2Cname&access_token={access_token}")

resposta = request.json()
if request.status_code == 200:
    nome = resposta["name"]
    nome_da_conta = resposta["username"]
    seguidores = resposta["followers_count"]
    seguindo = resposta["follows_count"]

    print(30 * "~=")
    print(F"\033[1mBEM-VINDO AO DADOS DA CONTA DE \033[1;34m{nome}\033[m")
    print(30 * "~=")
    print("\033[1m\nDADOS DO USUÁRIO \033[m")
    print(F"[*] Nome do usuário: \033[1m{nome}\033[m")
    print(F"[*] @ da conta: \033[1m{nome_da_conta}\033[m")
    print(F"[*] Quantas pessoas {nome} segue: \033[1m{seguindo}\033[m")
    print(F"[*] Quantos seguidores {nome} tem: \033[1m{seguidores}\033[m")
else:
    print(f" ERRO: {request.status_code} ")


# Fazendo um POST com o ID do Instagram, na qual, requisita o input do link da foto e sua legenda e para finalizar utilizar o token de acesso
request = requests.post(f"https://graph.facebook.com/v14.0/{instagramID}/media?image_url={link_da_foto}&caption={legenda_da_foto}&access_token={access_token}")

# Criando um ID do link da imagem para que possa concluir o POST
imageID = request.json()["id"]

# Por fim, fazer o POST com todas as informações
request2 = requests.post(f"https://graph.facebook.com/v14.0/{instagramID}/media_publish?creation_id={imageID}&access_token={access_token}")
resposta2 = request2.json()
