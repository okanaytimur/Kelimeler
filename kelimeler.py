import csv

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