<< FILES
# gamma attenuation data
absorp  ../../nuclear_data/decay/abs_2012

# index of nuclides to be included
ind_nuc  ../../nuclear_data/TENDL2017data/tendl17_decay12_index

# Library cross section data
enbins ../../nuclear_data/ebins/ebins_162
xs_endf ../../nuclear_data/TENDL2017data/tal2017-a/gxs-162

# Binary cross section data
xs_endfb ../../nuclear_data/bin/tal2017-a.bin

# Library probability tables for self-shielding
prob_tab  ../../nuclear_data/TENDL2017data/tal2017-n/tp-709-294

# fluxes
fluxes  fluxes
arb_flux  spectra

# Library decay data
dk_endf ../../nuclear_data/decay/decay_2012

# Library fission  data
fy_endf ../../nuclear_data/UKFY41data/ukfy4_1a

# Spontaneous fission data
sf_endf ../../nuclear_data/GEFY61data/gefy61_sfy

# Library regulatory data
hazards ../../nuclear_data/decay/hazards_2012
clear   ../../nuclear_data/decay/clear_2012
a2data  ../../nuclear_data/decay/a2_2012

# collapsed cross section data (in and out)
collapxi  COLLAPX
collapxo  COLLAPX

# condensed decay and fission data (in and out)
arrayx  ARRAYX
>>

<< -----condense decay data----- >>
CLOBBER
PROJ 4
SPEK
GETDECAY 1
FISPACT
* TENDL gxs-162: alpha   1 MeV - 200 MeV
END
* END OF RUN

