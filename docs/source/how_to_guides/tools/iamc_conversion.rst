GENeSYS-MOD IAMC Conversion Script
==================================

The IAMC conversion script converts GENeSYS-MOD results into the data format of
the `Integrated Assessment Modeling Consortium (IAMC) <https://www.iamconsortium.org/>`_.
The IIASA scenario explorers, such as the one of the iDesignRES project, and many
energy system and integrated assessment models use this format, so the converted
results can be uploaded, compared with the results of other models and analysed
with `pyam <https://pyam-iamc.readthedocs.io/>`_. The script reads the gdx results
of GENeSYS-MOD.gms or the csv results of GENeSYS-MOD.jl, maps technologies and
fuels to IAMC variables (e.g. ``Secondary Energy|Electricity|Wind|Onshore``), adds
the sums of variables and the regional totals, and writes one file per scenario
and one Excel file with all scenarios for the upload. Before the upload, it checks
this file with the scenario explorer's own upload workflow. This section explains
how to set up and run the script, and how to adapt it to a new release, model
version or project.

Requirements
-------------

**Python:** The script needs Python 3.11 or newer, because the current version of
``nomenclature-iamc``, which the scenario explorers use for their checks, does not
run on older versions. The easiest way to get Python with all packages is conda,
which comes with `Anaconda <https://www.anaconda.com/download>`_ or
`Miniforge <https://github.com/conda-forge/miniforge>`_.

**Packages:** The environment file ``environment.yml`` of the script installs
everything that is needed:

- `pyam-iamc <https://pyam-iamc.readthedocs.io/>`_
- `nomenclature-iamc <https://nomenclature-iamc.readthedocs.io/>`_
- `gdxpds <https://github.com/NREL/gdx-pandas>`_ and gdxcc (to read gdx files)
- gitpython, openpyxl and pyyaml
- Jupyter Notebook

**GAMS (for gdx results only):** gdx files are read through a local GAMS
installation, which you can download here: https://www.gams.com/download/. Its
folder is one of the settings of the script.

