[![LinkedIn][linkedin-shield]][linkedin-url]
 [![Python][Python]][python-url] 
 [![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

<h2 align='center'>Features-Extractor</h2>
<p align='center'> Work inspired by E. Viegas, A. Santin and V. Abreu's paper:<br>"Enabling Anomaly-based Intrusion Detection Through Model Generalization". </p>

<br>

## About the project

<p>L'obiettivo è quello di ricreare un IDS (Intrusion Detection System) addestrando un modello di Machine Learning sulla base del traffico ricreato all'interno di un ambiente virtuale.
Il traffico generato viene trattato in modo da essere indipendente dalla sessione simulata (ambiente virtuale).

Alla fine si ottengono 50 features indipendenti dallo scenario ed utilizzabili per l'addestramento del modello.
<details>
<summary>50 Features + Target:</summary>
<ol>
   <li>IP_TYPE</li>
   <li>IP_LEN</li>
   <li>FR_LENGHT</li>
   <li>IP_ID</li>
   <li>IP_RESERVED</li>
   <li>IP_DF</li>
   <li>IP_MF</li>
   <li>IP_OFFSET</li>
   <li>IP_PROTO</li>
   <li>IP_CHECKSUM</li>
   <li>UDP_SPORT</li>
   <li>UDP_DPORT</li>
   <li>UDP_LEN</li>
   <li>UDP_CHK</li>
   <li>ICMP_TYPE</li>
   <li>ICMP_CODE</li>
   <li>ICMP_CHK</li>
   <li>TCP_SPORT</li>
   <li>TCP_DPORT</li>
   <li>TCP_SEQ</li>
   <li>TCP_ACK</li>
   <li>TCP_FFIN</li>
   <li>TCP_FSYN</li>
   <li>TCP_FRST</li>
   <li>TCP_FPUSH</li>
   <li>TCP_FACK</li>
   <li>TCP_FURG</li>
   <li>COUNT_FR_SRC_DST</li>
   <li>COUNT_FR_DST_SRC</li>
   <li>NUM_BYTES_SRC_DST</li>
   <li>NUM_BYTES_DST_SRC</li>
   <li>NUM_PUSHED_SRC_DST</li>
   <li>NUM_PUSHED_DST_SRC</li>
   <li>NUM_SYN_FIN_SRC_DST</li>
   <li>NUM_SYN_FIN_DST_SRC</li>
   <li>NUM_FIN_SRC_DST</li>
   <li>NUM_FIN_DST_SRC</li>
   <li>NUM_ACK_SRC_DST</li>
   <li>NUM_ACK_DST_SRC</li>
   <li>NUM_SYN_SRC_DST</li>
   <li>NUM_SYN_DST_SRC</li>
   <li>NUM_RST_SRC_DST</li>
   <li>NUM_RST_DST_SRC</li>
   <li>COUNT_SERV_SRC_DST</li>
   <li>COUNT_SERV_DST_SRC</li>
   <li>NUM_BYTES_SERV_SRC_DST</li>
   <li>NUM_BYTES_SERV_DST_SRC</li>
   <li>FIRST_PACKET</li>
   <li>FIRST_SERV_PACKET</li>
   <li>CONN_STATUS</li>
   <li>TYPE</li>
</ol>
</details>
</p>

<br>

## Getting started
È necessario creare un ambiente virtuale come quello illustrato in figura:
<br>

![Enviroment][enviroment-screenshot]

<br>
È possibile usare qualsiasi virtualizzatore l'importante è che le macchine client possano comunicare esclusivamente con il server.
Il server è l'unico punto di accesso ad internet e si occupa di fornire connettività ai client.
<br>

Si può pensare di utilizzare per ogni macchina la seguente configuarazione in `\etc\network\interfaces`
```
auto eth0
iface eth0 inet dhcp #or static configuration

post-up route add default gw 10.0.1.2
```

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

## Example

[Python]: https://img.shields.io/badge/-python-yellow?style=for-the-badge&logo=python
[python-url]: https://www.python.org/
[linkedin-shield]: https://img.shields.io/badge/-LinkedIN-informational?style=for-the-badge&logo=linkedin
[linkedin-url]: https://www.linkedin.com/in/vincenzo-lapadula-85a937164/
[enviroment-screenshot]: res/image1.png