import time
import datetime
year = datetime.date.today().year

def SignUp():
    print("\n ****** KAYIT OL ****** \n")
    birth_confirmation = 0
    name = input("Adınızı giriniz: ")
    lastname = input("Soyadınızı giriniz: ")
    try:
        birth_year = int(input("Doğum yılınızı giriniz: "))
        if not (year - birth_year) >= 12:
            print("Üzgünüz, Ancak Yaşınız minimum 12 olmalı.")
        birth_confirmation = 1
    except ValueError:
        print("Lütfen Tekrar Deneyin!")
        SignUp()
    
    email = input("E-Mail'inizi giriniz: ")
    if not "@" or "com" in email:
        email_new3 = email.split("@")[1]
        if email_new3 == "" or email_new3 == None:
            print("Üzgünüz, Ancak geçerli bir gmail girmiyorsunuz! Lütfen tekrar deneyiniz!")
            SignUp()
        else:
            email_new = email.split("@")[1]
            email_new = email_new.split(".com")[0]
            if not email_new == "gmail" or email_new == "yandex":
                print("Üzgünüz, Ancak geçerli bir gmail girmiyorsunuz! Lütfen tekrar deneyiniz!")
                SignUp()
            else:
                email_new2 = email.split(".com")[1]
                if email_new2 != "" and email_new2 != None:
                    print("Üzgünüz, Ancak geçerli bir gmail girmiyorsunuz! Lütfen tekrar deneyiniz!")
                    SignUp()
                else:
                    password = input("Şifre giriniz: ")

                    if len(password) < 8:
                        print("Geçerli uzunlukta bir şifre girmediniz!")
                        SignUp()
                    elif len(password) > 16:
                        print("Geçerli uzunlukta bir şifre girmediniz! Lütfen tekrar deneyiniz!")
                        SignUp()

                    password_guvenlik = ["12345678", "123456789", "123456781", "123456780", "87654321", "876543210"]

                    if password in password_guvenlik:
                        print("Lütfen geçerli güvenlikte bir şifre giriniz!")
                        SignUp()
                    else:
                        print("\nTebrikler! Başarıyla Kayıt Oldunuz!\n")
                        global hesap_bilgileri
                        hesap_bilgileri = {
                            "ad": name,
                            "soyad": lastname,
                            "dogum_tarihi": birth_year,
                            "tarih_onay": birth_confirmation,
                            "mail": email,
                            "sifre": password
                        }

                        i = 0
                        while i < 1:
                            print("""Hesap Bilgileriniz: {} Adlı ve {} Soyadlı kişinin doğum tarihi {}, yaş onayı: {}, maili: {} ve şifresi de {}'dur.'""".format(hesap_bilgileri["ad"], hesap_bilgileri["soyad"], hesap_bilgileri["dogum_tarihi"], hesap_bilgileri["tarih_onay"], hesap_bilgileri["mail"], hesap_bilgileri["sifre"]))
                            i += 1
    else:
        print("Üzgünüz, Ancak geçerli bir gmail girmiyorsunuz! Lütfen tekrar deneyiniz!")
        SignUp()

# -----------------------> YOUR APP <----------------------------
    
    
    
    
def App():
    print("\n ****** UYGULAMA ****** \n")
    print("Welcome {} {}.".format(hesap_bilgileri["ad"], hesap_bilgileri["soyad"]))
    

    

# -----------------------> YOUR APP END <----------------------------
    
def Login():
    print("\n ****** GİRİŞ YAP ****** \n")
    l_email = input("E-Mail'inizi giriniz: ")
    l_password = input("Şifrenizi giriniz: ")

    if l_email == "" or l_email == None or l_password == "" or l_password == None:
        print("Üzgünüz, Ancak tüm girişleri doldurmadınız. Lütfen tekrar deneyiniz!")
        Login()
        
    if l_email == hesap_bilgileri["mail"] and l_password == hesap_bilgileri["sifre"]:
        print("Tebrikler Başarıyla giriş yaptınız!")
        print("{")
        for i in range(10):
            time.sleep(0.5)
            print("Uygulama'ya yönlendiriliyorsunuz...")
        print("}")
        print("\nTebrikler! Artık Uygulamadasınız!")
    else:
        print("Lütfen tekrar deneyiniz!")
        Login()

SignUp()
Login()
App()




