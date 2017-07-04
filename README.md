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

### Windows

- Install latest Python 3 (3.6.1 is currently out).
- Install latest NSIS (3.0.1 is currently out) - http://nsis.sourceforge.net/Download

```shell
python -m venv venv
call venv\Scripts\activate.bat
pip install pynsist
pynsist.exe installer.cfg
```
