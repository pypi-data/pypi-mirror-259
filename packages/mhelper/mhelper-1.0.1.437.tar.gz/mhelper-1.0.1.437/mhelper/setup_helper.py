import os
from typing import Dict, Optional, Sequence


def read_setup( package_dir ) -> "SetupInfo":
    file_name = os.path.join( package_dir, "setup.py" )
    
    if not os.path.isfile( file_name ):
        raise FileNotFoundError( f"I cannot find the setup file '{file_name}'." )
    
    import distutils.core as DUC
    import setuptools as SUT
    
    fs = _FakeSetup()
    orig_duc = DUC.setup
    orig_sut = SUT.setup
    
    try:
        DUC.setup = fs
        SUT.setup = fs
        
        import importlib.util
        spec = importlib.util.spec_from_file_location( "fake.name", file_name )
        foo = importlib.util.module_from_spec( spec )
        spec.loader.exec_module( foo )
    finally:
        DUC.setup = orig_duc
        SUT.setup = orig_sut
    
    return SetupInfo( fs.kwargs )


class SetupInfo:
    name: str = property( lambda self: self["name"] )
    packages: Sequence[str] = property( lambda self: self.get( "packages", () ) )
    version: Optional[str] = property( lambda self: self.get( "version", None ) )
    
    
    def __init__( self, kwargs ):
        self.kwargs: Dict[str, object] = kwargs
    
    
    def get( self, *args, **kwargs ):
        return self.kwargs.get( *args, **kwargs )
    
    
    def __getitem__( self, item ):
        return self.kwargs[item]


class _FakeSetup:
    def __init__( self ):
        pass
    
    
    def __call__( self, *args, **kwargs ):
        self.args = args
        self.kwargs = kwargs
