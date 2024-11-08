# Functional specification

## Background
CRISPR-based activation and interference (CRISPRai) allows us to regulate metabolism by up-regulating and down-regulating gene expression based on guide-RNA (gRNA) targeting.
In order to build large-scale genetic circuits, understanding and modeling the effects of multiple gRNA interactions is important.

## User profile
The package is usable by researchers and bioengineers in the space of CRISPR-based genetic circuits.
- User understands and can program in python
- User understands basic CRISPR-based activation and interference technology
- User udnerstands basic principles of genetic circuits

## Usecases
1. The user intends to understand the expression of their target gene based on the number of gRNA competitors in the system
2. The user intends to understand the expression of their target gene based on regulating the expression of CRISPRai machinery, primarily dCas9 and Activator-protein

## Expectation
1. The user should expect an I/O plot describing the expression of target gene based on changing the expression of their CRISPRai machinery
2. The user should expect the I/O plot to change depending when changing different parameters to understand underlying circuit changes.

