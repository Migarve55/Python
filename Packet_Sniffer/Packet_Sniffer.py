from datetime import datetime as dt
import socket
import struct
#import textWrap

register = open("Registro" + ".txt",'w')
#register.write('=' * 100 + '\n')
register.write(str(dt.now()) + '\n\n')

def main():

    HOST = socket.gethostbyname(socket.gethostname())
    print('IP: {}'.format(HOST))
    
    #conn = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.ntohs(3)) # LINUX
    conn = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP) # MICROSOFT

    conn.bind((HOST, 0))
    conn.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    conn.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    while True: #Main loop
        raw_data, addr = conn.recvfrom(65536)
        dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
        print('\nEthernet Frame:') #Imprime lo obtenido
        print('Destination: {}, Source: {}, Protocol: {}'.format(dest_mac, src_mac, eth_proto))
        if usar_registro == 't':
            save_data(dest_mac, src_mac, eth_proto)

def ethernet_frame(data):
    desc_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
    return get_mac_addr(desc_mac),get_mac_addr(src_mac),socket.htons(proto),data[14:]

def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    return ':'.join(bytes_str).upper()

def save_data(dest_mac, src_mac, eth_proto):
    register.write("Destination mac: " + str(dest_mac) + " Source mac: " + str(src_mac) + " Ethernet protocol: " + str(eth_proto) + '\n')
    return True

usar_registro = input("Para usar el registro, pulsa 't': ")    

main() # Main Loop
register.close()
