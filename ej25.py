import botxl as bot

personas = bot.extract("datos.xlsx", "Hoja2", "B5:E5", "B7:E13")

print personas

def T1(d):
    sexo = d["Sexo"]
    if sexo == "M" or sexo == "Muj." or sexo == "Femenino" or sexo == "Fem.":
        d["Sexo"] = "Mujer"
    if sexo == "H":
        d["Sexo"] = "Hombre"
    return d

personas = map(T1, personas)

print bot.column(personas, "Sexo")