import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statistics import mean as rata_rata
from matplotlib import style
import random
style.use('ggplot')


def create_dataset(jumlah_data,selisih,step=2,correlation=False):

    # jumlah_data = berapa banyak data yang kita ingingkan.terserah, namun semakin banyak data maka samakin lama untuk di proses
    # selisih = jarak point point dari garis regresi
    # step = nilai sebarapah jauh rata2 per titik
    # correlation = apakah garis hubungan nya postiive apa negative


    val = 1
    ys = []
    for i in range(jumlah_data):
        y = val + random.randrange(-selisih,selisih)
        ys.append(y)
        if (correlation and correlation == 'pos'):
            val+=step
        elif (correlation and correlation == 'neg'):
            val-=step

    xs = [i for i in range(len(ys))]

    return np.array(xs, dtype=np.float64),np.array(ys,dtype=np.float64)

# m = nilai kemiringan
# b = nilai perpotongan antara sumbu tegak(y)

def hitung_kemiringan_dan_b(x,y):
    m = (((rata_rata(x)*rata_rata(y)) - rata_rata(x*y)) /
         ((rata_rata(x)*rata_rata(x)) - rata_rata(x*x)))

    b = rata_rata(y) - m*rata_rata(x)

    return m, b

""" menghitung jumlah square error pada y"""

def kesalahan_kuadarat(y_asli,y_line):
    return sum((y_asli-y_line)**2)

"""determinan_koefisien berfungsi untuk mengkalkulasikan seberapah akurat data yang di prediksikan semakin tinngi nilai
r nya maka semakin besar data yg di prediksi akurat"""

def determinan_koefisien(ys_orig,ys_line):
    y_rata_rata_line = [rata_rata(ys_orig) for y in ys_orig]

    SE = sum((ys_line - ys_orig) * (ys_line - ys_orig))
    SE_rata2 = sum((y_rata_rata_line - ys_orig) * (y_rata_rata_line - ys_orig))

    print(SE)
    print(SE_rata2)

    r = 1 - (SE/SE_rata2)

    return r

x,y = create_dataset(402,100,5,correlation='pos')
m,b = hitung_kemiringan_dan_b(x,y)
# y = mx+b asumsikan y itu adalah nama variabel yg dibawah
rumus_regresi_linear = [(m*x+b) for x in x]
nilai_prediksix = 10
nilai_prediksiy = (m*nilai_prediksix+b)
kuadrat_r = determinan_koefisien(y,rumus_regresi_linear)
print(kuadrat_r)



plt.scatter(x,y,color='#003F72', label = 'data')
plt.scatter(nilai_prediksix,nilai_prediksiy,color='green',label='prediksi')
plt.plot(x, rumus_regresi_linear, label = 'garis regresi')
plt.legend(loc=4)
plt.title("Regresi Linear")
plt.show()
