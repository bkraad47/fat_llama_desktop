import tkinter as tk
from mpi4py import MPI
from fat_llama_desktop.ui import FatLlamaApp

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    if rank == 0:  # Master process
        root = tk.Tk()
        app = FatLlamaApp(root, comm)
        root.mainloop()
    else:
        while True:
            task = comm.recv(source=0, tag=11)
            if task is None:
                break
            file_path, output_file, iterations, threshold, bitrate, output_format = task
            try:
                # Call the actual processing function here
                from fat_llama_desktop.feed import upscale
                upscale(
                    input_file_path=file_path,
                    output_file_path=output_file,
                    source_format=file_path.split('.')[-1],
                    target_format=output_format,
                    max_iterations=iterations,
                    threshold_value=threshold,
                    target_bitrate_kbps=bitrate
                )
            except Exception as e:
                # Handle the exception as needed
                pass

if __name__ == "__main__":
    main()
