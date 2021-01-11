from flask import Flask, json, jsonify, request
from flask_cors import CORS # For localhost
from math import pow
from message import *

CORS_ORIGIN_WHITELIST = ['http://localhost:5000']

# Each stack must is identified with an identifier (an "id").
# Every id satisfies 0 ≤ id < BOUND, where BOUND is a positive integer.
BOUND = pow(2,16) # "Reasonable" bound. Feel free to set another one.

class RPN():
    '''
        This class defines 
        i. the flask application;
        ii. the list of all stacks;
        iii. A set of methods that frame the API implementation.
            Naming ('create', 'get',…) always refer to stack.
    '''
    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)
        self.stack_ = [] # Enlists stacks
        self.next_id = 0 
    
    # CREATE:
    def create(self):
        '''
            Creates a stack. The new stack is assigned an identifier. 
        '''
        
        # Actually, a stack is implemented as a two-key dict: 
        # The key 'id' is mapped to the id, as the key 'content' is mapped to  
        # the stack itself.
        if self.next_id < BOUND: 
            stack_id = self.next_id
            stack    = dict(id=stack_id, content=[])
            
            self.stack_.append(stack)
            self.next_id +=1
            
            return Message('Add a new stack (id = %s).'%stack_id)
        else: 
            return Message('Add a new stack.', False)
        #
    #
    
    # READ:
    def find_by_id(self, id):
        ''''
            Given 'id', spots the stack that is identified with 'id'.
        
            More specifically, returns the index of the stack in the 
            stack record (or -1 if no such stack were found).
        '''
        n = int(id)
        if -1 < n < self.next_id:
            i = 0
            for i in range(len(self.stack_)):
                if int(self.stack_[i]['id']) == n:
                    return i
                #
            #
            return -1
        else:
            return -1
    #
    
    # READ:
    def get(self, id):
        '''
            Getter. 
            Given 'stack_id', returns the stack that is identified with 
            'stack_id'.
        '''
        
        i = self.find_by_id(id)
        if i > -1:
            return self.stack_[i]['content']
        else:
            pass
        #
    #
    
    # UPDATE:
    def empty(self, id):
        '''
            Empty a given stack.
        '''
        
        i = self.find_by_id(id)
        if i > -1: 
            self.stack_[i]['content'] = []
            return Message('Empty stack %d.'%i)
        # else:
        return Message('Empty stack %d.'%i, False)
    #
    
    # DELETE:
    def delete(self, id):
        '''
            Setter.
            Given 'stack_id', deletes the stack that is identified with 
            'stack_id'.
        '''
        
        i = self.find_by_id(id)
        if i > -1:
            self.stack_.pop(i)
            return Message('Delete stack %d.'%i)
        else:
            return Message('Delete stack %d.'%i, False)
        #
    #
# We instantiate the app.
rpn = RPN()
app = rpn.app

# API implementation: BEGINNING ----------------------------------------------#
# List of all available N-ary operators (N > 0).
@app.route('/rpn/op', methods=['GET'])
def get_op_():
    dct = {
        'unary': {
            's': 'Opposite, i.e. symmetric with respect to +.',
            'i': 'Inverse, i.e. symmetric with respect to *.'
        },
        'binary': {
            '+': 'Addition',
            '-': 'Substraction',
            '*': 'Product',
            '/': 'Division',
            '^': 'Power'
            # And so on… Feel free to declare and implement other operators.
        }
    }
    return jsonify(dct)
    
