"""
An OOP, reflective derivative of argparse.

Note that `reflect` and `execute` are the primary functions.

Everything else is for backwards compatibility and should no longer be
considered a part of the API.
"""
import os
import argparse
import collections
import sys
import warnings
import inspect
from enum import Enum
from typing import Callable, TypeVar, Dict, Union, Optional, Type, cast, Iterable, List, Sequence, Any

import typing
from mhelper.exception_recorder import print_traceback
from mhelper import string_helper, ansi, exception_helper
from mhelper.documentation_helper import Documentation
from collections import abc


T = TypeVar( "T" )
_DEFAULT_TOPIC = ""
_DO_NOT_EXIT = "error"


def create_parser( module_name,
                   description_ex = "",
                   *,
                   help = True,
                   version = True,
                   epilog: Optional[str] = None ) -> "ArgumentParser":
    """
    Automatically instantiates an `ArgumentParser` based on the specified
    module's content (doc string and version number).
    
    .. note::
    
        The arguments will still need adding manually, for automated argument
        generation use the `reflect` function instead.
    
    :param module_name:     Module name 
    :param description_ex:  Optional additional doc string content 
    :param epilog:          Optional additional help content
    :param help:            True to use the module doc string. 
                            False to use no help.
                            Anything else to use that as the help (see `ArgumentParser`). 
    :param version:         True to use the module version.
                            False to use no version.
                            Anything else to use that as the version (see `ArgumentParser`). 
    :return:                `ArgumentParser` instance. 
    """
    warnings.warn( "Deprecated - consider using `reflect` or `execute`.", DeprecationWarning )
    ap = ArgumentParser()
    ap.add_help( source = module_name,
                 description_ex = description_ex,
                 help = help,
                 epilog = epilog )
    ap.add_module_version( module_name, version = version )
    return ap


def entry_point( f: Callable[..., Optional[int]] = None ):
    """
    !DECORATOR
    
    Produces a function, `g`, that calls `execute` on `fn` and immediately
    executes this function if the calling module is the entry point (i.e. it is
    ``__main__``), otherwise returns `g` (thereby replacing `f` when used as
    decorator). 
    
    .. note::
    
        * `f` will be inaccessible if `entry_point` is used as a decorator.
        * `g` takes no arguments.
        * `g` is suitable as a the target of `console_scripts` in `setup.py`.
        * Auto-call functionality is based on the the name of the calling module
          (rather than using the module in which `f` is defined). This allows 
          `entry_point` be used on external functions (but not as a decorator).
        * The program will `exit` with the result of `f` if `f` returns a
          non-`None` result.
    
    :param f:  Target function 
    :return:   Argumentless function that calls `execute` on `f`. 
    """
    if f is None:
        return entry_point
    
    frame = inspect.stack()[1]
    module = frame.frame.f_globals["__name__"]
    # module = fn.__module__
    ep = __EntryPoint( f )
    
    if module == "__main__":
        ep()
    
    return ep


class __EntryPoint:
    """
    Calls `execute` on `f`.
    """
    
    
    def __init__( self, f ):
        self.f = f
    
    
    def __call__( self ) -> None:
        r = execute( self.f )
        
        if r is not None:
            exit( r )


class CliError( Exception ):
    pass


