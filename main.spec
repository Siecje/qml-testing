# -*- mode: python -*-

import os

block_cipher = None

this_dir = os.path.abspath(os.path.dirname("__file__"))

datas = [
    (os.path.join(this_dir, "login.js"), "."),
    (os.path.join(this_dir, "Login.qml"), "."),
    (os.path.join(this_dir, "LoginManager.qml"), "."),
    (os.path.join(this_dir, "Main.qml"), "."),
    (os.path.join(this_dir, "Users.qml"), "."),
]

hidden_imports = [
     "PyQt5.QtQuick", "PyQt5.QtQml",
]

a_main = Analysis(['main.py'],
                  pathex=[this_dir],
                  binaries=[],
                  datas=datas,
                  hiddenimports=hidden_imports,
                  hookspath=[],
                  runtime_hooks=[],
                  excludes=[],
                  win_no_prefer_redirects=False,
                  win_private_assemblies=False,
                  cipher=block_cipher)
a_main2 = Analysis(['main2.py'],
                   pathex=[this_dir],
                   binaries=[],
                   datas=datas,
                   hiddenimports=hidden_imports,
                   hookspath=[],
                   runtime_hooks=[],
                   excludes=[],
                   win_no_prefer_redirects=False,
                   win_private_assemblies=False,
                   cipher=block_cipher)
MERGE( (a_main, 'main', 'main'),
       (a_main2, 'main2', 'main2'),
)



pyz_main = PYZ(a_main.pure,
               a_main.zipped_data,
               cipher=block_cipher)
exe_main = EXE(pyz_main,
               a_main.scripts,
               exclude_binaries=True,
               name='main',
               debug=False,
               strip=False,
               upx=True,
               console=True)

pyz_main2 = PYZ(a_main2.pure,
                a_main2.zipped_data,
                cipher=block_cipher)
exe_main2 = EXE(pyz_main2,
                a_main2.scripts,
                exclude_binaries=True,
                name='main2',
                debug=False,
                strip=False,
                upx=True,
                console=True)

coll_all = COLLECT(exe_main,
                   a_main.binaries,
                   a_main.zipfiles,
                   a_main.datas,
                   exe_main2,
                   a_main2.binaries,
                   a_main2.zipfiles,
                   a_main2.datas,
                   strip=False,
                   upx=True,
                   name='main')
