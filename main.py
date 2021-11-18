import os


def makeblacklist():
    target = open(r"C:\Windows\System32\drivers\etc\hosts", "w")
    blacklist = open("hosts", "r")

    target.write(blacklist.read())

    target.close()
    blacklist.close()


def addsite(str):
    target = open(r"C:\Windows\System32\drivers\etc\hosts", "a")
    target.write(f"\n0.0.0.0 {str}")
    target.close()


def makedefault():
    default_text = "# Copyright (c) 1993-2006 Microsoft Corp. # # This is a sample HOSTS file used by Microsoft TCP/IP for Windows. # # This file contains the mappings of IP addresses to host names. Each # entry should be kept on an individual line. The IP address should # be placed in the first column followed by the corresponding host name. # The IP address and the host name should be separated by at least one # space. # # Additionally, comments (such as these) may be inserted on individual # lines or following the machine name denoted by a '#' symbol. # # For example: # # 102.54.94.97 rhino.acme.com # source server # 38.25.63.10 x.acme.com # x client host # localhost name resolution is handle within DNS itself. # 127.0.0.1 localhost # ::1 localhost"
    target = open(r"C:\Windows\System32\drivers\etc\hosts", "w")
    target.write(default_text)
    target.close()


def main():
    os.system("cls")
    print("--------------------------------ADKILLER--------------------------------\n")
    print("Host Dosyanızı kara liste ile değiştirmek için 1'e basınız.\n")
    print("Host dosyanıza yeni bir site eklemek için 2'e basınız.\n")
    print("Hosts dosyanızı eski haline çevirmek için 3'e basınız.\n\n\n")
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
        elif(user_input == "3"):
            makedefault()
            print("Host dosyası eski haline döndürüldü.")
        else:
            break


if __name__ == "__main__":
    main()
