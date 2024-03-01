import subprocess

class Node:

    def __init__(self, ip_address: str, reputation: float=0.0) -> None:
        self.ip_address = ip_address
        self.reputation = reputation

    def get_reputation(self, ip_address, count=3) -> float:
        # Costruisci il comando di ping
        command = ['ping', '-c', str(count), ip_address]
        counter = 0
        reputation = 1.0

        try:
            # Esegui il comando e cattura l'output riga per riga
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            for line in process.stdout:
                counter +=1
                # print(f"{counter}: {line.strip()}")
                if counter == 7:
                    elements = line.strip().split(",")
                    value = elements[2].strip().split(" ")[0]
                    value = float(value[:-1])
                    print(f"packet loss? {type(value)} {value}%")
                    reputation = 100 if value == 0.0 else 10

            # Attendere che il processo termini
            process.wait()

            # Verifica se ci sono errori nel processo
            # if process.returncode != 0:
            #     print(f"Errore durante il ping. Codice di ritorno: {process.returncode}")
        except subprocess.CalledProcessError as e:
            # Se c'è un errore, stampa l'errore
            print(f"Errore durante il ping: {e}")
        
        return reputation

        