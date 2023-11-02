import instaloader

username = input("Instagram kullanıcı adını girin: ")

L = instaloader.Instaloader()

try:
    L.download_profile(username, profile_pic_only=True)
    

    profile = instaloader.Profile.from_username(L.context, username)

    print(f"Kullanıcı Adı: {profile.username}")
    print(f"Profil ID: {profile.userid}")
    print(f"Gönderi Sayısı: {profile.mediacount}")
    print(f"Takipçi Sayısı: {profile.followers}")
    print(f"Takip Ettiği Kişi Sayısı: {profile.followees}")
except instaloader.exceptions.ProfileNotExistsException:
    print(f"'{username}' kullanıcısı bulunamadı.")
except Exception as e:
    print(f"Hata oluştu: {e}")
