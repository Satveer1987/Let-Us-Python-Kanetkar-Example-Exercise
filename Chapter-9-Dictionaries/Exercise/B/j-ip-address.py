"""
Create a dictionary which stores the following data:

Interface   IPAddress  status
eth0        1.1.1.1     up
eth1        2.2.2.2     up
wlan0       3.3.3.3     down
wlan1       4.4.4.4     up


WAP to perfrom the following operations:
- Find the status of a given interface
- Find the interface and IP of all interfaces which are up
- Find the total number of interfaces
- Add two new entries to the dictionary
"""

ifs = {'eth0':{'ip':'1.1.1.1','status': 'up'}, 'eth1':{'ip': '2.2.2.2','status': 'up'}, 
       'wlan0':{'ip':'3.3.3.3','status' : 'down'}, 'wlan1':{'ip': '4.4.4.4','status': 'up'}}
print()
test=input('enter an interface:')
print(ifs[test]['status'])

for k,v in ifs.items():
    if v['status']=='up':
        print(k,v['ip'])
print()
print('total interfaces:',len(ifs))

print()
ifs['eth2']={'ip':'5.5.5.5','status' : 'up'}
ifs['wlan2']={'ip':'6.6.6.6','status' : 'down'}
for k,v in ifs.items():
    print(k,v)
