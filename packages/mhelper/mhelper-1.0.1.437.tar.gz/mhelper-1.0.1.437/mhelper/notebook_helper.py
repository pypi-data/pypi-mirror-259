"""
This is for Jupyter notebooks.
"""
import functools
import random
import sys
import time
from collections import Counter
from functools import partial
from typing import Callable, FrozenSet, List, Optional, Sequence, Set, TypeVar, Union, Any, Dict, Tuple, Protocol, Container
import math
import statistics
import html
from itertools import chain

from mhelper import io_helper, string_helper, state_helper, exception_formatter
from mhelper.accuracy_helper import ConfusionMatrix
from mhelper.jupyter_helper import add_handlers
from mhelper.location_helper import find_file

from mhelper.special_types import ArgsKwargs
from mhelper.property_helper import cached

from mhelper.bio_requests.uniprot_proteins import uniprot_proteins as uniprot

# noinspection PyPackageRequirements
from ipywidgets import interact, widgets
# noinspection PyPackageRequirements
import matplotlib
# noinspection PyPackageRequirements
import matplotlib.figure
# noinspection PyPackageRequirements
from matplotlib import pyplot
# noinspection PyPackageRequirements
import seaborn
# noinspection PyPackageRequirements
import pandas
# noinspection PyPackageRequirements
import scipy
# noinspection PyPackageRequirements
import numpy
# noinspection PyPackageRequirements
from IPython.core.display import HTML, Markdown, Image
# noinspection PyPackageRequirements
from IPython import get_ipython


TClass = TypeVar( "TClass" )

__all__ = [
    # Reexport
    "matplotlib", "pyplot", "seaborn", "pandas", "statistics", "scipy", "math", "numpy", "interact", "widgets", "chain",
    
    # Reexport (mine)
    "find_file", "add_handlers", "uniprot", "ConfusionMatrix",
    
    # Functions - plotting and display
    "new_plot", "hprint", "mprint", "minteract", "figure", "repr_ipython", "mview", "tprint", "Namespace", "get_fimp",
    
    # Functions - machine learning
    "DataSet", "ClassificationSet", "Regression", "ESpeed", "get_classifier_classes", "test_all_classifiers",
    
    # Constants
    "NAN",
    ]

NAN = float( "nan" )


def new_plot( title: str = "",
              *,
              caption: str = None,
              **kwargs
              ) -> matplotlib.figure.Axes:
    """
    Boilerplate code for creating a `pyplot`-like plot without reliance on its
    stateful model.
     
    :param title:       Plot title, optional 
    :param caption:     Plot caption (used only by the `figure` command below,
                        but specifying it along with the `title` here may be
                        more convenient)
    :param kwargs:      Figure constructor arguments 
    :return:            Axis (the plot) 
    """
    caption = f". {caption}" if caption else ""
    # mprint( f"**Figure**: *{title}* {caption}" )
    
    fig: matplotlib.figure.Figure = matplotlib.figure.Figure( **kwargs )
    axis: matplotlib.figure.Axes = fig.add_subplot()
    
    # Add the title
    axis.set_title( title )
    
    fig.mjr_title = title
    fig.mjr_caption = caption
    
    return axis


