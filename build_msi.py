import os
import subprocess
import sys

from cx_Freeze import setup

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
    from setup import BuildOptions, Executables, Name, Description, version
    BuildExe(version,
             Name,
             Description,
             BuildOptions,
             Executables
            )
    buildDir = os.path.join(THIS_DIR, "build", "exe.win-amd64-3.5")
    wxsPath = os.path.join(THIS_DIR, "wix", "QMLApp.wxs")
    wxsName = "QMLApp"
    BuildMsi(Name, buildDir, wxsPath, wxsName)
