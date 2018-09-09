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

## Best Practices for Designing a Pragmatic RESTful API
1. An API is a user interface for a developer - so put some effort into making it pleasant
2. Use RESTful URLs and actions
    1. `GET /tickets` - Retrieves a list of tickets
    2. `GET /tickets/12` - Retrieves a specific ticket
    3. `POST /tickets` - Creates a new ticket
    4. `PUT /tickets/12` - Updates ticket #12
    5. `PATCH /tickets/12` - Partially updates ticket #12
    6. `DELETE /tickets/12` - Deletes ticket #12
3. Use SSL Everywhere, no exceptions
4. An API is only as good as its documenation - so have great documentation
5. Version via the URL, not via headers
6. Use query parameters for Result Filtering, Sorting & Searching
    1. Filtering: `/tickets?state=open`
    2. Sorting: 
        1. `GET /tickets?sort=-priority` - Retrieves a list of tickets in descending order of priority
        2. `GET /tickets?sort=-priority,created_at` - Retrieves a list of tickets in descending order of priority. Within a specific priority, older tickets are ordered first
    3. Searching: Search queries should be passed straight to the search engine and API output should be in the same format as a normal list result.
    4. Combining these we can build queries like:
        1. `GET /tickets?sort=-updated_at` - Retrieve recently updated tickets.
        2. `GET /tickets?state=closed&sort=-updated_at` - Retrieve recently closed tickets.
        3. `GET /tickets?q=return&state=open&sort=-priority,created_at` - Retrieve the highest priority open tickets old first mentioning the word `return`.
7. Aliases for common queries: `GET /tickets/recently_closed` similar to `GET /tickets?state=closed&sort=-updated_at`
8. Limiting which fields are returned by the API.
    1. this minimizes the network traffic and speed up their own usage of the API.
    2. Use a `fields` query parameter that takes a comma separated list of fields to include. `GET /tickets?fields=id,subject,customer_name,updated_at&state=open&sort=-updated_at`
9. Updates & creation should return a resource representation.
10. ALWAYS HATEOAS. unless Requirements Unnecessary.
    ```
    {
      "data": [
       {
         "id": 1,
         "title": "Hello world",
         "description": "lorem ipsum dolor sit amet",
         "author": 10,
         "_links": [ 
          {
              "rel": "self",
              "type": "GET",
              "href": "http://api.awesomeblog.com/posts/1"
            },
            {
              "rel": "self",
              "type": "PATCH",
              "href": "http://api.awesomeblog.com/posts/1"
            },
            {
              "rel": "self",
              "type": "DELETE",
              "href": "http://api.awesomeblog.com/posts/1"
            },
            {
              "rel": "comments",
              "type": "GET",
              "href": "http://api.awesomeblog.com/comments"
            },
            {
              "rel": "author",
              "type": "GET",
              "href": "http://api.awesomeblog.com/users/10"
            }
          ]
       }
       ....
       ....
       ....
      ],
      "meta": {
        "total": 50,
        "per_page": 15,
        "current_page": 1,
        "last_page": 4,
        "_links": [ 
          {
            "rel": "next",
            "href": "http://api.awesomeblog.com/posts?page=2"
          },
          {
            "rel": "prev",
            "href": null
          }
        ]
      }
    }    
    ```
11. JSON Only Responses
    ```
    It's time to leave XML behind in APIs. It's verbose, it's hard to parse, it's hard to read, its data model isn't compatible with how most programming languages model data and its extendibility advantages are irrelevant when your output representation's primary needs are serialization from an internal representation
    ```
12. snake_case field names
13. Pretty Print Default and ensure gzip is supported.
    ```bash
    $ curl https://api.github.com/users/veesahni > with-whitespace.txt
    $ ruby -r json -e 'puts JSON JSON.parse(STDIN.read)' < with-whitespace.txt > without-whitespace.txt
    $ gzip -c with-whitespace.txt > with-whitespace.txt.gz
    $ gzip -c without-whitespace.txt > without-whitespace.txt.gz
    ```
    The Output Files have the following sizes:
    1. without-whitespace.txt - 1252 bytes
    2. with-whitespace.txt - 1369 bytes
    3. without-whitespace.txt.gz - 496 bytes
    4. with-whitespace.txt.gz - 509 bytes
