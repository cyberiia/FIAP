import socket
from datetime import datetime                                                                                                          
import time                                                                                                                            
import subprocess
import argparse
from argparse import RawTextHelpFormatter

print("Port Scanner - 0b1t\n\nThis is an academic projet, we are not resposible for any illegal activities!\n")

parser = argparse.ArgumentParser(description="scan target's logical ports\nusage example:\n\nportscanner.py 10.10.10.5 22\nportscanner.
py 128.0.0.2 8080-9000\nportscanner.py 192.168.0.1 22, 80, 443, 8080", formatter_class=RawTextHelpFormatter)

parser.add_argument('ip', metavar='ip', type=str, help='enter your target ip')
parser.add_argument('port', metavar='port', type=str, help='enter your target ip')
args = parser.parse_args()
target = args.ip
port = args.port
scan_started = time.time()                                                                                                             

if "-" in port:                                                                                                                        

    port_range = sorted(port.split("-"))                                                                                               
    ports = []                                                                                                                         
    for port in range(int(port_range[0]), int(port_range[-1]) + 1):                                                                    
        ports.append(port)                                                                                                             

elif ',' in port:                                                                                                                      

    ports = sorted(port.split(","))                                                                                                    

else:                                                                                                                                  

    ports = [port]                                                                                                                     

print("scanning...\n")                                                                                                                 

def scan(target_ip, ports):                                                                                                            

    for port in ports:                                                                                                                 

        try:                                                                                                                           

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:                                                            
                sock.settimeout(0.5)                                                                                                   
                result = sock.connect_ex((target_ip, int(port)))                                                                       
                if result == 0:                                                                                                        
                    print (f"port {port} is Open")                                                                                     
                    get_port = str(subprocess.run(f"getent services {port}", capture_output=True, shell=True).stdout)                  
                    get_port = get_port[2:-2]                                                                                          
                    print(f"service running: {get_port}")                                                                              
                sock.close()                                                                                                           

        except:                                                                                                                        

            pass                                                                                                                       

scan(target, ports)                                                                                                                    

scan_finished = time.time()                                                                                                            
scan_time = scan_finished - scan_started                                                                                               
print(f"\nyour scan took {scan_time} to finish, thanks for using it!")
