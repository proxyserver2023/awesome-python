#### Models and Databases

##### Models
1. Quick Examples
2. Using Models
3. Fields
4. Meta Options
5. Model Attributes
6. Model Methods
7. Model Inheritence
8. Organizing Models in a package.

##### Making Queries
1. Creating Objects
2. Saving changes to objects
3. Retrieving Objects
4. Complex lookups with Q objects
5. Comparing objects
6. Deleting objects
7. Copying model instances
8. Updating multiple objects at once
9. Related objects
10. Falling back to raw SQL

##### Aggregation
```python
Book.objects.count()
Book.objects.filter(publisher__name='BaloneyPress').count()

from django.db.models import Avg
Book.objects.all().aggregate(Avg('price'))

```
#### Handling HTTP Requests
#### Working with forms
#### Templates
#### Class based views
#### Migrations
#### Managing Files
#### Testing in django
#### User Authentication in Django
#### Django's Cache Framework
#### Conditional View Processing
#### Cryptographic Signing
#### Sending Email
#### Internationalization and localization
#### Logging
#### Pagination
#### Security in django
#### Performance and optimization
#### Serializing Django objects
#### Django Settings
#### Signals
#### System Check Framework
#### External Packages