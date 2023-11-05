import pandas as pd
import requests
from typing import Set 

def ej_1_cargar_datos_demograficos() -> pd.DataFrame:
    try:
        data = pd.read_csv("datos_demograficos.csv", encoding= 'utf-8', sep=';')
    except FileNotFoundError:
        print("El archivo 'datos_demograficos.csv' no se encontró.")
        return pd.DataFrame()
    return data

def ej_2_cargar_calidad_aire(ciudades: Set[str]) -> pd.DataFrame:
    datos = []
    for i, city in enumerate(ciudades):
        if i >= 9:  
            break
        api_url = 'https://api.api-ninjas.com/v1/airquality?city={}'.format(city)
        response = requests.get(api_url, headers={"X-Api-Key" : "VNz4lHcTiTed6/aBeTo2wA==zAZCzTir5Lf0oGD6"})
        if response.status_code == 200:
            data = response.json()
            print(response.text)
            datos_dict = {"city": city}
            for key, entry in data.items():
                if isinstance(entry, dict):
                    concentracion = entry.get("concentration", "Concentración no disponible")
                    datos_dict[key] = concentracion
            datos.append(datos_dict)
    df = pd.DataFrame(datos)
    df.sort_values(by=["city"], inplace=True) 
    df.to_csv("ciudades.csv", index=False) 

    result_dict = df.to_dict()

    return result_dict




df_demograficos = ej_1_cargar_datos_demograficos()
if not df_demograficos.empty:
    columnas_a_eliminar = ["Race", "Count", "Number of Veterans"]
    for columna in columnas_a_eliminar:
        if columna in df_demograficos.columns:
            df_demograficos.drop(columns=[columna], inplace=True)
    df_demograficos.drop_duplicates(inplace=True)

    ciudades1 = set(df_demograficos["City"])
    df_calidad_aire = ej_2_cargar_calidad_aire(ciudades1)
    