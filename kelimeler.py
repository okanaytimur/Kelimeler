import csv
#Verilen metni kelimelere bölüp satır satır yazar
#kelimeler.txt dosyasının içerisime çevirmek istediğiniz metni yapıştırıp kaydedin
#Programı çalıştırın CSV dosyasını Google Sheet e yükleyerek =GOOGLETRANSLETE() fonksiyonu ile çevirebilirsiniz
#  
dizi=[]
with open('kelimeler.txt','r') as file:
    for line in file:
        for word in line.split(sep=None):
                print(word)
                dizi.append(word)

file.close()


with open("kelimeler.csv", "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerows([elt] for elt in dizi)

csv_file.close()