**Git:** The check before an upload downloads the workflow repository of the
scenario explorer and the IAMC common definitions with git. Git therefore has to
be installed (https://git-scm.com/downloads), and the computer needs an internet
connection.

Set Up
-------
The script can be found here:
https://github.com/GENeSYS-MOD/GENeSYS_MOD.tools/tree/main/iamc_conversion

You can either clone the repository or download the files directly to your
computer. Then create the Python environment once: open a terminal with conda
(e.g. the Anaconda Prompt), go to the folder ``iamc_conversion`` and run:

::

    conda env create -f environment.yml
    conda activate genesysmod-iamc

To open the notebook, start ``jupyter notebook`` in this folder with the
environment activated, or open the notebook in VS Code and choose
``genesysmod-iamc`` as its kernel.

The folder is structured as follows:

- ``iamc_conversion_outputs.ipynb`` — the notebook that runs the conversion, with
  all settings in its settings cells.
- ``run.py`` — the same conversion from a terminal, with its own copy of the
  settings at its top.
- ``README.md`` — a short guide, the list of all mapping files and all
  assumptions of the conversion.
- ``environment.yml`` — the Python environment.
- ``genesysmod_to_iamc/`` — the Python module with the conversion code.
- ``genesysmod_to_iamc/input/`` — place the GENeSYS-MOD results to convert here.
- ``genesysmod_to_iamc/mappings/`` — the mappings from GENeSYS-MOD technologies
  and fuels to IAMC variables, and the sums of variables.
- ``genesysmod_to_iamc/out/`` — the converted results of each scenario.
- ``genesysmod_to_iamc/out/combined_excel/`` — the upload files with all
  scenarios.

The definitions of the IAMC variables, regions and units are not part of the
script: the check takes them from the workflow repository of the scenario
explorer (see *The check before an upload* below).

Input files
------------
Put the results of every scenario into ``genesysmod_to_iamc/input/``:

- **GENeSYS-MOD.gms:** the gdx file with the results, ``Output_<...>.gdx`` from
  the folder ``GdxFiles`` of the model, written with ``switch_write_output = gdx``
  (the default, see :doc:`Switches </how_to_guides/gams/user_guide/switches>`).
- **GENeSYS-MOD.jl:** the result csv files of the run, written with
  ``switch_processed_results = 1`` (see
  :doc:`Switches </how_to_guides/julia/user_guide/switches>`). The script reads
  the tables ``output_production``, ``output_capacity``, ``output_emission``,
  ``output_trade``, ``output_technology_costs_detailed`` and
  ``output_exogenous_costs`` whose file names contain the name of the run.
- **Only for the hourly series and load factors:** ``Timeseries_<file>.xlsx``,
  the hourly input data of the run (sheets such as ``TS_LOAD`` and ``TS_PV_AVG``),
  where ``<file>`` is the name of the result file.

The result files do not need to be renamed: the settings give each of them the
scenario name used in the outputs.

Configuration
--------------
All settings are Python variables in the four settings cells of the notebook,
each with a comment that explains it. Folders are relative to the folder of the
notebook. ``run.py`` has the same settings at its top, but keeps its own values:
a change in the notebook does not change ``run.py``, and the other way round.

**The results to convert:**

- ``gams_dir`` — the GAMS folder, e.g. ``'C:/GAMS/46'`` (only used for gdx
  results).
- ``input_dir`` — the folder with the results (default
  ``genesysmod_to_iamc/input``).
- ``file_type`` — ``'gdx'`` for results of GENeSYS-MOD.gms, ``'csv'`` for results
  of GENeSYS-MOD.jl.
- ``scenarios`` — the result file of every scenario, without extension (for csv
  results: the name of the run). The file names are also the scenario names in
  the outputs; to name a scenario differently, write ``{file: name}``:

  ::

      scenarios = ['Go RES', 'REPowerEU++', 'NECP Essentials', 'EU Trinity']

      # or, with scenario names that differ from the file names:
      scenarios = {'Output_Europe_GoRES_run1': 'Go RES', 'Output_Europe_Trinity_run1': 'EU Trinity'}

- ``years`` — the model years to report; other years in the results are left out.

**Names in the outputs:**

- ``model`` and ``release`` — the model name and the release of the results, e.g.
  ``'GENeSYS-MOD 4.1'`` and ``'v2.0.1'``. The release is added to the scenario
  names (``Go RES v2.0.1``).
- ``total_region`` and ``eu27_region`` — the names of the sum over all model
  regions and of the sum over the EU member states in the model.

**What to convert:**

- ``transmission`` — the network capacities between regions
  (``Network|...|Capacity``), with regions named ``origin>destination``, e.g.
  ``Austria>Czechia``.
- ``hourly_series`` — hourly demand series, in an extra file (needs
  ``Timeseries_<file>.xlsx``).
- ``load_factors`` — hourly load factors of PV, wind and run-of-river, in an
  extra file (also needs ``Timeseries_<file>.xlsx``).
- ``combine`` — one file per scenario with the yearly values and the hourly
  files.
- ``exogenous_costs`` and ``additional_emissions`` — switched off by default and
  kept for later use: capital, fixed and variable costs, and CO2 emissions per
  technology.

**Outputs and the check before an upload:**

- ``output_dir`` — the folder for the outputs (default ``genesysmod_to_iamc/out``).
- ``combined_file`` — the name of the upload file in ``combined_excel/``;
  ``{date}`` and ``{release}`` are filled in.
- ``leave_out`` — variables left out of the upload file, e.g. while their
  definitions wait for a change in the workflow repository of the explorer
  (``*`` matches anything). The files of the single scenarios keep them.
- ``run_validation`` — checks the upload file with the workflow of the scenario
  explorer.
- ``workflow_repo`` — the workflow repository of the scenario explorer, e.g.
  ``https://github.com/iiasa/idesignres-workflow``. For another project, only
  this address changes.

After a change, run the settings cell again and then the conversion cell; the
kernel does not need a restart.

Run the conversion
-------------------
In the notebook, run all cells (*Run → Run All Cells*). The conversion cell passes
the settings to the script and starts the conversion:

::

    excel_file = genesysmod_to_iamc.run()

The script converts every scenario and writes its yearly values to
``<file>_yearly.csv``. It then combines the yearly values of all scenarios in the
upload file and checks it. The output shows each step with the time it started,
and the last line says whether the check passed:

::

    [INFO] 16:02:37 - root: Converting scenario Go RES v2.0.1 (Go RES)
    ...
    [INFO] 16:13:52 - root: Done: Go RES, REPowerEU++, NECP Essentials, EU Trinity converted, upload file ...\combined_excel\GENeSYS-MOD-pathways_30-10-2026.xlsx, check PASSED

Four scenarios of the European model take about a quarter of an hour.

From a terminal, choose the settings at the top of ``run.py`` and run, with the
environment activated:

::

    python run.py                      # convert, combine and check
    python run.py --validate FILE      # only check an existing IAMC file (xlsx or csv)

The single steps can also be run on their own, e.g. in the cell *Single steps* of
the notebook:

::

    genesysmod_to_iamc.generate_data('Go RES')             # convert one scenario
    genesysmod_to_iamc.generate_combined_excel_yearly()    # combine all *_yearly.csv files in the output folder
    genesysmod_to_iamc.validate('path/to/file.xlsx')       # check an existing file

The check before an upload
---------------------------
Every IIASA scenario explorer checks uploads with the workflow of its project
repository, usually ``https://github.com/iiasa/<project>-workflow``. This
repository contains the definitions of the project and pulls the IAMC
`common definitions <https://github.com/IAMconsortium/common-definitions>`_. The
script keeps a copy of it in the folder ``.genesysmod_to_iamc`` in your user
folder, updates it before every check and runs the same workflow on the upload
file. No definitions have to be downloaded or updated by hand.

The result of the check is written to ``validation_report.txt`` in the output
folder: ``PASSED``, or every variable, region and unit that the explorer would
reject. Such errors are fixed in the mapping files (see *Adapting the conversion*
below), followed by a new conversion. A single file can be checked with
``python run.py --validate FILE`` or ``genesysmod_to_iamc.validate(FILE)``.

.. note::
    The scenario explorers check uploads with the newest version of
    ``nomenclature-iamc``. To check with the same version, update the packages
    before an upload: run ``pip install -U nomenclature-iamc pyam-iamc`` in the
    activated environment, or ``%pip install -U nomenclature-iamc pyam-iamc`` in
    a cell of the notebook and restart the kernel.

Outputs
--------
After the conversion, the output folder contains:

- ``<file>_yearly.csv`` — the yearly values of each scenario in IAMC format, with
  the columns Model, Scenario, Region, Variable, Unit, Subannual and one column
  per year,
- ``<file>_series.csv`` and ``<file>_loadfactors.csv`` — the hourly demand series
  and load factors, if they are switched on,
- ``<file>_combined.csv`` — the yearly values and the hourly files of a scenario
  in one file, if ``combine`` is on,
- ``combined_excel/<combined_file>`` — the upload file with the yearly values of
  all scenarios,
- ``validation_report.txt`` — the result of the check.

Only yearly values go into the upload file. Hourly values are given in Central
European Time (UTC+01:00), as ``MM-DD HH:MM+01:00`` in the column Subannual.
Regions are named by country (e.g. ``Austria``); the sums over all regions and
over the EU member states are named as in the settings.

Conventions of the conversion
------------------------------
The main assumptions of the conversion are:

- Units: energy in EJ/yr, capacities in GW, transport capacities in Gvkm and
  emissions in Mt CO2/yr. Network capacities are in MW for power lines and in GW
  for gas and hydrogen pipelines.
- Heat follows the IAMC definitions: ``Secondary Energy|Heat`` is the district
  heat of CHPs and heat plants, ``Final Energy|<sector>|Heat`` the district heat
  delivered to a sector. Heat produced in buildings and industry is useful
  energy, ``Useful Energy|<sector>|Heat|<source>``; the fuels it uses are final
  energy.
- The fuel and the emissions of CHPs are split into electricity and heat by
  operating mode. The fuel of a mode that produces both is split by the shares of
  electricity and heat in its output.
- The electricity demand that the model does not assign to a sector is reported
  as ``Final Energy|Other Sector|Electricity``, the exogenous emissions of the
  model as ``Emissions|CO2|Other``.
- EU27 is the sum over the 25 EU member states in the model (Malta and Cyprus are
  not modelled).
- Sums of variables, such as ``Capacity|Electricity``, are added from their parts
  as listed in ``mappings/aggregations.yaml``.

``README.md`` in the folder of the script lists all assumptions.

Adapting the conversion
------------------------
For a new release or another project, usually only the settings change. For a
new model version with new technologies or fuels, or for further variables, the
following files are changed:

.. list-table::
   :header-rows: 1
   :widths: 45 55

   * - To change
     - Edit
   * - which GENeSYS-MOD technology or fuel goes to which IAMC variable
     - the csv files in ``genesysmod_to_iamc/mappings/`` (listed in ``README.md``)
   * - the sums of variables (e.g. ``Capacity|Electricity`` from its parts) and the
       totals over all regions
     - ``genesysmod_to_iamc/mappings/aggregations.yaml``
   * - country codes to country names
     - ``genesysmod_to_iamc/mappings/GENeSYS-MOD 4.0.yaml``
   * - variables reported as zero when the model has none
     - ``genesysmod_to_iamc/mappings/zero_var.csv``
   * - which variables, regions and units the explorer accepts
     - the workflow repository of the explorer (a pull request there, not a change
       in this script)

The mapping files have two columns and no header: the GENeSYS-MOD name and the
full IAMC variable, for example:

::

    P_Coal_Lignite,Capacity|Electricity|Coal|Lignite|w/o CCS
    P_Gas_CCGT:2,Secondary Energy|Electricity|Biomass|w/o CCS

Several GENeSYS-MOD names can go to the same variable; their values are added. A
name may appear only once in a file, otherwise the script stops with an error. A
name ``technology:mode`` maps a single operating mode, such as mode 2 (biogas) of
the gas power plant above. Rows that start with ``#`` are switched off. Apart from
a few that the code selects itself (listed in ``README.md``), technologies and
fuels that are in none of the files are left out of the outputs, so new
technologies of the model need a row in the mapping files. Changes to the mapping
files apply at the next run; after changes to the code in ``genesysmod_to_iamc/``,
restart the kernel of the notebook.
