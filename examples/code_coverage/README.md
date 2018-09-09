```bash
pip install coverage
```

```bash
coverage report <script_name>
```

Example:
```bash
coverage report counter_demo.py
```
Outputs:
```
Name              Stmts   Miss  Cover
-------------------------------------
counter_demo.py      22      0   100%

```

Another Example
```bash
coverage report -m *.py
```

```
Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
__init__.py           0      0   100%
chain_map.py         12     12     0%   8-31
counter_demo.py      22      0   100%
-----------------------------------------------
TOTAL                34     12    65%

```