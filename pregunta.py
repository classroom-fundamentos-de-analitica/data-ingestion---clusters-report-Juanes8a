"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re


def ingest_data():
    df = open("clusters_report.txt","r")
    #
    # Inserte su código aquí
    #
    lista_pulida = []
    contador = 0
    anexo = 0
    for i in df:
        frase = r"\s{3,}"
        separado = re.split(frase,i)
        fila =  []
        if contador == 0:
        
            for p in range(len(separado)-1):
                if p == 0:
                    div1_fila = separado[p].split()
                    cluster = div1_fila[0].lower()
                    fila.append(cluster)
                    cantidad = div1_fila[1].lower()+" de palabras clave"
                    cantidad = cantidad.replace(" ","_")
                    fila.append(cantidad)
                
                elif p == 1:
                    porcentaje = separado[p].lower()+" palabras clave"
                    porcentaje = porcentaje.replace(" ","_")
                    fila.append(porcentaje)
                else:
                    principales = separado[p].lower().replace(" ","_") 
                    fila.append(principales)
            lista_pulida.append(fila)
            
        if contador > 3:
        
                if len(separado) > 1:
                    if separado[1] == "":
                        anexo = 0
                    elif anexo == 0:
                
                        fila += [int(separado[1]),int(separado[2])]
                        col3 = separado[3].split(",")
                        fila.append(float(col3[0]+"."+col3[1][0]))
                        separado[-1] = separado[-1].replace("\n"," ")
                        resto_fila = " ".join(separado[4:])
                        fila.append(resto_fila)
                        anexo = 1
                        lista_pulida.append(fila)
                    else:
                        separado[-1] = separado[-1].replace("\n"," ")
                        renglon_extra =  " ".join(separado[1:])
                        lista_pulida[-1][-1] += renglon_extra
                else:
                    anexo = 0
        contador +=1
    for k in lista_pulida:
        k[3] = k[3].replace("   "," ")
        k[3] = k[3].replace("  "," ")
        k[3] = k[3][:-2]

    lista_pulida[0][3] += "ve"
    df = pd.DataFrame(lista_pulida[1:],columns = lista_pulida[0])

    return df
