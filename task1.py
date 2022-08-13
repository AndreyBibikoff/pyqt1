import platform
import subprocess
import threading
from ipaddress import ip_address

result = {'Reachable hosts': "", "Unreachable hosts": ""}


def ping(ipv4, result, get_list):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    response = subprocess.Popen(["ping", param, '1', '-w', '1', str(ipv4)],
                                stdout=subprocess.PIPE)
    if response.wait() == 0:
        res = f"{ipv4} - Узел доступен"
        print(f'{res}\n')
        if get_list:
            result["Reachable hosts"] += f"{ipv4}\n"
        return res
    else:
        res = f"{str(ipv4)} - Узел недоступен"
        print(f'{res}\n')
        if get_list:
            result["Unreachable hosts"] += f"{ipv4}\n"
        return res


def ping_host(hosts, get_list=False):
    threads = []
    for host in hosts:
        try:
            ipv4 = ip_address(host)
        except:
            print(f'{host} - not ipv4, domain name')
            ipv4 = host

        thread = threading.Thread(target=ping, args=(ipv4, result, get_list), daemon=True)
        thread.start()
        threads.append(thread)
    # print(threads)
    for thread in threads:
        thread.join()
    if get_list:
        return result


if __name__ == '__main__':
    hosts = ['ya.ru', '77.88.8.1', '77.88.8.2', '77.88.8.3', '77.88.8.4',
             '77.88.8.5', '77.88.8.6', '77.88.8.7', '77.88.8.8', '77.88.8.9', ]
    ping_host(hosts)
    print(result)
