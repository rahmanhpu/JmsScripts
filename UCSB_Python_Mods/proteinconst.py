#!/usr/bin/env python


#DESC: Contains constant variables for protein.py


#LAST MODIFIED: 02-16-08

from numpy import *

#possible chain names
ChainNames = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

#residues without dihedrals
NoDihedrals = ["ACE","NHE","NME"]

#residues with fixed angles
FixedPhi = ["PRO"]
FixedPsi = []
FixedChi = {"ARG":[4]}

#lists of special atoms:
#atoms to remove when decapping
TerminiAtoms = ["OXT", "H2", "H3"]
#backbone atoms
BackboneAtoms = ["N", "CA", "C", "O", "H", "HT", "HA", "2HA", "3HA"]
#atoms to use when aligining side chains during mutations
BBAlignAtoms = ["N", "CA", "C"]
#atoms to use during backbone setting and getting (must include BBAlignAtoms first)
BBSetAtoms = BBAlignAtoms + ["O", "H"]

#aliases to be converted upon reading pdb files
AtomConvertAliases = {" HN ":" H  ", "HN":"H", "OCT1":"O", "OCT2":"OXT"}

#peptide and residue atom lookup aliases (for caps, proline and glycine);
#each atom's dictionary has a key for residue name (* is default) and a list
#of possible aliases; the "*" entry must be present in each dictionary
AtomAliases = {"H"  : {"PRO":["CD"], "*":["HN", "HT"]},
               "N"  : {"*":[]},
               "CA" : {"*":["CH3"]},
               "C"  : {"*":[]},
               "O"  : {"*":[]},
               "CB" : {"*":["CA", "CH3"]},
               "cen": {"*":["CB", "CA", "CH3"]},
               "*"  : {"*":[]}
               }

#atoms to be stored in an array for faster lookup;
#this must include backbone atoms for hbond functions
#to work properly
QuickAtoms = ["H", "N", "CA", "C", "O"] 

#peptide bond length constants
CNBondLen = 1.32
NHBondLen = 1.01
COBondLen = 1.23
CNFracOC = 0.516
NCFracHN = 0.5
NHFracCAC = 0.541
NHFracCN = 0.504
COFracCAC = 0.474
COFracNC = 0.506

#Van der Waals radii taken from amber
#covalent radii taken from rasmol
VDWRadii = {"default":2.00, "H":1.00, "C":1.85, "N":1.75, "O":1.60, "P":2.10, "S":2.00}
CovalentRadii = {"default":1.0, "H":0.6, "C":1.0, "N":0.96, "O":0.96, "P":1.316, "S":1.3}

#SqrtEps for VDW interactions, taken from amber
SqrtEps =  {"default":sqrt(0.0100), "H":sqrt(0.0157), "C":sqrt(0.0860), "N":sqrt(0.1700),
            "O":sqrt(0.2100), "P":sqrt(0.2000), "S":sqrt(0.2500)}

#angle ranges to try for phi-psi for a residue
ResAngleRanges = [[(-180., 90.), (-45., 180. )],  #beta
                 [(-135.,-75.),(-45.,30.)]      ] #helix
#ranges for trying for psi(n-1) and phi(n)
PepAngleRanges = [[(-180., 90.), (-45., 180. )],  #beta
                 [(-180.,-75.),(-45.,30.)]      ] #helix


#backbone hydrogen bonding coefficients (taken from autodock)
HBondLJA = 55332.873
HBondLJB = 18393.199
#backbone hydrogen bonding charge parameter (taken from DSSP paper)
HBondChargeScale = 332. * 0.42 * 0.20

#optimal ratio with steric/LJ score in order to produce hbonds with correct dist;
#0 is for coef=0 in the hbond function, and 1 is for coef=1;
#note that this depends on the standard VDW radiii
HBondChargeRatioToSteric0 = 35.2496
HBondChargeRatioToSteric1 = 81.3043
HBondChargeRatioToLJ0 = 1.71577
HBondChargeRatioToLJ1 = 3.95748

#backbone hydrogen bonding params for detecting
#(some taken from Petukhov et al, Prot Sci 13, 1, 2001)
#(some taken from DSSP paper)
HBondHODist = 3.1   #distance cutoff for O--H
HBondNODist = 4.1   #distance cutoff for O--N
HBondNHOAng = 60.   #acceptor-donor angle cutoff for N-H--O-C
HBondNOCAng = 60.   #angle cutoff for N--O-C

#DSSP hydrogen bonding constants
HBondDSSPScale = 332. * 0.42 * 0.20
HBondDSSPECut = -0.5
HBondDSSPDistCut = HBondDSSPECut / HBondDSSPScale

#hydrogen bonding mode: False = Geometry, True = DSSP
HBondDSSP = True


#distance cutoff for energy/score calculations
OverlapDistCut = 4.
HBondLJDistCut = 6.
HBondDipoleDistCut = 15.
HBondChargeDistCut = 25.
PhobicDistCut = 16.
ChargeDistCut = 16.

#dielectric
CoulFact = 331.94292

#scale for side chain atom size relative to Rg of side chain atoms when coarse graining
CoarseGrainRgScaleDflt = 1.4


