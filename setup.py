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
                "include_files": ["Main.qml", "Users.qml", "LoginManager.qml", "Login.qml", "login.js"],
                "include_msvcr": True, # Include msvcr100.dll
                }


Base = "Win32GUI" if sys.platform == "win32" else None

Executables = [
    Executable('main.py', base = Base),
]

Name = "QML"
Description = "QML Application"

version = "0.0.1"

BadPaths = [
    "C:\\Program Files\\",
    'Anaconda3',
]


def Removex64Paths(PathStr):
    pathList = PathStr.split(";")
    newPath = []
    for path in pathList:
        for badPath in BadPaths:
            if badPath in path:
                break
        else:
            newPath.append(path)
    return ";".join(newPath)


if __name__ == "__main__":
    import platform
    python32 = platform.architecture()[0] == "32bit"
    if python32:
        origPath = os.environ["PATH"]
        newPath = Removex64Paths(os.environ["PATH"])
        os.environ["PATH"] = r"C:\Users\cody\Desktop\pynsist\nsist\msvcrt\x86" + os.pathsep + newPath
    
    setup(name = Name,
          version = version,
          description = Description,
          options = dict(build_exe = BuildOptions,
                         ),
          executables = Executables
          )
    if python32:
        os.environ["PATH"] = origPath
