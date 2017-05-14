
# 勉強メモ

## Python 3.3 以降は __init__.py は無くてもパッケージとして認識される

- PEP 420: Implicit Namespace Packages
    - https://docs.python.org/3/whatsnew/3.3.html#pep-420-implicit-namespace-packages

## 相対インポート

参考: https://docs.python.org/3.6/tutorial/modules.html#packages

- relative import beyond top-level package error
    - "__main__" となる実行ファイルから見て、パッケージ間をまたいで相対インポートはできない

```
$ python main_02_relative_import_beyond_top-level_package_error.py
Traceback (most recent call last):
  File "main_02_relative_import_beyond_top-level_package_error.py", line 2, in <module>
    from pkg01.mod04 import d
  File "/Users/masakiiwamoto/tmp/py_test/pkg01/mod04/d.py", line 2, in <module>
    from ...config import conf
ValueError: attempted relative import beyond top-level package
```

```
$ python pkg01/mod02/b.py
Traceback (most recent call last):
  File "pkg01/mod02/b.py", line 2, in <module>
    from ..mod01 import a
ValueError: attempted relative import beyond top-level package
```

