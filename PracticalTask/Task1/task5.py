import argparse
import platform
import psutil
import getpass
import os
import socket

def get_distro_info():
    return platform.platform()

def get_memory_info():
    mem = psutil.virtual_memory()
    return f"Total: {round(mem.total / 1e+9, 2)} GB, Used: {round(mem.used / 1e+9, 2)} GB, Free: {round(mem.available / 1e+9, 2)} GB"

def get_cpu_info():
    cpu_model = platform.processor()
    cores = psutil.cpu_count(logical=False)
    threads = psutil.cpu_count(logical=True)
    freq = psutil.cpu_freq()
    return f"Model: {cpu_model}, Cores: {cores}, Threads: {threads}, Speed: {freq.current:.2f} MHz"

def get_user_info():
    return getpass.getuser()

def get_load_average():
    if hasattr(os, 'getloadavg'):
        load1, load5, load15 = os.getloadavg()
        return f"Load average (1/5/15 min): {load1:.2f}, {load5:.2f}, {load15:.2f}"
    else:
        return "Load average is not supported on this OS."

def get_ip_address():
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        return f"IP address: {ip}"
    except:
        return "Could not determine IP address."

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="System Information Script")

    parser.add_argument("-d", "--distro", action="store_true", help="Show distro info")
    parser.add_argument("-m", "--memory", action="store_true", help="Show memory info")
    parser.add_argument("-c", "--cpu", action="store_true", help="Show CPU info")
    parser.add_argument("-u", "--user", action="store_true", help="Show current user")
    parser.add_argument("-l", "--load", action="store_true", help="Show system load average")
    parser.add_argument("-i", "--ip", action="store_true", help="Show IP address")

    args = parser.parse_args()

    if args.distro:
        print(f"Distro: {get_distro_info()}")
    if args.memory:
        print(f"Memory: {get_memory_info()}")
    if args.cpu:
        print(f"CPU: {get_cpu_info()}")
    if args.user:
        print(f"Current user: {get_user_info()}")
    if args.load:
        print(f"Load: {get_load_average()}")
    if args.ip:
        print(f"{get_ip_address()}")

    if not any(vars(args).values()):
        parser.print_help()
