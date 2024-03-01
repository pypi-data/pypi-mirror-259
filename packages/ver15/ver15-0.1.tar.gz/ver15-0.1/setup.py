from setuptools import setup, find_packages

setup(
    name='ver15',
    version='0.1',
    
    packages=find_packages(),
    package_data={'ver15': ['src/*.py', 'images/*.png', 'settings/*.ini','requirements/*.txt']},
    install_requires=[
        # Add any dependencies your project needs
        'Pillow', 'openai==1.3.5',"prettytable"
    ],
    entry_points={
        'console_scripts': [
            'ver15=ver15.src.AIUT:main',  
        ],
    }
)

