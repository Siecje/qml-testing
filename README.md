On Windows in ```cmd```

```shell
> python -m venv venv
> call venv\Scripts\activate.bat
> pip install PyQt5 cx_Freeze
> python setup.py build_exe
```

To create .msi
```shell
> python build_msi.py
```

```wix\QML.msi``` will be created.