14. Don't use an envelope by default, but make it possible when needed.
    ```json
    {
      "data" : {
        "id" : 123,
        "name" : "John"
      }
    }
    ```
    JSONP requests come with an additional query parameter (usually named `callback` or `jsonp`) representing the name of the callback function. If this parameter is present, the API should switch to a full envelope mode where it always responds with a 200 HTTP Status Code and passes the real status code in the JSON Payload. Any additional HTTP headers that would have been passed alongside the response should be mapped to JSON fields, like so:
    
    ```js
    callback_function({
      status_code: 200,
      next_page: "https://..",
      response: {
        ... actual JSON response body ... 
      }
    })
    ```
15. JSON encoded POST, PUT and PATCH Bodies.
16. Pagination
    Link Header
    ```bash
    Link: <https://api.github.com/user/repos?page=3&per_page=100>; rel="next", <https://api.github.com/user/repos?page=50&per_page=100>; rel="last"
    ```
    But this isn't a complete solution as many API's do like to return the additional page information, like a count of the total number of available results. An API that requires sending a count can use a custom HTTP header like `X-Total-Count`.
17. Auto loading related resource representations.
    `embed` would be a comma separated list of fields to be embedded. Dot-notation could be used to refer to sub-fields. For Example:
    `GET /tickets/12?embed=customer.name,assigned_user`
    ```json
     
    {
      "id" : 12,
      "subject" : "I have a question!",
      "summary" : "Hi, ....",
      "customer" : {
        "name" : "Bob"
      },
      "assigned_user": {
       "id" : 42,
       "name" : "Jim"
      }
    }
    
    ```
18. Overriding the HTTP Method
    `X-HTTP-Method-Override`. Note that the override header should only be accepted on POST requests. GET requests should never change data on the server!

19. Rate Limiting.
    HTTP status code 429 Too Many Requests to accommodate this.
    `X-Rate-Limit-Limit` - the number of allowed requests in the current period.
    `X-Rate-Limit-Remaining` - The number of remaining requests in the current period.    `X-Rate-Limit-Reset` - The number of seconds left in the current period.

20. A RESTful API should be stateless. This means that request authentication should not depend on cookies or sessions. Instead, each request should come with some sort authentication credentials.

    By always using SSL, the authentication credentials can be simplified to a randomly generated access token that is delivered in the user name field of HTTP Basic Auth. The great thing about this is that it's completely browser explorable - the browser will just popup a prompt asking for credentials if it receives a 401 Unauthorized status code from the server. 
21. ETag, Last-Modified.
22. Errors
    
    ```json
    
    {
      "code" : 1024,
      "message" : "Validation Failed",
      "errors" : [
        {
          "code" : 5432,
          "field" : "first_name",
          "message" : "First name cannot have fancy characters"
        },
        {
           "code" : 5622,
           "field" : "password",
           "message" : "Password cannot be blank"
        }
      ]
    }
    
    ```

## Django REST Framework

1. Requests
2. Responses
3. Views
4. Generic Views
5. Routers
6. Parsers
7. Renderes


## APPENDIX
### HTTP Status Codes
1. 1XX Series - Informational
2. 2XX Series - Success
    1. 200 OK
    2. 201 Created
    3. 204 No Content
3. 3XX Series - Redirect
    1. 304 Not Modified
4. 4XX Series - Client Error
    1. `400 Bad Request`
    2. `401 Unauthorized`
    3. `403 Forbidden`
    4. `404 Not Found`
    5. `405 Method Not Allowed` - When an HTTP method is being requested that isn't allowed for the authenticated user
    6. `410 Gone` - Indicates that the resource at this end point is no longer available. Useful as a blanket response for old API versions.
    7. `415 Unsupported Media Type` - If Incorrect content type was provided as part of the request.
    8. `422 Unprocessable Entity` - Used for validation Errors.
    9. `429 Too Many Requests` - When a request is rejected due to rate limitting.
4. 5XX Series - Server Error