#force field data, taken from amber ff96.
#tuples are (vdw radius, sqrt of lj eps, partial charge);
#the lj equation is u(r) = eps * ((sig/r)^12 - 2*(sig/r)^6)
FFCharge14Scale = 1./1.2
FFLJ14Scale = 1./2.0
FFSteric14Scale = 1./2.0
FFResData = {
  'ALA' : {
    'N' : (1.8240, 0.4123, -0.4157),
    'H' : (0.6000, 0.1253, 0.2719),
    'CA' : (1.9080, 0.3308, 0.0337),
    'HA' : (1.3870, 0.1253, 0.0823),
    'CB' : (1.9080, 0.3308, -0.1825),
    'HB1' : (1.4870, 0.1253, 0.0603),
    'HB2' : (1.4870, 0.1253, 0.0603),
    'HB3' : (1.4870, 0.1253, 0.0603),
    'C' : (1.9080, 0.2933, 0.5973),
    'O' : (1.6612, 0.4583, -0.5679)
    },
  'ARG' : {
    'N' : (1.8240, 0.4123, -0.3479),
    'H' : (0.6000, 0.1253, 0.2747),
    'CA' : (1.9080, 0.3308, -0.2637),
    'HA' : (1.3870, 0.1253, 0.1560),
    'CB' : (1.9080, 0.3308, -0.0007),
    'HB2' : (1.4870, 0.1253, 0.0327),
    'HB3' : (1.4870, 0.1253, 0.0327),
    'CG' : (1.9080, 0.3308, 0.0390),
    'HG2' : (1.4870, 0.1253, 0.0285),
    'HG3' : (1.4870, 0.1253, 0.0285),
    'CD' : (1.9080, 0.3308, 0.0486),
    'HD2' : (1.3870, 0.1253, 0.0687),
    'HD3' : (1.3870, 0.1253, 0.0687),
    'NE' : (1.8240, 0.4123, -0.5295),
    'HE' : (0.6000, 0.1253, 0.3456),
    'CZ' : (1.9080, 0.2933, 0.8076),
    'NH1' : (1.8240, 0.4123, -0.8627),
    'HH11' : (0.6000, 0.1253, 0.4478),
    'HH12' : (0.6000, 0.1253, 0.4478),
    'NH2' : (1.8240, 0.4123, -0.8627),
    'HH21' : (0.6000, 0.1253, 0.4478),
    'HH22' : (0.6000, 0.1253, 0.4478),
    'C' : (1.9080, 0.2933, 0.7341),
    'O' : (1.6612, 0.4583, -0.5894)
    },
  'ASH' : {
    'N' : (1.8240, 0.4123, -0.4157),
    'H' : (0.6000, 0.1253, 0.2719),
    'CA' : (1.9080, 0.3308, 0.0341),
    'HA' : (1.3870, 0.1253, 0.0864),
    'CB' : (1.9080, 0.3308, -0.0316),
    'HB2' : (1.4870, 0.1253, 0.0488),
    'HB3' : (1.4870, 0.1253, 0.0488),
    'CG' : (1.9080, 0.2933, 0.6462),
    'OD1' : (1.6612, 0.4583, -0.5554),
    'OD2' : (1.7210, 0.4587, -0.6376),
    'HD2' : (0.0000, 0.0000, 0.4747),
    'C' : (1.9080, 0.2933, 0.5973),
    'O' : (1.6612, 0.4583, -0.5679)
    },
  'ASN' : {
    'N' : (1.8240, 0.4123, -0.4157),
    'H' : (0.6000, 0.1253, 0.2719),
    'CA' : (1.9080, 0.3308, 0.0143),
    'HA' : (1.3870, 0.1253, 0.1048),
    'CB' : (1.9080, 0.3308, -0.2041),
    'HB2' : (1.4870, 0.1253, 0.0797),
    'HB3' : (1.4870, 0.1253, 0.0797),
    'CG' : (1.9080, 0.2933, 0.7130),
    'OD1' : (1.6612, 0.4583, -0.5931),
    'ND2' : (1.8240, 0.4123, -0.9191),
    'HD21' : (0.6000, 0.1253, 0.4196),
    'HD22' : (0.6000, 0.1253, 0.4196),
    'C' : (1.9080, 0.2933, 0.5973),
    'O' : (1.6612, 0.4583, -0.5679)
    },
  'ASP' : {
    'N' : (1.8240, 0.4123, -0.5163),
    'H' : (0.6000, 0.1253, 0.2936),
    'CA' : (1.9080, 0.3308, 0.0381),
    'HA' : (1.3870, 0.1253, 0.0880),
    'CB' : (1.9080, 0.3308, -0.0303),
    'HB2' : (1.4870, 0.1253, -0.0122),
    'HB3' : (1.4870, 0.1253, -0.0122),
    'CG' : (1.9080, 0.2933, 0.7994),
    'OD1' : (1.6612, 0.4583, -0.8014),
    'OD2' : (1.6612, 0.4583, -0.8014),
    'C' : (1.9080, 0.2933, 0.5366),
    'O' : (1.6612, 0.4583, -0.5819)
    },
  'CYM' : {
    'N' : (1.8240, 0.4123, -0.4157),
    'HN' : (0.6000, 0.1253, 0.2719),
    'CA' : (1.9080, 0.3308, -0.0351),
    'HA' : (1.3870, 0.1253, 0.0508),
    'CB' : (1.9080, 0.3308, -0.2413),
    'HB3' : (1.3870, 0.1253, 0.1122),
    'HB2' : (1.3870, 0.1253, 0.1122),
    'SG' : (2.0000, 0.5000, -0.8844),
    'C' : (1.9080, 0.2933, 0.5973),
    'O' : (1.6612, 0.4583, -0.5679)
    },
  'CYS' : {
    'N' : (1.8240, 0.4123, -0.4157),
    'H' : (0.6000, 0.1253, 0.2719),
    'CA' : (1.9080, 0.3308, 0.0213),
    'HA' : (1.3870, 0.1253, 0.1124),
    'CB' : (1.9080, 0.3308, -0.1231),
    'HB2' : (1.3870, 0.1253, 0.1112),
    'HB3' : (1.3870, 0.1253, 0.1112),
    'SG' : (2.0000, 0.5000, -0.3119),
    'HG' : (0.6000, 0.1253, 0.1933),
    'C' : (1.9080, 0.2933, 0.5973),
    'O' : (1.6612, 0.4583, -0.5679)
    },
  'CYX' : {
    'N' : (1.8240, 0.4123, -0.4157),
    'H' : (0.6000, 0.1253, 0.2719),
    'CA' : (1.9080, 0.3308, 0.0429),
    'HA' : (1.3870, 0.1253, 0.0766),
    'CB' : (1.9080, 0.3308, -0.0790),
    'HB2' : (1.3870, 0.1253, 0.0910),
    'HB3' : (1.3870, 0.1253, 0.0910),
    'SG' : (2.0000, 0.5000, -0.1081),
    'C' : (1.9080, 0.2933, 0.5973),
    'O' : (1.6612, 0.4583, -0.5679)
    },
  'GLH' : {
    'N' : (1.8240, 0.4123, -0.4157),
    'H' : (0.6000, 0.1253, 0.2719),
    'CA' : (1.9080, 0.3308, 0.0145),
    'HA' : (1.3870, 0.1253, 0.0779),
    'CB' : (1.9080, 0.3308, -0.0071),
    'HB2' : (1.4870, 0.1253, 0.0256),
    'HB3' : (1.4870, 0.1253, 0.0256),
    'CG' : (1.9080, 0.3308, -0.0174),
    'HG2' : (1.4870, 0.1253, 0.0430),
    'HG3' : (1.4870, 0.1253, 0.0430),
    'CD' : (1.9080, 0.2933, 0.6801),
    'OE1' : (1.6612, 0.4583, -0.5838),
    'OE2' : (1.7210, 0.4587, -0.6511),
    'HE2' : (0.0000, 0.0000, 0.4641),
    'C' : (1.9080, 0.2933, 0.5973),
    'O' : (1.6612, 0.4583, -0.5679)
    },
  'GLN' : {
    'N' : (1.8240, 0.4123, -0.4157),
    'H' : (0.6000, 0.1253, 0.2719),
    'CA' : (1.9080, 0.3308, -0.0031),
    'HA' : (1.3870, 0.1253, 0.0850),
    'CB' : (1.9080, 0.3308, -0.0036),
    'HB2' : (1.4870, 0.1253, 0.0171),
    'HB3' : (1.4870, 0.1253, 0.0171),
    'CG' : (1.9080, 0.3308, -0.0645),
    'HG2' : (1.4870, 0.1253, 0.0352),
    'HG3' : (1.4870, 0.1253, 0.0352),
    'CD' : (1.9080, 0.2933, 0.6951),
    'OE1' : (1.6612, 0.4583, -0.6086),
    'NE2' : (1.8240, 0.4123, -0.9407),
    'HE21' : (0.6000, 0.1253, 0.4251),
    'HE22' : (0.6000, 0.1253, 0.4251),
    'C' : (1.9080, 0.2933, 0.5973),
    'O' : (1.6612, 0.4583, -0.5679)
    },
  'GLU' : {
    'N' : (1.8240, 0.4123, -0.5163),
    'H' : (0.6000, 0.1253, 0.2936),
    'CA' : (1.9080, 0.3308, 0.0397),
    'HA' : (1.3870, 0.1253, 0.1105),
    'CB' : (1.9080, 0.3308, 0.0560),
    'HB2' : (1.4870, 0.1253, -0.0173),
    'HB3' : (1.4870, 0.1253, -0.0173),
    'CG' : (1.9080, 0.3308, 0.0136),
    'HG2' : (1.4870, 0.1253, -0.0425),
    'HG3' : (1.4870, 0.1253, -0.0425),
    'CD' : (1.9080, 0.2933, 0.8054),
    'OE1' : (1.6612, 0.4583, -0.8188),
    'OE2' : (1.6612, 0.4583, -0.8188),
    'C' : (1.9080, 0.2933, 0.5366),
    'O' : (1.6612, 0.4583, -0.5819)
    },
  'GLY' : {
    'N' : (1.8240, 0.4123, -0.4157),
    'H' : (0.6000, 0.1253, 0.2719),
    'CA' : (1.9080, 0.3308, -0.0252),
    'HA2' : (1.3870, 0.1253, 0.0698),
    'HA3' : (1.3870, 0.1253, 0.0698),
    'C' : (1.9080, 0.2933, 0.5973),
    'O' : (1.6612, 0.4583, -0.5679)
    },
  'HID' : {
    'N' : (1.8240, 0.4123, -0.4157),
    'H' : (0.6000, 0.1253, 0.2719),
    'CA' : (1.9080, 0.3308, 0.0188),
    'HA' : (1.3870, 0.1253, 0.0881),
    'CB' : (1.9080, 0.3308, -0.0462),
    'HB2' : (1.4870, 0.1253, 0.0402),
    'HB3' : (1.4870, 0.1253, 0.0402),
    'CG' : (1.9080, 0.2933, -0.0266),
    'ND1' : (1.8240, 0.4123, -0.3811),
    'HD1' : (0.6000, 0.1253, 0.3649),
    'CE1' : (1.9080, 0.2933, 0.2057),
    'HE1' : (1.3590, 0.1225, 0.1392),
    'NE2' : (1.8240, 0.4123, -0.5727),
    'CD2' : (1.9080, 0.2933, 0.1292),
    'HD2' : (1.4090, 0.1225, 0.1147),
    'C' : (1.9080, 0.2933, 0.5973),
    'O' : (1.6612, 0.4583, -0.5679)
    },
  'HIE' : {
    'N' : (1.8240, 0.4123, -0.4157),
    'H' : (0.6000, 0.1253, 0.2719),
    'CA' : (1.9080, 0.3308, -0.0581),
    'HA' : (1.3870, 0.1253, 0.1360),
    'CB' : (1.9080, 0.3308, -0.0074),
    'HB2' : (1.4870, 0.1253, 0.0367),
    'HB3' : (1.4870, 0.1253, 0.0367),
    'CG' : (1.9080, 0.2933, 0.1868),
    'ND1' : (1.8240, 0.4123, -0.5432),
    'CE1' : (1.9080, 0.2933, 0.1635),
    'HE1' : (1.3590, 0.1225, 0.1435),
    'NE2' : (1.8240, 0.4123, -0.2795),
    'HE2' : (0.6000, 0.1253, 0.3339),
    'CD2' : (1.9080, 0.2933, -0.2207),
    'HD2' : (1.4090, 0.1225, 0.1862),
    'C' : (1.9080, 0.2933, 0.5973),
    'O' : (1.6612, 0.4583, -0.5679)
    },
  'HIP' : {
    'N' : (1.8240, 0.4123, -0.3479),
    'H' : (0.6000, 0.1253, 0.2747),
    'CA' : (1.9080, 0.3308, -0.1354),
    'HA' : (1.3870, 0.1253, 0.1212),
    'CB' : (1.9080, 0.3308, -0.0414),
    'HB2' : (1.4870, 0.1253, 0.0810),
    'HB3' : (1.4870, 0.1253, 0.0810),
    'CG' : (1.9080, 0.2933, -0.0012),
    'ND1' : (1.8240, 0.4123, -0.1513),
    'HD1' : (0.6000, 0.1253, 0.3866),
    'CE1' : (1.9080, 0.2933, -0.0170),
    'HE1' : (1.3590, 0.1225, 0.2681),
    'NE2' : (1.8240, 0.4123, -0.1718),
    'HE2' : (0.6000, 0.1253, 0.3911),
    'CD2' : (1.9080, 0.2933, -0.1141),
    'HD2' : (1.4090, 0.1225, 0.2317),
    'C' : (1.9080, 0.2933, 0.7341),
    'O' : (1.6612, 0.4583, -0.5894)
    },
  'HIS' : {
    'N' : (1.8240, 0.4123, -0.4157),
    'H' : (0.6000, 0.1253, 0.2719),
    'CA' : (1.9080, 0.3308, -0.0581),
    'HA' : (1.3870, 0.1253, 0.1360),
    'CB' : (1.9080, 0.3308, -0.0074),
    'HB2' : (1.4870, 0.1253, 0.0367),
    'HB3' : (1.4870, 0.1253, 0.0367),
    'CG' : (1.9080, 0.2933, 0.1868),
    'ND1' : (1.8240, 0.4123, -0.5432),
    'CE1' : (1.9080, 0.2933, 0.1635),
    'HE1' : (1.3590, 0.1225, 0.1435),
    'NE2' : (1.8240, 0.4123, -0.2795),
    'HE2' : (0.6000, 0.1253, 0.3339),
    'CD2' : (1.9080, 0.2933, -0.2207),
    'HD2' : (1.4090, 0.1225, 0.1862),
    'C' : (1.9080, 0.2933, 0.5973),
    'O' : (1.6612, 0.4583, -0.5679)
    },
  'ILE' : {
    'N' : (1.8240, 0.4123, -0.4157),
    'H' : (0.6000, 0.1253, 0.2719),
    'CA' : (1.9080, 0.3308, -0.0597),
    'HA' : (1.3870, 0.1253, 0.0869),
    'CB' : (1.9080, 0.3308, 0.1303),
    'HB' : (1.4870, 0.1253, 0.0187),
    'CG2' : (1.9080, 0.3308, -0.3204),
    'HG21' : (1.4870, 0.1253, 0.0882),
    'HG22' : (1.4870, 0.1253, 0.0882),
    'HG23' : (1.4870, 0.1253, 0.0882),
    'CG1' : (1.9080, 0.3308, -0.0430),
    'HG12' : (1.4870, 0.1253, 0.0236),
    'HG13' : (1.4870, 0.1253, 0.0236),
    'CD1' : (1.9080, 0.3308, -0.0660),
    'HD11' : (1.4870, 0.1253, 0.0186),
    'HD12' : (1.4870, 0.1253, 0.0186),
    'HD13' : (1.4870, 0.1253, 0.0186),
    'C' : (1.9080, 0.2933, 0.5973),
    'O' : (1.6612, 0.4583, -0.5679)
    },
  'LEU' : {
    'N' : (1.8240, 0.4123, -0.4157),
    'H' : (0.6000, 0.1253, 0.2719),
    'CA' : (1.9080, 0.3308, -0.0518),
    'HA' : (1.3870, 0.1253, 0.0922),
    'CB' : (1.9080, 0.3308, -0.1102),
    'HB2' : (1.4870, 0.1253, 0.0457),
    'HB3' : (1.4870, 0.1253, 0.0457),
    'CG' : (1.9080, 0.3308, 0.3531),
    'HG' : (1.4870, 0.1253, -0.0361),
    'CD1' : (1.9080, 0.3308, -0.4121),
    'HD11' : (1.4870, 0.1253, 0.1000),
    'HD12' : (1.4870, 0.1253, 0.1000),
    'HD13' : (1.4870, 0.1253, 0.1000),
    'CD2' : (1.9080, 0.3308, -0.4121),
    'HD21' : (1.4870, 0.1253, 0.1000),
    'HD22' : (1.4870, 0.1253, 0.1000),
    'HD23' : (1.4870, 0.1253, 0.1000),
    'C' : (1.9080, 0.2933, 0.5973),
    'O' : (1.6612, 0.4583, -0.5679)
    },
  'LYN' : {
    'N' : (1.8240, 0.4123, -0.4157),
    'H' : (0.6000, 0.1253, 0.2719),
    'CA' : (1.9080, 0.3308, -0.0721),
    'HA' : (1.3870, 0.1253, 0.0994),
    'CB' : (1.9080, 0.3308, -0.0485),
    'HB2' : (1.4870, 0.1253, 0.0340),
    'HB3' : (1.4870, 0.1253, 0.0340),
    'CG' : (1.9080, 0.3308, 0.0661),
    'HG2' : (1.4870, 0.1253, 0.0104),
    'HG3' : (1.4870, 0.1253, 0.0104),
    'CD' : (1.9080, 0.3308, -0.0377),
    'HD2' : (1.4870, 0.1253, 0.0116),
    'HD3' : (1.4870, 0.1253, 0.0116),
    'CE' : (1.9080, 0.3308, 0.3260),
    'HE2' : (1.1000, 0.1253, -0.0336),
    'HE3' : (1.1000, 0.1253, -0.0336),
    'NZ' : (1.8240, 0.4123, -1.0358),
    'HZ2' : (0.6000, 0.1253, 0.3860),
    'HZ3' : (0.6000, 0.1253, 0.3860),
    'C' : (1.9080, 0.2933, 0.5973),
    'O' : (1.6612, 0.4583, -0.5679)
    },
  'LYS' : {
    'N' : (1.8240, 0.4123, -0.3479),
    'H' : (0.6000, 0.1253, 0.2747),
    'CA' : (1.9080, 0.3308, -0.2400),
    'HA' : (1.3870, 0.1253, 0.1426),
    'CB' : (1.9080, 0.3308, -0.0094),
    'HB2' : (1.4870, 0.1253, 0.0362),
    'HB3' : (1.4870, 0.1253, 0.0362),
    'CG' : (1.9080, 0.3308, 0.0187),
    'HG2' : (1.4870, 0.1253, 0.0103),
    'HG3' : (1.4870, 0.1253, 0.0103),
    'CD' : (1.9080, 0.3308, -0.0479),
    'HD2' : (1.4870, 0.1253, 0.0621),
    'HD3' : (1.4870, 0.1253, 0.0621),
    'CE' : (1.9080, 0.3308, -0.0143),
    'HE2' : (1.1000, 0.1253, 0.1135),
    'HE3' : (1.1000, 0.1253, 0.1135),
    'NZ' : (1.8240, 0.4123, -0.3854),
    'HZ1' : (0.6000, 0.1253, 0.3400),
    'HZ2' : (0.6000, 0.1253, 0.3400),
    'HZ3' : (0.6000, 0.1253, 0.3400),
    'C' : (1.9080, 0.2933, 0.7341),
    'O' : (1.6612, 0.4583, -0.5894)
    },
  'MET' : {
    'N' : (1.8240, 0.4123, -0.4157),
    'H' : (0.6000, 0.1253, 0.2719),
    'CA' : (1.9080, 0.3308, -0.0237),
    'HA' : (1.3870, 0.1253, 0.0880),
    'CB' : (1.9080, 0.3308, 0.0342),
    'HB2' : (1.4870, 0.1253, 0.0241),
    'HB3' : (1.4870, 0.1253, 0.0241),
    'CG' : (1.9080, 0.3308, 0.0018),
    'HG2' : (1.3870, 0.1253, 0.0440),
    'HG3' : (1.3870, 0.1253, 0.0440),
    'SD' : (2.0000, 0.5000, -0.2737),
    'CE' : (1.9080, 0.3308, -0.0536),
    'HE1' : (1.3870, 0.1253, 0.0684),
    'HE2' : (1.3870, 0.1253, 0.0684),
    'HE3' : (1.3870, 0.1253, 0.0684),
    'C' : (1.9080, 0.2933, 0.5973),
    'O' : (1.6612, 0.4583, -0.5679)
    },
  'PHE' : {
    'N' : (1.8240, 0.4123, -0.4157),
    'H' : (0.6000, 0.1253, 0.2719),
    'CA' : (1.9080, 0.3308, -0.0024),
    'HA' : (1.3870, 0.1253, 0.0978),
    'CB' : (1.9080, 0.3308, -0.0343),
    'HB2' : (1.4870, 0.1253, 0.0295),
    'HB3' : (1.4870, 0.1253, 0.0295),
    'CG' : (1.9080, 0.2933, 0.0118),
    'CD1' : (1.9080, 0.2933, -0.1256),
    'HD1' : (1.4590, 0.1225, 0.1330),
    'CE1' : (1.9080, 0.2933, -0.1704),
    'HE1' : (1.4590, 0.1225, 0.1430),
    'CZ' : (1.9080, 0.2933, -0.1072),
    'HZ' : (1.4590, 0.1225, 0.1297),
    'CE2' : (1.9080, 0.2933, -0.1704),
    'HE2' : (1.4590, 0.1225, 0.1430),
    'CD2' : (1.9080, 0.2933, -0.1256),
    'HD2' : (1.4590, 0.1225, 0.1330),
    'C' : (1.9080, 0.2933, 0.5973),
    'O' : (1.6612, 0.4583, -0.5679)
    },
  'PRO' : {
    'N' : (1.8240, 0.4123, -0.2548),
    'CD' : (1.9080, 0.3308, 0.0192),
    'HD2' : (1.3870, 0.1253, 0.0391),
    'HD3' : (1.3870, 0.1253, 0.0391),
    'CG' : (1.9080, 0.3308, 0.0189),
    'HG2' : (1.4870, 0.1253, 0.0213),
    'HG3' : (1.4870, 0.1253, 0.0213),
    'CB' : (1.9080, 0.3308, -0.0070),
    'HB2' : (1.4870, 0.1253, 0.0253),
    'HB3' : (1.4870, 0.1253, 0.0253),
    'CA' : (1.9080, 0.3308, -0.0266),
    'HA' : (1.3870, 0.1253, 0.0641),
    'C' : (1.9080, 0.2933, 0.5896),
    'O' : (1.6612, 0.4583, -0.5748)
    },
  'SER' : {
    'N' : (1.8240, 0.4123, -0.4157),
    'H' : (0.6000, 0.1253, 0.2719),
    'CA' : (1.9080, 0.3308, -0.0249),
    'HA' : (1.3870, 0.1253, 0.0843),
    'CB' : (1.9080, 0.3308, 0.2117),
    'HB2' : (1.3870, 0.1253, 0.0352),
    'HB3' : (1.3870, 0.1253, 0.0352),
    'OG' : (1.7210, 0.4587, -0.6546),
    'HG' : (0.0000, 0.0000, 0.4275),
    'C' : (1.9080, 0.2933, 0.5973),
    'O' : (1.6612, 0.4583, -0.5679)
    },
  'THR' : {
    'N' : (1.8240, 0.4123, -0.4157),
    'H' : (0.6000, 0.1253, 0.2719),
    'CA' : (1.9080, 0.3308, -0.0389),
    'HA' : (1.3870, 0.1253, 0.1007),
    'CB' : (1.9080, 0.3308, 0.3654),
    'HB' : (1.3870, 0.1253, 0.0043),
    'CG2' : (1.9080, 0.3308, -0.2438),
    'HG21' : (1.4870, 0.1253, 0.0642),
    'HG22' : (1.4870, 0.1253, 0.0642),
    'HG23' : (1.4870, 0.1253, 0.0642),
    'OG1' : (1.7210, 0.4587, -0.6761),
    'HG1' : (0.0000, 0.0000, 0.4102),
    'C' : (1.9080, 0.2933, 0.5973),
    'O' : (1.6612, 0.4583, -0.5679)
    },
  'TRP' : {
    'N' : (1.8240, 0.4123, -0.4157),
    'H' : (0.6000, 0.1253, 0.2719),
    'CA' : (1.9080, 0.3308, -0.0275),
    'HA' : (1.3870, 0.1253, 0.1123),
    'CB' : (1.9080, 0.3308, -0.0050),
    'HB2' : (1.4870, 0.1253, 0.0339),
    'HB3' : (1.4870, 0.1253, 0.0339),
    'CG' : (0.0000, 0.0000, -0.1415),
    'CD1' : (1.9080, 0.2933, -0.1638),
    'HD1' : (1.4090, 0.1225, 0.2062),
    'NE1' : (1.8240, 0.4123, -0.3418),
    'HE1' : (0.6000, 0.1253, 0.3412),
    'CE2' : (1.9080, 0.2933, 0.1380),
    'CZ2' : (1.9080, 0.2933, -0.2601),
    'HZ2' : (1.4590, 0.1225, 0.1572),
    'CH2' : (1.9080, 0.2933, -0.1134),
    'HH2' : (1.4590, 0.1225, 0.1417),
    'CZ3' : (1.9080, 0.2933, -0.1972),
    'HZ3' : (1.4590, 0.1225, 0.1447),
    'CE3' : (1.9080, 0.2933, -0.2387),
    'HE3' : (1.4590, 0.1225, 0.1700),
    'CD2' : (1.9080, 0.2933, 0.1243),
    'C' : (1.9080, 0.2933, 0.5973),
    'O' : (1.6612, 0.4583, -0.5679)
    },
  'TYR' : {
    'N' : (1.8240, 0.4123, -0.4157),
    'H' : (0.6000, 0.1253, 0.2719),
    'CA' : (1.9080, 0.3308, -0.0014),
    'HA' : (1.3870, 0.1253, 0.0876),
    'CB' : (1.9080, 0.3308, -0.0152),
    'HB2' : (1.4870, 0.1253, 0.0295),
    'HB3' : (1.4870, 0.1253, 0.0295),
    'CG' : (1.9080, 0.2933, -0.0011),
    'CD1' : (1.9080, 0.2933, -0.1906),
    'HD1' : (1.4590, 0.1225, 0.1699),
    'CE1' : (1.9080, 0.2933, -0.2341),
    'HE1' : (1.4590, 0.1225, 0.1656),
    'CZ' : (1.9080, 0.2933, 0.3226),
    'OH' : (1.7210, 0.4587, -0.5579),
    'HH' : (0.0000, 0.0000, 0.3992),
    'CE2' : (1.9080, 0.2933, -0.2341),
    'HE2' : (1.4590, 0.1225, 0.1656),
    'CD2' : (1.9080, 0.2933, -0.1906),
    'HD2' : (1.4590, 0.1225, 0.1699),
    'C' : (1.9080, 0.2933, 0.5973),
    'O' : (1.6612, 0.4583, -0.5679)
    },
  'VAL' : {
    'N' : (1.8240, 0.4123, -0.4157),
    'H' : (0.6000, 0.1253, 0.2719),
    'CA' : (1.9080, 0.3308, -0.0875),
    'HA' : (1.3870, 0.1253, 0.0969),
    'CB' : (1.9080, 0.3308, 0.2985),
    'HB' : (1.4870, 0.1253, -0.0297),
    'CG1' : (1.9080, 0.3308, -0.3192),
    'HG11' : (1.4870, 0.1253, 0.0791),
    'HG12' : (1.4870, 0.1253, 0.0791),
    'HG13' : (1.4870, 0.1253, 0.0791),
    'CG2' : (1.9080, 0.3308, -0.3192),
    'HG21' : (1.4870, 0.1253, 0.0791),
    'HG22' : (1.4870, 0.1253, 0.0791),
    'HG23' : (1.4870, 0.1253, 0.0791),
    'C' : (1.9080, 0.2933, 0.5973),
    'O' : (1.6612, 0.4583, -0.5679)
    },
  'ACE' : {
    'HH31' : (1.4870, 0.1253, 0.1123),
    'CH3' : (1.9080, 0.3308, -0.3662),
    'HH32' : (1.4870, 0.1253, 0.1123),
    'HH33' : (1.4870, 0.1253, 0.1123),
    'C' : (1.9080, 0.2933, 0.5972),
    'O' : (1.6612, 0.4583, -0.5679)
    },
  'NME' : {
    'N' : (1.8240, 0.4123, -0.4157),
    'H' : (0.6000, 0.1253, 0.2719),
    'CH3' : (1.9080, 0.3308, -0.1490),
    'HH31' : (1.3870, 0.1253, 0.0976),
    'HH32' : (1.3870, 0.1253, 0.0976),
    'HH33' : (1.3870, 0.1253, 0.0976)
    },
  'NHE' : {
    'N' : (1.8240, 0.4123, -0.4630),
    'HN1' : (0.6000, 0.1253, 0.2315),
    'HN2' : (0.6000, 0.1253, 0.2315)
    }
  }
