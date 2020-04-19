import subprocess
subprocess.call('pip install pandas', shell=False)

import pandas as pd

# .csv uzantılı dosyayı oku
df = pd.read_csv('input_dir_name/input_hw_2.csv', delimiter = ';')

# okunan csv dosyasını listeye dönüştür 
data = [list(row) for row in df.values]

# ihtiyaç duyulan kolon data[3] olduğu için diğer kolonları veri üzerinde
# çalışmayı kolaylaşması için çıkar
for i in data:
    del i[0]
for j in data:
    del j[0]
for k in data:
    del k[0]
    
liste = []
for x in data:
    for y in x:
        for z in y:
            ilk_bas = y[5]
            ikinci_bas = y[6]
        if(ilk_bas == '0'):
            liste.append(int(ikinci_bas))
        else:
            liste.append(int(ilk_bas + ikinci_bas))
#HISTOGRAM

def freq_w_dict(list):
    freq_dict = {}
    for item in list:
        if(item in freq_dict):
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    return freq_dict

yeni_liste = freq_w_dict(liste)

def bubble_sort(my_list):
    n=len(my_list)
    
    for i in range(n-1,-1,-1):
        for j in range(0,1):
            if not (my_list[j]<my_list[j+1]):
                temp=my_list[j]
                my_list[j]=my_list[j+1]
                my_list[j+1]=temp
    return my_list
bubble_sort(liste)
#MEDYAN
def my_median(my_list):
    my_list_2=bubble_sort(my_list)
    
    n=len(my_list_2)
    if n%2==1:
        middle=int(n/2)+1
        median=my_list_2[middle]
        
    else:
        middle_1=my_list_2[int(n/2)]
        middle_2=my_list_2[int(n/2)+1]
        median=(middle_1+middle_2)/2
    return median

median = my_median(liste)

#ORTALAMA
def my_mean(my_list):
    s,t=0,0
    for item in my_list:
        s=s+1
        t=t+item
    mean=t/s
    return mean
ortalama = my_mean(liste)

with open("output_dir_name/170401052_hw_2_output.txt","w") as dosya:
    dosya.write("Medyan "+str(median)+"\n")
    dosya.write("Ortalama "+str(ortalama))