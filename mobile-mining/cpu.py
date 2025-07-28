import psutil
import os
import cpuinfo
import platform

cpu_info = platform.processor()
cpu_count = psutil.cpu_count(logical=False)
logical_cpu_count = psutil.cpu_count(logical=True)
system_info = platform.uname()

print(f"\033[1;32;40mCPU Information\033[00m\n")
print(f"Processor: \033[1;33;40m{cpu_info}\033[00m\n")
print(f"Threads: \033[1;33;40m{cpu_count}\033[00m\n")
print("\033[1;32;40mSystem Information\033[00m\n")
print(f"System: \033[1;33;40m{system_info.system}\033[00m\n")
print(f"Node Name: \033[1;33;40m{system_info.node}\033[00m\n")
print(f"Processor: \033[1;33;40m{system_info.processor}\033[00m\n")