#ff atom data, default for unknown res
FFAtomData = {
  'C' : (1.9080, 0.2933, 0.5973),
  'CA' : (1.9080, 0.3308, -0.0249),
  'CB' : (1.9080, 0.3308, -0.0123),
  'CD' : (1.9080, 0.3308, 0.0486),
  'CD1' : (1.9080, 0.2933, -0.1638),
  'CD2' : (1.9080, 0.2933, -0.1256),
  'CE' : (1.9080, 0.3308, -0.0143),
  'CE1' : (1.9080, 0.2933, -0.0170),
  'CE2' : (1.9080, 0.2933, -0.1704),
  'CE3' : (1.9080, 0.2933, -0.2387),
  'CG' : (1.9080, 0.3126, 0.0162),
  'CG1' : (1.9080, 0.3308, -0.1811),
  'CG2' : (1.9080, 0.3308, -0.3192),
  'CH2' : (1.9080, 0.2933, -0.1134),
  'CH3' : (1.9080, 0.3308, -0.3662),
  'CZ' : (1.9080, 0.2933, 0.3226),
  'CZ2' : (1.9080, 0.2933, -0.2601),
  'CZ3' : (1.9080, 0.2933, -0.1972),
  'H' : (0.6000, 0.1253, 0.2719),
  'HA' : (1.3870, 0.1253, 0.0902),
  'HA2' : (1.3870, 0.1253, 0.0698),
  'HA3' : (1.3870, 0.1253, 0.0698),
  'HB' : (1.4870, 0.1253, 0.0043),
  'HB1' : (1.4870, 0.1253, 0.0603),
  'HB2' : (1.4870, 0.1253, 0.0352),
  'HB3' : (1.4870, 0.1253, 0.0352),
  'HD1' : (1.4090, 0.1225, 0.2062),
  'HD11' : (1.4870, 0.1253, 0.0593),
  'HD12' : (1.4870, 0.1253, 0.0593),
  'HD13' : (1.4870, 0.1253, 0.0593),
  'HD2' : (1.4090, 0.1225, 0.1239),
  'HD21' : (1.0435, 0.1253, 0.2598),
  'HD22' : (1.0435, 0.1253, 0.2598),
  'HD23' : (1.4870, 0.1253, 0.1000),
  'HD3' : (1.4370, 0.1253, 0.0506),
  'HE' : (0.6000, 0.1253, 0.3456),
  'HE1' : (1.3590, 0.1225, 0.1435),
  'HE2' : (1.1000, 0.1253, 0.1543),
  'HE21' : (0.6000, 0.1253, 0.4251),
  'HE22' : (0.6000, 0.1253, 0.4251),
  'HE3' : (1.2435, 0.1253, 0.0910),
  'HG' : (0.6000, 0.1253, 0.1933),
  'HG1' : (0.0000, 0.0000, 0.4102),
  'HG11' : (1.4870, 0.1253, 0.0791),
  'HG12' : (1.4870, 0.1253, 0.0514),
  'HG13' : (1.4870, 0.1253, 0.0514),
  'HG2' : (1.4870, 0.1253, 0.0249),
  'HG21' : (1.4870, 0.1253, 0.0791),
  'HG22' : (1.4870, 0.1253, 0.0791),
  'HG23' : (1.4870, 0.1253, 0.0791),
  'HG3' : (1.4870, 0.1253, 0.0249),
  'HH' : (0.0000, 0.0000, 0.3992),
  'HH11' : (0.6000, 0.1253, 0.4478),
  'HH12' : (0.6000, 0.1253, 0.4478),
  'HH2' : (1.4590, 0.1225, 0.1417),
  'HH21' : (0.6000, 0.1253, 0.4478),
  'HH22' : (0.6000, 0.1253, 0.4478),
  'HH31' : (1.4870, 0.1253, 0.1123),
  'HH32' : (1.4870, 0.1253, 0.1123),
  'HH33' : (1.4870, 0.1253, 0.1123),
  'HN' : (0.6000, 0.1253, 0.2719),
  'HN1' : (0.6000, 0.1253, 0.2315),
  'HN2' : (0.6000, 0.1253, 0.2315),
  'HZ' : (1.4590, 0.1225, 0.1297),
  'HZ1' : (0.6000, 0.1253, 0.3400),
  'HZ2' : (0.6000, 0.1253, 0.3400),
  'HZ3' : (0.6000, 0.1253, 0.3400),
  'N' : (1.8240, 0.4123, -0.4157),
  'ND1' : (1.8240, 0.4123, -0.3811),
  'ND2' : (1.8240, 0.4123, -0.9191),
  'NE' : (1.8240, 0.4123, -0.5295),
  'NE1' : (1.8240, 0.4123, -0.3418),
  'NE2' : (1.8240, 0.4123, -0.4261),
  'NH1' : (1.8240, 0.4123, -0.8627),
  'NH2' : (1.8240, 0.4123, -0.8627),
  'NZ' : (1.8240, 0.4123, -0.7106),
  'O' : (1.6612, 0.4583, -0.5679),
  'OD1' : (1.6612, 0.4583, -0.5931),
  'OD2' : (1.6911, 0.4585, -0.7195),
  'OE1' : (1.6612, 0.4583, -0.6086),
  'OE2' : (1.6911, 0.4585, -0.7350),
  'OG' : (1.7210, 0.4587, -0.6546),
  'OG1' : (1.7210, 0.4587, -0.6761),
  'OH' : (1.7210, 0.4587, -0.5579),
  'SD' : (2.0000, 0.5000, -0.2737),
  'SG' : (2.0000, 0.5000, -0.3119)
  }
