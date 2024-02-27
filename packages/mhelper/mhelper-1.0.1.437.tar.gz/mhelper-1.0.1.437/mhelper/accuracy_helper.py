from typing import Iterable, List, Tuple, Union, Dict
from mhelper import utf_table


__all__ = "ConfusionMatrix"

_aliases = { }


def alias( aliases ):
    def dec( f ):
        _aliases[f.fget.__name__] = [x.strip() for x in aliases.split( "|" )]
        return f
    
    
    return dec


class ConfusionMatrix:
    
    
    def __init__( self, *, tp, fp, tn, fn ):
        assert tp is not None
        assert fp is not None
        assert tn is not None
        assert fn is not None
        
        self.tp = tp
        self.fp = fp
        self.tn = tn
        self.fn = fn
    
    
    def __getstate__( self ) -> Dict[str, object]:
        return { "tp": self.tp,
                 "fp": self.fp,
                 "tn": self.tn,
                 "fn": self.fn }
    
    
    def __setstate__( self, state: Dict[str, object] ):
        self.tp = state["tp"]
        self.fp = state["fp"]
        self.tn = state["tn"]
        self.fn = state["fn"]
    
    
    def invert( self ) -> "ConfusionMatrix":
        """
        For a binary classifier, assumes the predictor was working the other way
        around, predicting 1 as 0 and 0 as 1. This method produces a new matrix
        with the predicted values flipped::
        
                        Pred
                        T<->F
            Actual  T   TP  FN
                    F   FP  TN         
        """
        return ConfusionMatrix( tp = self.fn,
                                fp = self.tn,
                                tn = self.fp,
                                fn = self.tp )
    
    
    @staticmethod
    def from_predictions( p: Union[Iterable[object], Tuple[object, object]],
                          a: Iterable[object] = None ):
        tp = 0
        fp = 0
        tn = 0
        fn = 0
        
        if a is None:
            pa = p
        else:
            pa = zip( p, a )
        
        for _p, _a in pa:
            if _p:
                # Predicted TRUE
                if _a:
                    # Actual TRUE
                    tp += 1
                else:
                    # Actual FALSE
                    fp += 1
            else:
                # Predicted FALSE
                if _a:
                    # Actual TRUE
                    fn += 1
                else:
                    # Actual FALSE
                    tn += 1
        
        return ConfusionMatrix( tp = tp, fp = fp, tn = tn, fn = fn )
    
    
    def __str__( self ):
        return f"TP={self.tp} FP={self.fp} TN={self.tn} FN={self.fn}"
    
    
    @alias( "F1 | Harmonic mean of precision and recall | 2 / (Sn^-1 + PPV^-1)" )
    @property
    def f1( self ):
        return 2 / ((1 / self.sensitivity) + (1 / self.precision))
    
    
    @alias( "Sn | TPR | Sensitivity | true positive rate | recall | TP/(TP+FN)" )
    @property
    def sensitivity( self ):
        return self.tp / (self.tp + self.fn)
    
    
    @alias( "Sp | TNR | Specificity | true negative rate | TN/(TN+FP)" )
    @property
    def specificity( self ):
        return self.tn / (self.tn + self.fp)
    
    
    @alias( "PPV | Precision | Positive predictive value | TP/(TP+FP)" )
    @property
    def precision( self ):
        if self.tp + self.fp == 0:
            return float( "nan" )
        
        return self.tp / (self.tp + self.fp)
    
    
    @alias( "Ac | Accuracy | (TP+TN)/(TP+TN+FP+FN)" )
    @property
    def accuracy( self ):
        return (self.tp + self.tn) / (self.tp + self.tn + self.fp + self.fn)
    
    
    @alias( "FDR | False discovery rate | FP/(TP+FP)" )
    @property
    def fdr( self ):
        return self.fp / (self.tp + self.fp)
    
    
    @alias( "FPR | False positive rate | FP/(FP+TN)" )
    @property
    def fpr( self ):
        return self.fp / (self.fp + self.tn)
    
    
    @alias( "FNR | False negative rate | FN/(FN+TP)" )
    @property
    def fnr( self ):
        return self.fn / (self.fn + self.tp)
    
    
    @alias( "FOR | False omission rate | FN/(TN+FN)" )
    @property
    def false_omission_rate( self ):
        return self.fn / (self.tn + self.fn)
    
    
    @alias( "PPCR | Predicted positive condition rate | (TP+FP)/(TP+FP+TN+FN)" )
    @property
    def ppcr( self ):
        return (self.tp + self.fp) / (self.tp + self.fp + self.tn + self.fn)
    
    
    @alias( "Sor | Sn*PPV | sorgenfrei | Sorgenfrei coefficient | correlation ratio | TP^2/((TP+FN)(TP+FP))" )
    @property
    def sorgenfrei( self ):
        # Consequence uses Sensitivity (SN) × Positive Predictive Value (PPV).
        # that's this:
        return self.sensitivity * self.precision
    
    
    def get_metrics_table( self, core = False ) -> "ConfusionMatrix.MetricsTable":
        return ConfusionMatrix.MetricsTable( self, core )
    
    
    def get_confusion_matrix_html( self ):
        cm = """
        <table>
            <tr>
                 <td>
                    <em>Actual</em>
                 </td>
                 <td>
                 </td>
                 <td>
                     T
                 </td>
                 <td>
                     F
                 </td>
            </tr>
            <tr>
                 <td rowspan=2>
                     <em>Predicted</em>
                 </td>
                 <td>
                     T
                 </td>
                 <td style="color: green;">
                     {:,}
                 </td>
                 <td>
                     {:,}
                 </td>
            </tr>
                 <td>
                     F
                 </td>
                 <td>
                     {:,}
                 </td>
                 <td style="color: darkred;">
                     {:,}
                 </td>
            </tr>
        </table>
        """
        
        a = []
        a.append( cm.format( self.tp, self.fp, self.fn, self.tn ) )
        return "".join( a )
    
    
    def _repr_html_( self ) -> str:
        a_ = self.get_confusion_matrix_html()
        b_ = self.get_metrics_table().to_html()
        return f"<table><tr style='background: white;'><td>{a_}</td><td>{b_}</td></tr></table>"
    
    
    class MetricsTable:
        __slots__ = "rows",
        
        
        class Row:
            __slots__ = "name", "value", "aliases"
            
            
            def __init__( self, name: str, value: float, aliases = None ):
                self.name = name
                self.value = value
                self.aliases = aliases or (name,)
            
            
            @property
            def alias_text( self ):
                return ", ".join( self.aliases )
            
            
            @property
            def value_text( self ):
                v = self.value
                
                if isinstance( v, float ):
                    if v != v:
                        # NAN or DBZ
                        v = "/0"
                    elif 0 <= v <= 1:
                        v = f"{v:.2f}"
                        
                        if v.startswith( "0." ):
                            v = v[1:]
                
                elif isinstance( v, int ):
                    v = f"{v:,}"
                else:
                    v = f"{v.__class__.__name__}:{v}"
                
                return str( v )
        
        
        def __init__( self, cm: "ConfusionMatrix", core: bool ):
            rows = []
            
            if core:
                rows.append( ConfusionMatrix.MetricsTable.Row( "TP", cm.tp ) )
                rows.append( ConfusionMatrix.MetricsTable.Row( "TN", cm.tn ) )
                rows.append( ConfusionMatrix.MetricsTable.Row( "FP", cm.fp ) )
                rows.append( ConfusionMatrix.MetricsTable.Row( "FN", cm.fn ) )
            
            for prop in ConfusionMatrix.__dict__.values():
                if not hasattr( prop, "fget" ):
                    continue
                
                prop_name = prop.fget.__name__
                aliases = _aliases[prop_name]
                name = aliases[0]
                
                try:
                    v = prop.fget( cm )
                except ZeroDivisionError:
                    v = float( "nan" )
                
                rows.append( ConfusionMatrix.MetricsTable.Row( name, v, aliases ) )
            
            self.rows = rows
        
        
        def to_float_table( self ) -> List[Tuple[str, float]]:
            return [(x.name, x.value) for x in self.rows]
        
        
        def to_table( self ) -> List[Tuple[str, str]]:
            return [(x.name, x.value_text) for x in self.rows]
        
        
        def to_text( self, box = None ) -> str:
            tab = [None, *self.to_table(), None]
            
            return utf_table.TextTable.from_table( tab, box = box ).to_string()
        
        
        def to_html( self ) -> str:
            b = []
            b.append( "<table>" )
            
            for index, row in enumerate( self.rows ):
                if index % 3 == 0:
                    if index != 0:
                        b.append( "</tr>" )
                    
                    b.append( "<tr>" )
                
                b.append( f'<td title="{row.alias_text}"><em>{row.name}</em></td><td title="{repr( row.value )}">{row.value_text}</td>' )
            
            b.append( "</tr>" )
            b.append( "</table>" )
            return "".join( b )
