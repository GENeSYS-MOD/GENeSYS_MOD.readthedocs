Release Notes
=============

GENeSYS-MOD has had several changes and expansions over time. The image below shows some of the key additions across the multiple major versions of GENeSYS-MOD.
The naming scheme of GENeSYS-MOD versions is as follows: major model versions (v1 / v2 /vX) highlight a fundamental change in underlying data structure that is not cross-compatible. 
This means that GENeSYS-MOD v1.0 data sets would not be compatible with the GENeSYS-MOD v2.0 model code without modifications. 
This is usually due to a large change in the fidelity of input data (e.g. going from 6 time slices in v1.0 to 16 in v2.x to a flexible time series in v3.0+).
Minor versions (v4.X) highlight meaningful changes, including new features, but those follow the same overall model and data structure as the previous minor version.
Sub-versions (v4.0.X) mark small changes and bugfixes, and might differ between the GAMS and Julia implementations. Those will be release on a need-oriented basis, e.g. if issues arise or bugs are found.

.. image:: /_static/genesysmod_blocks_v4.png
    :width: 650

.. centered:: *Major changes and additions to GENeSYS-MOD across major model versions.*


In addition, once there have been official releases on the new GitHub repositories, you will be able to find their release notes here. :)


.. toctree::
   :maxdepth: 1
   :caption: Release notes per repository

   genesysmod_gms
   genesysmod_jl
   genesysmod_data
   genesysmod_tools
   genesysmod_readthedocs