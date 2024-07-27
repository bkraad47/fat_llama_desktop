from PyInstaller.utils.hooks import collect_dynamic_libs, collect_data_files, collect_submodules

# Collect dynamic libraries
binaries = collect_dynamic_libs('pyfftw')

# Collect all submodules
hiddenimports = collect_submodules('pyfftw')

# Collect data files
datas = collect_data_files('pyfftw')
