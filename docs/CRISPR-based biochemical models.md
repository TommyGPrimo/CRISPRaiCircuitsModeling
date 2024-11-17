# CRISPR-based biochemical models
The ordinary differential equations (ODEs) used to generate the models in this package are referenced below. Originally written in Matlab and converted to tellurium.
This document briefly explains each biochemical model for ease of understanding each model.

## CRISPRa modality one
This model of CRISPRa is composed of an activator fused to the dCas9 machinery and allows to model input and output response for controlling concentration of the single machinery complex

**Chemical Reactions**
1. $R1: d + s_i \xleftrightarrow[k_i^-]{k_i^+}A_{1,i}$
2. $R2: A_{1,i} + D_i \xleftrightarrow[l_i^-]{l_i^+} c_i$
3. $R3: c_i \xrightarrow{\kappa_i} Y_i + c_i$

*Chemical reaction Explanation*
- Reaction #1 specifies dCas9 concentration with gRNA concentration to form the activator complex $A$ based on coupling and decoupling kinetics $k$
- Reaction #2 specifies the activator complex $A$ and the target DNA to form a transcriptional/translational complex $c$ based on binding and unbinding kinetics $l$
- Reaction #3 specifies the transcriptional/translational complex $c$ to produce the protein $Y$ while still having the complex $c$ bound with production rate $\kappa$

**Kinetic Equations**
1. $\dot{s_i} = u_i + {k_i^-}*A_{1,i} - {k_i^+}ds_i - \delta s_i$
2. $\dot{A_{1,i}} = {k_i^+}ds_i - {k_i^-}*A_{1,i} + {l_i^-} c_i - {l_i^+}A_{1,i}D_i$
3. $\dot{c_i} = {l_i^+}A_{1,i}D_i - {l_i^-} c_i$
4. $\dot{Y_i} = \kappa c_i - \gamma Y_i$

### dCas9 and DNA
The total concentration of dCas9 and target DNA in this system is conserved
- The total concentration of dCas9 is: $d_t = d + \sum_{i=1}^{N}A_{1,i} + \sum_{i=1}^{N}c_i$
- The total concentration of DNA is: $D_{it} = D_i + c_i$


## CRISPRa modality two