class DataSet:
    def __init__( self,
                  x: pandas.DataFrame,
                  y: Union[pandas.DataFrame, Sequence[object]],
                  *,
                  name: str = "dataset",
                  x_name: str = "x",
                  y_name: str = "y" ):
        """
        :param x:        A pandas data-frame describing the data.
                         a.k.a. Data, independent variables, input vectors 
        :param y:        A pandas dataframe or a list of objects corresponding
                         to each row (see `get_attr`).
                         a.k.a. Metadata, dependent variables, response vectors 
        """
        self.x = x
        self.y = y
        self.name = name
        self.x_name = x_name
        self.y_name = y_name
        self.num_classes = len( set( self.y ) )
        
        assert len( self.x ) == len( self.y )
    
    
    def split( self,
               p_training: float = 0.8,
               stratify: bool = None,
               random_state: int = 1
               ):
        """
        Splits into training and validation sets.
        
        :param p_training:      Training proportion. 
        :param stratify:        If present, the training and validation sets
                                will be constructed to maintain the same
                                proportions of each class.
                                Note that the response vector must be discrete
                                for this to work. 
        :param random_state:     random seed
        :return: 
        """
        training_i: List[int]
        validation_i: List[int]
        
        training_i = []
        validation_i = []
        
        if stratify is None:
            stratify = self.num_classes == 2
        
        if stratify:
            klasses: FrozenSet[TClass] = frozenset( self.y )
            
            for klass in klasses:
                self.__add_vector( p_training, random_state, training_i, validation_i, lambda x: x == klass )
        else:
            self.__add_vector( p_training, random_state, training_i, validation_i, lambda _: True )
        
        assert not set.intersection( set( training_i ), set( validation_i ) )
        
        return ClassificationSet( self.subset( training_i, name = f"{self.x_name}::Tr" ),
                                  self.subset( validation_i, name = f"{self.x_name}::Vl" ),
                                  name = self.name )
    
    
    def __add_vector( self, p_training, random_seed, training_i, validation_i, predicate ):
        indices = [i for i in range( self.nobs ) if predicate( self.y[i] )]
        
        generator = random.Random( random_seed )
        generator.shuffle( indices )
        
        n_training = int( (len( indices ) * p_training) + 0.5 )
        
        training_i += indices[:n_training]
        validation_i += indices[n_training:]
    
    
    def breakdown( self ):
        """
        Returns the class breakdown of count(X):Y 
        """
        return Counter( self.y )
    
    
    def subset( self,
                row_indices: Sequence[int],
                name: str = None ) -> "DataSet":
        """
        Subsets the dataset by observation/row.
        """
        if name is None:
            name = f"{self.x_name}::Ss"
        
        assert len( row_indices ) <= self.nobs
        assert len( row_indices ) == len( frozenset( row_indices ) )
        
        data_ss = self.x.iloc[row_indices, :]
        
        if isinstance( self.y, pandas.DataFrame ):
            meta_ss = self.y.iloc[row_indices, :]
        else:
            meta_ss = [self.y[i] for i in row_indices]
        
        return DataSet( data_ss, meta_ss, name = name, x_name = self.x_name, y_name = self.y_name )
    
    
    def for_attr( self, attr: str ) -> "DataSet":
        """
        Returns a new dataset with the meta-data focused on one attribute.
        See `get_attr`.
        """
        return DataSet( x = self.x,
                        y = self.get_attr_vector( attr ),
                        name = self.name,
                        x_name = self.x_name,
                        y_name = attr )
    
    
    def get_attr_vector( self, attr: str ) -> List[object]:
        """
        See `get_attr`.
        """
        if isinstance( self.y, pandas.DataFrame ):
            return list( self.y[attr] )
        else:
            return [getattr( x, attr ) for x in self.y]
    
    
    def get_attr( self, attr: str, index: int ) -> object:
        """
        Gets a meta-data attribute.
        
        :param attr:    The attribute to get.
                        If the meta-data is a pandas DataFrame, this is the column name.
                        If the meta-data is a vector, this is the field or attribute name.
        :param index:   Index of the row to get the attribute for. 
        :return:        Meta-data value.                                                    
        """
        if isinstance( self.y, pandas.DataFrame ):
            return self.y[attr][index]
        else:
            return getattr( self.y[index], attr )
    
    
    @property
    def nobs( self ):
        return self.x.shape[0]
    
    
    @property
    def nvars( self ):
        return self.x.shape[1]
    
    
    @property
    def nmetavars( self ) -> int:
        if isinstance( self.y, pandas.DataFrame ):
            return self.y.shape[1]
        else:
            return 0
    
    
    @property
    def metavardesc( self ) -> str:
        mv = self.nmetavars
        if mv:
            return f"{mv:,}"
        else:
            return type( self.y[0] ).__name__
    
    
    def __repr__( self ):
        return f"{self.name!r} - Dataset of {self.nobs:,} observations. {self.nvars:,} variables, with {self.metavardesc} meta-data fields."
    
    
    def _repr_html_( self ):
        return f"{self.name!r} - <b>Dataset</b> of <em>{self.nobs:,}</em> observations. <em>{self.nvars:,}</em> variables, with <em>{self.metavardesc}</em> meta-data fields."


class ClassificationSet:
    def __init__( self, training: DataSet, validation: DataSet, name = None ):
        self.training: DataSet = training
        self.validation: DataSet = validation
        self.name = name or training.name
        
        assert self.training.nvars == self.validation.nvars
        assert self.training.nmetavars == self.validation.nmetavars
        assert self.training.y_name == self.validation.y_name
    
    
    @property
    def y_name( self ):
        return self.training.y_name
    
    
    def __repr__( self ):
        return f"{self.name!r} - Split dataset comprising {self.training.nobs:,} training and {self.validation.nobs:,} validation observations. {self.training.nvars:,} variables, with {self.training.metavardesc} meta-data fields."
    
    
    def _repr_html_( self ):
        return f"{self.name!r} - <b>Split</b> comprising <em>{self.training.nobs:,}</em> training and <em>{self.validation.nobs:,}</em> validation observations. <em>{self.training.nvars:,}</em> variables, with <em>{self.training.metavardesc}</em> meta-data fields."
    
    
    def for_attr( self, attr: str ) -> "ClassificationSet":
        return ClassificationSet( self.training.for_attr( attr ),
                                  self.validation.for_attr( attr ),
                                  f"{self.name}::{attr}" )


