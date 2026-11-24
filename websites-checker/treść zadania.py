# ==================================================
# PROJEKT NR 6
# Wielowątkowe sprawdzanie dostępności stron WWW
# ==================================================
# Cel:Napisz program, który sprawdza dostępność wielu stron internetowych jednocześnie 
# przy użyciu kilku wątków. 
# WYMAGANIA:
# 1. Utwórz plik:  websites.txt
# 2. Zapisz w nim kilka adresów stron:
#    https://python.org
#    https://duckduckgo.com
#    https://github.com
#    https://stackoverflow.com
#    https://google.com
# 3. Wczytaj adresy URL z pliku.
# 4. Utwórz klasę Websites. Klasa powinna: - przechowywać listę stron,
# - zwracać kolejną stronę do sprawdzenia,- przechowywać wyniki sprawdzeń
# 5. Utwórz klasę Worker,klasa powinna dziedziczyć po: threading.Thread
# 6. Każdy wątek powinien: - pobrać kolejny adres URL ,
# - sprawdzić stronę przy pomocy requests.get(), - zapisać kod odpowiedzi HTTP
# 7. Utwórz 3 wątki: Worker-1, Worker-2, Worker-3
# 8. Użyj: threading.Lock() aby zabezpieczyć wspólne dane.
# 9. Po zakończeniu programu wyświetl raport:
#    python.org -> 200
#    duckduckgo.com -> 200
#    github.com -> 200
#    stackoverflow.com -> 200
#    google.com -> 200
# 10. Wyświetl:
#     - liczbę sprawdzonych stron
#     - czas wykonania programu
# ==================================================
# WERSJA ROZSZERZONA
# ==================================================
# Dla każdej strony zapisz:- adres URL, - status HTTP,- datę sprawdzenia
# do pliku:  report.txt
# ==================================================
# UMIEJĘTNOŚCI
# ==================================================
# - requests, - threading, - Thread, - Lock, - klasy, - OOP, - pliki TXT
# - raportowanie, - pomiar czasu
# ==================================================
# PRZYKŁADOWY REZULTAT
# ==================================================
# Worker-1 checking: python.org
# Worker-2 checking: github.com
# Worker-3 checking: google.com
# python.org        -> 200
# github.com        -> 200
# google.com        -> 200
# stackoverflow.com -> 200
# duckduckgo.com    -> 200
# Checked websites: 5
# Execution time: 1.23 seconds
# ==================================================