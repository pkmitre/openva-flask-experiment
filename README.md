# Experimental openVA RESTful Interface Approach

This repository demonstrates a simple approach to organizing openVA algorithms and services into a service oriented architecture using RESTful interfaces. Note that this sketch organizes all the interfaces using synchronous access, and an asynchronous structure would be more appropriate if this approach is adopted.

## Setup

First set up the demonstration algorithm and format translation services, following the README documentation in each repository:

* https://github.com/pkmitre/InterVA5/tree/microservice-experiment

* https://github.com/pkmitre/pyCrossVA/tree/microservice-experiment

Then run the demonstration user interface:

```
  FLASK_ENV=development FLASK_APP=openva.py flask run -p5000
```

The service can then be accessed at http://127.0.0.1:5000/