# noinspection PyPackageRequirements
class Regression:
    """
    Simply boilerplate code for performing regressions and classifications 
    using sklearn and plotting the results in Jupyter.
    
    Use `Regression.fit` to generate such objects.
    """
    
    
    def __init__( self,
                  *,
                  regression,
                  dataset: Union[DataSet, ClassificationSet],
                  class_type,
                  scores,
                  actual,
                  predicted_raw,
                  predicted,
                  sources,
                  confusion_matrix: ConfusionMatrix,
                  exception = None ):
        """     
        The "response" is Y, i.e. the dependent variable or class.
        
        :param dataset:             Set used to train and validate. 
        :param regression:          An sklearn-like regression or classification model. 
        :param class_type:          Type of `actual` and `predicted_class`.
                                    Typically `int` for classification and `float` for regression.
        :param actual:              Actual Y. 
        :param scores:              Transformation (`None` for pure classification). 
        :param predicted_raw:       Absolute predicted values. 
        :param predicted:           Reinterpreted predicted classes.
                                    This is usually the same as `predicted`, however for models such
                                    as regression-as-classification the raw values require rounding
                                    to obtain the class prediction.
        :param sources:             The vector of the origin set for each `actual` or `predicted`
                                    element. `True` for validation, `False` for training.
        :param confusion_matrix:    Confusion matrix, for validation set only.
        """
        self.dataset = dataset
        self.regression = regression
        self.class_type = class_type
        
        self.actual = actual
        self.predicted = predicted_raw
        self.predicted_class = predicted
        self.sources = sources
        
        self.scores = scores
        
        self.confusion_matrix = confusion_matrix
        self.exception = exception
    
    
    @property
    def reg_name( self ):
        return self.regression.__class__.__name__
    
    
    @property
    def x_name( self ):
        return self.dataset.x_name
    
    
    @property
    def y_name( self ):
        return self.dataset.y_name
    
    
    @staticmethod
    def fit( regression,
             dataset: Union[DataSet, ClassificationSet],
             prt = True,
             random_state: int = 1,
             catch: bool = False ) -> "Regression":
        """
        Fits a dataset to a model and wraps up the results.
        
        :param random_state: random state 
        :param regression:  * An sklearn-like regression model.
                            * An sklearn-like classification model.
                            * A string denoting one of the inbuilt values:
                              "plsr", "pca"
        :param dataset:     A `DataSet` to train on and predict against, or
                            a `ClassificationSet` comprising training and
                            validation subsets. 
        :param prt:         Predict training values as well.
        :return:            A `Regression` object describing the model and
                            results. 
        """
        # Create our validation set
        if isinstance( dataset, ClassificationSet ):
            all_x = dataset.validation.x
            all_ay = dataset.validation.y
            all_src = [True for _ in dataset.validation.y]
            
            if prt:
                all_x = concatenate( all_x, dataset.training.x )
                all_ay = concatenate( all_ay, dataset.training.y )
                all_src += [False for _ in dataset.training.y]
            
            train_on = dataset.training
        else:
            all_x = dataset.x
            all_ay = dataset.y
            all_src = [True for _ in dataset.y]
            
            train_on = dataset
        
        if isinstance( regression, str ):
            regression = Regression.__resolve_name( regression )
        
        class_type = type( train_on.y[0] )
        
        if class_type is numpy.float64:
            class_type = float
        
        # Fit the model on the training data
        numpy.random.seed( random_state )
        numpy.random.default_rng( random_state )
        
        try:
            regression.fit( train_on.x, train_on.y )
        except Exception as ex:
            if not catch:
                raise
            
            return Regression( regression = regression,
                               dataset = dataset,
                               scores = None,
                               actual = all_ay,
                               class_type = class_type,
                               predicted_raw = None,
                               predicted = None,
                               sources = all_src,
                               confusion_matrix = None,
                               exception = ex )
        
        if hasattr( regression, "transform" ):
            scores = regression.transform( all_x )
        else:
            scores = None
        
        if hasattr( regression, "predict" ):
            all_py = regression.predict( all_x )
            
            if class_type is int:
                all_pc = [int( x + 0.5 ) for x in all_py]
            else:
                all_pc = all_py
            
            assert len( all_py ) == len( all_ay ) == len( all_src )
            
            cm = ConfusionMatrix.from_predictions( (p, a)
                                                   for p, a, s
                                                   in zip( all_py, all_ay, all_src )
                                                   if s )
        else:
            all_py = None
            all_pc = None
            cm = None
        
        return Regression( regression = regression,
                           dataset = dataset,
                           scores = scores,
                           actual = all_ay,
                           class_type = class_type,
                           predicted_raw = all_py,
                           predicted = all_pc,
                           sources = all_src,
                           confusion_matrix = cm )
    
    
    @staticmethod
    def __resolve_name( regression ):
        if regression == "plsr":
            from sklearn.cross_decomposition import PLSRegression
            return PLSRegression( n_components = 5 )
        elif regression == "pca":
            from sklearn.decomposition import PCA
            return PCA( n_components = 5 )
        elif regression == "pca":
            from sklearn.decomposition import PCA
            return PCA( n_components = 5 )
        else:
            raise KeyError( regression )
    
    
    def plot_predicted( self ):
        """
        Makes a predicted-v-actual plot.
        """
        hprint( "<h4>Versus density plot</h4>" )
        
        if self.class_type is not int:
            hprint( "Not making the plot because this is not classification." )
            return
        
        if self.predicted is None:
            hprint( "Not making the plot because this is not prediction." )
            return
        
        import matplotlib
        from matplotlib import lines
        plt = new_plot( f"{self.x_name}: {self.reg_name} predicted v. actual {self.y_name}" )
        
        actual = self.__sub( self.actual )
        predicted = self.__sub( self.predicted )
        
        klasses = set( actual )
        
        mxk = max( k for k in klasses ) + 0.5
        mnk = min( k for k in klasses ) - 0.5
        
        plt.set_xlim( mnk, mxk )
        
        for klass in klasses:
            v = [p
                 for p, a
                 in zip( predicted, actual )
                 if a == klass]
            seaborn.distplot( v,
                              label = f"{len( v )} CLASS {klass}" )
        
        y = -0.02
        
        for n, klass in enumerate( klasses ):
            klass = float( klass )
            l = klass - 0.5
            u = klass + 0.5
            
            l = lines.Line2D( xdata = [l, u],
                              ydata = [y, y],
                              color = plt.get_lines()[n].get_c(),
                              linewidth = 1,
                              clip_on = False )
            plt.add_line( l )
        
        matplotlib.pyplot.legend()
    
    
    def plot_predicted2( self ):
        hprint( "<h4>Versus scatter plot</h4>" )
        
        if self.class_type is not float:
            hprint( "Not making the plot because this is not regression." )
            return
        
        if self.predicted is None:
            hprint( "Not making the plot because this is not prediction." )
            return
        
        actual = self.__sub( self.actual )
        predicted = self.__sub( self.predicted )
        
        klasses = set( actual )
        
        if len( klasses ) <= 8:
            return
        
        seaborn.scatterplot( actual, predicted )
    
    
    def plot_scores( self, n: int = 0, m: Optional[int] = None ):
        """
        Makes a scores plot (does nothing for scoreless models).
        
        :param n:   Index of first component.
                    Defaults to 0. 
        :param m:   Index of second component.
                    Defaults to n + 1.
        :return: 
        """
        hprint( "<h4>Scores plot</h4>" )
        
        if self.scores is None:
            hprint( "Not making the scores plot because there are no scores." )
            return
        
        klasses = self.__sub( self.actual )
        
        if m is None:
            m = n + 1
        
        fig = new_plot( f"{self.x_name}: {self.reg_name} C{n} and {m} showing {self.y_name}" )
        
        for ss in "tv":
            x = self.__sub( self.scores[:, n], ss )
            y = self.__sub( self.scores[:, m], ss )
            
            if len( klasses ) <= 4:
                z = self.__sub( self.actual, ss )
            else:
                z = None
            
            fig.scatter( x, y, 1, c = z, alpha = 0.25 if ss == "t" else 1 )
    
    
    def plot_confusion_matrix( self ):
        hprint( "<h4>Confusion matrix</h4>" )
        
        if self.class_type is not int:
            hprint( "Not making the confusion matrix because this is not classification." )
            return
        
        if self.predicted is None:
            hprint( "Not making the confusion matrix because this is not prediction." )
            return
        
        hprint( f"<h3>Confusion matrix for {self.reg_name}</h3>" )
        _display( self.confusion_matrix )
    
    
    def __sub( self, v, ss = "v" ):
        assert len( v ) == len( self.sources )
        
        if ss == "v":
            return [x for x, s in zip( v, self.sources ) if s]
        elif ss == "t":
            return [x for x, s in zip( v, self.sources ) if not s]
        elif ss == "tv":
            return v
        else:
            raise KeyError( ss )
    
    
    def plot( self ) -> "Regression":
        """
        Plots all the plots.
        
        :return: Fluent interface for `x = Regression.fit(...).plot()`.
        """
        self.plot_confusion_matrix()
        self.plot_predicted()
        self.plot_predicted2()
        self.plot_scores()
        return self
    
    
    def _repr_html_( self ) -> str:
        if self.class_type is int and self.confusion_matrix is not None:
            # noinspection PyProtectedMember
            return self.confusion_matrix._repr_html_()
        else:
            return "Regression object"


