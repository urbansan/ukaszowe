import setuptools


setuptools.setup(
    name="ukaszowe",
    version="1.0.0",
    packages=["ukaszowe"],
    package_dir={"": "src"},
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "premier_league_sc = ukaszowe.main:premier",
            "polska_liga_sc = ukaszowe.main:champions",
        ]
    },
)
