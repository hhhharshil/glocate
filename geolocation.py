import requests
import ipaddress


with open('ips.txt', 'r') as ipf:
    iplist = ipf.readlines()

def geo_locate():
        for ip in iplist:
            if '/' in ip:
                addrs = ipaddress.ip_network(ip.replace("\n",''))
                for addr in addrs:
                    response = requests.get("https://api.iplocation.net/?ip=" + str(addr))
                    details = response.json()
                    print("=====================================")
                    print('IP Address: '+ details['ip']) 
                    print('Country: ' + details['country_name'])
                    print('Organization: ' + details['isp'])
                    print("=====================================")
            else:
                response = requests.get("https://api.iplocation.net/?ip=" + ip.rstrip())
                details = response.json()
                print("=====================================")
                print('IP Address: '+ details['ip']) 
                print('Country: ' + details['country_name'])
                print('Organization: ' + details['isp'])
                print("=====================================")

geo_locate()