def branch( branches: Dict[Union[str, Sequence[str]], object],
            call = None,
            docs: Callable[[str, object], None] = None ) -> int:
    """
    Executes one of several branches.
    
    The program name is updated accordingly.
    
    :param branches:    Branch names and executors.
                        Branch names are case insensitive and ignore non-alphanumeric characters.
    :param call:        When set this is called with the branch value.
                        When unset, the branch value is assumed to be a callable and is called directly.
    :param docs:        Function to return the documentation from the branch name and function. 
    :return:            Return value of executed function.
    """
    
    norm_branches = { }
    
    for keys, value in branches.items():
        if isinstance( keys, str ):
            keys = keys,
        
        for key in keys:
            key = string_helper.normalise( key )
            norm_branches[key] = keys[0], value
    
    selected: str = sys.argv[1] if len( sys.argv ) > 1 else ""
    selected = string_helper.normalise( selected )
    is_help = selected == "help"
    
    if selected and not is_help and selected in norm_branches:
        selected_name, selected_fn = norm_branches[ selected ]
        
        if selected_fn is not None:
            set_program_name( get_program_name() + " " + selected_name )
            del sys.argv[1]
            
            if call:
                return call( selected_fn )
            else:
                return selected_fn()
    
    #
    # Nothing selected, show help
    #
    prog = get_program_name()
    
    from mhelper import ansi
    
    X = ansi.FORE_BRIGHT_WHITE
    N = ansi.FORE_BRIGHT_YELLOW
    T = ansi.FORE_BRIGHT_RED
    
    p = lambda x: print( x, file = sys.stderr )
    
    p( T )
    p( f"***** Usage *****{X}" )
    p( "" )
    p( "This application runs in multiple modes, each with their own arguments, please" )
    p( "specify the mode before continuing." )
    p( "" )
    p( f"    {N}{prog} <mode> [arguments ...]{X}" )
    p( "" )
    p( "For help on a mode:" )
    p( "" )
    p( f"    {N}{prog} <mode> --help{X}" )
    p( "" )
    p( T )
    p( f"***** Modes *****{X}" )
    p( "" )
    
    for keys, f in branches.items():
        if isinstance( keys, str ):
            keys = keys,
        
        branch = string_helper.array_to_string( (f"-{N}{k}{X}" if len( k ) == 1 else f"--{N}{k}{X}" for k in keys),
                                                delimiter = ", ",
                                                last_delimiter = " or " )
        
        doc = docs( keys[0], f ) if docs is not None else None
        doc = str( doc ) if doc is not None else None
        
        if doc:
            fl = string_helper.first_line( doc.lstrip() )
            p( f" * {branch} - {fl}" )
        else:
            p( f" * {branch}" )
    
    p( ansi.RESET )
    
    return 1


g_program_name = None


def set_program_name( value: str ) -> None:
    global g_program_name
    g_program_name = value


def get_program_name() -> str:
    """
    Gets the program name.
    Unlike argparse this recognises when the program is executed from within Python.
    """
    global g_program_name
    
    if g_program_name is None:
        g_program_name = os.path.basename( sys.argv[0] )
        
        if g_program_name == "__main__.py":
            g_program_name = os.path.basename( os.path.dirname( sys.argv[0] ) )
    
    return g_program_name


