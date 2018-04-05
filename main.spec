# -*- mode: python -*-

import os

block_cipher = None

this_dir = os.path.abspath(os.path.dirname("__file__"))

a = Analysis(['main.py'],
             pathex=[this_dir],
             binaries=[],
             datas=[
                 (os.path.join(this_dir, "login.js"), "."),
                 (os.path.join(this_dir, "Login.qml"), "."),
                 (os.path.join(this_dir, "LoginManager.qml"), "."),
                 (os.path.join(this_dir, "Main.qml"), "."),
                 (os.path.join(this_dir, "Users.qml"), "."),
             ],
             hiddenimports=[
                  "PyQt5.QtQuick", "PyQt5.QtQml",
             ],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='main',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='main')
