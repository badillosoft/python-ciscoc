import botxl as bot

personas = bot.extract("datos.xlsx", "Hoja2", "B5:E5", "B7:E13")

# TODO: Crear un mapeo que reciba la lista de personas y devuelva
# la lista que contiene solo los nombres.
# Hint: En la funcion de transformacion tooma el diccionario que 
# que representa a una sola persona y devuelve el valor en su
# clave "Nombre"

nombres = bot.column(personas, "Nombre")

print nombres

# ["Ana", "Beto", "Carla, Daniel", "Erika", "Fatima", "Gaby"]