def reflect( source: object,
             args: Iterable[str] = None,
             inverse: Union[None, str, bool, Callable] = "",
             exceptions: Sequence[BaseException] = (CliError,),
             interrupts: Sequence[BaseException] = (KeyboardInterrupt,),
             boilerplate: bool = False,
             construct: object = None,
             predefined: Optional[Dict[str, object]] = None,
             help = True,
             epilog = None,
             description_ex: str = None ) -> T:
    """
    Automatically instantiates an `argparse.ArgumentParser` based on a 
    function or class's annotations, then calls the function or instantiates the
    class using the parsed arguments.
    
    Help and argument help is generated from the docstring.
    
    If the main body of the docstring is blank, the documentation of the 
    enclosing module is used instead.
    
    
    
    :param source:     The function or class to reflect upon.
                        
                        This should be a function to call, or a class to
                        construct.
                        
                        Any castable type is supported for the annotations, in
                        addition the following generics are recognised. Note
                        that T is used as the cast for the CLI argument, with
                        any other type variables being ignored:
                        
                        * `Union[T, U, ...]`
                        * `Optional[T]`
                        * `Sequence[T]`
                        
                        .. note::
                        
                            A `list` or `tuple` of items may be passed instead
                            of one. In this case the parameters are merged and
                            the result is a list rather than a single item.
                        
                        .. hint::
                         
                            If you want to reflect upon a class's constructor, 
                            rather than its own annotations, set `source` to 
                            ``MyClass.__init__`` and `construct` to `MyClass`.
                        
    :param args:        Optional arguments to be parsed.
                        Defaults to `sys.argv[1:]`.
    
    :param inverse:     Governs how arguments for boolean yes/no arguments
                        should be generated.
                        This only applies to booleans without defaults or that
                        default to `False`.
                         
                        * True: 
                            * ``--argument/--no_argument``.
                        * Blank:
                            * `--argument value`.
                        * Custom-string
                            * As `True`, but uses this string to format ``--no_argument``.
                        
    :param exceptions:  A list of "safe exceptions". If the function or 
                        constructor raises an exception in this list it is
                        handled, causing the program to close with the error
                        message and help instead of a traceback.
    
    :param interrupts:  A list of "interrupt exceptions". As for `exceptions`,
                        but no help message is displayed. 
                        
    :param boilerplate: Add standard boilerplate calls - sets up logging to the console
                        and installs ansi_format_helper's error hook. May change in future.
                        
    :param construct:   Allows a target in lieu of the provided class or function
                        reflected upon. If the provided class or function is a list,
                        then this *must* be of the same length.
                         
                        .. hint:
                        
                            This might be useful to call an unannotated function
                            by constructing your own annotated protocol.
    
                        * None/False:
                            * The normal mode.
                            * For a function, calls the source verbatim.
                            * For a class, the class is constructed directly,
                              bypassing the constructor. The values are then set
                              using `setattr`.
                        * True:
                            * Special mode for classes. As per the normal mode,
                              but the class is constructed using the default
                              (empty) constructor, prior to using setattr.
                        * callable:
                            The provided object is called, with the reflected kwargs.
                            * e.g. pass the class itself to construct the class using
                                   the constructor, passing the values into the constructor
                                   as `**kwargs`
                                   
    :param predefined:  Dictionary of predefined arguments and/or examples:
    
                        * key:   name of example
                        * value: the arguments, either:
                                 * a string (the command line)
                                 * a dictionary of argument names to values
                                 * a callable returning a dictionary
    
                        These are used for examples and testing - a set of
                        predefined arguments may be used by passing the
                        name of the predefined set as the sole command line
                        argument. Only examples identified by a string are
                        displayed in the help; dictionary or callable arguments
                        are available but not documented.
                        
    :param help:        See `ArgumentParser.add_help(help)`.
    
    :param epilog:      See `help`.
    
    :param description_ex: See `help`.
                            
    :return:            Result of function call.
                        If  
    """
    # Catch exceptions
    if boilerplate:
        from mhelper import exception_hooks
        exception_hooks.install_error_hooks( "CONSOLE" )
    
    #
    # Ensure parameters are always lists
    #
    if not isinstance( source, list ) and not isinstance( source, tuple ):
        r1 = True
        source = source,
    else:
        r1 = False
    
    if not isinstance( construct, list ) and not isinstance( construct, tuple ):
        construct = construct,
    
    assert len( construct ) == len( source ), "`source` and `construct` lengths differ."
    
    #
    # Get documentation
    #
    p = ArgumentParser()
    p.add_help( source = source,
                predefined = predefined,
                description_ex = description_ex,
                epilog = epilog,
                help = help )
    
    #
    # Get param documentation, for each source
    #
    in_use = set()
    is_first = True
    source_to_params = collections.defaultdict( set )
    
    for src in source:
        d = Documentation( src.__doc__ )
        
        if isinstance( src, type ):
            param_docs = d["cvar"]
        else:
            param_docs = d["param"]
        
        #
        # Get annotations
        #
        ssig: Iterable[inspect.Parameter]
        
        if isinstance( src, type ):
            # Class
            ssig = _get_class_sig( src )
        else:
            # Function
            sig = inspect.signature( src )
            ssig = sig.parameters.values()
        
        #
        # Add parameters
        #
        for param in ssig:  # type: inspect.Parameter
            k = param.name
            
            if k == "self":
                continue
            
            a = param.annotation
            d = param.default
            
            assert k not in in_use, f"Parameter {k} is used by more than one source."
            in_use.add( k )
            source_to_params[src].add( k )
            
            if a is param.empty:
                raise RuntimeError( f"Parameter {k!r} is missing annotation, cannot generate CLI arguments." )
            
            if d is param.empty:
                is_required = True
                d = None
            else:
                is_required = False
            
            #
            # Get documentation
            #
            doc = param_docs.get( k, "" )
            
            if not doc.endswith( "." ):
                doc += "."
            
            doc += f"\nType: {string_helper.type_name( type = a )}"
            
            #
            # Get specifier
            #
            if is_first and param.kind != inspect.Parameter.KEYWORD_ONLY:
                # Make the first positional argument the primary
                fk = f"{k}"
                is_positional = True
            else:
                # All other arguments are explicit
                fk = f"--{k}"
                is_positional = False
            
            is_first = False
            
            #
            # Convert
            # Union[..., None] to Union[...] 
            #
            
            if typing.get_origin( a ) is Union:
                argz = list( a.__args__ )
                
                if type( None ) in argz:
                    argz.remove( type( None ) )
                
                a = argz[0]
            
            if typing.get_origin( a ) is collections.abc.Sequence:
                is_sequence = True
                a = a.__args__[0]
            
            else:
                is_sequence = False
            
            if is_sequence:
                nargs = "+" if is_required else "*"
                p.add( fk, action = "store", nargs = nargs, type = a, help = doc, default = [] )
            elif isinstance( a, type ) and issubclass( a, Enum ):
                p.add( fk, action = "store", type = cast( Type[Enum], a ).__getitem__, help = doc, default = d )
            elif a is bool:
                if d is False:
                    p.add( f"--{k}", action = "store_true", help = doc )
                elif inverse:
                    nk = inverse.format( k )
                    
                    if d is False:
                        p.add( f"--{nk}", dest = k, action = "store_false", help = doc )
                    else:
                        group = p.add_mutually_exclusive_group( required = True )
                        p.add( f"--{k}", dest = k, action = "store_true", help = doc, group = group )
                        p.add( f"--{nk}", dest = k, action = "store_false", help = "Converse of --{k}.", group = group )
                else:
                    p.add( fk, action = "store", type = string_helper.string_to_bool, help = doc, required = is_required, default = d )
            else:
                if is_positional:
                    p.add( fk, action = "store", type = a, help = doc, default = d )
                else:
                    p.add( fk, action = "store", type = a, help = doc, required = is_required, default = d )
    
    #
    # Handle choosing from predefined set
    #
    c0 = sys.argv[1].lstrip( "-" ) if sys.argv.__len__() == 2 else None
    
    if predefined is not None and c0 in predefined:
        pdv = predefined[c0]
        
        if callable( pdv ):
            pdv = pdv()
        
        if isinstance( pdv, list ) or isinstance( pdv, tuple ):
            kwargs = p.parse( pdv ).data
        elif isinstance( pdv, str ):
            kwargs = p.parse( pdv.split( " " ) ).data
        elif isinstance( pdv, dict ):
            kwargs = pdv
        else:
            raise exception_helper.type_error( f"predefined[{sys.argv[1]}]", pdv, [str, dict, Callable] )
    else:
        kwargs = p.parse( args ).data
    
    # Catching an empty list is forbidden, so do this
    if not interrupts:  # None or empty list
        interrupts = _AnExceptionClass
    
    if not exceptions:  # None or empty list
        exceptions = _AnExceptionClass
    
    #
    # Execute
    #
    r = []
    
    try:
        for src, con in zip( source, construct ):
            if con in (True, False, None):
                src_pars = source_to_params[src]
                src_args = { k: v for k, v in kwargs.items() if k in src_pars }
                
                if isinstance( src, type ):
                    if con:
                        # TRUE --> Class, ctor, normal call
                        inst = src()
                    else:
                        # FALSE --> Class, direct, normal call
                        # noinspection PyArgumentList
                        inst = src.__new__( src )
                    
                    for key, value in src_args.items():
                        setattr( inst, key, value )
                    
                    r.append( inst )
                else:
                    # Function, normal call
                    # noinspection PyCallingNonCallable
                    r.append( src( **src_args ) )
            else:
                # Custom call
                src_pars = source_to_params[src]
                src_args = { k: v for k, v in kwargs.items() if k in src_pars }
                r.append( con( **src_args ) )
    except exceptions as ex:
        p.print_help()
        print( f"{ansi.FORE_BRIGHT_RED}{ex}{ansi.RESET}", file = sys.stderr )
        print_traceback( ex, "The CLI program got a CliError.", is_verbose = True )
        exit( 1 )
    except interrupts as ex:
        print( f"[{ex.__class__.__qualname__}]", file = sys.stderr )
        print_traceback( ex, "The CLI program got an interrupt.", is_verbose = True )
        exit( 1 )
    except Exception as ex:
        print_traceback( ex, "The CLI program encountered an error." )
        exit( 1 )
    
    if r1:
        return r[0]
    else:
        return r


