[![LinkedIn][linkedin-shield]][linkedin-url]
 [![Python][Python]][python-url] 
 [![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

<h2 align='center'>Features-Extractor</h2>
<p align='center'> Programma Ispirato dal lavoro di E. Viegas, A. Santin e V. Abreu:<br>"Enabling Anomaly-based Intrusion Detection Through Model Generalization". </p>

<br>

## About the project

<p>L'obiettivo è quello di ricreare un IDS (Intrusion Detection System) addestrando un modello di Machine Learning sulla base del traffico ricreato all'interno di un ambiente virtuale.
Il traffico generato viene trattato in modo da essere indipendente dalla sessione simulata (ambiente virtuale).

Alla fine si ottengono 50 features indipendenti dallo scenario ed utilizzabili per l'addestramento del modello.
(Elenco 50 features)</p>

<br>

## Getting started
Si presuppone la creazione dell'ambiente virtuale e del traffico che si vuole generare

### Prerequisites

Per la creazione del dataset si sfrutta la libreria nota _pandas_:
  
  ```sh
  pip install pandas
  ```

<br>

## Usage

Ad activation.py è necessario passare il numero di macchine client e i loro indirizzi.

1. Clone the repo
   ```sh
   git clone https://github.com/Theviki20110/Features-Extractor.git
   ```
2. Launch the script:
   ```sh
   sudo python3 activation.py
   ```



[Python]: https://img.shields.io/badge/-python-yellow?style=for-the-badge&logo=python
[python-url]: https://www.python.org/
[linkedin-shield]: https://img.shields.io/badge/-LinkedIN-informational?style=for-the-badge&logo=linkedin
[linkedin-url]: https://www.linkedin.com/in/vincenzo-lapadula-85a937164/