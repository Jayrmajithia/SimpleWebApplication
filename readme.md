# Lyft Interview, Simple Web Application

I created a simple web applications where it has following end points and it would return the result as provided below using on your localhost.

## To initialize the server use following command
```
$ python -m flask run
```

The web application has following endpoints

url = http://localhost:port or url = http://127.0.0.1:port

## url/
this is the root page with a message of ```Welcome to the index page for Lyft apprenticeship program```

## url/hi
this page will ask you a question ```Who are you?```

## url/hi/username
this page will return with a messsage ```Hi there, {username} welcome to the Lyft apprenticeship application!```

for example if username = ```Jay```
it would return ```Hi there, Jay welcome to the Lyft apprenticeship application! ```

## url/test
when used with post method by sending a Json format data with the one single parameter ```string_to_cut``` it return json result with parameter of ```return_string``` containing every third letter of the string.

for example
If you POST {"string_to_cut": "iamyourlyftdriver"}, it will return: {"return_string": "muydv"}.
```
curl -X POST http://127.0.0.1:port/test --data '{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'
```