@app.route('/rpn/stack', methods=['DELETE', 'GET', 'POST', 'PUT'])
def deal_with_stacks():
    '''
        This method nests all processes that aim at stack.
    '''
    
    if request.method == 'POST':
        # # # # # # # # # # # # # # # # # # # # #
        # UPDATE:                               #
        # If params are OK, we update the stack:#
        # # # # # # # # # # # # # # # # # # # # #
        if {'stack_id', 'value'} == set(request.form):
            id    = request.form['stack_id']
            value = request.form['value']
            
            try:
                rpn.get(id).append(float(value))
                return Message('Add value %s to stack %s.'%(value, id))
            except IndexError:
                return Message('Add value %s to stack %s.'%(value, id), False)
        
        # # # # # # # # # # # # # # 
        # IF not: CREATE new stack#
        # # # # # # # # # # # # # # 
        return rpn.create() 
    elif request.method == 'GET':
        # # # # # # # # # # # # #
        # READ: Get all stacks. #
        # # # # # # # # # # # # #
       return jsonify(rpn.stack_)
    
    elif request.method == 'DELETE':
        # # # # # # # # # # # # # # # # #
        # DELETE: Delete a given stack. #
        # # # # # # # # # # # # # # # # # 
        id = request.args.get('stack_id', '')
        return rpn.delete(id)
    else:
        pass
    #
#

@app.route('/rpn/stack/<id>', methods=['GET', 'PUT'])
def compute(id):
    '''
        This method encompasses all arithmetic computations a given stack 
        can be addressed.
    '''
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # GET:                                                            #
    # The stack #id is now an input for (successive) computation(s).  #
    # For instance '10 5 6 +' yields (6+5) = 11                       #
    #     (the stack ends up as […, 10, 11]), where '10 5 6 ++' yields#
    #     (6+5) + 10 = 21).                                           #
    # In the latter case, the stack tail is 21.                       #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    if request.method == 'GET':
        array   = rpn.get(id)
        symbol_ = request.args.get('op', '')    # e.g. ++/- .
        n       = len(symbol_)                  # number of operation(s).
        
        # Pathological case
        if array is None: 
            return Message('Perform the requested %d computation%s from value%s in stack %s.'
                    %(n, Message.plural(n), Message.plural(n), id), 
                    comment='Failed: The stack was empty.',
                    is_a_success=False)
                #
            #
        # Else (regular case)
        for symbol in symbol_:
            # First, unary operators cases:
            if symbol == 's': 
                array[-1] = -array[-1]  # Opposite.
            elif symbol == 'i':
                array[-1] = 1/array[-1] # Inverse.
            # And so on. You may define here any other wished function, e.g.
            # sin, cos, tan, erf.
            
            # Next, all binary operators:
            if len(array) > 1:
                # Read the stack
                operand_first = float(array[-2])
                operand_last  = float(array[-1])
            
                # Remove the last read values
                array.pop(-1)
                array.pop(-1)
            
                # Get the relevant arithmetic operation
                #
                if symbol == '+':
                    operator = lambda x, y: x+y
                elif symbol == '-':
                    operator = lambda x, y: x-y
                elif symbol == '*':
                    operator = lambda x, y: x*y
                elif symbol == '/':
                    operator = lambda x, y: x/y
                elif symbol == '^':
                    operator = lambda x, y: pow(x,y)
                #
                # And so on. You may define here any other wished operation.
                
                else:
                    # 0-ary operator i.e. constant.
                    operator = lambda x, y: y
                #
                # Compute then 'inject' the new output into the stack.
                array.append(operator(operand_first, operand_last))
                
            else: # Failure
                return Message('Perform the requested %d computation%s from value%s in stack %s.'
                        %(n, Message.plural(n), Message.plural(n), id), 
                        comment='Failed: Not enough operands in stack.',
                        is_a_success=False
                    #
                )
            #
        return Message('Perform %d computation%s, from value%s in stack %s.'
                %(n, Message.plural(n), Message.plural(n), id))
            #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # UPDATE:                                                         #
    # Empty a stack, i.e. reset before a new series of computation(s) #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    elif request.method == 'PUT':
        return rpn.empty(id) 
    #
#
# API implementation: END ----------------------------------------------------#

# Running the app:
if __name__ == "__main__":
    app.run()

# END
