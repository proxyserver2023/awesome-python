Profiling
=========
```shell
python -m cProfile -o <output_file_name> <script_to_run>
```

Analyze python script
```python
import pstats
p = pstats.Stats('<output_file_name>')
p.sort_stats('calls')
p.print_stats(5)
```
