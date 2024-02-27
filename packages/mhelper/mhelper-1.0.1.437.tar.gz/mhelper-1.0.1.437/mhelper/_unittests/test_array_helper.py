from mhelper import array_helper
from mhelper._unittests._test_base import test, testing


@test
def test_remover():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    with array_helper.Remover( my_list ) as my_list_:
        for item in my_list_:
            if item % 2 == 0:
                my_list_.drop()
    
    testing( my_list ).EQUALS( [1, 3, 5, 7, 9] )


@test
def test_rank():
    testing( array_helper.rank( "CAB" ) ).EQUALS( [1, 2, 0] )
    testing( array_helper.order( "CAB" ) ).EQUALS( [2, 0, 1] )
    testing( array_helper.rank_tie( "CABC" ) ).EQUALS( [2, 0, 1, 2] )


if __name__ == "__main__":
    test.execute()
