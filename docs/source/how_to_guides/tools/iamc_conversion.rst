GENeSYS-MOD IAMC Conversion Script
==================================

The IAMC conversion script translates GENeSYS-MOD result files into the common
IAMC data format using the `openENTRANCE <https://openentrance.eu/>`_
nomenclature. This makes model results directly usable in IAMC-based workflows
and tools such as `pyam <https://pyam-iamc.readthedocs.io/>`_, and allows
uploading them to scenario databases. The output consists of CSV files in IAMC
format and, optionally, a combined Excel workbook.

Requirements
-------------

**Python packages:**

- pandas
- `pyam-iamc <https://github.com/IAMconsortium/pyam>`_
- `nomenclature-iamc <https://github.com/openENTRANCE/nomenclature>`_
- `gdxpds <https://github.com/NREL/gdx-pandas>`_ (only required when converting ``.gdx`` result files)

**GAMS (for gdx inputs only):** Reading ``.gdx`` files requires a local GAMS
installation. The path to the GAMS directory must be set manually, because
``gdxpds`` may not locate it automatically: open
``genesysmod_to_iamc/_statics.py`` and adjust the variable ``DEF_GAMS_DIR``
(e.g. ``"C:/GAMS/46"``) to point to your installed GAMS distribution. Further
defaults, such as the reported model name and version, can be changed in the
same file.

Set Up
-------
The conversion module can be found here:
https://github.com/GENeSYS-MOD/GENeSYS_MOD.tools/tree/main/iamc_conversion

The folder is structured as follows:

- ``iamc_conversion_outputs.ipynb`` — Jupyter notebook with an exemplary conversion workflow.
- ``genesysmod_to_iamc/`` — the Python module with the conversion source code.
- ``genesysmod_to_iamc/mappings/`` — mappings from GENeSYS-MOD variables to the openENTRANCE nomenclature.
- ``genesysmod_to_iamc/definitions/`` — the data-structure definitions (regions, variables) used for validation.
- ``genesysmod_to_iamc/input/`` — place the GENeSYS-MOD result files to be converted here.
- ``genesysmod_to_iamc/out/`` — the generated CSV files in IAMC format.
- ``genesysmod_to_iamc/out/combined_excel/`` — combined Excel files across pathways.

Usage
------
Import the module in a notebook or script and call the conversion function:

::

    import genesysmod_to_iamc

    genesysmod_to_iamc.generate_data("Sample_Model_Run", "gdx")

The first argument is the result file name without extension; the second is the
file type. Two file types are supported:

- ``"gdx"`` — results from the GAMS version of GENeSYS-MOD. Requires GAMS and
  ``gdxpds`` (see above).
- ``"csv"`` — results from the Julia version of GENeSYS-MOD. These consist of
  several CSV files whose names start with the output type, followed by the
  name of the model run (e.g. ``output_energy_balance_Sample_Model_Run.csv``).
  The files must keep this naming convention; the model-run name (the second
  part of the file name) is what is passed as the first argument.

Optional parameters
--------------------
``generate_data`` accepts four optional boolean parameters, all defaulting to
``False``:

- ``generate_series_data`` — additionally exports full hourly demand time
  series (e.g. final electricity demand by sector) in the sub-annual IAMC
  format.
- ``generate_load_factors`` — additionally exports hourly load factors for the
  renewable technologies.
- ``generate_transmission_data`` — additionally exports transmission data
  between regions (reported as directional ``origin>destination`` regions).
- ``combine_outputs`` — combines the generated outputs into a single file per
  model run.

Example with all options:

::

    genesysmod_to_iamc.generate_data("Sample_Model_Run",
                                     "gdx",
                                     generate_series_data=False,
                                     generate_load_factors=False,
                                     generate_transmission_data=False,
                                     combine_outputs=True)

For convenience, the module includes a ``Pathways`` enumeration with the file
names of the four openENTRANCE storylines, which can be passed directly as the
first argument:

::

    class Pathways(Enum):
        TF = "TechnoFriendly"
        DT = "DirectedTransition"
        GD = "GradualDevelopment"
        SC = "SocietalCommitment"

    genesysmod_to_iamc.generate_data(genesysmod_to_iamc.Pathways.TF.value, "gdx")

Validation against the IAMC nomenclature
-----------------------------------------
Before any output is written, the conversion runs a validation routine built on
the `nomenclature-iamc <https://nomenclature-iamc.readthedocs.io/>`_ package.
The region and variable dimensions of the converted data are checked against
the data-structure definitions shipped in ``genesysmod_to_iamc/definitions/``
(with sub-annual time slices validated where present), and region aggregation
and renaming are applied according to the files in
``genesysmod_to_iamc/mappings/``. If a variable, region or unit does not
conform to the nomenclature, the validation raises an error and the conversion
stops — this guarantees that every produced file is consistent with the IAMC
format and can be uploaded to a scenario database without further checks.

The definitions bundled with the module reflect the openENTRANCE nomenclature
at the time of release. The most current definitions (variables, regions and
units) are maintained in the openENTRANCE nomenclature repository:
https://github.com/openENTRANCE/openentrance/tree/main/definitions

If the conversion rejects a variable that you believe is valid, compare the
bundled definitions against that repository and update the files in
``genesysmod_to_iamc/definitions/`` accordingly.

Outputs
--------
The converted results are written as CSV files in IAMC format to
``genesysmod_to_iamc/out/``. Sub-annual data is reported in Central European
Time (UTC+01:00).

To create one combined Excel workbook with all converted pathways, run:

::

    genesysmod_to_iamc.generate_combined_excel_yearly()

Only yearly values are aggregated into the workbook, due to the row limits of
Excel files; the full hourly detail remains available in the CSV outputs.
