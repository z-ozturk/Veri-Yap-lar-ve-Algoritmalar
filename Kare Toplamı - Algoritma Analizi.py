#Kare toplamı fonksiyonu oluşturulur. Farklı N değerleri için algoritmanın çalışma zamanı ölçülür ve grafiği çizilir.

import time
import matplotlib.pyplot as plt
import pandas as pd

#çalışma zamanını ölçen fonksiyon
def measure_time(algorithm, input_data):
    
    start_time = time.time()
    algorithm(input_data)
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    return elapsed_time

#deneyde kullanacağımız fonksiyon
def kare_toplami(N):
    
    toplam = 0
    
    #N e kadar olan sayıların karelerinin toplamı hesaplanır
    for i in range (1,N+1):
        toplam += i * i
    return toplam

#deneyde kullanılacak N değerleri
experiment = [1, 10, 100, 1000, 10000, 100000]

#deney sonuçlarını içine yazacağımız boş liste
exp_results = []

#deney listesindeki her N değeri için fonk. çalışma zamanı hesaplanır
for exp in experiment:
    exp_results.append((exp, measure_time(kare_toplami,exp)))

#deney verilerini tablo haline getirir
df = pd.DataFrame(exp_results, columns = ['N sayısı', 'Çalışma zamanı'])

#verilerle grafik oluşturulur
plt.plot(df['N sayısı'], df['Çalışma zamanı'], marker='o')
plt.title('Kare Toplamı Çalışma zamanı Grafiği')
plt.xlabel('N Sayısı')
plt.ylabel('Çalışma Zamanı')

plt.grid()       #grafiğe ızgara ekliyor
plt.xscale('log')

plt.xticks(df['N sayısı'], labels=[f'{int(n):,}' for n in df['N sayısı']])  # X eksenindeki değerleri göster

plt.tight_layout()     #grafikte çakışmaları engelliyor

plt.show()