"""
Provides pretty formatting of standard types for Jupyter notebooks.
"""
# !EXPORT_TO_README
import datetime
from html import escape







def add_handlers():
    CSS = """
    @import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');
    @import url(https://fonts.googleapis.com/css?family=Indie+Flower);
    
    div.jupyter-widgets-output-area div.output_scroll
    {
        height: 100%;
    }
    
    div.text_cell_render h1
    {
        font-size: 20px;
    }
    
    /* headings. h1 is the title. p is the subtitle and should look like it */
    div.text_cell_render h1 + p
    {
        font-size: 18px;
        color: #404040;
        font-weight: normal;
        letter-spacing: 1px;
    }
    
    div.text_cell_render p
    {
        font-size: 16px;
    }
    
    /* Markdown cells look like paper */
    div.text_cell_render
    {
        position:relative;
        line-height: 25px;
        font-family: 'Indie Flower';  
        padding-left: 52px;
    }
    
    div.text_cell_render::before 
    {
        content: '';
        position: absolute;
        left: 45px;
        height: 100%;
        width: 2px;
        background: rgba(255,0,0,0.4);
    }
    
    div.rendered_html
    {
        letter-spacing: 0.5px;
    }
    
    .rendered_html:hover
    {
        outline: 1px dotted cornflowerblue;
        z-index: 9999;
    }
    
    /* Make interactive areas more obvious */
    div.output_wrapper > div.output > div.output_area > div.output_subarea
    {
        background-color: #F0F0F0;  
        background-image: linear-gradient(135deg, hsla(0,0%,0%,0), hsla(0,0%,0%,.05) );
        background-size: 1px 5px;
        border: none;
    }
    
    div.jupyter-widgets-output-area.output_wrapper > div.output > div.output_area > div.output_subarea
    {
        background-color: #D0D0D0;  
        background-image: linear-gradient(135deg, hsla(0,0%,0%,0), hsla(0,0%,0%,.05) );
        background-size: 5px 5px;
        border: none;
    }
    
    div.output_wrapper > div.output > div.output_area > div.output_subarea.jupyter-widgets-view
    {
        background-color: #E0E0E0;  
        background-image: linear-gradient(135deg, hsla(0,0%,0%,0), hsla(0,0%,0%,.05) );
        background-size: 5px;
        border: none;
    }
    
    div.jupyter-widgets-output-area
    {
        background: rgba(0,0,0,0.5);
        background-image: none;
    }
    
    button.jupyter-button
    {
        border-radius: 0;
        background: rgba(255,255,255,0.5);
        border: none;
        font-weight: bold;
    }
    
    button.jupyter-button:enabled:hover
    {
        border-radius: 0;
        background: rgba(255,255,255,0.75);
        border: none;
        font-weight: bold;
    }
    
    /* Normally, collapsed output is barely noticeable, make it more noticeable */
    div.output_collapsed
    {
        border: 1px outset silver;
        background: silver;
    }

    /* This is the var-box used by the formatters here */
       
    .var_box_name
    {
        border-top-left-radius: 8px;
        border-bottom-left-radius: 8px;
        border: 1px solid silver;
        background: #EEEEEE;
        color: #404040;
        padding: 4px;
        font-weight: bold;
        margin-right: 4px;
    }    
        
    div.output_stream pre
    {
        font-family: 'VT323', monospace;
        background: rgba(0,0,0,0.75);
        color: #00FF00;
        padding: 4px;
        font-size: 18px;
        filter: blur(0.5px);
        margin: 0;
    }
    
    div.output_stream.output_stderr pre
    {
        color: #80FF00;
    }
    """
    
    MAX_DISPLAY = 500
    
    
    def int_formatter( obj ):
        vn = escape( type( obj ).__name__ )
        vv = escape( str( obj ) )
        
        html = []
        html.append( "<div class='var_box'>" )
        html.append( "<span class='var_box_name'>" )
        html.append( vn )
        html.append( "</span>" )
        html.append( "<span class='var_box_value'>" )
        html.append( vv )
        html.append( "</span>" )
        html.append( "</div>" )
        
        return "".join( html )
    
    
    def dict_formatter( obj ):
        html = []
        html.append( "<table>" )
        html.append( f"<thead><tr><th colspan=3><var>{type( obj ).__name__}</var> of {len( obj )} items</th></tr>" )
        html.append( "<tr>" )
        html.append( "<th>Index</th>" )
        html.append( "<th>Key</th>" )
        html.append( "<th>Value</th>" )
        html.append( "</tr></thead>" )
        
        for i, (key, value) in enumerate( obj.items() ):
            if i >= MAX_DISPLAY:
                __append_dots( html, 3 )
                break
            
            html.append( "<tr>" )
            html.append( "<td>{0}</td>".format( i ) )
            html.append( "<td>{0}</td>".format( escape( str( key ) ) ) )
            html.append( "<td>{0}</td>".format( escape( str( value ) ) ) )
            html.append( "</tr>" )
        html.append( "</table>" )
        
        return "".join( html )
    
    
    def __append_dots( html, num_cols ):
        html.append( "<tr>" )
        for _ in range( num_cols ):
            html.append( "<td>...</td>" )
        html.append( "</tr>" )
    
    
    def list_formatter( obj ):
        html = []
        html.append( "<table>" )
        html.append( f"<thead><tr><th colspan=2><var>{type( obj ).__name__}</var> of {len( obj )} items</th></tr>" )
        html.append( "<tr>" )
        html.append( "<th>Index</th>" )
        html.append( "<th>Value</th>" )
        html.append( "</tr></thead>" )
        
        for i, value in enumerate( obj ):
            if i >= MAX_DISPLAY:
                __append_dots( html, 2 )
                break
            
            html.append( "<tr>" )
            html.append( "<td>{0}</td>".format( i ) )
            
            if isinstance( value, list ) or isinstance( value, tuple ):
                for cell in value:
                    html.append( "<td>{0}</td>".format( escape( str( cell ) ) ) )
            else:
                html.append( "<td>{0}</td>".format( escape( str( value ) ) ) )
            html.append( "</tr>" )
        
        html.append( "</table>" )
        
        return "".join( html )
    
    
    # noinspection PyPackageRequirements
    import IPython
    ip = IPython.get_ipython()
    
    formatter = ip.display_formatter.formatters['text/html']
    
    DICT_TYPES = { dict }
    LIST_TYPES = { list, tuple, set, frozenset, type( { }.keys() ), type( { }.values() ) }
    BASIC_TYPES = { int, float, bool, str, type( None ) }
    ALL_TYPES = set.union( LIST_TYPES, BASIC_TYPES )
    
    for ty in DICT_TYPES:
        formatter.for_type( ty, dict_formatter )
    
    for ty in LIST_TYPES:
        formatter.for_type( ty, list_formatter )
    
    for ty in BASIC_TYPES:
        formatter.for_type( ty, int_formatter )
    
    from mhelper.exception_hooks import install_error_hooks, EHook
    install_error_hooks( EHook.JUPYTER )
    
    ts = ', '.join( f"<code>{x.__name__}</code>" for x in ALL_TYPES )
    time = datetime.datetime.now().strftime( "%Y-%m-%d %H:%M" )
    __display( __HTML( f"<style>{CSS}</style>The current time is {time}." ) )
    __display( __HTML( f"The <code>MHelper</code> formatter has been enabled: {ts}" ) )


