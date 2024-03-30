import socket

def get_ip_address(host_name_list):
    """
    Obtiene la dirección IP de una lista de nombres de host.

    Args:
        host_name_list (list): Lista de nombres de host.

    Returns:
        dict: Un diccionario donde las claves son los nombres de host y los valores son las direcciones IP correspondientes.
    """
    # Diccionario para almacenar las direcciones IP
    ip_addresses = {}

    # Itera sobre cada nombre de host en la lista
    for host_name in host_name_list:
        try:
            # Obtiene la dirección IP del nombre de host
            ip_address = socket.gethostbyname(host_name)
            # Almacena la dirección IP en el diccionario
            ip_addresses[host_name] = ip_address
        except socket.herror:
            # Si hay un error al obtener la dirección IP se almacenara un mensaje de error en el diccionario
            ip_addresses[host_name] = "No se encontró la dirección IP"

    # Devuelve el diccionario de direcciones IP
    return ip_addresses

if __name__ == "__main__":
    # Lista de nombres de host para consultar sus direcciones IP
    host_name_list = ["www.umsa.bo", "www.google.com", "www.putty.org"]

    # Obtiene las direcciones IP para los nombres de host dados
    results = get_ip_address(host_name_list)

    # Imprime los resultados
    for host_name, ip_address in results.items():
        print(f"La dirección IP de {host_name} es {ip_address}")
