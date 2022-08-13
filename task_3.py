from tabulate import tabulate
from task2 import host_range_ping


def host_range_ping_tab():
    res_dict = host_range_ping(True)
    print(tabulate([res_dict], headers='keys', tablefmt='rst', stralign='center'))


if __name__ == "__main__":
    host_range_ping_tab()