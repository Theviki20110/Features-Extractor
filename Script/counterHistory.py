clients = ['10.0.1.3', '10.0.2.3', '10.0.3.3']
servers = ['10.0.1.2', '10.0.2.2', '10.0.3.2']

data = []
k = 0

#Frame and byte
frame_byte_client = [0,0,0,0]
frame_byte_server = [0,0,0,0]

#[PUSH, SYNFIN, FIN, ACK, SYN, RST]
flag_inviati = [0,0,0,0,0,0]
flag_ricevuti = [0,0,0,0,0,0]

def flag_check(packet):
    if packet[8] != 'TCP':
        pass

    if packet[10] in clients:
        flag_inviati[0] += packet[-3] #PUSH

        if packet[-5] == '1' and packet[-6] == '1': #SYN e FIN
            flag_inviati[1] += 1 #FYN
        else:
            flag_inviati[2] += packet[-6] #FIN
            flag_inviati[4] += packet[-5] #SYN

        flag_inviati[3] += packet[-2] #ACK
        flag_inviati[5] += packet[-4] #RST

    elif packet[10] in servers:
        flag_ricevuti[0] += packet[-3] #PUSH

        if packet[-5] == '1' and packet[-6] == '1': #SYN e FIN
            flag_ricevuti[1] += 1
        else:
            flag_ricevuti[2] += packet[-6] #FIN
            flag_ricevuti[4] += packet[-5] #SYN

        flag_ricevuti[3] += packet[-2] #ACK
        flag_ricevuti[5] += packet[-4] #RST

with open('E:/Mega/Università/Tirocinio/FeaturesExtractor/FormattedTraffic/totaltraffic.txt', 'r') as f, open('E:/Mega/Università/Tirocinio/FeaturesExtractor/FormattedTraffic/countedtraffic.txt', 'w') as f1:
    for line in f:
        packet = line.split(', ')
        k += 1
        try:
            packet[0] = packet[0].split('[')[1]
            packet[-1] = packet[-1].split(']')[0]
            packet[0] = packet[0].split("'")[1]
            packet[8] = packet[8].split("'")[1]
            packet[10] = packet[10].split("'")[1]
        except:
            print(k)
            print(packet)
            continue

        for i in range(0, 28):
            if i == 0 or i == 8 or i == 10:
                continue

            packet[i] = int(packet[i])

        if packet[10] in clients:
            data.append('Attack')
            frame_byte_client[0] += 1
            frame_byte_client[2] += packet[2]
            frame_byte_server[1] += 1
            frame_byte_server[3] += packet[2]

        elif packet[10] in servers:
            data.append('Normal')
            frame_byte_client[1] += 1
            frame_byte_client[3] += packet[2]
            frame_byte_server[0] += 1
            frame_byte_server[2] += packet[2]
        else:
            print(k)
            print('ALTRO IP TROVATO:' + packet[10])
            continue

        flag_check(packet)

        for i in range(0, 4):
            data.append(frame_byte_client[i])

        for i in range(0, 6):
            data.append(flag_inviati[i])
            data.append(flag_ricevuti[i])

        for i in range(0, 4):
            data.append(frame_byte_server[i])

        data.append(packet[10])

        #packet.pop(10)
        """
        for i in range(0, len(data)):
            packet.append(data[i])"""

        f1.write(str(data))
        f1.write('\n')
        #print(k)
        data = []