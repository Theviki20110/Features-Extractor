clients = ['10.0.1.3', '10.0.2.3', '10.0.3.3']
servers = ['10.0.1.2', '10.0.2.2', '10.0.3.2']

first_packet = 0
first_packet_serv = 0
status = ['NEW', 'ESTABLISHED', 'CLOSED']

connections = []
first_connections = []
data = []
k = 0


def extraction(line, k):
    packet = line.split(', ')
    print(packet)
    if packet == ['[]\n']:
        return []
    try:
        packet[0] = packet[0].split('[')[1]
        packet[-1] = packet[-1].split(']')[0]
        packet[0] = packet[0].split("'")[1]
        packet[8] = packet[8].split("'")[1]
        packet[10] = packet[10].split("'")[1]
    except:
        print(packet)
        input()

    for i in range(0, 28):
        if i == 0 or i == 8 or i == 10:
            continue

        packet[i] = int(packet[i])

    if packet[10] not in clients and packet[10] not in servers:
        print(str(k) + ': ' + packet[10])
        return []

    return packet


with open("totaltraffic.txt", 'r') as f, open("connection.txt", 'w') as f1:
    for line in f:
        k += 1

        if line == '[]' or line == "['']":
            continue

        packet = extraction(line, k)

        if packet == [] or packet == ['']:
            continue

        data.append(k)

        # Check FIRST_PACKET:
        # If stateless: search ID in first_connection
        # oth check TCP flag

        if packet[8] == 'UDP' or packet[8] == 'ICMP':
            if packet[3] not in first_connections or packet[3] == 0:

                if packet[10] in clients:
                    first_packet = 1

                elif packet[10] in servers:
                    first_packet_serv = 1

                first_connections.append(packet[3] + 1)
            else:
                first_connections.remove(packet[3])
                first_connections.append(packet[3] + 1)

        elif packet[8] == 'TCP':
            if (packet[-5] and not packet[-6]) or (packet[-2] and packet[-3]):

                if packet[10] in clients:
                    first_packet = 1

                elif packet[10] in servers:
                    first_packet_serv = 1

        else:
            print('Altro protocollo')

        data.append(first_packet)
        data.append(first_packet_serv)

       #CONN_STATUS: If stateless -> ESTABLISHED oth check TCP Flags
        if packet[8] == 'UDP' or packet[8] == 'ICMP':
            data.append(status[1])

        elif packet[8] == 'TCP':
            # FLAG SYN == 1 and FIN == 0
            if packet[-5] and not packet[-6]:
                data.append(status[0])
                
            # FLAG SYN == 1 and FIN == 1 or FIN == 1 or RST == 1
            elif (packet[-5] and packet[-6]) or (packet[-4] or packet[-5]):
                data.append(status[2])
            elif packet[-2]:
                data.append(status[1])

        f1.write(str(data))
        f1.write('\n')

        first_packet = 0
        first_packet_serv = 0
        data = []
