# Instalar libreria google
# 1. Abrir un simbolo del sistema en modo administrador
# 2. $ pip install google

from google import search

for url in search('cat .ogg', stop=20):
    print(url)