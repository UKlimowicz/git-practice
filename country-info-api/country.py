# ==================================================
# CZĘŚĆ 1
# ==================================================
# Utwórz plik country.py. Zaimportuj requests
# Skorzystaj z API: https://restcountries.com/v3.1/name/poland
# Pobierz dane z API. Zapisz odpowiedź do zmiennej: response
# Zamień odpowiedź na JSON. Zapisz wynik do zmiennej: data

import requests

response = requests.get("https://restcountries.com/v3.1/name/poland")
data = response.json()
print(data)