def load_source( path_to_file, module_name = None ):
    if module_name is None:
        import os
        module_name = os.path.basename( os.path.dirname( path_to_file ) ) + "." + os.path.splitext( os.path.basename( path_to_file ) )[0]
    
    import importlib.util
    spec = importlib.util.spec_from_file_location( module_name, path_to_file )
    module = importlib.util.module_from_spec( spec )
    spec.loader.exec_module( module )
    return module


def restart_kernel():
    __display_html( "<script>Jupyter.notebook.kernel.restart()</script>", raw = True )


def rst( x ):
    from mhelper.rst_helper import rst_to_html_fragment
    __display_html( rst_to_html_fragment( x ) )


def download_file( file_name: str ) -> None:
    import os
    # noinspection PyPackageRequirements
    from IPython.display import FileLink
    
    if not os.path.isfile( file_name ):
        __display( __HTML( f"This file doesn't exist: {file_name}" ) )
        return
    
    base_name: str = os.path.basename( file_name )
    k_info_file: str = ".download_file_info.txt"
    
    # Remove previous link
    if os.path.isfile( k_info_file ):
        with open( k_info_file, "r" ) as fin:
            previous_file = fin.read()
        
        if os.path.isfile( previous_file ):
            __display( __HTML( f"Removed previous file link: {previous_file}" ) )
            os.remove( previous_file )
    
    # Remember current link
    with open( k_info_file, "w" ) as fout:
        fout.write( base_name )
    
    # Create the link
    if os.path.isfile( base_name ):
        __display( __HTML( f"There is already a file with this name: {base_name}" ) )
        return
    
    os.symlink( file_name, base_name )
    
    # Return the link
    __display( FileLink( base_name ) )


