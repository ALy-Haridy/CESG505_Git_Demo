'''
Created on Apr 19, 2009
Revised on April 27, 2009
Revised on Nov 9, 2020

@author: Peter Mackenzie
'''

import math

class Vector(object):
    '''
    The Vector class implements basic vector operations
    '''

    def __init__(self, data):
        '''
        Constructor
        '''
        self.v = map( float, data )
        self.dimension = len(data)
    
    def __getitem__(self, i):
        return self.v[i]
    
    def __setitem__(self, i, val):
        self.v[i] = float( val )
    
    def __len__(self):
        val = self.norm()
        return val
    
    def dim(self):  # return dimension
        return self.dimension
        
    def __add__(self, x):
        if type(x) == Vector and self.dimension == x.dimension:
            w = self.v[:]
            for i in range(0,self.dimension):
                w[i] += x[i]
            return w
        else:
            raise TypeError
        
    def __sub__(self, x):
        if type(x) == Vector and self.dimension == x.dimension:
            w = self.v[:]
            for i in range(0,self.dimension):
                w[i] -= x[i]
            return w
        else:
            raise TypeError
        
    def __mul__(self, x):
        if type(x) == Vector and self.dimension == x.dimension:
            w = 0.0
            for i in range(0,len(self)):
                w += self.v[i] * x[i]
            return w
        else:
            raise TypeError

    def __div__(self, x):
        raise NotImplemented
    
    def __str__(self):
        return str( self.v )
    
    def __repr__(self):
        return "Vector('{}')".format(self.__str__())
    
    def norm(self):
        val = math.sqrt( sum( x for x in self.v ) )
        return val
        