class _AnExceptionClass( Exception ):
    pass


def execute( *args, **kwargs ):
    """
    Alias of `reflect` with boilerplate code enabled by default.
    Intended to act as the entry point for CLI apps.
    """
    return reflect( *args, boilerplate = True, **kwargs )


def _get_class_sig( klass: Type ) -> List[inspect.Parameter]:
    r = []
    
    for key, value in klass.__annotations__.items():
        r.append( inspect.Parameter( name = key,
                                     kind = inspect.Parameter.KEYWORD_ONLY,
                                     default = getattr( klass, key, inspect.Parameter.empty ),
                                     annotation = value ) )
    
    return r


class ParsedArgs:
    def __init__( self, data: argparse.Namespace ):
        self._legacy = data
        self.data = data.__dict__
    
    
    def __getitem__( self, *args, **kwargs ):
        return self.data.__getitem__( *args, **kwargs )
    
    
    def get( self, *args, **kwargs ):
        return self.data.get( *args, **kwargs )


class ArgWrapper:
    def __init__( self, owner: "ArgumentParser", action: argparse.Action ):
        self.owner = owner
        self.action = action
    
    
    def read( self ):
        return self.owner.parse()[self.action.dest]
    
    
    def __str__( self ):
        return self.action.option_strings[0] if self.action.option_strings else self.action.dest