def __display( *args, **kwargs ):
    # noinspection PyPackageRequirements
    from IPython.core.display import display
    display( *args, **kwargs )


def __display_html( *args, **kwargs ):
    # noinspection PyPackageRequirements
    from IPython.core.display import display_html
    display_html( *args, **kwargs )


def __HTML( *args, **kwargs ):
    # noinspection PyPackageRequirements
    from IPython.core.display import HTML
    return HTML( *args, **kwargs )


g_cache_mode = "rwx"


def set_cache_mode( x: str ) -> None:
    """
    Sets the cache mode.
    
    e.g. 
    
    * "rwx" effectively enables the cache.
    * "x" disables the cache.
    * "d" deletes entries from the cache as they are encountered.
    * "rxd" is the same as "d", but produces viable return values, either from
      the cache before it is deleted, or computed.
    
    :param x: Zero or more flags:
    
              * "r" - read cache values
              * "w" - write cache values (ignored if "x" is not set)
              * "x" - execute function (if not set result is always `None`)
              * "d" - delete cache values
              
              "+" and "-" prefixes are permitted to modify the current mode. 
    """
    global g_cache_mode
    
    if x.startswith( "+" ):
        x = "".join( set.union( set( x[1:] ), set( g_cache_mode ) ) )
    elif x.startswith( "-" ):
        x = "".join( set.difference( set( g_cache_mode ), set( x[1:] ) ) )
    
    assert all( v in "rwxd" for v in x )
    
    g_cache_mode = x
    __display_html( f"Cache mode set to <tt>{x}</tt>." )


def dcache( fun ):
    """
    Disk-cached function (decorator-like usage).
    See also `set_cache_mode`. 
    
    Assumed to be executed from Jupyter, this caches to a subdirectory of the
    current folder.
    """
    
    
    def decorated( *args, **kwargs ):
        from mhelper.string_helper import string_to_hash, format_size, timedelta_to_string
        from mhelper.io_helper import load_binary, save_binary
        from html import escape as _escape
        import time
        import os
        
        def escape( x ):
            return f"<tt>{_escape( x )}</tt>"
        
        
        def efn( xx ):
            legit = set( "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-_ .,#@~()" )
            return "".join( x if x in legit else "~" for x in xx )
        
        
        sig = f"{fun.__qualname__}( *{args!r}, **{kwargs!r} )"
        html_sig = escape( sig )
        
        if "at 0x" in sig:
            raise RuntimeError( f"Cannot cache a non-`repr`able function: {sig}" )
        
        hash = string_to_hash( sig )
        sentinel = object()
        start = time.perf_counter()
        
        directory = "mhelper.jupyter_helper.dcache"
        
        if not os.path.isdir( directory ):
            os.mkdir( directory )
        
        name = efn( sig[:100] ) + "~" + hash
        path = os.path.join( directory, name ) + ".pkl"
        html_path = escape( path )
        
        if os.path.isfile( path ) and "r" in g_cache_mode:
            sz = escape( format_size( os.path.getsize( path ) ) )
            tm = escape( timedelta_to_string( time.perf_counter() - start ) )
            result = load_binary( path, default = sentinel )
            
            if result is not sentinel:
                __display( __HTML( f"Loaded from cache {html_sig} --> {html_path} ({sz}, {tm})." ) )
                return result
        
        if "x" in g_cache_mode:
            result = fun( *args, **kwargs )
            
            if "w" in g_cache_mode:
                save_binary( path, result )
                sz = escape( format_size( os.path.getsize( path ) ) )
                tm = escape( timedelta_to_string( time.perf_counter() - start ) )
                __display( __HTML( f"Saved to cache {html_sig} --> {html_path} ({sz}, {tm})." ) )
        else:
            result = None
        
        if "d" in g_cache_mode:
            if os.path.isfile( path ):
                os.remove( path )
                __display( __HTML( f"Deleted cache {html_sig} --> {html_path}." ) )
        
        return result
    
    
    return decorated


def arbitrary( *args, **kwargs ):
    return f"ARBITRARY{args}{kwargs}"
