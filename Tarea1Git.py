import pandas as pd 
import numpy as np

pelicula={"Nombre": ["Super Mario Bros", "The Whale", "Spiderman: Across", "Notting Hill", "Kiki:entregas a domicilio", "Green Book"], 
"Género":["animada", "drama", "animada", "romance", "anime", "Drama" ],
"Duración": ["1h32m", "1h57m", "2h20m", "2h04m", "1h42m", "2h10m"],
"Puntaje Rotten Tomatoes": [60, 65, 96, 85, 99, 77]}
pl= pd.DataFrame(pelicula)
nueva_informacion = {
    "Nombre": ["Titanic", "The Avengers", "Interstellar", "The Shawshank Redemption", "The Dark Knight", "Inception"],
    "Género": ["romance", "acción", "ciencia ficción", "drama", "acción", "ciencia ficción"],
    "Duración": ["3h14m", "2h23m", "2h49m", "2h22m", "2h32m", "2h28m"],
    "Puntaje Rotten Tomatoes": [89, 92, 74, 91, 94, 87]
}
nueva_pl = pd.DataFrame(nueva_informacion)
pl_actualizado = pd.concat([pl, nueva_pl], axis=0).reset_index(drop=True)
print(pl_actualizado)


### ARIANA ###

nuevos_datos={"Nombre": ["Orgullo y Prejuicio", "Notting Hill", "Kiki:entregas a domicilio"], 
"Género":["romance", "romance", "anime" ],
"Duración": ["2h07m", "2h04m", "1h42m"],
"Puntaje Rotten Tomatoes": [88, 85, 99]}

dt_act= pd.concat([pl_actualizado, pd.DataFrame(nuevos_datos)], ignore_index=True)
print(dt_act)

###################
#  Oscar Centeno  #
###################

datos_centeno = {"Nombre": ["Avengers: End Game"],
                  "Género":["Fantasía" ],
                    "Duración": ["2h59m"],
                    "Puntaje Rotten Tomatoes": [99]}

df_centeno = pd.DataFrame(datos_centeno)


df = dt_act.append(df_centeno, ignore_index=True)
print(df)


