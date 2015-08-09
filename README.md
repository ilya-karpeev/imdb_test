# imdb_test

to run these tests you need python 2.7 with selenium, pytest and PyYAML libraries

command line to run these tests
---
with configuration file
```
py.test -v --cfg configuration_example.yaml tests\chart_top_test.py
```
without configuration file
```
py.test -v tests\chart_top_test.py
```
