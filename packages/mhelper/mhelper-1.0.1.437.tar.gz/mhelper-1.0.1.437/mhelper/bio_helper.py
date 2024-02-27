"""
Functions for parsing and dealing with bioinformatics data formats.

Notably a FASTA parser that can deal with the various FASTA variations.
"""
# !EXPORT_TO_README
import csv
import re
from io import StringIO
from itertools import chain
from typing import Iterator, Tuple, Iterable, Union, Callable, TypeVar, Mapping, Sequence


_BIOPYTHON_FIX = re.compile( "([0-9.]+):[0-9.]+" )

T = TypeVar( "T" )


def make_fasta( array: Union[Mapping[str, str], Iterable[Union[T, str, Tuple[str, str]]]],
                key: Callable[[T], str] = None,
                value: Callable[[T], str] = None ) -> str:
    """
    Formats data as Fasta.
    
    :param array:       Sequences, either an:
            
                        * iterable of key-value (name-sequence) pairs
                        * an iterable of values (sequences alone) - they will be given arbitrary names
                        * an iterable of `T` - use the `key` and `value` arguments to define the content.
                        * a `dict` (whose `items` shall be invoked, as for key-value)
                        
    :param key:         How to obtain peptide keys (names) from list elements, if array elements are `T`. 
    :param value:       How to obtain peptide keys (names) from list elements, if array elements are `T`. 
    :return:            Fasta, as a string. An empty string if there are no sequences.
    """
    if isinstance( array, Mapping ):
        array = array.items()
    
    it = iter( array )
    
    try:
        first = next( it )
    except StopIteration:
        # No elements
        return ""
    
    r = []
    
    if isinstance( first, str ):
        if key is None:
            key = lambda x: f"A{len( r ) // 2}"
        
        if value is None:
            value = lambda x: x
    else:
        if key is None:
            key = lambda x: x[0]
        
        if value is None:
            value = lambda x: x[1]
    
    for element in chain( (first,), it ):
        key_ = key( element )
        value_ = value( element )
        r.append( f">{key_}" )
        r.append( value_ )
    
    return "\n".join( r )


def convert_file( in_filename, out_filename, in_format, out_format ):
    from Bio import AlignIO
    
    with open( in_filename, "rU" ) as input_handle:
        with open( out_filename, "w" ) as output_handle:
            alignments = AlignIO.parse( input_handle, in_format )
            AlignIO.write( alignments, output_handle, out_format )


def parse_phylip( *, text = None, file = None, lines = None, ignore_num_seq: bool = False ) -> Iterator[Tuple[str, str]]:
    """
    Same as :function:`parse_fasta`, but for PHYLIP.
    """
    lines = __read_file( file, text, lines )
    
    heading = [x for x in lines[0].split( " " ) if x]
    count = int( heading[0] )
    length = int( heading[1] )
    num = 0
    
    for index, line in enumerate( lines[1:] ):
        if not line:
            continue
        
        if "\t" not in line:
            raise ValueError( "This PHYLIP file is invalid because I don't understand the line #«{}», «{}»".format( index, line ) )
        
        name, value = line.split( "\t", 1 )
        name = name.strip()
        value = value.strip()
        
        if len( value ) != length:
            raise ValueError( "This PHYLIP file is invalid because sequence #«{}» («{}») is «{}» sites long but the header stipulates «{}» sites.".format( index, name, len( value ), length ) )
        
        num += 1
        yield name, value
    
    if not ignore_num_seq and num != count:
        raise ValueError( "This PHYLIP file is invalid because it contains «{}» sequences but the header stipulates «{}».".format( num, count ) )


def parse_tsv( file: str, header = False ) -> Iterator[Sequence[str]]:
    with open( file ) as fin:
        r = csv.reader( fin, delimiter = "\t" )
        
        if header:
            headers = next( r )
        else:
            headers = None
        
        for row in r:
            yield row


def parse_fasta( *, allow_empty = True, **kwargs ) -> Iterator[Tuple[str, str]]:
    """
    Parses a FASTA file.
    
    * Accepts multi-line sequences.
    * Accepts ';' comments in the file.
    * Ignores flanking whitespace.
    * Ignores flanking numbers and padding asterisks in sequences.
    * Ignores spaces in sequences.
    
    ..
    
    note::
     
        BioPython's SeqIO.parse doesn't handle comments for FASTA.
    
    :param kwargs:  Specify text  = FASTA text 
                            file  = Path to FASTA file 
                            lines = FASTA lines
                            
    :return:        Tuples of sequence names and sites 
    """
    lines = __read_file( kwargs )
    
    heading = None
    sequence = []
    
    for line in lines:
        line = line.strip()
        
        if line.startswith( ">" ):
            if heading is not None:
                sq = "".join( sequence )
                assert allow_empty or sq, "Empty sequences forbidden."
                yield heading, sq
            
            heading = line[1:]
            sequence = []
        elif not line.startswith( ";" ):
            line = line.strip( "0123456789*" )
            line = line.replace( " ", "" )
            line = line.replace( "\t", "" )
            sequence.append( line )
    
    if heading is not None:
        sq = "".join( sequence )
        assert allow_empty or sq, "Empty sequences forbidden."
        yield heading, sq


def __read_file( kw ) -> Sequence[str]:
    if len( kw ) != 1:
        raise ValueError( "One input and only one input must be provided." )
    
    key, value = next( iter( kw.items() ) )
    
    if key == "file":
        from mhelper import file_helper
        result = file_helper.read_all_lines( value )
    elif key == "text":
        result = value.split( "\n" )
    elif key == "lines":
        result = value
    else:
        raise ValueError( "Must specify either :param:`file`, :param:`text` or :param:`lines` when calling :function:`__read_file`." )
    
    if not result:
        raise ValueError( "Cannot read the input because there is no data.\n"
                          f"{kw}" )
    
    return result


def biotree_to_newick( tree ) -> str:
    from Bio.Phylo.BaseTree import Tree
    tree: Tree
    
    handle = StringIO()
    Phylo.write( [tree], handle, "newick" )
    result = handle.getvalue()
    
    # Work around stupid BioPython bug
    # https://github.com/biopython/biopython/issues/1315
    # TODO: Remove this fix when the issue is fixed
    result = _BIOPYTHON_FIX.sub( "\\1", result )
    
    return result


def newick_to_biotree( newick ):
    from Bio import Phylo
    from Bio.Phylo.BaseTree import Tree
    handle = StringIO( newick )
    r: Tree = Phylo.read( handle, "newick" )
    return r