class _ParseError( Exception ):
    """
    Internal exception raised during parsing failure.
    """
    pass


class _ArgumentParser( argparse.ArgumentParser ):
    """
    Our internal variant of `argparse.ArgumentParser`.
    Pretty much the same, but raises exceptions instead of doing its own stuff. 
    """
    
    
    def error( self, message ):
        raise _ParseError( message )


class ArgumentParser:
    __slots__ = "_parser", "_parsed", "_topics", "_arg_help", "_arg_version", "_groups", "_current_group"
    
    
    def __init__( self ):
        self._parser = _ArgumentParser( formatter_class = cast( Any, argparse.RawTextHelpFormatter ),
                                        add_help = False,
                                        prog = get_program_name() )
        self._parsed: Optional[ParsedArgs] = None
        self._current_group = None
        self._groups = { }
        self._arg_help: Optional[ArgWrapper] = None
        self._arg_version: Optional[ArgWrapper] = None
    
    
    def add_version_argument( self, version: Optional[Union[str, Callable[[], str]]] ) -> None:
        """
        Adds a "--version" argument.
        
        If `_HelpTopicAction` is in use, then the version is added as a help
        topic, and the "--version" argument, whilst still available, is hidden.
        
        :param version: Version text (a `str` or lazy `str`), or a falsy value,
                        for no version text (this call ignored).
                        
        :exception RuntimeError: Already has a version argument 
        """
        if self._arg_version:
            raise RuntimeError( "This parser already has a version argument." )
        
        if not version:
            return
        
        ah = getattr( self._arg_help, "action", None )
        
        if isinstance( ah, _HelpTopicAction ):
            ah.topics["version"] = version
            self._arg_version = self.add( '--version', action = 'version', version = version, help = argparse.SUPPRESS )
        else:
            self._arg_version = self.add( '--version', action = 'version', version = version )
    
    
    def add_help_argument( self, topics: object ) -> None:
        """
        :param topics: Specify one of:
                        * The help text
                            * Specify any `str` or a lazy `str` such as `UsageHelp`. 
                        * No help (this call ignored)
                            * Specify any falsy value, such as `None` or `False`. 
                        * Help topics
                            * Specify a dictionary of help topic names (`str`) to their content (`str` or lazy `str`).
                            
        :exception RuntimeError: Already has a help argument
        """
        if self._arg_help is not None:
            raise RuntimeError( "This parser already has a help argument." )
        
        if not topics:
            return
        
        if isinstance( topics, dict ):
            self._arg_help = self.add( "--help", "-?",
                                       action = _HelpTopicAction,
                                       topics = topics )
        else:
            self._arg_help = self.add( "--help", "-?",
                                       action = _HelpTextAction,
                                       content = topics )
    
    
    def add_module_help( self, module_name, *, description = "", help = True, epilog: Optional[str] = None ):
        warnings.warn( "Deprecated - use add_help", DeprecationWarning )
        return self.add_help( source = module_name,
                              description_ex = description,
                              epilog = epilog,
                              help = help )
    
    
    def add_help( self,
                  *,
                  source: object,
                  predefined: Optional[Dict[str, object]] = None,
                  description_ex: Optional[str] = None,
                  epilog: Optional[str] = None,
                  help = True ):
        """
        Creates a help command.

        :param source:          Function or name of module to obtain documentation from.
                                May be a list or tuple of multiple objects.
        :param predefined:      Dictionary of available predefined arguments (see `reflect`).        
        :param description_ex:  Usage help prefix (before arguments) 
        :param epilog:          Usage help suffix (after arguments)
        :param help:            Optional help topics.
                                `True` -->  No help topics, "--help" displays only the usage help
                                `dict` -->  One or more help topics, displayed by "--help <topic>".
                                            "--help" alone displays the `_DEFAULT_TOPIC`.
                                            If `_DEFAULT_TOPIC` is not already in the dict, it
                                            displays the usage help.
                                `type` --> Uses `dir(type)`, as for `dict`
                                `False` --> No help, ignore this command
        :return: 
        """
        documentations = []
        
        if not isinstance( source, list ) and not isinstance( source, tuple ):
            source = source,
        
        for src in source:
            if isinstance( src, str ):
                module_info = _ModuleInfo( src )
                
                if module_info.description:
                    documentations.append( module_info.description )
            else:
                module_name = getattr( src, "__module__" )
                module_info = _ModuleInfo( module_name )
                
                d = Documentation( src.__doc__ )
                documentation = d[""][""]
                
                if not documentation.strip():
                    if module_info:
                        documentation = module_info.description
                
                if documentation:
                    documentations.append( documentation )
        
        if predefined:
            predef = []
            
            for key, value in predefined.items():
                predef.append( f"%(prog) {key}:\n" )
                
                if isinstance( value, list ) or isinstance( value, tuple ):
                    predef.append( f"    %(prog) {' '.join( value )}" )
                elif isinstance( value, str ):
                    predef.append( f"    %(prog) {value}" )
                elif isinstance( value, dict ):
                    predef.append( f"    {value}" )
                else:
                    predef.append( f"    (internal)" )
            
            if predef:
                documentations.append( "Predefined command lines\n------------------------\n\n{}".format( "\n".join( predef ) ) )
        
        if description_ex:
            documentations.append( description_ex )
        
        description = "\n\n".join( documentations )
        
        usage_help_callable = UsageHelp( self, description, epilog )
        
        if isinstance( help, type ):
            help = { k: getattr( help, k ) for k in dir( help ) if not k.startswith( "_" ) }
        
        if help is True:
            help = usage_help_callable
        elif help is False:
            return
        elif isinstance( help, dict ) and _DEFAULT_TOPIC not in help:
            help[_DEFAULT_TOPIC] = usage_help_callable
            
            if "usage" not in help:
                help["usage"] = help[_DEFAULT_TOPIC]
        
        self.add_help_argument( help )
        
        if module_info:
            self.add_version_argument( module_info.version )
    
    
    def add_module_version( self, module_name, *, version = True ):
        module = _ModuleInfo( module_name )
        
        if version is True:
            version = module.version
        
        self.add_version_argument( version )
    
    
    @property
    def arg_help( self ) -> Optional[ArgWrapper]:
        """
        The help argument created via `add_help_argument`.
        """
        return self._arg_help
    
    
    def add_argument( self, *args, **kwargs ):
        """
        For legacy compatibility with `argparse`.
        Not supported.
        """
        warnings.warn( "Deprecated. Do not rely on compatibility with argparse.", DeprecationWarning )
        self._parser.add_argument( *args, **kwargs )
    
    
    def parse_args( self ) -> argparse.Namespace:
        warnings.warn( "Deprecated. Do not rely on compatibility with argparse.", DeprecationWarning )
        return self.parse()._legacy
    
    
    def add_mutually_exclusive_group( self, required: bool ) -> object:
        """
        Creates a set of mutually exclusive arguments.
        
        :param required: Is at least one argument required.
        :return:         A value suitable for passing to `add(group=)` 
        """
        return self._parser.add_mutually_exclusive_group( required = required )
    
    
    def add_group( self, title: str ) -> None:
        """
        Adds an argument group.
        
        Further arguments will be added to this group by default.
        """
        self._current_group = self._parser.add_argument_group( title )
    
    
    def parse( self, args: Optional[Iterable[str]] = None ) -> ParsedArgs:
        """
        Parses the specified arguments.
        """
        if self._parsed is None:
            try:
                namespace = self._parser.parse_args( args )
            except _ParseError as ex:
                self.print_help()
                
                print( "\n" + ansi.FORE_BRIGHT_RED + ansi.BACK_BLACK + str( ex ) + ansi.RESET, file = sys.stderr )
                exit( 1 )
                assert False
            
            self._parsed = ParsedArgs( namespace )
        
        return self._parsed
    
    
    def add( self, *args, group = None, **kwargs ) -> ArgWrapper:
        if "help" in kwargs:
            if "default" in kwargs:
                d = kwargs['default']
                
                if any( isinstance( d, x ) for x in (int, str, float, bool) ) and d != argparse.SUPPRESS:
                    kwargs["help"] += "\n" + ansi.ITALIC + f"Default: {d!r}" + ansi.ITALIC_OFF
            
            kwargs["help"] = string_helper.highlight_quotes( kwargs["help"], "`", "`", ansi.UNDERLINE, ansi.UNDERLINE_OFF )
        
        if group is None:
            p = self._current_group or self._parser
        elif isinstance( group, argparse._ActionsContainer ):
            p = group
        else:
            p = self._groups.get( group )
            
            if p is None:
                p = self._groups[group] = self._parser.add_argument_group( group )
        
        action = p.add_argument( *args, **kwargs )
        return ArgWrapper( self, action )
    
    
    def print_help( self ):
        """
        Prints the help argument, if any.
        """
        if self._arg_help:
            self._arg_help.action( self._parser, argparse.Namespace(), _DO_NOT_EXIT, None )
        else:
            raise RuntimeError( "Cannot print help because I do not have a help argument." )


