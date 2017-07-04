import os
import platform
import shutil
import subprocess
import sys

from cx_Freeze import setup

from setup import BuildOptions, Executables, Name, Description, Removex64Paths, version

THIS_DIR = os.path.abspath(os.path.dirname(__file__))

def BuildExe(Version, Name, Description, BuildOptions, Executables):
    # cx_Freeze reads operation from sys.argv
    sys.argv = []
    sys.argv.append(__file__)
    sys.argv.append("build_exe")

    setup(
      name = Name,
      version = Version,
      description = Description,
      options = dict(build_exe = BuildOptions,
                     ),
      executables = Executables
    )

def BuildMsi(Naame, BuildDir, WxsPath, WxsName):
    args = [os.path.join(THIS_DIR, "wix", "create_msi.bat"),
            Name,
            BuildDir,
            WxsPath,
            WxsName,
    ]
    p = subprocess.run(args)


if __name__ == "__main__":
    shutil.rmtree(os.path.join(THIS_DIR, "build"), ignore_errors = True)
    
    python32 = platform.architecture()[0] == "32bit"
    if python32:
        origPath = os.environ["PATH"]
        newPath = Removex64Paths(os.environ["PATH"])
        os.environ["PATH"] = r"C:\Users\cody\Desktop\pynsist\nsist\msvcrt\x86" + os.pathsep + newPath

    BuildExe(version,
             Name,
             Description,
             BuildOptions,
             Executables
            )
    if python32:
        os.environ["PATH"] = origPath
    buildDir = os.path.join(THIS_DIR, "build", "exe.win32-3.5")
    wxsPath = os.path.join(THIS_DIR, "wix", "QMLApp.wxs")
    wxsName = "QMLApp"
    BuildMsi(Name, buildDir, wxsPath, wxsName)
