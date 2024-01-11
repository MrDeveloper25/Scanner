import socket
import random
import struct

def scan_ip_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # Tiempo de espera para la conexión en segundos
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"Intento {port}: El puerto {port} está abierto en la IP {ip}")
                # Obtener información adicional
                try:
                    host = socket.gethostbyaddr(ip)[0]
                    print(f"Host asociado: {host}")
                except socket.herror:
                    print("No se pudo resolver el nombre de host")
            else:
                print(f"Intento {port}: El puerto {port} está cerrado en la IP {ip}")
    except socket.error:
        pass

def scan_random_ports(ip_list):
    common_ports = [21, 22, 23, 25, 53, 80, 443, 3306, 3389]  # Lista de puertos comunes a escanear
    while True:
        for ip in ip_list:
            print(f"Escaneando IP: {ip}")
            for port in common_ports:
                scan_ip_port(ip, port)
            print("")

        choice = input("Presiona 'r' para detener el escaneo y mostrar estadísticas: ")
        if choice.lower() == 'r':
            # Muestra estadísticas aquí
            print("¡Estadísticas!")
            break

def generate_ip_list(count):
    ip_list = []
    while len(ip_list) < count:
        ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))  # Genera una dirección IP aleatoria
        ip_list.append(ip)
    return ip_list

ip_list = generate_ip_list(10)  # Genera una lista de 10 direcciones IP aleatorias

print("Presiona 'r' para detener el escaneo y mostrar estadísticas.")
print("Escaneando direcciones IP...")

scan_random_ports(ip_list)
