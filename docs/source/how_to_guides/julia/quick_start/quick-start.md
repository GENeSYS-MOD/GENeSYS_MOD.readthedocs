# Quick Start

## Installation

1.	We suggest using [Visual Studio Code](https://code.visualstudio.com/).

2.	Download the latest stable version of [the Julia Programming Language (julialang.org)](https://julialang.org/downloads/).

3.	Install Julia extension in Visual Studio Code:
  * Click 'Extensions' buttion in Visual Studio Code on the left ribbon.
  * Search for 'Julia', then install. 

4.	Download an optimization solver and get a license:
  *	Gurobi
    - Academic licensed are issued by [Gurobi](https://www.gurobi.com/academia/academic-program-and-licenses/).
    - Commercial License.
  *	[CPLEX](https://www.ibm.com/products/ilog-cplex-optimization-studio/cplex-optimizer)
  *	[HiGHS](https://highs.dev/), open source solver.

5.  Open the Julia REPL by using the Alt+J+O command. The REPL(read-eval-print loop) is the interactive command line interface in Julia.

6.	Install packages in Visual Studio:
  *	In the REPL terminal, type ']' to change to enter pkg mode
  * Type 'add <package>', where package is equal to:
    - GENeSYSMOD
    - JuMP
    - Dates
    - XLSX
    - DataFrames
    - CSV	
    - Ipopt
    - *(your chosen solver)*

7.	You have now installed all packages necessary to run GENeSYS-MOD and can run a case by using the genesysmod function. Examples can be found in the tests.

## Running a case

Create a folder where you will be able to store your scripts, inputs and outputs of the model. 

For simply running the model without modifying the model or constraints, use:
```julia
using GENeSYSMOD
```

You can then run the model by running the function `genesysmod` with the appropriate `Switches` (see documentation here: [Switches](/how_to_guides/julia/user_guide/switches)).

## Example script

You can use the following example script to then run GENeSYS-MOD with the open solvers HiGHS and Ipopt:

```julia
using GENeSYSMOD
using HiGHS
using Ipopt

solver = HiGHS.Optimizer

const TEST_RESULTS_DIR = joinpath(pkgdir(GENeSYSMOD),"test","TestData","Results")

model, data = genesysmod(;elmod_daystep = 80, elmod_hourstep = 4, solver=solver, DNLPsolver = Ipopt.Optimizer, threads=0,
inputdir = joinpath(pkgdir(GENeSYSMOD),"test","TestData","Inputs"),
resultdir = pwd(),
data_file="RegularParameters_testdata",
hourly_data_file = "Timeseries_testdata",
switch_infeasibility_tech = NoInfeasibilityTechs(),
switch_investLimit=1,
switch_ccs=1,
switch_ramping=0,
switch_weighted_emissions=1,
switch_intertemporal=0,
switch_base_year_bounds = 0,
switch_peaking_capacity = 0,
set_peaking_slack = 0,
set_peaking_minrun_share = 0,
set_peaking_res_cf = 0,
set_peaking_startyear = 2025,
switch_peaking_with_storages = 0,
switch_peaking_with_trade = 0,
switch_peaking_minrun = 0,
switch_employment_calculation = 0,
switch_endogenous_employment = 0,
employment_data_file = "",
elmod_starthour = 0,
elmod_dunkelflaute= 0,
#switch_raw_results = CSVResult(),
switch_raw_results = TXTandCSV("result_test"),
switch_processed_results = 1,
write_reduced_timeserie = 1,
model_region="europe"
);
```

## Using the published dataset

A dataset is published on the repository GENeSYS-MOD.data: (https://github.com/GENeSYS-MOD/GENeSYS_MOD.data)
This repository contains the data including the sources and assumptions necessay to run the model at a european level with a country resolution. Data for over regions may be added with time. 
It also contains the tools necessary to produce the input file for the model from this data. The tools are accessed via a jupyter notebook script. More information can be found on the repository.

You can directly retrieve preprocessed datafiles that are part of releases of the data repository for the main geographic scopes and storylines. To do this you can use the `fetch_data_release` function.

It is also possible to use the function `update_and_process_data` to automatically clone the data repository if needed, pull the latest changes and create the input files based on your own requirements of e.g. countries, and technologies to include, defined in the file `Set_filter_files.xlsx`. In order to do this, you first need to copy the file CondaPkg.toml to your work directory and add a call to CondaPkg to your code:
```julia
using CondaPkg
```

## Installation for advanced users

If you want to develop GENeSYS-MOD and/or change features, add equations, etc., then working with the package installation might not be the best option. For a guide on a more advanced installation, refer to the [User Manual](/how_to_guides/julia/user_guide/local_develop).