import botxl as bot
import re

personas = bot.extract("datos.xlsx", "Hoja2", "B5:E5", "B7:E13")

print personas

def T1(d):
    sexo = d["Sexo"]
    if re.search("^(m|f)[^as]?", sexo, re.IGNORECASE):
        d["Sexo"] = "Mujer"
    if re.search("^h", sexo, re.IGNORECASE):
        d["Sexo"] = "Hombre"
    return d

personas = map(T1, personas)

print bot.column(personas, "Sexo")