# noinspection PyPackageRequirements
def _display( x ):
    """
    Local `display` alias (prints to the output sub-cell in Jupyter.).
    """
    from IPython.core.display import display
    # noinspection PyTypeChecker
    display( x )


# noinspection PyPackageRequirements
def hprint( x ):
    """
    Prints HTML to the output sub-cell in Jupyter.
    """
    # noinspection PyTypeChecker
    _display( HTML( x ) )


def mprint( x ):
    """
    Prints markdown to the output sub-cell in Jupyter.
    """
    # noinspection PyTypeChecker
    _display( Markdown( x ) )


# noinspection PyPackageRequirements
def tprint( x ):
    """
    Prints a doc section above a button
    """
    # noinspection PyTypeChecker
    CSS = """
    div.tprint_box
    {
        color: #000000;
        padding: 8px;
        font-weight: bold; 
    }    
    """
    
    _display( HTML( f"<style>{CSS}</style><div class='tprint_box'>{x}</div>" ) )


def repr_ipython( x ) -> str:
    """
    Behaves like Jupyter's `display` method, but returns the results as a string
    rather than printing it to the output sub-cell.
    """
    data, metadata = get_ipython().display_formatter.format( x )
    
    if "image/png" in data:
        x = data["image/png"]
        x = Image( data = x )._repr_png_()
        h = f'<img src="data:image/png;base64, {x}"/>'
    elif "text/html" in data:
        h = data["text/html"]
    elif "text/plain" in data:
        x = data["text/plain"]
        x = html.escape( x )
        h = f"<textarea rows=20 cols=80 readonly>{x}</textarea>"
    else:
        raise ValueError( f"Cannot render {x} because I don't understand the data: {data}" )
    
    return h


