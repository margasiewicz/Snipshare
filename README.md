# Snipshare
Repozytorium backendowe projektu zespołowego zespołu MAK
#### Instalacja
Klonowanie repozytorium i zapewnienie zgodności lokalnego mastera:
```bash
git clone https://github.com/margasiewicz/Snipshare.git
git pull origin master
cd <ścieżka do repozytorium>
```
#### Tworzenie wirtualnego środowiska
###### Windows
```bash
py -m venv <venv_name>
```
###### Linux
```bash
python3 -m venv <wybrana_nazwa>
```
#### Aktywacja wirtualnego środowiska oraz instalacja potrzebnych bibliotek
###### Windows
```bash
<wybrana_nazwa>\Scripts\activate.bat
pip install -r requirements.txt
```
###### Linux
```bash
source <wybrana_nazwa>/bin/activate
pip install -r requirements
```
#### Uruchomienie
```bash
python3 <ścieżka_do>/run.py
```

