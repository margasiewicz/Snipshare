# Snipshare
Repozytorium backendowe projektu zespołowego zespołu MAK
#### Instalacja
Klonowanie repozytorium
```bash
git clone https://github.com/margasiewicz/Snipshare.git
cd Snipshare
```
#### Tworzenie wirtualnego środowiska
###### Windows
```bash
pip3 install virtualenv
virtualenv myenv
```
###### Linux
```bash
sudo apt-get install python-pip
pip3 install virtualenv
virtualenv myenv
```
#### Aktywacja wirtualnego środowiska oraz instalacja potrzebnych bibliotek
###### Windows
```bash
myenv\Scripts\activate
pip3 install -r requirements.txt
```
###### Linux
```bash
source myenv/bin/activate
pip3 install -r requirements
```
#### Inicjowanie bazy danych
```bash
python
from apka import db
from apka.models import Message, User, Room
db.create_all()
exit()
```
#### Uruchomienie aplikacji
```bash
python run.py
```