__figure_css = """
    details.mhnh_figure summary
    {
        border: 1px solid #A0A0FF;
        background: #C0C0FF;
        color: #000000;
        outline: none;
        border-radius: 8px;
    }
     
    details.mhnh_figure > summary:hover 
    {
        background: #E0E0FF;
    }
     
    details.mhnh_figure[open] > summary 
    {
        border: 1px solid #A0A0FF;
        background: #F0F0FF;
    }
    
    details.mhnh_figure[open] > summary:hover
    {
        background: #FFFFFF;
    }
    
    details.mhnh_figure:not([open]):after {
      content: "";
      display: block;
      background-repeat: repeat;
      height: 2px;
      background-size: 12px 10px;
      background-image:
        radial-gradient(circle at 5px -4px, #A0A0A0 6px, transparent 6.5px);
    }
    
    div.mhnh_content
    {
        margin: 8px;
        margin-top: 0;
        border: 1px solid #A0A0FF;
        border-top: none;
        border-bottom-left-radius: 8px;
        border-bottom-right-radius: 8px;
        overflow: auto; /* prevent margin collapse */
    }
    
    span.mhnh_caption
    {
    display: none;
    }
    
    details[open] summary span.mhnh_title
    {
    font-style: italic;
    }
    
    details[open] summary span.mhnh_caption
    {
    display: inline;
    } 
"""


def figure( x, title = "", caption = "", open = True ) -> None:
    """
    Prints to the output sub-cell in Jupyter.
    
    Output appears in a <details> with a title and caption.
    
    :param x:       Object to print 
    :param title:   Title
                    If empty this is taken from the object, if possible. 
    :param caption: Caption.
                    If empty this is taken from the object, if possible.
    :param open:    Whether the details element should be open by default.
    """
    if x.__class__.__qualname__ == "AxesSubplot":
        x = x.figure
    
    title = title or getattr( x, "mjr_title", "" )
    caption = caption or getattr( x, "mjr_caption", "" )
    
    if not title.endswith( "." ):
        title += "."
    
    txt = repr_ipython( x )
    open_ = "open" if open else ""
    
    if caption:
        caption = f"{caption}<br/>"
    
    hprint( f"<style>{__figure_css}</style><details class='mhnh_figure' {open_}><summary><strong>Figure:</strong> <span class='mhnh_title'>{title}</span> <span class='mhnh_caption'>{caption}</span></summary><div class='mhnh_content'>{txt}</div></details>" )


class ESpeed:
    """
    Approximate speeds of the methods.
    
    These are guesses based on the Consequence Dataset - not actual speeds,
    which would depend on the data.
    """
    MILLISECONDS = 1.2
    SECONDS = 5
    MINUTES = 3
    ANY = 9999


def __get_classifier_name( par ):
    return f"{par.func.__name__} {ArgsKwargs( *par.args, **par.keywords )}"


class ClassifierProtocol( Protocol ):
    """
    Sklearn seems to rely on duck-typing, so this is its Protocol.
    """
    
    
    def fit( self ):
        pass


