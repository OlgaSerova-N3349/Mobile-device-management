Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================== RESTART: /Users/macbook/Desktop/mobilki.py ==================
                         timestamp  msisdn_dest  call_duration  sms_number
msisdn_origin                                                             
915783624      2020-01-01 00:00:00    911926375          36.23          15
911926375      2020-01-01 00:05:00    968247916           9.20           5
936415793      2020-01-01 00:10:00    915642913           7.52          24
914976835      2020-01-01 00:15:00    914976835          96.70          97
962365794      2020-01-01 00:20:00    933156729         110.44          15
966714385      2020-01-01 00:25:00    915783624          12.34           5
968247916      2020-01-01 00:30:00    962365794          91.48          57
933156729      2020-01-01 00:35:00    936415793          83.22          73
915642913      2020-01-01 00:40:00    966714385          85.70          18
Введите номер абонента-968247916

Введите условия тарификации:
Для исходящих звонков-3

Для входящих звонков-1

Для СМС сообщений-1

Входящие- 274.44 
Исходящие- 9.2 
Телефония итого- 283.64 
СМС- 57
>>> 
================== RESTART: /Users/macbook/Desktop/mobilki.py ==================
Traceback (most recent call last):
  File "/Users/macbook/Desktop/mobilki.py", line 3, in <module>
    data=pd.read_csv('data.csv', index_col='msisdn_origin')
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/pandas/io/parsers.py", line 676, in parser_f
    return _read(filepath_or_buffer, kwds)
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/pandas/io/parsers.py", line 448, in _read
    parser = TextFileReader(fp_or_buf, **kwds)
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/pandas/io/parsers.py", line 880, in __init__
    self._make_engine(self.engine)
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/pandas/io/parsers.py", line 1114, in _make_engine
    self._engine = CParserWrapper(self.f, **self.options)
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/pandas/io/parsers.py", line 1891, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas/_libs/parsers.pyx", line 374, in pandas._libs.parsers.TextReader.__cinit__
  File "pandas/_libs/parsers.pyx", line 674, in pandas._libs.parsers.TextReader._setup_parser_source
FileNotFoundError: [Errno 2] File data.csv does not exist: 'data.csv'
>>> 
================== RESTART: /Users/macbook/Desktop/mobilki.py ==================
Введите номер абонента-968247916

Введите условия тарификации:
Для исходящих звонков-3

Для входящих звонков-1

Для СМС сообщений-1

Входящие- 274.44 
Исходящие- 9.2 
Телефония итого- 283.64 
СМС- 57
>>> 
>>> 
==================== RESTART: /Users/macbook/Desktop/mob1.py ===================
Введите номер абонента-968247916

Введите условия тарификации:
Для исходящих звонков-3

Для входящих звонков-1

Для СМС сообщений-1

Входящие- 274.44 
Исходящие- 9.2 
Телефония итого- 283.64 
СМС- 57
>>> 
>>> 
==================== RESTART: /Users/macbook/Desktop/mob2.py ===================
Введите множитель тарифного плана k руб/Mb-1
Введите ip-адрес клиента-217.15.20.194
Результат тарификации- 175.7 руб.
>>> 
>>> 
=================== RESTART: /Users/macbook/Desktop/tests.py ===================
176808151

=================== RESTART: /Users/macbook/Desktop/tests.py ===================
176808151

=================== RESTART: /Users/macbook/Desktop/tests.py ===================
176808151

=================== RESTART: /Users/macbook/Desktop/tests.py ===================
Traceback (most recent call last):
  File "/Users/macbook/Desktop/tests.py", line 10, in <module>
    file=open('/Users/macbook/Downloads/grep',"r+")
FileNotFoundError: [Errno 2] No such file or directory: '/Users/macbook/Downloads/grep'
>>> 
=================== RESTART: /Users/macbook/Desktop/tests.py ===================
176808151
Traceback (most recent call last):
  File "/Users/macbook/Desktop/tests.py", line 43, in <module>
    while not data[k]==".":
KeyboardInterrupt

>>> 
=================== RESTART: /Users/macbook/Desktop/tests.py ===================
176808151
>>> 
>>> 