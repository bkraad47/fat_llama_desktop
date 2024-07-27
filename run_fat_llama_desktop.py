import os
import subprocess

def main():
    num_processors = os.cpu_count()
    print(num_processors)
    if num_processors is None:
        num_processors = 1  # Fallback to 1 if cpu_count() is not supported
    
    command = f'mpiexec -n {num_processors} python -m fat_llama_desktop.main'
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    main()
