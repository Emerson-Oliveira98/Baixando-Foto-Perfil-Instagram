import instaloader

app = instaloader.Instaloader()
user_name = input("Digite seu User Nome do instagram, para ser baixado a foto do perfil: ")
app.download_profile(user_name, profile_pic_only=True)
print("Download realizado com Sucesso!!")