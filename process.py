import requests
from bs4 import BeautifulSoup 
import concurrent.futures as cf

#with cf.ThreadPoolExecutor() as executor:
#    jobs = [executor.submit(p.recorrer_lista,x) for x in listas]
#    for job in cf.as_completed(jobs):
#        print(job.result())
#        r = job.result()
#        if len(r) != 0:
#            for a in r:
#                errorObras.append(a)

def get_image(datasrc):
    r = requests.get("https://mapainversiones.obraspublicas.gob.ar%s" % datasrc)
    return r.status_code

def recorrer_lista(lista_obras):
    errorObras = []
    for obra in lista_obras:
        print('Procesando Obra: ',obra)
        response = requests.get("https://mapainversiones.obraspublicas.gob.ar/Proyecto/PerfilProyecto/%s" % obra)
        r = response.text
        soup = BeautifulSoup(r,"html.parser")
        images_tags = soup.find_all("div",class_="enlace_img")
        all_tags = []
        for repElem in images_tags:
            all_tags.append(repElem.get('data-src'))
            print(repElem.get('data-src'))
        with cf.ThreadPoolExecutor() as executor:
            jobs = [executor.submit(get_image,x) for x in all_tags]
        for r in cf.as_completed(jobs):
            if r.result() != 200:
                obraJSON = {
                    'IdProyecto': obra,
                    'image': '',
                    'error': r.result()
                }
                errorObras.append(obraJSON)
            else:
                print(r.result())
    return errorObras