from task1 import ping_host

from ipaddress import ip_address


def host_range_ping(get_list=False):
    while True:
        start_ip = input("start ip: ")
        try:
            ip = ip_address(start_ip)
            last_oct = int(start_ip.split('.')[3])
            break
        except Exception as e:
            print(e)
    while True:
        num_of_hosts = input("number of hosts: ")
        if not num_of_hosts.isdigit():
            print("Ошибка, необходимо ввести целое число")
        else:
            if (last_oct + int(num_of_hosts)) > 255+1:
                print(f"максимальное число хостов {255+1 - last_oct}")
            else:
                break
    host_list = []
    [host_list.append(str(ip + x)) for x in range(int(num_of_hosts))]
    if not get_list:
        ping_host(host_list)
    else:
        return ping_host(host_list, True)


if __name__ == "__main__":
    host_range_ping()

