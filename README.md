# imdb_test

to run these tests you need python 2.7 with selenium and pytest libraries
to have possibility to use configuration file you need PyYAML python library
to have possibility to see log in test report you need pytest-capturelog library

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
without specifying test name (test would be picked up automatically by py.test)
```
py.test -v
```