def test_all_classifiers( data_sets: Union[ClassificationSet, Sequence[ClassificationSet]],
                          score: Callable[[Regression], object],
                          classifiers: Union[str, float, partial, ClassifierProtocol] = ESpeed.ANY,
                          cache_path: Optional[str] = None,
                          reps: Sequence[int] = (1,),
                          rand = True,
                          reraise = False,
                          pick: Container[str] = None,
                          skip: Container[str] = None
                          ) -> List:
    """
    :param skip:             Filter classifiers by names not to use
    :param pick:             Filter classifiers by names not to only use
    :param data_sets:          Dataframe or dataframes
    :param score:     Scoring function 
    :param classifiers:         Which classifiers to use.
                                int: everything in the default set faster than this time (0 for all)
                                str: name of a single classifier to use (from the default set)
                                partial: custom classifier
                                ClassifierProtocol: custom classifier
    :param cache_path:          Cache file name
    :param reps:        Array of replicates to use.
                        This is useful for stochastic models.
                        Replicates be identified by integers above zero - these
                        will be used as the random seed, see `rand`.
                        Use 0 to include any replicates already in the cache as
                        well.
    :param rand:        When on, tries to make the random seed equal to the rep,
                        when off, the random seed is always 1. Used for comparing
                        results. 
    :param reraise:     Don't catch errors
    :return:            List of sklearn models 
    """
    if not isinstance( data_sets, list ) and not isinstance( data_sets, tuple ):
        data_sets = data_sets,
    
    assert len( set( x.name for x in data_sets ) ) == len( data_sets ), "Datasets must have unique names"
    
    results = []
    
    # root ... algorithms
    root_cache = io_helper.load_json_data( cache_path, default = { } ) if cache_path else { }
    
    classifiers = __get_all_classifiers( classifiers )
    
    algorithms = classifiers
    
    if pick:
        algorithms = [x for x in algorithms if x[0] in pick]
    
    if skip:
        algorithms = [x for x in algorithms if x[0] not in skip]
    
    algorithms = sorted( algorithms,
                         key = lambda x: root_cache.get( x[0], { } ).get( "1", { } ).get( "score", 9999 ),
                         reverse = True )
    
    reps = [x for x in reps]
    
    if 0 in reps:
        reps.remove( 0 )
        all_reps = True
    else:
        all_reps = False
    
    hprint( f"<h2>Testing {len( algorithms )} classifiers on {len( data_sets )} datasets</h2>" )
    
    best_for_datasets = { data_set: [None, None] for data_set in data_sets }
    
    for algo_name, algo_params in algorithms:
        hprint( f"<h3>{algo_name}</h3>" )
        
        # root/algorithm ... datasets
        algo_cache: Dict = root_cache.setdefault( algo_name, { } )
        
        for data_set in data_sets:
            if len( data_sets ) > 1:
                hprint( f"<h4>{data_set.name}</h4>" )
            
            # root/algorithm/dataset ... reps
            dataset_cache: Dict = algo_cache.setdefault( data_set.name, { } )
            
            existing_reps = [int( x ) for x in dataset_cache if int( x ) not in reps] if all_reps else []
            all_reps = reps + existing_reps
            rep_scores = []
            rep_times = []
            
            for rep in all_reps:
                assert isinstance( rep, int )
                
                if rand:
                    rep_key = str( rep )
                    random_state = rep
                else:
                    rep_key = f"1/{rep}"
                    random_state = 1
                
                m_cache: Dict = dataset_cache.setdefault( rep_key, { } )
                assert isinstance( m_cache, dict )
                
                if isinstance( m_cache.get( "score" ), float ):
                    r_time = m_cache.get( "time", None )
                    r_score = m_cache.get( "score" )
                    confusion_state = m_cache.get( "confusion" )
                    r_confusion = state_helper.restore_state( ConfusionMatrix, confusion_state ) if confusion_state is not None else None
                    r_is_cached = True
                else:
                    if rep in existing_reps:
                        hprint( f"[{rep}] ?" )
                        continue
                    
                    if rand and "random_state" in algo_params.keywords:
                        algo_params.keywords["random_state"] = random_state
                    
                    model = algo_params()
                    results.append( model )
                    start_time = time.perf_counter()
                    
                    try:
                        regression = Regression.fit( model, data_set, prt = False, random_state = random_state )
                    except Exception as ex:
                        r_score = str( ex )
                        regression = None
                        if reraise:
                            raise
                    else:
                        r_score = score( regression )
                    
                    r_time = time.perf_counter() - start_time
                    r_confusion = regression.confusion_matrix if regression is not None else None
                    
                    m_cache["time"] = r_time
                    m_cache["score"] = r_score
                    m_cache["confusion"] = state_helper.retrieve_state( r_confusion ) if r_confusion is not None else None
                    
                    if cache_path:
                        io_helper.save_json_data( cache_path, root_cache )
                    
                    r_is_cached = False
                
                r_name = f"[{rep}] " if len( all_reps ) != 1 else ""
                r_time_tooltip = "cached" if r_is_cached else "not cached"
                
                rep_scores.append( r_score )
                rep_times.append( r_time )
                
                _print_score( r_time_tooltip, r_name, r_score, r_time, r_confusion )
            
            valid_rep_scores = [x for x in rep_scores if isinstance( x, float )]
            max_score = max( valid_rep_scores ) if valid_rep_scores else 0
            
            if len( rep_scores ) != 1:
                total_time = sum( rep_times )
                
                _print_score( "", "[★] ", max_score, total_time, None )
            
            best_ever = best_for_datasets[data_set]
            
            if best_ever[0] is None or max_score > best_ever[0]:
                best_ever[0] = max_score
                best_ever[1] = algo_name
    
    hprint( f"<h3>Best algorithms</h3>" )
    
    for data_set, (best_score, best_algorithm) in best_for_datasets.items():
        hprint( f"<strong>{data_set.name}</strong> = <code>{best_algorithm}</code> at {_float_to_html( best_score )}" )
    
    return results


def _print_score( time_tooltip: str,
                  title: str,
                  score: object,
                  time_taken: float,
                  confusion_matrix: Optional[ConfusionMatrix],
                  ) -> None:
    score_name = _float_to_html( score )
    
    h = []
    
    h.append( f"<details>" )
    h.append( f"    <summary>" )
    h.append( f"        {title}{score_name}" )
    h.append( f"        <sub title='{time_tooltip}'>" )
    h.append( f"            (in {string_helper.timedelta_to_string( time_taken )})" )
    h.append( f"        </sub>" )
    h.append( f"    </summary>" )
    if confusion_matrix is not None:
        h.append( f"    {confusion_matrix._repr_html_()}" )
    else:
        h.append( f"    (no confusion matrix available)" )
    h.append( f"</details>" )
    
    hprint( "".join( h ) )


def _float_to_html( score: object ):
    if isinstance( score, float ):
        score_name = f"<span title='{score}'>{score:.2f}</span>"
    else:
        score_name = f"{score}"
    return score_name


