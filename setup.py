from setuptools import setup, find_packages

setup(
    name='fat_llama_desktop',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'cupy-cuda12x',
        'pydub',
        'soundfile',
        'mutagen',
        'scipy',
        'tk',
        'fat_llama @ git+https://github.com/bkraad47/fat_llama.git',
    ],
    package_data={
        'fat_llama_desktop': ['app/*.py', 'tests/*.py', 'assets/*'],
    },
    entry_points={
        'console_scripts': [
            'fat_llama_desktop=fat_llama_desktop.main:main',
        ],
    },
    author='RaAd',
    author_email='bulkguy47@gmail.com',
    description='Fat Llama Desktop Application for batch processing/upscaling audio files using fat_llama package.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/bkraad47/fat_llama_desktop',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    license='BSD-3-Clause',
)