def _indent_lines( x, w ):
    return string_helper.indent( f"{ansi.RESET}\n".join( string_helper.wrap( x, 80 ) ), w )


class _HelpTextAction( argparse.Action ):
    
    def __init__( self,
                  option_strings,
                  content,
                  dest = argparse.SUPPRESS ):
        _ = dest
        super().__init__(
                option_strings,
                dest = argparse.SUPPRESS,
                default = argparse.SUPPRESS,
                nargs = 0,
                help = "Show this help message and exit." )
        self.content = content
    
    
    def __call__( self, parser: "ArgumentParser", namespace, values, option_string = None ):
        no_exit = values == _DO_NOT_EXIT
        
        content = self.content
        
        if callable( content ):
            content = content()
        
        assert isinstance( content, str )
        
        print( content, file = sys.stderr )
        
        if not no_exit:
            exit( 0 )


class _HelpTopicAction( argparse.Action ):
    
    def __init__( self,
                  option_strings,
                  topics,
                  dest = argparse.SUPPRESS ):
        _ = dest
        super().__init__(
                option_strings,
                dest = argparse.SUPPRESS,
                default = argparse.SUPPRESS,
                nargs = "?",
                metavar = "TOPIC" )
        self.topics: Dict[str, Union[str, Callable[[], str]]] = { k.lower(): v for k, v in topics.items() }
    
    
    @property
    def help( self ):
        return (f"Shows a help topic, or this message if no topic is specified.\n"
                f"Available topics: {', '.join( sorted( f'`{x.upper()}`' for x in self.topics if x ) )}.")
    
    
    @help.setter
    def help( self, _ ):
        pass
    
    
    def __call__( self, parser: "ArgumentParser", namespace, values: str, option_string = None ):
        no_exit = False
        
        if values == _DO_NOT_EXIT:
            no_exit = True
            values = _DEFAULT_TOPIC
        
        topic_id: str = values or ""
        topic = self.topics.get( topic_id.lower(), None )
        
        if topic is None:
            lst = "\n".join( f" * {topic} " for topic in self.topics )
            print( f"There is no such help topic as '{values.upper()!r}'. "
                   f"Please choose a help topic from the list below.\n\n"
                   f"{lst}\n\n"
                   f"Leave the topic field blank to view the main help page instead.", file = sys.stderr )
            exit()
            return
        
        if not isinstance( topic, str ):
            topic = topic()
        
        print( ansi.BOLD + f"===== HELP - {topic_id} =====" + ansi.RESET, file = sys.stderr )
        print( topic, file = sys.stderr )
        
        if not no_exit:
            exit( 0 )


