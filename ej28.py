# _*_ coding: utf-8 _*_

import botxl as bot

personas = bot.extract("datos.xlsx", "Hoja2", "B5:E5", "B7:E2074")

N = len(personas)

print "Personas: %d" % N

# Contar el numero de Hombres
def FH(p):
    return p["Sexo"] == "Hombre"

H = len(filter(FH, personas))

print "Hombres: %d (%.1f%%)" % (H, 100. * H / N)

# Contar el numero de Mujeres
def FM(p):
    return p["Sexo"] == "Mujer"

M = len(filter(FM, personas))

print "Mujeres: %d (%.1f%%)" % (M, 100. * M / N)

print "-" * 40

# Contar cuantos tienen primaria
def FP(p):
    return p["Escolaridad"] == "Primaria"

p_primaria = filter(FP, personas)

PP = len(p_primaria)

print "Primaria: %d" % PP

for p in p_primaria:
    print "* %s (%d/%s)" % (p["Nombre"], p["Edad"], p["Sexo"][0])

print "-" * 40

# Bloque Secundaria
def FS(p):
    return p["Escolaridad"] == "Secundaria"

p_secundaria = filter(FS, personas)

PS = len(p_secundaria)

print "Secundaria: %d" % PS

for p in p_secundaria:
    print "* %s (%d/%s)" % (p["Nombre"], p["Edad"], p["Sexo"][0])

print "-" * 40

def bloque(escolaridad):
    def F(p):
        return p["Escolaridad"] == escolaridad

    p_filtradas = filter(F, personas)

    n = len(p_filtradas)

    print "%s: %d" % (escolaridad, n)

    for p in p_filtradas:
        print "* %s (%d/%s)" % (p["Nombre"], p["Edad"], p["Sexo"][0])

    print "-" * 40

# Bloque Preparatoria
bloque("Preparatoria")

# Bloque Universidad
bloque("Universidad")