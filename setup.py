import os
import sys

from cx_Freeze import setup, Executable


BuildOptions = {"packages": ["PyQt5.QtNetwork"],
                "excludes": ["tkinter", "sqlite3", "tcl", "scipy",
                             "PyQt4", "PyQt5.QtSql",
                             "PIL",
                             "tornado", "zmq",
                             "virtualenv", "boto", "alabaster", "bs4", "jinja2", "sphinx", "sphinx_rtd_theme", "sqlalchemy",
                             ],
                "optimize": 2,
                "include_files": "",
                "include_msvcr": True, # Include msvcr100.dll
                }


Base = "Win32GUI" if sys.platform == "win32" else None

Executables = [
    Executable('main.py', base = Base),
]

Name = "QML"
Description = "QML Application"

version = "0.0.1"

if __name__ == "__main__":
    setup(name = Name,
          version = version,
          description = Description,
          options = dict(build_exe = BuildOptions,
                         ),
          executables = Executables
          )