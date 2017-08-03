import botxl as bot

print bot.extract("datos.xlsx", "Hoja2", "B5:E5", "B7:E13")
print bot.extract_dep("datos.xlsx", "Hoja2", "B5:E5", "B7:E13")