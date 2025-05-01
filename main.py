import socket

def get_ip_address(domain):
    """
    Holt die IP-Adresse einer Domain.
    :param domain: Domain-Name als String
    :return: IP-Adresse als String oder Fehlermeldung
    """
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror:
        return None

def main():
    print("=" * 50)
    print("Aweb - Advanced Web Intelligence Tool".center(50))
    print("=" * 50)

    domain = input("Gib den Namen der Webseite ein: ").strip()
    if not domain:
        print("Fehler: Du musst eine Domain eingeben!")
        return

    ip = get_ip_address(domain)
    if ip:
        print(f"[+] IP-Adresse von {domain}: {ip}")
    else:
        print("[-] Ungültiger Domain-Name. Bitte überprüfe die Eingabe.")

    print("=" * 50)
    print("Danke, dass du Aweb benutzt!")
    print("=" * 50)

if __name__ == "__main__":
    main()