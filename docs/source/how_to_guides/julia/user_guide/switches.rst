Switches
==============

.. _switches-julia:

The list below provides a list of all available settings / switches for GENeSYS-MOD that are given to the user as a default.

.. list-table::
   :header-rows: 1
   :widths: 26 14 8 48

   * - Name
     - Options
     - Default
     - Description
   * - **General settings**
     -
     -
     -
   * - data_file
     - *[string]*
     -
     - The data file to use for the calculations (can be overwritten if using a pre-defined scenario option)
   * - hourly_data_file
     - *[string]*
     -
     - The timeseries file to use for the calculations (can be overwritten if using a pre-defined scenario option)
   * - model_region
     - *[string]*
     -
     - Name of the modeled region (relevant for the use of a region-specific scenario data file)
   * - data_base_region
     - *[string]*
     -
     - Name of the base region of the modeled region (the base region will be used to populate missing data)
   * - year
     - *[string]*
     - 2018
     - The start-year of the modelling horizon
   * - emissionPathway
     - *[string]*
     -
     - Name of the scenario / pathway to compute
   * - emissionScenario
     - *[string]*
     -
     - Additional scenario information, e.g. for distribution purposes
   * - **Timeseries reduction**
     -
     -
     -
   * - timeseries_method
     - *[elmod]*
     - elmod
     - Chooses the timeseries reduction method. Currently, only elmod is implemented
   * - elmod_nthhour
     - *[integer]*
     - 484
     - Defined the step-size for the timeseries reduction algorithm. Good choices include 784, 484, 244, 122, 73, 25. Lower numbers will lead to more time slices and more computational requirements
   * - elmod_starthour
     - *[integer]*
     - 8
     - Determines the start-hour of the timeseries reduction algorithm
   * - elmod_dunkelflaute
     - *[0,1]*
     - 0
     - Enables / disables injection of an artificial "Dunkelflaute" into the timeseries
   * - **Data input/output**
     -
     -
     -
   * - switch_test_data_load
     - *[0,1]*
     - 0
     - If enabled, the code will just perform a test loading of all data and terminate before the equations are constructed
   * - switch_only_load_gdx
     - *[0,1]*
     - 0
     - If enabled, the model will just read in the data in .gdx format and not attempt to read from the Excel file
   * - switch_unixPath
     - *[0,1]*
     - 0
     - Determines the structure of the directory paths. Needs to be 1 for Unix-based systems (e.g. Mac OS, Linux) and 0 for Windows
   * - switch_read_data_long
     - *[0,1]*
     - 1
     - Determines the data structure, the codes assumes to read. 1 assumes tables in long format, 0 assumes tables in wide format
   * - switch_write_output
     - *[gdx,csv,xls]*
     - gdx
     - Type of output files to be created. For single runs, csv or xls is recommended. If multiple runs should be compared, using .gdx and then merging it with the script in the results folder is recommended
   * - switch_only_write_results
     - *[0,1]*
     - 0
     - Reads in a result gdx file and outputs the results as e.g. xls without re-computation
   * - **Technical settings**
     -
     -
     -
   * - solver
     - *[lp solver]*
     - cplex
     - Choice of LP solver for the model
   * - threads
     - *[integer]*
     - 6
     - Number of threads to be used. Can also be 0 (all available threads) or an offset (e.g. -2 will use all but two available threads)
   * - **Debugging**
     -
     -
     -
   * - switch_investLimit
     - *[0,1]*
     - 1
     - Enables / disables "smoothing constraints" that make results more realistic. Only disable for debugging
   * - switch_infeasibility_tech
     - *[0,1]*
     - 0
     - Enables / disables the infeasibility technologies that can provide unmet demand at very high cost. Only enable for debugging if model is infeasible
   * - switch_base_year_bounds
     - *[0,1]*
     - 1
     - Enables / disables the base year calibration
   * - switch_base_year_bounds_debugging
     - *[0,1]*
     - 0
     - Enables / disables a slack for the base year calibration. Only enable for debugging
   * - **Features / functionality options**
     -
     -
     -
   * - switch_ccs
     - *[0,1]*
     - 1
     - Enables / disables Carbon Capture and Storage (CCS) in the model
   * - switch_ramping
     - *[0,1]*
     - 0
     - Enables / disables ramping requirements for technologies
   * - switch_short_term_storage
     - *[0,1]*
     - 1
     - Chooses the kind of storage formulation. For elmod-timeseries, 1 is required
   * - switch_all_regions
     - *[0,1]*
     - 1
     - If set to 1, the model will consider all regions, if set to 0, only the first 4-5 regions will be considered. This is for testing purposes only
   * - switch_aggregate_region
     - *[0,1]*
     - 0
     - If set to 1, the model will aggregate all regions into one single region. For calibration purposes only
   * - switch_intertemporal
     - *[0,1]*
     - 0
     - If set to 1, the model will consider age-appropriate efficiencies of technologies, but at increased computational complexity
   * - switch_weighted_emissions
     - *[0,1]*
     - 1
     - If set to 1, emissions will be weighted between two modeled years to determine the overall emissions (relevant for emission budget calculations)
   * - set_symmetric_transmission
     - *[share,0-1]*
     - 0.9
     - Determines the build-out of electricity transmission lines. 0 means the model can completely freely decide, a 1 would mean full symmetric build-out
   * - switch_hydrogen_blending_share
     - *[share,0-1]*
     - 1
     - The amount of hydrogen allowed in natural gas pipelines (as a share)
   * - set_storagelevelstart_up
     - *[share,0-1]*
     - 0.75
     - The upper bound for the start-level of the storage at the beginning of the year
   * - set_storagelevelstart_low
     - *[share,0-1]*
     - 0.25
     - The lower bound for the start-level of the storage at the beginning of the year
   * - switch_e2pratio_deviationfactor
     - *[float]*
     - 2
     - The maximum deviation from the defined E2P-ratio of storages
   * - **Peaking constraint options**
     -
     -
     -
   * - switch_peaking_capacity
     - *[0,1]*
     - 1
     - Enable / disable the peaking constraints. The purpose of these constraints is to ensure proper peak capacity build-out based on the original (non-reduced) timeseries
   * - switch_peaking_with_trade
     - *[0,1]*
     - 1
     - Enable / disable the consideration of transmission lines in the peaking requirements
   * - switch_peaking_with_storages
     - *[0,1]*
     - 1
     - Enable / disable the consideration of storages in the peaking requirements
   * - switch_peaking_minrun
     - *[0,1]*
     - 1
     - Enable / disable a mininum run constraint for peaking capacities that are in reserve. The amount can be decided in the minrun_share
   * - set_peaking_slack
     - *[share,0-1]*
     - 1
     - Set the slack of the peaking constraints. 1 means that there is no slack at all, forcing the full enforcement of the peaking constraints
   * - set_peaking_res_cf
     - *[share,0-1]*
     - 0.5
     - Set a factor for renewable capacities to be considered in the peaking constraints. The reasoning is that non-dispatchable renewables should not be factored in too well into these reserve capacities
   * - set_peaking_min_thermal
     - *[share,0-1]*
     - 0.25
     - Set a minimum share of thermal plants in the peaking / reserve capacities
   * - set_peaking_startyear
     - *[integer]*
     - 2030
     - Set the start year for the reserve constraints to be enforced in the model
   * - set_peaking_minrun_share
     - *[share,0-1]*
     - 0.15
     - Sets the amount of the minimum run requirement (if enabled). 0 would mean they do not need to be operated at all, 1 would mean that they need to run permanently
   * - **Employment module options**
     -
     -
     -
   * - switch_employment_calculation
     - *[0,1]*
     - 1
     - Enables / disables the employment module
   * - eployment_data_file
     - *[string]*
     -
     - Defines the filename of the employment data file