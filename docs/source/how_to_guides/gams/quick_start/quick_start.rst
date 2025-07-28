GAMS Quick Start Guide
======================

This page serves as a first help install the General Algebraic Modelling System (GAMS) on your machine
and setting up GENeSYS-MOD.gms in a way to start your first model run.

GAMS Installation
-----------------

This page refers to the GAMS version of GENeSYS-MOD. Therefore, the first step is to install GAMS on your machine. GAMS is an
algebraic modeling language designed to solve mathematical optimization and equilibrium problems. The
language makes it possible to write as close as possible to the respective mathematical equivalents and saves
the user the learning of a special syntax and programming. Compared to other classic programming languages,
learning GAMS is easily possible if you have the mathematical formulation on hand. In general, GAMS
consists of a compiler and a multitude of different solution algorithms, which can be used depending on the
modelling. GAMS also comed with its own development engine / user interface (GAMS Studio).

The most recent version of GAMS can be retrieved from their website (www.gams.com). It is available for MS
Windows (32, 64 Bit), MacOS, and Linux (both 64 Bit). GAMS has a free licensed version, but it is limited
to some solvers and, more importantly, to only a small number of variables and elements. AS GENeSYS-MOD
is focused on large-scale energy system models, you will likely need to obtain a license for GAMS. Solver-side, the use of open source solvers is possible, but larger and more complex model setups will require a commercial solver as well.

.. note::

   GENeSYS-MOD uses the command-line tool gdxxrw.exe, which is provided by GAMS, to read and convert
   Excel-files (.xls and .xlsx) to GAMS Data Exchange (.gdx) files. Unfortunately, this command-line tool is only working a DOS/Windows environment
   and cannot be used in Unix systems (Linux/Mac) without the usage of a emulation software (e.g., Wine for
   Linux). Therefore, you either need to run GENeSYS-MOD under a Windows environment, or you need to
   transform Excel-files to .gdx-files with other tools (e.g., with the exceltogdx-package for python).

For a general documentation of GAMS, as well as GAMS Studio and their features, please refer to the GAMS website.

Running GENeSYS-MOD.gms
------------------------


The Middle-Earth test data set
------------------------------


Result analysis
---------------

Further information
-------------------

For a full list of options (frequently called switches in GENeSYS-MOD), please refer to the full user guide. For more information on the inputs and outputs of GENeSYS-MOD, as well as the structure, please refer to the mathematical formulation.