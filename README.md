# Example QML Application

To demonstrate how to test and package a PyQt5 QML Application.

## Development Instructions

### Linux

```shell
git clone https://github.com/siecje/qml-testing
cd qml-testing
```

```shell
python3 -m venv venv
source venv/bin/activate
pip install PyQt5
python main.py
```

### Windows

```shell
git clone https://github.com/siecje/qml-testing
cd qml-testing
```

```shell
python3 -m venv venv
call venv\Scripts\activate.bat
pip install PyQt5
python main.py
```

Then enter 'user' as the password.

## Packaging

On Windows in `cmd`

### Install .NET for Wix

https://www.microsoft.com/en-US/Download/confirmation.aspx?id=17718

### Install Wix

http://wixtoolset.org/releases/

### Create .msi

```shell
python -m venv venv
call venv\Scripts\activate.bat
pip install PyQt5 cx_Freeze
python setup.py build_exe
```

To create .msi
```shell
python build_msi.py
```

`wix\QML.msi` will be created.
