class Message(dict):
    '''
        A 'message' is a HR-response that declares
        - how it was interpreted in terms of action ("task")- furthermore;
        - whether such task were successfully performed.
    '''
    def __init__(self, describe, is_a_success=None, comment=None):
        self['task'] = describe
        
        if is_a_success in (None, True):
            self['success'] = True
        else:
            self['success'] = False
        
        if comment: 
            self['comment'] = comment
    #
    
    @staticmethod
    def plural(n):
        '''
            Returns 's' if we deal with n > 1 objects. If not, returns the 
            empty string.
        '''
        if n > 1:
            return 's'
        return ''
#

# END