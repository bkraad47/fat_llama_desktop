# Fat Llama Desktop Application

## Overview
Fat Llama Desktop is a desktop application for upscaling audio files. It supports multiple formats and utilizes concurrent processing to optimize the upscaling process. The application allows users to add multiple audio files, specify a target folder, and convert the files to a specified format using configurable parameters.

## Features
- Supports various audio formats: MP3, FLAC, WAV, OGG.
- Uses a new interpolation algorithm for upscaling audio data.
- Implements Iterative Soft Thresholding (IST) with concurrent processing for optimized performance.
- Provides a graphical user interface (GUI) for easy file management and conversion.
- Logs each step of the processing for better traceability and debugging.

## Requirements
- Python 3.12
- Required Python libraries:
  - numpy
  - pyfftw
  - pydub
  - soundfile
  - mutagen
  - tkinter
  - concurrent.futures

## Installation
### Prerequisites
- Ensure that Python 3.12 is installed.
- Install FFmpeg for audio processing.

### Python Libraries
You can install the required Python libraries using pip:
```bash
pip install numpy pyfftw pydub soundfile mutagen tkinter
```
Building the Application
You can use PyInstaller to build the application into an executable. Ensure you have PyInstaller installed:

bash
Copy code
pip install pyinstaller
Creating the Executable
Generate the executable using the provided .spec file:

bash
Copy code
pyinstaller fat_llama_desktop.spec
Usage
Running the Application
You can run the application from the command line:

bash
Copy code
python run_fat_llama_desktop.py
Or, if you have built the executable:

bash
Copy code
./dist/FatLlamaDesktop/FatLlamaDesktop.exe
GUI Overview
Add Files: Add audio files to the list for processing.
Select Target Folder: Choose the folder where the processed files will be saved.
Process Files: Start the upscaling process.
Clear List: Clear the list of files.
Upscaling Configuration
You can configure the upscaling parameters such as:

max_iterations: Maximum number of iterations for IST.
threshold_value: Threshold value for IST.
target_bitrate_kbps: Target bitrate in kbps.
Code Structure
main.py: Entry point for the application.
ui.py: Defines the GUI and handles user interactions.
feed.py: Contains the core upscaling logic and audio processing functions.
Logging
The application logs each step of the processing to provide better traceability and debugging. Logs are displayed in the console output.