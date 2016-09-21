```shell
git clone https://github.com/siecje/qml-testing
python -m venv osnap
call osnap\Scripts\activate.bat
pip install osnap
pip install requests jinja2
(osnap) C:\Users\cody\Desktop>pip freeze
Jinja2==2.8
MarkupSafe==0.23
osnap==0.0.2
requests==2.11.1
```

```shell
cd qml-testing/
python -m osnap.osnapy
pip install -r requirements.txt
python build.py
```
