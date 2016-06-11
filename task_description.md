# Task Requirements

### Implement search

Using the API endpoints that return JSON objects, as described in the `api_documentation.md` file, implement the search functionality using HTML/JS and the existing endpoints.

When user enters a search term the server should be queried for the results and the table updated with only the appropriate results showing. Upon deleting the search query the table should list the original items that were present when the user first opened the page.

You are free to rewrite any part of the frontend including, but not limited to, the way table is set up on the first page load -- with the only constraint being that the initial table information should be populated using the templating engine i.e. using the `{% for user in users %}` loop and not javascript.

*Note:* Usage of 3rd party js libraries is allowed.

### Implement sorting

Using the second documentend endpoint, implement sorting. Users can select by which field they want to sort the list and in which order, ascending or descending. The endpoint will return JSON object that should be used to construct the table.

*Hint:* Search results can, and should, be also sorted if the sorting is done after search has been executed. See the documentation for the `GET /api/v1/search` endpoint to see how to apply sorting. If the user has not searched for anything then use the `GET /api/v1/sort` endpoint.

# Optional Tasks

### Optimize search

We don't want to query the server every single time the user types a letter, for example while writing out the email address. Optimize the search so it's more server friendly and doesn't consume as much resources.

### Improve table

Re-implement table using some library for building UI interfaces, such as React for example so that it's easier to work with.

### Go to user pages

Clicking *anywhere* on the row in the table should go to `/view/<user_id>` url - (for example `http://127.0.0.1:5000/view/1`) which will show user data in a separate page.

# Task constraints
 
 * Backend can not be modified.
 
 * Links to static files should use template engine syntax (see exsisting templates for examples).
 
 * VCS(e.g. git) must be used during development.
 
 * If parts of the code are copied from 3rd parties (GitHub, StackOverflow etc) they must include accompanying licenses (if specified/required by the license)
 