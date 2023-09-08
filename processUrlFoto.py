import requests
import pandas as pd
import concurrent.futures as cf

fotosArray = []
fotoDF = pd.read_excel('cargar482022.xlsx')
fotoDict = fotoDF.to_dict('record')

def get_image(data):
    r = requests.get("https://mapainversiones.obraspublicas.gob.ar%s" % data.get('UrlImageGrande'))
    obraJSON = {
            'IdProyecto': data.get('IdProyecto'),
            'image': data.get('UrlImageGrande'),
            'estado': r.status_code
    }
    return obraJSON

with cf.ThreadPoolExecutor() as executor:
    jobs = [executor.submit(get_image,x) for x in fotoDict]
for r in cf.as_completed(jobs):
    obj = r.result()
    fotosArray.append(obj)

dfResult = pd.DataFrame.from_records(fotosArray)
dfResult.to_excel('result.xlsx',header=True,index=False)