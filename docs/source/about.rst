What is GENeSYS-MOD?
====================

The Global Energy System Model - or GENeSYS-MOD - is an open source cross-sectoral energy system model aimed at long-term developments of the energy system.



GENeSYS-MOD is originally based on the Open-Source Energy Modeling System (`OSeMOSYS  <http://www.osemosys.org/>`_) framework. While still part of the OSeMOSYS family of models, various aspects have been redesigned, expanded, or added. GENeSYS-MOD is a linear program, minimizing total system costs. Energy demands are exogenously predefined and the model needs to provide the necessary capacities to meet them. The modeling framework is very flexible in its use cases. Based on research question and input data, calculations can be done from a household-basis to a global aggregation of regions.

The model covers the sectors electricity, buildings, industry, and transport. It also includes all linkages between those sectors, as well as flexibility options and energy trade between regions.

.. image:: _static/genesysmod_structure_new_drawio.png
    :width: 650

.. centered:: *(Highly) simplified structure of the coverage of GENeSYS-MOD.*

A main focus of GENeSYS-MOD is to be easily understandable and usable, offering multiple model versions in the GAMS and Julia programming languages, making it available for a wide range of potential users. By offering flexible time aggregation methods, the model can be used on any kind of machine, including PCs and laptops, without the requirement for expensive hardware.

If you want to learn more about GENeSYS-MOD, the underlying principles and mathematical formulation, look over to :doc:`the mathematical Formulation page </mathematical_formulation/overview>`.

GENeSYS-MOD is published under the :doc:`Apache 2.0 license <license>`, which means that it is completely open source and free to use, redistribute, modify, etc.

Plenty of research has been conducted using GENeSYS-MOD - head over to the :doc:`References <references>` section to see a list of all published works with the framework.