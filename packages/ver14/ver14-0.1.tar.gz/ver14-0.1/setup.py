from setuptools import setup, find_packages

setup(
    name='ver14',
    version='0.1',
    
    packages=find_packages(),
    package_data={'ver14': ['src/*.py', 'images/*.png', 'settings/*.ini']},
    install_requires=[
        # Add any dependencies your project needs
        'Pillow', 'openai'
    ],
    entry_points={
        'console_scripts': [
            'ver14=ver14.src.AIUT:main',  
        ],
    }
)

