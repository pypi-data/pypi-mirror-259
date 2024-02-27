from mhelper.special_types import Sentinel


AMINO_ACIDS = frozenset( "RKWDENQHSTYACGILMFPV" )


# noinspection SpellCheckingInspection
class _Constants:
    AMINO_ACIDS = AMINO_ACIDS
    
    E_HYDRO_PHOBIC = Sentinel( "E_HYDROPHOBIC" )
    E_HYDRO_NEUTRAL = Sentinel( "E_NEUTRAL" )
    E_HYDRO_PHILIC = Sentinel( "E_HYDROPHILIC" )
    E_CHEM_ALIPHATIC = Sentinel( "E_CHEM_ALIPHATIC" )
    E_CHEM_AROMATIC = Sentinel( "E_CHEM_AROMATIC" )
    E_CHEM_SULFUR = Sentinel( "E_CHEM_SULFUR" )
    E_CHEM_HYDROXYL = Sentinel( "E_CHEM_HYDROXYL" )
    E_CHEM_BASIC = Sentinel( "E_CHEM_BASIC" )
    E_CHEM_ACIDIC = Sentinel( "E_CHEM_ACIDIC" )
    E_CHEM_AMIDE = Sentinel( "E_CHEM_AMIDE" )
    E_H_ACCEPTOR = Sentinel( "E_H_ACCEPTOR" )
    E_H_DONOR = Sentinel( "E_H_DONOR" )
    E_H_BOTH = Sentinel( "E_H_BOTH" )
    E_H_NONE = Sentinel( "E_H_NONE" )
    K_VOL_MAX_VERY_SMALL = 89.0
    K_VOL_MIN_SMALL = 108.5
    K_VOL_MAX_SMALL = 116.1
    K_VOL_MIN_MEDIUM = 138.4
    K_VOL_MAX_MEDIUM = 153.2


# noinspection SpellCheckingInspection
class CustomAaIndex:
    ALL = { }
    
    HYDROPATHY = {
        **{ k: _Constants.E_HYDRO_PHOBIC for k in "ACILMFWV" },
        **{ k: _Constants.E_HYDRO_NEUTRAL for k in "GHPSTY" },
        **{ k: _Constants.E_HYDRO_PHILIC for k in "RNDQEK" }
        }
    
    CHEMICAL = {
        **{ k: _Constants.E_CHEM_ALIPHATIC for k in "AGILPV" },
        **{ k: _Constants.E_CHEM_AROMATIC for k in "FWY" },
        **{ k: _Constants.E_CHEM_SULFUR for k in "CM" },
        **{ k: _Constants.E_CHEM_HYDROXYL for k in "ST" },
        **{ k: _Constants.E_CHEM_BASIC for k in "RHK" },
        **{ k: _Constants.E_CHEM_ACIDIC for k in "DE" },
        **{ k: _Constants.E_CHEM_AMIDE for k in "NQ" },
        }
    
    HDONOR = {
        **{ k: _Constants.E_H_ACCEPTOR for k in "RKW" },
        **{ k: _Constants.E_H_DONOR for k in "DE" },
        **{ k: _Constants.E_H_BOTH for k in "NQHSTY" },
        **{ k: _Constants.E_H_NONE for k in "ACGILMFPV" },
        }
    
    CHARGE = {
        **{ k: 1 for k in "RHK" },
        **{ k: -1 for k in "DE" },
        **{ k: 0 for k in "ANCQGILMFPSTWYV" },
        }
    
    POLARITY = {
        **{ k: 1 for k in "RNDQEHKSTY" },
        **{ k: 0 for k in "ACGILMFPWV" },
        }
    
    VOLUME = {
        "G": 60.1,  # VERY SMALL
        "A": 88.6,
        "S": 89.0,
        "C": 108.5,  # SMALL
        "D": 111.1,
        "P": 112.7,
        "N": 114.1,
        "T": 116.1,
        "E": 138.4,  # MEDIUM
        "V": 140.0,
        "Q": 143.8,
        "H": 153.2,
        "M": 162.9,  # LARGE
        "I": 166.7,
        "L": 166.7,
        "K": 168.6,
        "R": 173.4,
        "F": 189.9,  # VERY LARGE
        "Y": 193.6,
        "W": 227.8
        }
    
    ZERO = { k: 0 for k in _Constants.AMINO_ACIDS }
    ONE = { k: 1 for k in _Constants.AMINO_ACIDS }
    IS_BASIC = { k: v == 1 for k, v in CHARGE.items() }
    IS_NEUTRAL = { k: v == 0 for k, v in CHARGE.items() }
    IS_K = { **ZERO, "K": 1 }  # We actually define these for all AA in _initialise class
    IS_R = { **ZERO, "R": 1 }
    IS_MEDIUM = { k: _Constants.K_VOL_MIN_MEDIUM <= v <= _Constants.K_VOL_MAX_MEDIUM for k, v in VOLUME.items() }
    IS_SMALL = { k: v < _Constants.K_VOL_MIN_MEDIUM for k, v in VOLUME.items() }
    
    
    @staticmethod
    def _initialise_class():
        for aa in _Constants.AMINO_ACIDS:
            attr = f"IS_{aa}"
            
            if not hasattr( CustomAaIndex, attr ):
                setattr( CustomAaIndex, attr, { **CustomAaIndex.ZERO, aa: 1 } )
        
        for name, dictionary in CustomAaIndex.__dict__.items():
            if name.startswith( "_" ) or name == "ALL":
                continue
            
            if not isinstance( dictionary, dict ):
                continue
            
            v0 = dictionary["R"]
            
            if isinstance( v0, Sentinel ):
                continue
            
            assert len( dictionary ) == len( _Constants.AMINO_ACIDS )
            assert all( x in dictionary for x in _Constants.AMINO_ACIDS )
            
            CustomAaIndex.ALL[name] = dictionary


CustomAaIndex._initialise_class()
