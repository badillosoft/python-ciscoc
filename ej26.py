import botxl as bot

personas = bot.extract("datos.xlsx", "Hoja2", "B5:E5", "B7:E13")

def F(d):
    if d["Sexo"][0] == "M" or d["Sexo"][0] == "m":
        return True

mujeres = filter(F, personas)

M = len(mujeres)
T = len(personas)

print "Hay %d mujeres de un total de %d personas (%.2f%%)" % (M, T, 100. * M / T)
print mujeres