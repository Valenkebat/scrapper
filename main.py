import pandas as pd
import process as p
import concurrent.futures as cf
#-1658255333.57 seconds ..
import time

import multiprocessing as mp
print("Number of processors: ", mp.cpu_count())

start = time.time()

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

df = pd.read_excel('fotoBase (cambio IdProyecto 13092022).xlsx')
lista = df['nuevo IdProyecto'].unique()
B, C = split_list(lista)
lista1, lista2 = split_list(B)
lista3, lista4 = split_list(C)
listas = []
listas.append(lista1)
listas.append(lista2)
listas.append(lista3)
listas.append(lista4)

print(listas)
errorsList = []

p.recorrer_lista(lista)

#with cf.ThreadPoolExecutor(max_workers=4) as executor:
#    jobs = [executor.submit(p.recorrer_lista,x) for x in listas]
#    for job in cf.as_completed(jobs):
#        print(job.result())
#        r = job.result()
#        if len(r) != 0:
#            for a in r:
#                errorsList.append(a)


        #for indexLists in listas:
        #    future = executor.submit(p.recorrer_lista, indexLists)
        #    return_value = future.result()
        #    print(return_value)


end = time.perf_counter()
print("{} seconds ..".format(round(end-start,2)))
if len(errorsList) > 0:
    for e in errorsList:
        print(e)
else:
    print('S/ errores')