import socket
import time

def run_server(host='', port=9876):
    """
    Inicia un servidor UDP que devuelve la fecha y hora del sistema a los clientes que se conectan.

    Args:
        host (str): La dirección IP del servidor. Por defecto, escucha en todas las interfaces.
        port (int): El número de puerto en el que el servidor escuchará las conexiones entrantes. Por defecto, 9876.
    """
    # Crea un socket UDP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Enlaza el socket al puerto y dirección especificados
    server_socket.bind((host, port))

    print(f"Servidor UDP escuchando en el puerto {port}...")

    try:
        while True:
            # Recibe el mensaje del cliente
            data, client_address = server_socket.recvfrom(1024)
            print(f"Mensaje recibido desde: {client_address}")

            # Obtiene la fecha y hora del sistema
            date_time_str = get_date_time()

            # Envía la fecha y hora al cliente
            server_socket.sendto(date_time_str.encode(), client_address)
    except KeyboardInterrupt:
        # Si el servidor es interrumpido, cierra el socket del servidor
        print("\nServidor detenido.")
        server_socket.close()

def get_date_time():
    """
    Obtiene la fecha y hora actual del sistema en formato AAAA-MM-DD HH:MM:SS.

    Returns:
        str: La fecha y hora actual del sistema.
    """
    return time.strftime("%Y-%m-%d %H:%M:%S")

if __name__ == '__main__':
    run_server()