class UsageHelp:
    def __init__( self,
                  parser: ArgumentParser,
                  description: Optional[str] = None,
                  epilog: Optional[str] = None, ):
        self.parser = parser
        self.description = description
        self.epilog = epilog
    
    
    # noinspection PyProtectedMember
    def __call__( self ):
        pp = self.parser._parser
        r = []
        p = r.append
        
        p( f"{ansi.BOLD}{string_helper.capitalise_first( pp.prog )}:{ansi.BOLD_OFF}" )
        txt = self.description.replace( "%(prog)", pp.prog )
        p( _indent_lines( txt, 4 ) )
        p( "" )
        
        p( f"{ansi.BOLD}Usage:{ansi.BOLD_OFF}" )
        
        # Usage
        u = [pp.prog]
        
        for action in pp._actions:
            if not action.required:
                u.append( "[" )
            
            if action.option_strings:
                u.append( action.option_strings[0] )
            else:
                u.append( action.dest )
            
            u.append( self.__format_metavar( action ) )
            
            if not action.required:
                u.append( "]" )
        
        p( _indent_lines( " ".join( u ), 4 ) )
        p( "" )
        
        for group in pp._action_groups:
            if not group._group_actions:
                continue
            
            p( f"{ansi.BOLD}{string_helper.capitalise_first( group.title )}:{ansi.BOLD_OFF}" )
            for action in group._group_actions:
                help_ = action.help
                
                if help_ is argparse.SUPPRESS:
                    continue
                elif help_ is None:
                    help_ = "Undocumented argument."
                
                assert isinstance( help_, str ), f"Help isn't str or SUPPRESS for {action}"
                
                t = [self.__format_option_str( action ), self.__format_metavar( action )]
                
                p( string_helper.indent( ' '.join( x for x in t if x ), 4 ) )
                p( _indent_lines( help_, 8 ) )
                
                if action.required:
                    p( f"        {ansi.ITALIC}Required{ansi.ITALIC_OFF}" )
                
                p( "" )
        
        return "\n".join( r )
    
    
    @staticmethod
    def __format_option_str( action ):
        if not action.option_strings:
            return ""
        
        long_pos = [x for x in action.option_strings if x.startswith( "--" )]
        short_pos = [x for x in action.option_strings if x.startswith( "-" ) and not x.startswith( "--" )]
        
        S = ansi.BOLD
        N = ansi.BOLD_OFF
        
        if len( long_pos ) == 1 and len( short_pos ) == 1:
            return f"{S}{(N + ' ' + S).join( (*short_pos, *long_pos) )}{N}"
        
        return f"{S}{(N + ' | ' + S).join( action.option_strings )}{N}"
    
    
    @staticmethod
    def __format_metavar( action ):
        u = []
        
        mv = action.metavar or action.dest.upper()
        if action.nargs == "?" or action.nargs is None:
            if mv:
                u.append( f"[{mv}]" )
        elif action.nargs == "*":
            u.append( f"[{mv} ...]" )
        elif action.nargs == "+":
            u.append( f"{mv} [...]" )
        elif action.nargs == 0:
            pass
        elif isinstance( action.nargs, int ):
            if isinstance( mv, list ) or isinstance( mv, tuple ) and len( mv ) == action.nargs:
                u.append( " ".join( mv ) )
            else:
                u.append( mv + " " + " ".join( ".." for _ in range( action.nargs - 1 ) ) )
        else:
            u.append( "nargs=" + str( action.nargs ) )
        
        return " ".join( u )


