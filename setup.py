from distutils.core import setup

setup(
    name="compvid",
    version='1.0.0',
    entry_points={
        "console_scripts": [
            "compv = compv:main",
        ]
    },
    py_modules=["compv"],
)