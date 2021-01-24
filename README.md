# Snipshare
Repozytorium backendowe projektu zespołowego zespołu MAK
#### Instalacja
Klonowanie repozytorium i zapewnienie zgodności lokalnego mastera:
```bash
git clone https://github.com/margasiewicz/flippery.git
git pull origin master
cd <directory path>
```
#### Tworzenie wirtualnego środowiska
###### Windows
```bash
py -m venv <venv_name>
```
###### Linux
```bash
python3 -m venv <venv_name>
```
#### Aktywacja wirtualnego środowiska oraz instalacja potrzebnych bibliotek
###### Windows
```bash
<venv_name>\Scripts\activate.bat
pip install -r requirements.txt
```
###### Linux
```bash
source <venv_name>/bin/activate
pip install -r requirements
```