#ff data by element, default for unknown res and atom
FFElementData = {
  'H' : (0.6000, 0.1253, 0.0000),
  'O' : (1.6612, 0.4583, 0.0000),
  'C' : (1.9080, 0.2933, 0.0000),
  'N' : (1.8240, 0.4123, 0.0000),
  'S' : (2.0000, 0.5000, 0.0000),
  'P' : (2.1000, 0.4472, 0.0000),
  'Li' : (1.1370, 0.1353, 0.0000),
  'K' : (2.6580, 0.0181, 0.0000),
  'Rb' : (2.9560, 0.0130, 0.0000),
  'Cs' : (3.3950, 0.0090, 0.0000),
  'I' : (2.3500, 0.6325, 0.0000),
  'F' : (1.7500, 0.2470, 0.0000),
  '*' : (2.0000, 0.3000, 0.0000)
  }

#ff data for backbone torsions, taken from ff96
#each consecutive three in the array gives
#V, n, a where the dihedral potential is given by
#a sum over the different terms for the equation
#V * (1 + cos(n*ang - a)).  All units are given
#in degrees.
FFDihPhi = array([[0.3, 2., 180.], [0.85, 1.0, 0.]], float)
FFDihPsi = array([[0.3, 2., 180.], [0.85, 1.0, 0.]], float)


