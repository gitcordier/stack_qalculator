# stack_qalculator

## Introduction 
The the application is a [Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation) calculator. 
In other words, you can think of it as a stack-based process: First, push numbers in the stack, next compute then save the result as tail of the stack. 

It is implemented as a client-server whole: The very computations are performed by a [Flask](https://flask.palletsprojects.com/en/1.1.x/) backend, as the final user submits computation requests online. 
Those computation can easily be automated, thanks to a relevant API.
Nevertheless, an ordinary html page offers a visual interface with the backend. 

## What the folder contains
- rpn.py, the Flask bakckend;
- message.py, where an extension of dict is defined;
- client.py the client-client, for tests and automation purposes;
- page.html, the prototype of the web client;
- script.js, implementation of requests (PUT, DELETE) we cannot have with pure HTML;
- style.css, a style sheet for page.html
- todo.md, some TODOS;
- roadmap.md, some ideas for futher maintain and development;
- LICENSE; regular MIT license;
- .gitignore;
- This README.md

## The API
The first route is 

    /rpn/stack

and is literally the path to all processes that aim at stack, namely

- POST:
  - UPDATE a stack by appending a new value (keys: 'stack_id' and 'value');
  - CREATE a new stack 
- GET:
  - A specific stask (key: 'stack_id');
  - All current stacks
- DELETE a given stack (key: 'stack_id')


Parallely, there exists the following class of paths:

    /rpn/stack/<stack_id>'
    
They are routing to arithmetic computations of statcks. So, with more detail:

- GET, getting the result of the desired computations. A wished operation is passed as a GET parameter. 
  Note that 
  
  
      It is possible to chain computations once the stack is sufficiently full. 
      For istance, given a stack tail …,X,Y,Z], the parameter '++' means X + Y + Z.


      
- PUT: Empty a stack, so that we can restart a new series of computations

## How to run it
To launch the backend, 

    python3 rpn.py

The default IP is localhost:5000

To launch the frontend, 

    python3 client.py

You can also launch page.html with your favorite browser and reach localhost:5000.


 