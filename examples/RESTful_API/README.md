# RESTful API Guide

## Characteristics of GOOD API
1. Easy to learn (notice the priority placement of learn-ability...)
2. Intuitive / Easy to use even without documentation
Hard to misuse (write tests for "undesirable" behaviour)
3. Easy to read and maintain code that uses it
4. Sufficiently powerful to satisfy requirements
5. Easy to evolve (the simpler the initial API the easier it will be to extend)
6. Appropriate to audience (make it beginner friendly...)
7. Opinionated (means people don't have to think)

## Verbs
1. GET
2. POST
3. PUT
4. PATCH
5. DELETE

| HTTP Verb     | CRUD           | Collection                                                                 | Item                                                     |
| ------------- |:-------------  |:--------------------------------------------------------------------------:|:--------------------------------------------------------:|
| GET           | READ           | 200[ok], list, pagination, filtering and sorting to navigate big list      | 200[ok] single item, 404[not found]                      |
| POST          | CREATE         | 201 (Created), 'Location' header with link to /customers/{id} containing new ID. | 404 (Not Found), 409 (Conflict) if resource already exists|
| PUT           | Update/Replace | 405 (Method Not Allowed), unless you want to update/replace every resource in the entire collection. | 200 (OK) or 204 (No Content). 404 (Not Found), if ID not found or invalid.|
| PATCH         | Update/Modify  | 405 (Method Not Allowed), unless you want to modify the collection itself. | 200 (OK) or 204 (No Content). 404 (Not Found), if ID not found or invalid. |
| DELETE        | Delete         | 405 (Method Not Allowed), unless you want to delete the whole collection—not often desirable.| 200 (OK). 404 (Not Found), if ID not found or invalid.|

### Examples

1. GET /comment - Returns a list of all comments
2. GET /comment/:id - Returns a comment with the given id
3. POST /comment - Creates a new comment
4. PUT /comment/:id - Updates a comment with the given id
5. DELETE /comment/:id - Deletes a comment with the given id

### Tips
To reduce the amount of data retrieved, we can specify the exact fields we want in the url e.g.:
```
GET /accounts/1234/fields=firstname,surname,etc
```

## Design Principles
Five things every API must have
1. Error Handling
2. Error Logging
3. Validation - e.g. JSON Schema Validation
4. Authentication and Authorization
5. Testing

### Best Practices for designing a pragmatic RESTful API



# Django REST Framework

1. Requests
2. Responses
3. Views
4. Generic Views
5. Routers
6. Parsers
7. Renderes
