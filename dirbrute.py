#---------------------------

# Colors

vermcl = '\033[1;91m'
cincl = '\033[1;96m'
amacl = '\033[1;93m'
cl = '\033[1;97m'
verd = '\033[1;32m'


from src import banner
from os import  system
from requests.models import Request

def cls(): 
    system('cls||clear')


def hour():
    print(strftime(f'{cl}[{vermcl}'+'%X'+f'{cl}]'))

# trying import libs.

try:
    from requests import get
except:
    print(f'{cl}[{vermcl}'+'%X'+f'{cl}] Trying install requests.')
    try:
        system('pip install requests')
        system('cls||clear')
    except:
        print(f'{cl}[{vermcl}'+'%X'+f'{cl}] Trying install requests.')
        try:
            system('apt install pip')
            system('cls||clear')
        except:
            print(f'{cl}[{vermcl}'+'%X'+f'{cl}] Trying install requests.')
            system('pacman -S install python-pip')
            system('cls||clear')


cls()

from time import sleep, strftime 
from sys import argv
from argparse import ArgumentParser
from requests import get


class basic():
    def banner():
        banner.basic.banner()


class args():
    def arg():
        parser = ArgumentParser()
        parser.add_argument("-f",nargs="?", help="Force to use.{brute} {middle} {light}")
        parser.add_argument("-u",nargs="?", help="Url to attack.")

        if len(argv) <= 1:
            parser.print_help()
            exit(1)

        args = parser.parse_args()

        if not args.f:
            print("Force required!")
            parser.print_help()
            exit(1)
        
        if not args.u:
            print("Url required!")
            parser.print_help()
            exit(1)

        if args.f == 'brute':
            if not args.u:
                print('Url required!')
                parser.print_help()
                exit(1)


        elif args.f == 'middle':
            if not args.u:
                print('Url required!')
                parser.print_help()
                exit(1)

        elif args.f == 'light':
            if not args.u:
                print('Url required!')
                parser.print_help()
                exit(1)
        else:
            print('Error!')
            parser.print_help()
            exit(1)
    


        if args.f == 'brute' and args.u:
            if args.u[-1] != '/':
                args.u += '/'
                if not 'http://' in args.u and not "https://" in args.u:
                    http = "".join("http://"+args.u)
                    args.u = http
                basic.banner()
                print(strftime(f'{cl}[{vermcl}'+'%X'+f'{cl}]'+f' Attacking: {args.u}'))
                try:
                    lists.brute(website=args.u)
                except KeyboardInterrupt:
                    print(f'An error has ocurred.')
                    print('Quitting.')
                    exit(0)
            else:
                basic.banner()
                print(strftime(f'{cl}[{vermcl}'+'%X'+f'{cl}]'+f' Attacking: {args.u}'))
                try:
                    lists.brute(website=args.u)
                except KeyboardInterrupt:
                    print('An error has ocurrred.')
                    print('Quitting.')
                    exit(0)

        if args.f == 'middle' and args.u:
            if args.u[-1] != '/':
                args.u += '/'
                if not 'http://' in args.u and not "https://" in args.u:
                    http = "".join("http://"+args.u)
                    args.u = http
                basic.banner()
                print(strftime(f'{cl}[{vermcl}'+'%X'+f'{cl}]'+f' Attacking: {args.u}'))
                try:
                    lists.middle(website=args.u)
                except KeyboardInterrupt:
                    print(f'An error has occurred.')
                    print('Quitting.')
                    exit(1)
            else:
                try:
                    lists.middle(website=args.u)
                except KeyboardInterrupt:
                    print('An error has ocurred.')
                    print('Quitting.')
                    exit(0)

        if args.f == 'light' and args.u:
            if args.u[-1] != '/':
                args.u += '/'
                if not 'http://' in args.u and not "https://" in args.u:
                    http = "".join("http://"+args.u)
                    args.u = http
                basic.banner()
                print(strftime(f'{cl}[{vermcl}'+'%X'+f'{cl}]'+f' Attacking: {args.u}'))
                try:
                    lists.light(website=args.u)
                except KeyboardInterrupt:
                    print(f'An error has occurred.')
                    print('Quitting.')
                    exit(1)
            else:
                try:
                    lists.light(website=args.u)
                except KeyboardInterrupt:
                    print('An error has ocurred.')
                    print('Quitting.')
                    exit(0)
        
        else:
            print('error!')
            print('quiting!')
            exit(0)
    
    def setURL(http):
        if not "http://" in http and not \
                "https://" in http:
            http = "".join("http://" + http)

        return http



class lists():
    def light(website):
        sleep(2)
        with open('wordlists/small.txt') as f:
            li = f.readlines()
            for l in li:
                try:
                    r=get(f'{website}/{l.strip()}')
                    if r.status_code == 200:
                            print(strftime(f'{cl}[{vermcl}'+'%X'+f'{cl}]'+f' {r.url}'))
                    else:
                        continue

                except ConnectionRefusedError:
                    cls()
                    print('Ocured an error!')
                    print('quitting!')
                    exit(1)

                except:
                    cls()
                    print(f'Ocurred an error!')
                    print(f'Quitting!')
                    exit(1)


    def middle(website):
        sleep(2)
        with open('wordlists/common.txt') as file:
            for line in file:
                try:
                    r=get(f'{website}/{line.strip()}')
                    if r.status_code == 200:
                            print(strftime(f'{cl}[{vermcl}'+'%X'+f'{cl}]'+f' {r.url}'))
                    else:
                        continue

                except ConnectionRefusedError:
                    cls()
                    print('Ocured an error!')
                    print('quitting!')
                    exit(1)
                
                except KeyboardInterrupt:
                    cls()
                    print(f'Ocurred an error!')
                    print(f'Quitting!')
                    exit(1)

    def brute(website):
        sleep(2)
        with open('wordlists/big.tx'+  't', encoding="ISO-8859-1") as b:
            op = b.readlines()
            for i in op:
                try:
                    r=get(f'{website}/{i.strip()}')
                    if r.status_code == 200:
                            print(strftime(f'{cl}[{vermcl}'+'%X'+f'{cl}]'+f' {r.url}'))
                    else:
                        continue

                except ConnectionRefusedError:
                    cls()
                    print('Ocured an error!')
                    print('quitting!')
                    exit(1)

                except KeyboardInterrupt:
                    print(f'Quiting.')
                    exit(0)

    
try:
    args.arg()

except KeyboardInterrupt:
    print('Quitting!')
    exit(0)
