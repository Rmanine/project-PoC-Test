[![AWS: Lambda](https://img.shields.io/badge/AWS-Lambda-blueviolet)](https://img.shields.io/badge/AWS-Lambda-blueviolet)
![Python](https://img.shields.io/badge/python-3.11-blue?logo=python)

<!-- Pytest Coverage Comment:Begin -->
<a href="https://github.com/Rmanine/project-PoC-Test/blob/main/README.md"><img alt="Coverage" src="https://img.shields.io/badge/Coverage-80%25-green.svg" /></a><details><summary>Coverage Report </summary><table><tr><th>File</th><th>Stmts</th><th>Miss</th><th>Cover</th><th>Missing</th></tr><tbody><tr><td colspan="5"><b>src/hello_world</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Rmanine/project-PoC-Test/blob/main/src/hello_world/__init__.py">__init__.py</a></td><td>0</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Rmanine/project-PoC-Test/blob/main/src/hello_world/app.py">app.py</a></td><td>3</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td colspan="5"><b>src/trusted_contacts</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Rmanine/project-PoC-Test/blob/main/src/trusted_contacts/AwsDynamoApi.py">AwsDynamoApi.py</a></td><td>37</td><td>8</td><td>78%</td><td><a href="https://github.com/Rmanine/project-PoC-Test/blob/main/src/trusted_contacts/AwsDynamoApi.py#L39-L51">39&ndash;51</a>, <a href="https://github.com/Rmanine/project-PoC-Test/blob/main/src/trusted_contacts/AwsDynamoApi.py#L76-L80">76&ndash;80</a></td></tr><tr><td><b>TOTAL</b></td><td><b>40</b></td><td><b>8</b></td><td><b>80%</b></td><td>&nbsp;</td></tr></tbody></table></details>
<!-- Pytest Coverage Comment:End -->

[![Quality Gate Status](http://localhost:9000/api/project_badges/measure?project=prova-app_che_protegger_e_trasforma-MVP&metric=alert_status&token=sqb_5f299b6506e2019d3d5c9d5e893eba4f07982ace)](http://localhost:9000/dashboard?id=prova-app_che_protegger_e_trasforma-MVP)

La documentazione completa relativa PoC si può consultare alla [Wiki](https://github.com/SWE-BitByBit/project-PoC/wiki) della presente repository.

## Requisiti di sistema
 
| Strumento | Versione minima | Note |
|-----------|----------------|-------|
| **Docker** | 24.x+ | Necessario per SonarQube |
| **Docker Compose** | v2.x+ | Incluso in Docker Desktop |
| **Python** | 3.12+ | Per il backend |
| **Flutter** | 3.x+ | Per il frontend |
| **AWS SAM CLI** | latest | Per build/deploy Lambda |
| **Make** | qualsiasi | Per eseguire i comandi del Makefile |

### Guida per installazione AWS SAM CLI
AWS SAM estende le funzionalità di AWS CDK e aggiungere funzionalità di building e di testing per applicazioni serverless.

1. [Instllare AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

2. Configurare AWS CDK con le proprie credenziali

```bash
$ aws configure
AWS Access Key ID [None]: <tua_ID_accesso>
AWS Secret Access Key [None]: <tua_chiave_accesso>
Default region name [None]: ue-north-1
Default output format [None]: json
```

3. [Installare AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)

## Installazione dipendenze
 
1. Clona la repo
 
```bash
git clone <url-repo>
cd <nome-repo>
```
2. Backend (Python)
 
```bash
cd sam_local_backend
make install        # crea il venv e installa le dipendenze
```

## Analisi della qualità del codice con SonarQube
 
Il progetto usa **SonarQube** per l'analisi statica del codice.  
L'istanza gira localmente tramite Docker — non è necessario installare nulla oltre a Docker.
 
### Primo avvio (una tantum)
 
```bash
# Dalla root del progetto
sudo chown -R 1000:1000 ./volumes/   # permessi necessari per SonarQube
docker compose up -d                  # avvia SonarQube + PostgreSQL
```


## Setup ambiente 
1. Crea un file `.env` nella cartella `frontend/`
   
2. Copia `.env.example` in `.env`

3. Sostituisci `API_BASE_URL` con l'endpoint
 
4. Esegui `flutter pub get`

## Setup Flutter 

1. Installare Flutter seguendo la **guida ufficiale**

https://docs.flutter.dev/install/quick

3. Eseguire il **setup del development environment** per poter compilare, eseguire, testare e deployare l'app su Android

https://docs.flutter.dev/platform-integration/android/setup

4. **Verificare** l'ambiente
```sh
flutter doctor
```
4. Installare le **dipendenze necessarie** da dentro la directory del progetto
```sh
flutter pub get
```
5. Creare un **nuovo emulatore con Android Studio**

https://developer.android.com/studio/run/managing-avds?hl=it

6. **Verificare** la presenza degli **emulatori**
```sh
flutter emulators && flutter devices
```
Il nome da usare nello step seguente è quello che si ha dato all'emulatore in Android Studio, che dovrebbe comparire dopo aver eseguito il comando.

7. **Eseguire** l'app sull'emulatore
```sh
flutter emulators --launch <Nome emulatore completo>
```
```sh
flutter run
```
### Risoluzione errori e problemi vari
- **In caso di errore Lint `Windows file separators (\) and drive letter separators (':') must be escaped`**: fare l'escape dei `:` nel path sdk.dir in `android/local.properties`. Il path dovrebbe essere qualcosa del tipo `C:\\Users\\mario\\AppData\\Local\\Android\\sdk`. Verificarne la risoluzione tramite `gradlew lintDebug`; eventualmente chiudere e riaprire VS Code.
- **In caso di app bloccata allo step `Running Gradle task 'assembleDebug'...`**: fare `cd android`, poi `./gradlew clean build`. Questo comando può richiedere una decina di minuti per terminare.
- **In caso di emulatore che non carica (schermata nera)**: Provare a premere il pulsante di avvio a fianco del simulatore (quello a forma di cerchio con la linea dentro). In alternativa, provare anche ad andare sul dispositivo in Android Studio (dalla schermata principale: tre puntini > virtual device manager), premere i 3 puntini sul dispositivo d'interesse > Wipe Data.

### Miglioramento prestazioni emulatore
- Da Android Studio, recarsi sulla lista dei dispositivi (dalla schermata principale: tre puntini > virtual device manager), premere i 3 puntini sul dispositivo d'interesse > Edit > Advanced Settings > Abilitare Quick Boot e aumentare RAM
- Se non si può cambiare la RAM: premere i 3 puntini sul dispositivo d'interesse > Show On Disk. Aprire `config.ini` e impostare `hw.ramSize` a piacimento
- Con emulatore avviato, premere i 3 puntini sul menu affianco all'emulatore in esecuzione > Settings > Advanced > Impostare OpenGL ES Renderer a `Desktop Native OpenGL`
