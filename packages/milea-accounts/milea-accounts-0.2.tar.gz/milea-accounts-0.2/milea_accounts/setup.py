from setuptools import find_packages, setup

setup(
    name='milea-accounts',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,  # Schließt Dateien ein, die in MANIFEST.in aufgeführt sind
    install_requires=[
        'milea-base>=0.1',
        'django-countries>=7.5.1',
    ],
    author='red-pepper-services',
    author_email='pypi@schiegg.at',
    description='Milea Framework - Account Module',
    license='MIT',
)
