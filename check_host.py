import sys
import subprocess

if(len(sys.argv) <= 1):
    print("IP address belum diberikan")
else:
    host_ip = sys.argv[1]
    status, result = subprocess.getstatusoutput("ping -c1 " + host_ip)
    print(result)
    if(status == 0):
        print(f'Host {host_ip} is UP')
    else:
        print(f'Host {host_ip} is DOWN')
