import os


def makeblacklist():
    target = open(r"C:\Windows\System32\drivers\etc\hosts", "w")
    blacklist = open("host", "r")

    target.write(blacklist.read())

    target.close()
    blacklist.close()


def addsite(str):
    target = open(r"C:\Windows\System32\drivers\etc\hosts", "a")
    target.write(f"\n0.0.0.0 {str}")
    target.close()


def main():
    os.system("cls")
    print("--------------------------------ADKILLER--------------------------------\n")
    print("Host Dosyanızı kara liste ile değiştirmek için 1'e basınız.\n")
    print("Host dosyanıza yeni bir site eklemek için 2'e basınız.\n \n \n")
    while(True):
        user_input = input("Bir seçenek belirleyin. Çıkmak için 0'a basın\n")
        os.system("cls")

        if(user_input == "0"):
            break
        elif(user_input == "1"):
            print("UYARI Host dosyanız değiştirilecektir. Mesuliyet kabul etmiyoruz. \n")
            print("Ne yaptığınızı biliyorsanız 1'e iptal etmek için 0'a basınız.\n")

            zort = input()
            if(zort == "0"):
                break
            elif(zort == "1"):
                makeblacklist()
                break
            else:
                print("Yanlış bir tuşa bastınız.")
                break
        elif(user_input == "2"):
            print("UYARI Host dosyanız değiştirilecektir. Mesuliyet kabul etmiyoruz. \n")
            site_url = input("Site adresini giriniz.\n")
            addsite(site_url)

        else:
            break


if __name__ == "__main__":
    main()
