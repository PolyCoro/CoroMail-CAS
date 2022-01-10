from setuptools import setup, find_packages

setup(
    name="CoroMail-CAS",
    version="0.0.1",
    author="Isma Bennis, Alexandra Deac, Karim El Kharroubi, Paul-Édouard Graves, Édouard Matheu, Julie Rago, Clément Roger, Clément Leboulenger, Vincent Lefebvre",
    author_email="polycoro@gmail.com",
    url="https://github.com/PolyCoro/CoroMail",
    description="Central Authentication Server for CoroMail",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
    ],
    install_requires=[],
    entry_points={"console_scripts": ["coromail-cas = src.main:main"]},
)