class _ModuleInfo:
    """
    Obtains information about a module, principally its name, description and version.
    """
    __slots__ = "prog_name", "description", "version"
    
    
    def __init__( self, module_name ):
        module = sys.modules[module_name]
        version = getattr( module, "__version__", None )  #
        
        MAIN_SCRIPT = ".__main__"
        if version is None and module_name.endswith( MAIN_SCRIPT ):
            module_2_name = module_name[:-len( MAIN_SCRIPT )]
            module_2 = sys.modules[module_2_name]
            version = getattr( module_2, "__version__", None )
            date = getattr( module_2, "__date__", '' )
            
            if isinstance( date, tuple ) or isinstance( date, list ):
                date = '-'.join( str( x ) for x in date if date )
            
            if date:
                version += f". ({date})"
            
            extra = [getattr( module_2, "__author__", '' ),
                     getattr( module_2, "__license__", '' ),
                     getattr( module_2, "__copyright__", '' )
                     ]
            
            sv = str( sys.version ).replace( "\n", "" )
            module_2_name = string_helper.capitalise_first_and_fix( module_2_name )
            author = ". ".join( str( x ) for x in extra if x )
            if author:
                author += ".\n"
            version = f"{module_2_name} {version}.\n{author}Using Python {sv} at {sys.executable}"
        
        self.description = string_helper.strip_lines_to_first( module.__doc__ )
        self.version = version


# region Deprecated

def args_to_function( *args, **kwargs ):
    warnings.warn( "Deprecated - use `reflect`", DeprecationWarning )
    return execute( *args, **kwargs )

# endregion