# noinspection PyPackageRequirements
@cached
def get_classifier_classes() -> Any:
    """
    Sklearn puts all its algorithms into packages that require separate imports.
    This method returns a namespace with all the algorithms attached to the root.
    
    Note: The naming of the method is somewhat unfortunate, since it returns both classifers and regressors.  
    """
    r = []
    
    from sklearn.linear_model import BayesianRidge, RidgeClassifier, SGDClassifier, LogisticRegression, Ridge
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.naive_bayes import GaussianNB
    from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
    from sklearn.svm import SVC
    from sklearn.ensemble import IsolationForest, GradientBoostingClassifier, RandomForestClassifier, AdaBoostClassifier
    from sklearn.neural_network import MLPClassifier
    from sklearn.cross_decomposition import PLSRegression
    
    r.extend( [BayesianRidge, RidgeClassifier, SGDClassifier, LogisticRegression, Ridge] )
    r.extend( [DecisionTreeClassifier] )
    r.extend( [KNeighborsClassifier] )
    r.extend( [GaussianNB] )
    r.extend( [QuadraticDiscriminantAnalysis] )
    r.extend( [SVC] )
    r.extend( [IsolationForest, GradientBoostingClassifier, RandomForestClassifier, AdaBoostClassifier] )
    r.extend( [MLPClassifier] )
    r.extend( [PLSRegression] )
    
    
    class Namespace:
        pass
    
    
    x = Namespace()
    
    for klass in r:
        setattr( x, klass.__name__, klass )
    
    return x


class _Getter:
    def __init__( self, x ):
        self.x = x
    
    
    def __call__( self ):
        return self.x


def __get_all_classifiers( constraints ) -> List[Tuple[str, Callable]]:
    """
    Obtains a list of machine learning algorithms (regressors or classifiers).
    The supported constraints are described in `test_all_classifiers` and are not repeated here.
    """
    modes = { "classification", "regression" }
    constrain_time: Optional[int] = None
    constrain_mode: Set[str] = set()
    constrain_name: Set[str] = set()
    constrain_only: List[Tuple[str, Callable]] = []
    
    if not isinstance( constraints, list ) and not isinstance( constraints, tuple ):
        constraints = constraints,
    
    for constraint in constraints:
        if isinstance( constraint, int ):
            assert constrain_time is None, "Can only specify one time constraint"
            constrain_time = constraint
        elif isinstance( constraint, str ):
            if constraint in modes:
                constrain_mode.add( constraint )
            else:
                constrain_name.add( constraint )
        elif isinstance( constraint, partial ):
            constrain_only.append( ("[User] " + __get_classifier_name( constraint ), constraint) )
        elif hasattr( constraint, "fit" ):
            constrain_only.append( ("[User] " + repr( constraint ), _Getter( constraint )) )
        else:
            raise RuntimeError( "Invalid classifier constraint." )
    
    if constrain_only:
        return constrain_only
    
    if constrain_time is None:
        constrain_time = 0
    
    r = []
    
    
    def pr( *ar, _t: float, _m: str, **kw ):
        if _t > constrain_time:
            return
        
        assert _m in modes
        
        if constrain_mode and _m not in constrain_mode:
            return
        
        call = partial( *ar, **kw )
        name = __get_classifier_name( call )
        
        if constrain_name and name not in constrain_name:
            return
        
        r.append( (name, call) )
    
    
    c = get_classifier_classes()
    
    pr( c.BayesianRidge, _t = 0.078, _m = "classification" )
    pr( c.RidgeClassifier, random_state = 1, _t = 0.044, _m = "classification" )
    pr( c.SGDClassifier, random_state = 1, _t = 0.96, _m = "classification" )
    pr( c.LogisticRegression, max_iter = 10000, random_state = 1, _t = 3, _m = "classification" )
    
    pr( c.IsolationForest, random_state = 1, _t = 1, _m = "classification" )
    pr( c.GradientBoostingClassifier, random_state = 1, _t = 17, _m = "classification" )
    pr( c.RandomForestClassifier, random_state = 1, _t = 6, _m = "classification" )
    # pr( RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1) ) -- why not?
    pr( c.AdaBoostClassifier, random_state = 1, _t = 3, _m = "classification" )
    
    pr( c.MLPClassifier,
        solver = 'lbfgs',
        alpha = 1e-5,
        hidden_layer_sizes = (5, 2),
        max_iter = 10000,
        random_state = 1,
        _t = 15, _m = "classification" )  # 00:25
    pr( c.MLPClassifier, alpha = 1, max_iter = 1000, random_state = 1, _t = 18, _m = "classification" )  # 00:17
    pr( c.MLPClassifier, random_state = 1, _t = 36, _m = "classification" )  # 00:26 
    
    pr( c.DecisionTreeClassifier, random_state = 1, _t = 1, _m = "classification" )  # 812ms
    pr( c.DecisionTreeClassifier, max_depth = 5, random_state = 1, _t = 0.35, _m = "classification" )  # 303ms
    
    pr( c.KNeighborsClassifier, n_neighbors = 3, _t = 2, _m = "classification" )  # 00:01
    pr( c.KNeighborsClassifier, n_neighbors = 5, _t = 2, _m = "classification" )  # 00:01
    
    # pr( GaussianProcessClassifier( 1.0 * RBF( 1.0 ) ) ) -- slow
    # pr( GaussianProcessClassifier() ) -- slow
    
    
    pr( c.GaussianNB, _t = 0.036 )  # 38ms
    
    pr( c.QuadraticDiscriminantAnalysis, _t = 0.1, _m = "classification" )  # 105ms
    
    pr( c.SVC, kernel = "linear", random_state = 1, _t = 126, _m = "classification" )  # 02:36
    pr( c.SVC, kernel = "poly", random_state = 1, _t = 10, _m = "classification" )
    pr( c.SVC, kernel = "rbf", random_state = 1, _t = 7, _m = "classification" )
    pr( c.SVC, kernel = "sigmoid", random_state = 1, _t = 10, _m = "classification" )
    pr( c.SVC, kernel = "linear", C = 0.025, random_state = 1, _t = 21, _m = "classification" )
    # pr( SVC( gamma=2, C=1 ) ) -- why not?
    
    
    return rr


