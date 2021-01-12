import requests


# Get all operators
#'/rpn/op', method = 'GET'
get = requests.get('http://localhost:5000/rpn/op')
print('Get all operators:\n ', get.text)

# CREATE stacks
#'/rpn/stack', method = POST (1)
print('Create stacks')
post = requests.post('http://localhost:5000/rpn/stack')
print(post.text)
post = requests.post('http://localhost:5000/rpn/stack')
print(post.text)
post = requests.post('http://localhost:5000/rpn/stack')
print(post.text)
post = requests.post('http://localhost:5000/rpn/stack')
print(post.text)

# Get all stacks
#'/rpn/stack', method = GET
get = requests.get('http://localhost:5000/rpn/stack')
print('Get all stacks:\n', get.text)

# Update a given stack
#'/rpn/stack', method = POST (2)
post = requests.post('http://localhost:5000/rpn/stack', data = {'stack_id': 2, 'value': 10})
print(post.text)
post = requests.post('http://localhost:5000/rpn/stack', data = {'stack_id': 2, 'value': 5})
print(post.text)
post = requests.post('http://localhost:5000/rpn/stack', data = {'stack_id': 2, 'value': 6})
print(post.text)

# Get all stacks
#'/rpn/stack', method = GET
get = requests.get('http://localhost:5000/rpn/stack')
print('Get all stacks:\n', get.text)

# Compute
# /rpn/stack/<stack_id>', method = GET
get = requests.get('http://localhost:5000/rpn/stack/2', params = {'op': '+-'})
print('Computation(s) within a stack:\n', get.text)

# Get all stacks
#'/rpn/stack', method = GET
get = requests.get('http://localhost:5000/rpn/stack')
print('Get all stacks:\n', get.text)

# Get a specific stack
#'/rpn/stack', method = GET
get = requests.get('http://localhost:5000/rpn/stack', params = {'stack_id': 2})
print('Get a specific stack:\n', get.text)

# Empty stack
# /rpn/stack/<stack_id>', method = PUT
put = requests.put('http://localhost:5000/rpn/stack/2')
print('Empty a given stack:\n', put.text)

# Get all stacks
#'/rpn/stack', method = GET
get = requests.get('http://localhost:5000/rpn/stack')
print('Get all stacks:\n', get.text)

# Delete stack
# #'/rpn/stack', method = DELETE
delete = requests.delete('http://localhost:5000/rpn/stack', params = {'stack_id': 2})
print('Delete the stack:\n', delete.text)

# Get all stacks
#'/rpn/stack', method = GET
get = requests.get('http://localhost:5000/rpn/stack')
print('Get all stacks:\n', get.text)

#
#END

