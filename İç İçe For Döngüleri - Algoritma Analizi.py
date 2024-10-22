#İç içe 2 for döngüsüyle işlem yapan bir fonksiyon oluşturup, farklı N değerleri için çalışma zamanını ölçerek grafiğe yansıtıyoruz.

import time
import matplotlib.pyplot as plt
import pandas as pd

#deneyde kullanılacak N değerleri
n_degerleri=[1, 10, 100, 1000, 10000, 100000]

#deney sonuçlarını yazdıracağımız boş liste
exp_times=[]

#çalışma zamanını ölçen fonksiyon
def measure_time(algorithm, input_data):
    
    start_time = time.time()
    algorithm(input_data)
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    return elapsed_time

#deneyde çalışma zamanını ölçeceğimiz fonksiyon
def deney_fonk(N):
    
    toplam = 0
    for i in range (N):
        for j in range(N):
            toplam=toplam+1
    
    return(toplam)

#N değerleri için fonksiyonun çalışma zamanı ölçülür ve listeye yazılır
for N in n_degerleri:
    exp_times.append((N, measure_time(deney_fonk, N)))

#deney verileri tablo haline getirilir
df = pd.DataFrame(exp_times, columns = ['N sayısı', 'Çalışma zamanı'])

#grafik oluşturulur
plt.plot(df['N sayısı'], df['Çalışma zamanı'], marker='o')
plt.title('İç İçe For Döngüleri Çalışma zamanı Grafiği')
plt.xlabel('N Sayısı')
plt.ylabel('Çalışma Zamanı')

plt.grid()      #grafiğe ızgara ekliyor
plt.xscale('log')
plt.yscale('log') 

plt.xticks(df['N sayısı'], labels=[f'{int(n):,}' for n in df['N sayısı']])

plt.tight_layout()    #grafikte çakışmaları engelliyor

plt.show()