#secondary structure assignments;
#a list of types with (Label, NLocal, [(MinPhi1, MaxPhi1, MinPsi1, MaxPsi1), ...], ContMapTmpl) 
SSTypes = [["HHHHH", 5,
            [(-180,180,-90,60),(-180,0,-90,60),(-180,0,-90,60),
             (-180,0,-90,60),(-180,0,-180,180)],
            array([[0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [-1, 0, 0, 0, 0],
                   [1, 0, 0, 0, 0]], int)],
           ["EEEEEE", 3,
            [(-180,180,-180,180),(-180,0,0,180),(-180,180,-180,180),
             (-180,180,-180,180),(-180,0,0,180),(-180,180,-180,180)],
            array([[0,  0, 0, 0,  0, 1],
                   [0,  0, 0, 0, -1, 0],
                   [0,  0, 0, 1,  0, 0],
                   [0,  0, 1, 0,  0, 0],
                   [0, -1, 0, 0,  0, 0],
                   [1,  0, 0, 0,  0, 0]], int)],
           [" E EEE", 3,
            [(-180,180,-180,180),(-180,0,0,180),(-180,180,-180,180),
             (-180,180,-180,180),(-180,0,0,180),(-180,180,-180,180)],
            array([[ 0,  0,  0, -1,  0,  0],
                   [ 0,  0,  0,  1, -1,  0],
                   [ 0,  0,  0,  0,  0, -1],
                   [-1,  0,  0,  0,  0,  0],
                   [ 0, -1,  0,  0,  0,  0],
                   [ 0,  1, -1,  0,  0,  0]], int)],
           ["GGGG", 4,
            [(-180,180,-36,-16),(-59,-39,-36,-16),
             (-59,-39,-36,-16),(-59,-39,-180,180),],
            array([[0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [1, 0, 0, 0]], int)],
           ["IIIIII", 6,
            [(-180,180,-80,-60),(-65,-45,-80,-60),(-65,-45,-80,-60),
             (-65,-45,-80,-60),(-65,-45,-80,-60),(-65,-45,-180,180)],
            array([[0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [1, 0, 0, 0, 0, 0]], int)],
           [" EEEE ", 3,
            [(-180,180,-180,180),(-180,0,0,180),(-180,180,-180,180),
             (-180,180,-180,180),(-180,0,0,180),(-180,180,-180,180)],
            array([[ 0,  0,  0,  0,  0,  0],
                   [ 0,  0,  0,  0, -1,  0],
                   [ 0,  0,  0,  1,  0,  0],
                   [ 0,  0,  1,  0,  0,  0],
                   [ 0, -1,  0,  0,  0,  0],
                   [ 1,  0,  0,  0,  0,  0]], int)],
           ["EE  EE", 3,
            [(-180,180,-180,180),(-180,0,0,180),(-180,180,-180,180),
             (-180,180,-180,180),(-180,0,0,180),(-180,180,-180,180)],
            array([[ 0,  0,  0,  0,  0,  1],
                   [ 0,  0,  0,  0, -1,  0],
                   [ 0,  0,  0,  0,  0,  0],
                   [ 0,  0,  1,  0,  0,  0],
                   [ 0, -1,  0,  0,  0,  0],
                   [ 1,  0,  0,  0,  0,  0]], int)],
           ["EE  EE", 3,
            [(-180,180,-180,180),(-180,0,0,180),(-180,180,-180,180),
             (-180,180,-180,180),(-180,0,0,180),(-180,180,-180,180)],
            array([[ 0,  0,  0,  0,  0,  1],
                   [ 0,  0,  0,  0, -1,  0],
                   [ 0,  0,  0,  1,  0,  0],
                   [ 0,  0,  0,  0,  0,  0],
                   [ 0, -1,  0,  0,  0,  0],
                   [ 1,  0,  0,  0,  0,  0]], int)],
           [" EEEE ", 3,
            [(-180,180,-180,180),(-180,0,0,180),(-180,180,-180,180),
             (-180,180,-180,180),(-180,0,0,180),(-180,180,-180,180)],
            array([[ 0,  0,  0,  0,  0,  1],
                   [ 0,  0,  0,  0, -1,  0],
                   [ 0,  0,  0,  1,  0,  0],
                   [ 0,  0,  1,  0,  0,  0],
                   [ 0, -1,  0,  0,  0,  0],
                   [ 0,  0,  0,  0,  0,  0]], int)]           
          ]


#ramachandran map probabilities;
#built from a histogram from a glycine simulation
RamaProb = array(
 [[0.0014, 0.0004, 0.0002, 0.0001, 0.0001, 0.0001, 0.0003, 0.0003, 0.0003, 0.0003, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0001, 0.0002, 0.0004, 0.0010, 0.0018, 0.0031, 0.0040, 0.0032],
  [0.0086, 0.0029, 0.0010, 0.0006, 0.0006, 0.0007, 0.0014, 0.0020, 0.0020, 0.0008, 0.0003, 0.0001, 0.0000, 0.0000, 0.0002, 0.0002, 0.0006, 0.0007, 0.0012, 0.0025, 0.0053, 0.0101, 0.0168, 0.0218, 0.0174],
  [0.0152, 0.0058, 0.0025, 0.0013, 0.0011, 0.0016, 0.0031, 0.0049, 0.0038, 0.0015, 0.0005, 0.0003, 0.0002, 0.0003, 0.0007, 0.0008, 0.0012, 0.0019, 0.0032, 0.0055, 0.0106, 0.0192, 0.0289, 0.0359, 0.0298],
  [0.0100, 0.0039, 0.0017, 0.0014, 0.0015, 0.0016, 0.0028, 0.0034, 0.0027, 0.0014, 0.0008, 0.0002, 0.0002, 0.0006, 0.0007, 0.0009, 0.0015, 0.0014, 0.0028, 0.0053, 0.0079, 0.0138, 0.0207, 0.0251, 0.0198],
  [0.0057, 0.0024, 0.0010, 0.0005, 0.0007, 0.0011, 0.0013, 0.0023, 0.0022, 0.0009, 0.0008, 0.0005, 0.0004, 0.0006, 0.0005, 0.0006, 0.0010, 0.0012, 0.0017, 0.0026, 0.0049, 0.0078, 0.0097, 0.0117, 0.0096],
  [0.0041, 0.0017, 0.0006, 0.0005, 0.0003, 0.0007, 0.0011, 0.0017, 0.0022, 0.0017, 0.0010, 0.0010, 0.0005, 0.0005, 0.0005, 0.0006, 0.0007, 0.0012, 0.0021, 0.0028, 0.0043, 0.0061, 0.0070, 0.0092, 0.0065],
  [0.0057, 0.0017, 0.0006, 0.0002, 0.0003, 0.0003, 0.0013, 0.0032, 0.0054, 0.0045, 0.0037, 0.0020, 0.0012, 0.0005, 0.0003, 0.0006, 0.0013, 0.0021, 0.0031, 0.0052, 0.0076, 0.0093, 0.0134, 0.0140, 0.0105],
  [0.0041, 0.0008, 0.0003, 0.0001, 0.0001, 0.0007, 0.0017, 0.0053, 0.0116, 0.0134, 0.0089, 0.0036, 0.0011, 0.0005, 0.0002, 0.0002, 0.0009, 0.0019, 0.0041, 0.0078, 0.0143, 0.0195, 0.0250, 0.0228, 0.0128],
  [0.0013, 0.0002, 0.0000, 0.0000, 0.0000, 0.0001, 0.0013, 0.0059, 0.0153, 0.0165, 0.0084, 0.0016, 0.0003, 0.0001, 0.0001, 0.0000, 0.0002, 0.0004, 0.0010, 0.0057, 0.0118, 0.0191, 0.0223, 0.0166, 0.0056],
  [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0007, 0.0025, 0.0066, 0.0051, 0.0014, 0.0001, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0002, 0.0013, 0.0037, 0.0058, 0.0056, 0.0024, 0.0005],
  [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0001, 0.0007, 0.0009, 0.0006, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0003, 0.0006, 0.0006, 0.0003, 0.0000, 0.0000],
  [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0001, 0.0001, 0.0001, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0001, 0.0000, 0.0000, 0.0000],
  [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0001, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
  [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0001, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
  [0.0000, 0.0000, 0.0000, 0.0001, 0.0001, 0.0000, 0.0001, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0001, 0.0001, 0.0001, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
  [0.0000, 0.0000, 0.0001, 0.0003, 0.0003, 0.0003, 0.0003, 0.0001, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
  [0.0001, 0.0003, 0.0002, 0.0002, 0.0002, 0.0003, 0.0003, 0.0002, 0.0001, 0.0001, 0.0000, 0.0001, 0.0000, 0.0001, 0.0001, 0.0001, 0.0001, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0001],
  [0.0000, 0.0000, 0.0001, 0.0000, 0.0001, 0.0001, 0.0000, 0.0001, 0.0001, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
  [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0001, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
  [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
  [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
  [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
  [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
  [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
  [0.0001, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0001, 0.0002, 0.0002, 0.0003, 0.0002]
 ], float)
RamaNPhi, RamaNPsi = RamaProb.shape
RamaDPhi = 360. / RamaNPhi
RamaDPsi = 360. / RamaNPsi
RamaProb += 1.e-8
RamaProb = RamaProb / RamaProb.sum()