def concatenate( x1, x2 ):
    # This is why duck typing doesn't work...
    if isinstance( x1, pandas.DataFrame ):
        return pandas.concat( (x1, x2) )
    elif isinstance( x1, numpy.ndarray ):
        return numpy.concatenate( (x1, x2) )
    elif isinstance( x1, list ):
        return x1 + x2
    else:
        raise TypeError( "Cannot concatenate" )


def minteract( a = None, auto = True, doc = None, **kwargs ):
    """
    An `ipywidgets.interact`-like decorator
    
    * The function is run automatically.
    * Execution time is displayed on completion.
    * The user may rerun the function by pressing a button.
    * Parameters are optional (if available they may be modified as usual for
      `interact`)
    * Arguments to interact.options and interact are combined into kwargs:
      this avoids the "`interact.options(...)(...)` is not a decorator" issue.
      (As a consequence the function cannot have parameter names that conflict
      with `interact.options`, but this is unlikely to be an issue since as
      these are few and unique).
    """
    if a is None:
        return partial( minteract, auto = auto, doc = doc, **kwargs )
    
    if doc:
        tprint( doc )
    
    # noinspection PyPackageRequirements
    from ipywidgets import interact
    
    d = interact.options( manual = True, manual_name = "Run" )
    
    o = { }
    
    for k in d.opts:
        if k in kwargs:
            o[k] = kwargs.pop( k )
    
    if o:
        d = d.options( **o )
    
    first_run = [1]
    
    
    @functools.wraps( a )
    def dec( *args, **kwargs ):
        if (not d.opts["manual"] or not auto) and first_run:
            print( "1 Please press RUN", file = sys.stderr )
            first_run.clear()
            return
        
        start_time = time.perf_counter()
        
        try:
            r = a( *args, **kwargs )
        except Exception as ex:
            hprint( exception_formatter.format_traceback_ex( ex, "the minteract-decorated function failed", "error", "html" ) )
            return None
        
        total_time = time.perf_counter() - start_time
        total_time_str = string_helper.timedelta_to_string( total_time )
        
        print( f"0 OK - {total_time_str}", file = sys.stderr )
        return r
    
    
    dec = d( dec, **kwargs )
    
    dec.widget.update()
    
    return dec


def mview_( x ) -> HTML:
    return mview( x, private = True )


def mview( x, private = False ) -> HTML:
    r = []
    
    r.append( "<table>" )
    
    for k in dir( x ):
        if private and k.startswith( "_" ):
            continue
        
        if k == "__dict__":
            v = "..."
        else:
            try:
                v = getattr( x, k )
                v = str( v )
            except Exception as ex:
                v = f"{ex.__class__.__name__}: {ex}"
        
        r.append( "<tr>" )
        r.append( "<td>" )
        r.append( html.escape( k ) )
        r.append( "</td>" )
        r.append( "<td>" )
        r.append( html.escape( v ) )
        r.append( "</td>" )
        r.append( "</tr>" )
    
    r.append( "</table>" )
    
    return HTML( "\n".join( r ) )


def calculate_vips( model ):
    """
    Calculates the VIP scores for a PLSR model.
    """  # TODO: TEST
    t = model.x_scores_
    w = model.x_weights_
    q = model.y_loadings_
    p, h = w.shape
    vips = numpy.zeros( (p,) )
    s = numpy.diag( numpy.matmul( numpy.matmul( numpy.matmul( t.T, t ), q.T ), q ) ).reshape( h, -1 )
    total_s = numpy.sum( s )
    for i in range( p ):
        weight = numpy.array( [(w[i, j] / numpy.linalg.norm( w[:, j] )) ** 2 for j in range( h )] )
        vips[i] = numpy.sqrt( p * (numpy.matmul( s.T, weight )) / total_s )
    return vips


def get_fimp( algo ) -> Tuple[str, Optional[Sequence[float]]]:
    """
    Extracts the feature importance from a model, e.g. VIP scores for PLS,
    feature_importances for Random Forest, or, if all else fails, the
    coefficients. Returns None if the class does not support anything.   
    """
    
    if algo.__class__.__name__ == "PLSRegression":
        return "vip scores", calculate_vips( algo )
    
    if hasattr( algo, "feature_importances_" ):
        return "feature importances", algo.feature_importances_
    
    if hasattr( algo, "coef_" ):
        return "coefficients", algo.coef_
    
    return "cannot determine feature importance", None


class NamespaceType( type ):
    def __getitem__( self, item ):
        class Derived( Namespace ):
            pass
        
        
        if "." in item:
            name = item.rsplit( ".", 1 )[1]
        else:
            name = item
        
        Derived.__name__ = name
        Derived.__qualname__ = item
        return Derived


class Namespace( metaclass = NamespaceType ):
    def __init__( self, d = None, **kwargs ):
        if d is not None:
            self.__dict__.update( d )
        
        self.__dict__.update( kwargs )
    
    
    def __getitem__( self, item ):
        return self.__dict__[item]
    
    
    def get( self, item ):
        return self.__dict__.get( item )
