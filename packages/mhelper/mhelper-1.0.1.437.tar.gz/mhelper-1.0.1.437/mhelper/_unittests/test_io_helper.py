import json
from enum import Enum
import os
from mhelper import io_helper, specific_locations
from mhelper._unittests._test_base import test, testing


my_dir = specific_locations.get_application_directory( "mhelper", "tests", "test_io_helper" )


class ETest( Enum ):
    ALPHA = 1
    BETA = 2
    GAMMA = 3


# @test
# def open_write_doc():
#     testing( io_helper.open_write_doc() ).IS_READABLE( "Open write documentation generator" )


@test
def json_enum():
    obj = dict( alpha = ETest.ALPHA,
                beta = ETest.BETA,
                another = dict( gamma = ETest.GAMMA ),
                string = "Nothing::Nothing"
                )
    txt = io_helper.EnumJsonEncoder( supported_enums = [ETest] ).encode( obj )
    obj2 = io_helper.EnumJsonDecoder( supported_enums = [ETest] ).decode( txt )
    
    testing( obj2 ).EQUALS( obj )


@test
def test_open_for_write():
    test_fn = os.path.join( my_dir, "test.txt" )
    
    #
    # NORMAL WRITING
    #
    if os.path.isfile( test_fn ):
        os.remove( test_fn )
    
    with io_helper.open_for_write( test_fn ) as fout:
        fout.write( "test" )
    
    assert os.path.isfile( test_fn )
    
    # Check written using Python
    with open( test_fn ) as fin:
        assert fin.read() == "test"
    
    # Test `open_for_read`
    with io_helper.open_for_read( test_fn ) as fin:
        assert fin.read() == "test"
    
    os.remove( test_fn )
    
    #
    # FAILURE WRITING (shouldn't write because we are using an intermediate)
    #
    try:
        with io_helper.open_for_write( test_fn ) as fout:
            fout.write( "test" )
            raise ValueError()
    except Exception:
        pass
    
    assert not os.path.isfile( test_fn )
    
    #
    # Gzip case
    #
    test_fn += ".gz"
    
    with io_helper.open_for_write( test_fn ) as fout:
        fout.write( "test" )
    
    assert os.path.isfile( test_fn )
    
    # Check not written plain text using Python
    with open( test_fn ) as fin:
        assert fin.read() != "test"
    
    # Test `open_for_read`
    with io_helper.open_for_read( test_fn ) as fin:
        assert fin.read() == "test"
    
    os.remove( test_fn )
    
    #
    # FAILURE WRITING GZIP
    #
    try:
        with io_helper.open_for_write( test_fn ) as fout:
            fout.write( "test" )
            raise ValueError()
    except Exception:
        pass
    
    assert not os.path.isfile( test_fn )


if __name__ == "__main__":
    test.execute()
