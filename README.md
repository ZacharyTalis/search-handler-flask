# search-handler-flask

A Flask app that performs URL substitutions/redirections.

## URL Arguments

All arguments are mandatory. `%26` is the escape code for `&`.

| Argument | Example Value                   | Behavior      |
| -------- | ------------------------------- | ------------- |
| ?url     | http://example.com/?arg1%26arg2 | Base URL      |
| ?subs    | arg1~red,arg2~blue              | Substitutions |

Per the example values above:

```
[host]?url=http://example.com/?arg1%26arg2&subs=arg1~red,arg2~blue
->
http://example.com/?red&blue
```
