# Two Scoops of Django

## Coding Style

### Django Coding Style

* Good URL Pattern names in Django
```python
patterns = [
    url(
        regex='^add/$',
        view=views.add_topping,
        name='add_topping',
    )
]
```
* Underscores in template block names
