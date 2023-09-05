# Filmweb-scraper

  <h3 align="center">Filmweb data scraper</h3>

  <p align="center">
    Bardzo prosty data scraper ze strony filmweb.pl. Aplikacja została napisana z braku jakichkolwiek aktualnych i działających alternatyw do pobierania danych z filmwebu.
  </p>
</div>



## To do

- [x] Baza danych filmów w csv
- [ ] Przejście reklamy filmwebu
- [ ] Wyszukiwanie w zależności od VOD (zrobione w 90%)
- [ ] Pobieranie opini o filmie
- [ ] Optymalizacja działania wczytywania stron
- [ ] Zastąpienie time.sleepów lepszym rozwiązaniem
- [ ] Automatyzacja pętli np. zatrzymuje się po 10000 filmów w bazie danych
- [ ] Lepsze ogarnięcie wyjątków w kodzie

 


## O projekcie

Data scraping odbywa sie w sposób "manualny" - mozolny. Aplikacja otwiera przeglądarke Chromium i zbiera response'y od filmwebu podczas automatycznego scrollowania, następnie robi z nich dataframe w pandas i skleja do pliku csv. Sam proces trwa bardzo wolno, natomiast hipotetycznie można by go puścić w chmurze na pare godzin, w trakcie których bez problemu zebrałby parenaście tysięcy filmów.

Obecnie otrzymywane dane to: Rok wypuszczenia filmu, tytuł oryginalny, streszczenie, entity_name(film czy serial), source_type, gatunek/gatunki, opis, ilość ocen, ocena, ile osób chce film obejrzeć.


## Jak zacząć

### Wymagania
- numpy
  
  ```sh
   pip install numpy
   ```
- pandas
  
  ```sh
   pip install pandas
   ```
- playwright
  
  ```sh
   pip install playwright
   ```
  ```sh
   playwright install
   ```

### Instalacja

1. Sklonuj repozytorium
   ```sh
   git clone https://github.com/eryk0wski/Filmweb-scraper.git
   ```
2. Zainstaluj wszystkie potrzebne biblioteki
   ```sh
   pip install -r requirements.txt
   playwright install
   ```

### Użytkowanie

Największym aktualnym minusem aplikacji jest wymóg przeklikania 15 sekundowej reklamy,natomiast występuje ona tylko podczas rozruchu. Pliki cookies przeklikują się same.

1. Wpisz URL strony, filmweb w swoim url określa filtrowanie i sortowanie, więc można ustawić filtry na stronie i przekleić samo URL.
```sh
pageURL = 'https://www.filmweb.pl/search#/films?orderBy=rate.desc&count=20000%2C'
```
2. Określ liczbę iteracji (scrollowania)
```sh
iterations = ....
```

### Output

Na wyjściu otrzymujemy 3 pliki z danymi:
Plik danych na temat filmu, plik danych z ocenami i plik połączony.

![image](https://github.com/eryk0wski/Filmweb-scraper/assets/121037666/3b2fe7f4-8077-4938-86d7-7196d97bd776)


## Kontrybucje

Jest to bardzo prosty projekt do rozpoczęcia swojej przygody z pythonem, data-science, pandas i data scrapingiem. Zachęcam do kontrubowania do projektu.
Jak zacząć:

1. Zforkuj projekt
2. Dodaj gałąź 
3. Zacommituj zmiany
4. Pushnij gałąź
5. Otwórz Pull Request

