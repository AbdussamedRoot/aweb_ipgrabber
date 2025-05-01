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

    domain = input("Please type the name of the domain: ").strip()
    if not domain:
        print("invalid domain!")
        return

    ip = get_ip_address(domain)
    if ip:
        print(f"[+] IP-Adress of {domain}: {ip}")
    else:
        print("[-] Error: Unable to resolve the domain name.")

    print("=" * 50)
    print("Thank you for using Aweb!")
    print("=" * 50)

if __name__ == "__main__":
    main()
