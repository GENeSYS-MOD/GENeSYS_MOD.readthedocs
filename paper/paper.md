---
title: 'The Global Energy System Model (GENeSYS-MOD) v4.0 - A Flexible Energy System Modelling Framework for Julia and GAMS'
tags:
  - energy system modelling
  - optimization
  - long-term energy transition analysis
  - GAMS
  - Julia
  
authors:
  - name: Konstantin Löffler
    orcid: 0000-0002-5435-1880
    corresponding: true # (This is how to denote the corresponding author)
    affiliation: "1, 2" # (Multiple affiliations must be quoted)
  - name: Stian Backe
    orcid: 0000-0002-7330-772X
    affiliation: "2, 3"
  - name: Julian Bornemann
    affiliation: 1
  - name: Alena Diesing
	affiliation: 1
  - name: Karlo Hainsch
    affiliation: 1
  - name: Jonathan Hanto
    affiliation: "1, 4"
  - name: Philipp Herpich
    affiliation: "1, 4"
  - Name: Nikita Moskalenko
    affiliation: 1
  - name: Dimitri Pinel
    affiliation: 3
  - name: Martha Pedersen
	affiliation: 3
  - name: Dana Reulein
    affiliation: 4
  - name: Shweta Tiwari
    affiliation: 3
	
affiliations:
  - name: Technische Universität Berlin, Workgroup for Infrastructure Policy (WIP), Straße des 17. Juni 135, 10623 Berlin, Germany
    index: 1
  - name: Norwegian University of Science and Technology, Department of Industrial Economics and Technology Management (IØT), Alfred Getz vei 3, 7491 Trondheim, Norway
    index: 2
  - name: SINTEF Energy Research, Energy Systems Department, Sem Sælands vei 11, 7034 Trondheim
    index: 3
  - name: Norwegian University of Science and Technology, Department of Electric Energy (IEL), O. S. Bragstads plass 2E, 7491 Trondheim, Norway
    index: 4
	
	
date: 17 May 2025
bibliography: paper.bib

---

# Summary

GENeSYS-MOD is a flexible framework to model energy systems at various degrees of detail, with a focus on sector coupling and the computation of long-term pathways for the energy system.  

# Statement of need

Energy system models are powerful tools that can help answer 
The Global Energy System Model (GENeSYS-MOD) has been 

# General framework structure

Single dollars ($) are required for inline mathematics e.g. $f(x) = e^{\pi/x}$

Double dollars make self-standing equations:

$$\Theta(x) = \left\{\begin{array}{l}
0\textrm{ if } x < 0\cr
1\textrm{ else}
\end{array}\right.$$

You can also use plain \LaTeX for equations
\begin{equation}\label{eq:fourier}
\hat f(\omega) = \int_{-\infty}^{\infty} f(x) e^{i\omega x} dx
\end{equation}
and refer to \autoref{eq:fourier} from text.

## Overview over the functionality and capabilities of GENeSYS-MOD

Figure \autoref{fig:inputs_outputs} shows some of the core inputs and outputs of the model.
![Main inputs and outputs of GENeSYS-MOD.](GENeSYS-MOD_inputs_outputs.png)

## Methodology background




# New features of GENeSYS-MOD version 4

Figure \autoref{fig:version_blocks} displays the additions across multiple major versions of GENeSYS-MOD.
![Functionality additions of major GENeSYS-MOD versions.](genesysmod_blocks_v4.pdf)

## 

## 

## 

# Applications



Citations to entries in paper.bib should be in
[rMarkdown](http://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html)
format.

If you want to cite a software repository URL (e.g. something on GitHub without a preferred
citation) then you can do it with the example BibTeX entry below for.

For a quick reference, the following citation commands can be used:
- `@author:2001`  ->  "Author et al. (2001)"
- `[@author:2001]` -> "(Author et al., 2001)"
- `[@author1:2001; @author2:2001]` -> "(Author1 et al., 2001; Author2 et al., 2002)"

# Perspective



# Acknowledgements

We would like to thank everyone that has been involved in this project over the years, especially Thorsten Burandt, who has been one of the original co-creators of the framework, as well as Pao-Yu Oei and Christian von Hirschhausen who have guided us over the years. A special thanks also goes out to everyone that keeps contributing and using our tool, and provides valuable feedback for us. We also acknowledge funding from TU Berlin and SINTEF Energy Research, which has enabled us to work on the topic, as well as several research projects that have made contributions to the further development of the framework and surrounding tools. This work was supported by the CETPartnership project Man0EUvRE under Grant Agreement number 101069750 as well as the Horizon Europe project iDesignRES (GA number 101095849).

# References