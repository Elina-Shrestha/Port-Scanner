import socket

def scan_port(target, port):
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result=s.connect_ex((target,port))
        s.close()
        return result==0
    except socket.gaierror:
        return None

def scan_range(target, start_port, end_port):
    print(f"\nScanning{target} from port {start_port} to {end_port}...")
    open_ports=[]
    for port in range(start_port, end_port+1):
        is_open = scan_port(target,port)
        if is_open is None:
            print("Invalid target address.")
        if is_open:
            print(f"Port{port} is open")
            open_ports.append(port)
    print(f"\nScan complete. {len(open_ports)} open port(s) found:{open_ports}")

target= input("Enter an IP address to scan (e.g. 127.0.0.1)")
start = int(input("Start port(e.g.1):"))
end= int(input("End port (e.g. 100):"))
scan_range(target, start, end)