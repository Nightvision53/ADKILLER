import os
import ctypes
import sys

target_dest = r"C:\Windows\System32\drivers\etc\hosts"


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def savedefault():
    target = open(target_dest, "r")

    # check if default_hosts file exists, if not then create backup.
    if os.path.isfile('default_hosts') == False:
        print("Yedek bulunamadı. Host dosyanızın yedeği oluşturuluyor.")

        default_hosts = open('default_hosts', 'w')
        default_hosts.write(target.read())

        default_hosts.close()

    target.close()


def makeblacklist():
    target = open(target_dest, "a")
    blacklist = open("HOSTS", "r")

    target.write(blacklist.read())

    target.close()
    blacklist.close()


def addsite(str):
    target = open(target_dest, "a")
    target.write(f"\n0.0.0.0 {str}")
    target.close()


def makedefault():
    default_text = open("default_hosts", "r")
    target = open(target_dest, "w")
    target.write(default_text)
    target.close()
    default_text.close()


def main():
    savedefault()
    while(True):
        os.system("cls")
        print("--------------------------------ADKILLER--------------------------------\n")
        print("Host Dosyanızı kara liste ile değiştirmek için 1'e basınız.\n")
        print("Host dosyanıza yeni bir site eklemek için 2'e basınız.\n")
        print("Hosts dosyanızı eski haline çevirmek için 3'e basınız.\n\n\n")
        user_input = input("Bir seçenek belirleyin. Çıkmak için 0'a basın\n")

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
    if is_admin():
        main()
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1)
