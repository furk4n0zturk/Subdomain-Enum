import os
import tldextract
import wget

domain = tldextract.extract(input("Domain: "))
def subbrute(domain):
    print("(1/4) Subbrute Çalıştırılıyor...\n")
    print("Wordlist Alınıyor...")
    remote_url = 'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/DNS/subdomains-top1million-20000.txt'
    local_file = 'topwordlist.txt'
    wget.download(remote_url, local_file)
    print('\n')
    os.system("python3 ./subbrute/subbrute.py -s topwordlist.txt -o subbruteilk.txt -p " + (domain.domain+'.'+domain.suffix))
    print("OK.\n")

def subbrute_list():
    bir = open("subbruteilk.txt","r+")
    subbrute_list = []
    for i in a:
        a = i.split(",")
        subbrute_list.append(a)
    bir.close()
    iki = open("subbrute.txt","w")
    for i in subbrute_list:
        iki.write(i[0] + "\n")

def amass(domain):
    print("\n(2/4) Amass Çalıştırılıyor...\n")
    os.system(" amass enum -o amass.txt -d " + (domain.domain + "." + domain.suffix))
    print("OK.\n")
def sublist3r(domain):
    print("\n(3/4) Sublist3r Çalıştırılıyor...\n")
    os.system("python3 ./Sublist3r/sublist3r.py -o sublist3r.txt -d " + (domain.domain + '.' + domain.suffix))
    print("OK.\n")
def subfinder(domain):
    print("(4/4) Subfinder Çalıştırılıyor...\n")
    os.system("subfinder -o subfinder.txt -d " + (domain.domain+'.'+domain.suffix))
    print('OK.\n')

def comparing():
    subbrute_file = open("subbrute.txt", "r+")
    subbrute_list = []
    for subbrute_row in subbrute_file:
        subbrute_list.append(subbrute_row)

    sublist3r_file = open("sublist3r.txt", "r+")
    sublist3r_list = []
    for sublist3r_row in sublist3r_file:
        sublist3r_list.append(sublist3r_row)

    amass_file = open("amass.txt", "r+")
    amass_list = []
    for amass_row in amass_file:
        amass_list.append(amass_row)

    subfinder_file = open("subfinder.txt", "r+")
    subfinder_list = []
    for subfinder_row in subfinder_file:
        subfinder_list.append(subfinder_row)

    birinci = list(set(subbrute_list+amass_list))
    ikinci = list(set(birinci+subfinder_list))
    cikti = list(set(ikinci+sublist3r_list))
    print("Tarama Sonuçları :\n ")
    ciktidosya = open("cikti.txt", "w")
    for i in cikti:
        ciktidosya.write(i)

subbrute(domain)
subbrute_list()
amass(domain)
sublist3r(domain)
subfinder(domain)
comparing()

dosya = open("cikti.txt","r",encoding="utf-8")
oku = dosya.read()
print(oku)
