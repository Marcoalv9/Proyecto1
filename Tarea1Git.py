import pandas as pd 
import numpy as np

pelicula={"Nombre": ["Super Mario Bros", "The Whale", "Spiderman: Across", "Notting Hill", "Kiki:entregas a domicilio", "Green Book"], 
"Género":["animada", "drama", "animada", "romance", "anime", "Drama" ],
"Duración": ["1h32m", "1h57m", "2h20m", "2h04m", "1h42m", "2h10m"],
"Puntaje Rotten Tomatoes": [60, 65, 96, 85, 99, 77]}

pl= pd.DataFrame(pelicula)
print(pl)