import sys
from enum import auto, Enum
from typing import List, Sequence

from mhelper import arg_parser
from mhelper._unittests._test_base import test, testing


class ETestEnum( Enum ):
    ALPHA = auto()
    BETA = auto()
    GAMMA = auto()
    DELTA = auto()


class Checker:
    instance: "Checker" = None
    
    
    def __init__( self, **kwargs ):
        self.kwargs = kwargs
        self.n = 1 if self.instance is None else self.instance.n + 1
        self.constructed = None
    
    
    @staticmethod
    def check( n: int, c ):
        self = Checker.instance
        
        for k, v in self.kwargs.items():
            print( f"{k:>20} = {v!r}" )
        
        testing( self.n ).EQUALS( n )
        testing( self.constructed ).EQUALS( c )
        testing( self.kwargs["alpha"] ).EQUALS( 1 )
        testing( self.kwargs["beta"] ).EQUALS( 'A' )
        testing( self.kwargs["gamma"] ).EQUALS( [1, 2, 3] )
        testing( self.kwargs["delta"] ).EQUALS( ['A', 'B', 'C'] )
        testing( self.kwargs["epsilon"] ).EQUALS( True )
        testing( self.kwargs["zeta"] ).EQUALS( True )
        testing( self.kwargs["eta"] ).EQUALS( False )
        testing( self.kwargs["theta"] ).EQUALS( ETestEnum.GAMMA )


def test_function( alpha: int, beta: str = "default", *, gamma: Sequence[int], delta: Sequence[str] = ("DEFAULT",), epsilon: bool = False, zeta: bool = True, eta: bool,
                   theta: ETestEnum ):
    """
    Help for test_function goes here.
    
    :param alpha:      Help for parameter alpha goes here.  
    :param beta:       Help for parameter beta goes here.  
    :param gamma:      Help for parameter gamma goes here.  
    :param delta:      Help for parameter delta goes here.  
    :param epsilon:    Help for parameter epsilon goes here.  
    :param zeta:       Help for parameter zeta goes here.  
    :param eta:        Help for parameter eta goes here.
    :return: 
    """
    Checker.instance = Checker( alpha = alpha,
                                beta = beta,
                                gamma = gamma,
                                delta = delta,
                                epsilon = epsilon,
                                zeta = zeta,
                                eta = eta,
                                theta = theta )


class TestClass:
    alpha: int
    beta: str = "default"
    gamma: Sequence[int]
    delta: Sequence[str] = ("DEFAULT",)
    epsilon: bool = False
    zeta: bool = True
    eta: bool
    theta: ETestEnum
    
    
    def __init__( self ):
        self.constructed = True
    
    
    def print( self ):
        test_function( alpha = self.alpha,
                       beta = self.beta,
                       gamma = self.gamma,
                       delta = self.delta,
                       epsilon = self.epsilon,
                       zeta = self.zeta,
                       eta = self.eta,
                       theta = self.theta )
        Checker.instance.constructed = getattr( self, "constructed", False )


@test
def test_from_function():
    args1 = "1 --beta A --gamma 1 2 3 --delta A B C --epsilon --zeta TRUE --eta OFF --theta GAMMA".split( " " )
    args2 = "--alpha 1 --beta A --gamma 1 2 3 --delta A B C --epsilon --zeta TRUE --eta OFF --theta GAMMA".split( " " )
    arg_parser.reflect( test_function, args1, )
    Checker.check( 1, None )
    arg_parser.reflect( TestClass, args2 ).print()
    Checker.check( 2, False )
    arg_parser.reflect( TestClass, args2, construct = True ).print()
    Checker.check( 3, True )
    arg_parser.reflect( TestClass, args2, construct = test_function )
    Checker.check( 4, None )
    
    try:
        arg_parser.reflect( test_function, [] )
    except SystemExit:
        pass


if __name__ == "__main__":
    test.execute()
