# Best Practices

## Naming

- Variables, functions, methods, packages, modules
  - `lower_case_with_underscores`
- Classes and Exceptions
  - `CapWords`
- Protected methods and internal functions
  - `_single_leading_underscore(self, ...)`
- Private Methods
  - `__double_leading_underscore(self, ...)`
- Constants
  - `ALL_CAPS_WITH_UNDERSCORES`

## Module and Package importing Order

1. System Imports
2. Third-Party Imports
3. Local Source Tree Imports

### Good Python Import

The import order in a django project is:
- Standard library imports
- Imports from core Django
- Imports from third-party apps including those unrelated to Django
- Imports from the apps that you created as part of your Django project.

```python
# Stdlib imports
from math import sqrt
from os.path import abspath

# Core Django imports
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Third-party app imports
from django_extension.db.models import TimeStampedModel

# Import from your apps
from splits.models import BananaSplit
```

### Bad Python Imports

**Avoid Implicit Relative Imports**. Always use explicit Relative imports.
An example of Implicit Relative imports.

```python
# cones/views.py
from django.views.generic import CreateView

# Don't do this!
# Hardcoding of the `cones` package
# with implicit relative imports 
from cones.models import WaffleCone
from cones.forms import WaffleConeForm
from core.views import FoodMixin

class WaffleConeCreateView(FoodMixin, CreateView):
    model = WaffleCone
    form_class = WaffleConeForm
```

If we use **Explicit Relative Imports** then the example look like following:

```python
# cones/views.py
from django.views.generic import CreateView

# Relative imports of the `cones` package
from .models import WaffleCone
from .forms import WaffleConeForm
from core.views import FoodMixin

class WaflleConeCreateView(FoodMixin, CreateView):
    model = WaffleCone
    form_class = WaffleConeForm
```

### Rule of thumbs
* **Absolute Import** - Use when using another packages's attribute
* **Explicit Relative Import** - Use when using on the same package
* Never import *
* Aliasing for same name
```python
from django.db.models import CharField as ModelCharField
from django.forms import CharField as FormCharField
``` 