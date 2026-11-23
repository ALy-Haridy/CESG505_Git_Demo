"""
class implementation of a 2D rotation class

creator: Peter Mackenzie-Helnwein
date: Oct 29, 2019
"""

# import libraries
import numpy as np


# class definition
class PlateElement(object):
    """
    !class: Rotation

    variables:
        self.nodes = [X1,X2,X3]
        self.C  ... material stiffness tensor
        self.A  ... element area
        self.g1 ... covariant base vector 1
        self.g2 ... covariant base vector 2
        self.h1 ... dual base vector 1
        self.h2 ... dual base vector 2
        self.B1 ... kinematic matrix for node 1
        self.B2 ... kinematic matrix for node 2
        self.stress ... Cauchy stress

    methods:
        __init__(self, X1,X2,X3, params)
        setDisp(self, U1,U2,U3)
        getF1(self)
        getF2(self)
        getF3(self)
        getKe(self)
    """

    def __init__(self, X1, X2, X3, params):

        self.nodes  = [X1, X2, X3]
        self.stress = np.zeros(3)

        if 'E' in params.keys():
            E = params['E']
        else:
            E = 1.0

        if 'nu' in params.keys():
            nu = params['nu']
        else:
            nu = 0.0

        self.C = np.array([[1.,nu,0.],
                           [nu,1.,0.],
                           [0.,0.,(1-nu)/2.]]) * E/(1.-nu*nu)

        # compute base vectors
        self.g1 = X1 - X3
        self.g2 = X2 - X3

        # compute metric
        G = np.array([[np.dot(self.g1,self.g1),np.dot(self.g1,self.g2)],
                      [np.dot(self.g2,self.g1),np.dot(self.g2,self.g2)]])

        # compute jacobian and area
        J = np.sqrt( np.linalg.det(G) )
        self.A = J/2.

        # compute dual vectors
        H = np.linalg.inv(G)
        h1 = H[0][0] * self.g1 + H[0][1] * self.g2
        h2 = H[1][0] * self.g1 + H[1][1] * self.g2

        self.B1 = np.array([[h1[0],0.0],[0.0,h1[1]],[h1[1],h1[0]]])
        self.B2 = np.array([[h2[0],0.0],[0.0,h2[1]],[h2[1],h2[0]]])

    def setDisp(self, U1, U2, U3):
        strain =  self.B1 @ (U1 - U3)
        strain += self.B2 @ (U2 - U3)
        self.stress = self.C @ strain

    def getF1(self):
        return self.stress @ self.B1 * self.A

    def getF2(self):
        return self.stress @ self.B2 * self.A

    def getF3(self):
        return self.stress @ (self.B1 + self.B2) * (-self.A)

    def getKe(self):
        self.B3 = -(self.B1 + self.B2)
        K11 = self.B1.T @ self.C @ self.B1 * self.A
        K12 = self.B1.T @ self.C @ self.B2 * self.A
        K13 = self.B1.T @ self.C @ self.B3 * self.A
        K22 = self.B2.T @ self.C @ self.B2 * self.A
        K23 = self.B2.T @ self.C @ self.B3 * self.A
        K33 = self.B3.T @ self.C @ self.B3 * self.A

        Ke = np.vstack( ( np.hstack( (K11  ,K12  ,K13) ),
                          np.hstack( (K12.T,K22  ,K23) ),
                          np.hstack( (K13.T,K23.T,K33) ) ) )
        return Ke


