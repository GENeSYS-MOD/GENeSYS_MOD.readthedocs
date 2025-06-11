Overview
========

The Global Energy System Model (GENeSYS-MOD) is a framework for the computation of developments for the energy system including both dispatch as well as investment decisions across multiple years. The focus is usually on creating cost-optimal strategies for the decarbonization of the energy system across its multiple sectors (typical coverage includes buildings, transport, industry, and electricity). This then specifically includes the integration of renewable energy sources into the system, alongside sector coupling, flexibility options, energy transmission, etc.

GENeSYS-MOD has been in development since 2016, when it was first created as a fork of the Open-Source Energy Modeling System (`OSeMOSYS  <http://www.osemosys.org/>`_).

.. image:: /_static/genesysmod_timeline_small.jpg
    :width: 650

.. centered:: *Timeline of the development and noteworthy events in the history of GENeSYS-MOD.*

The model has since been featured in a wide range of academic research papers and projects (see :doc:`references </references>`). It now includes multiple repositories, spanning an entire ecosystem around the actual model core. You can find the GitHub page here: `https://github.com/GENeSYS-MOD  <https://github.com/GENeSYS-MOD>`_
This readthedocs focuses mostly on the model core and mathematical formulation, there are, however, also several guides on the tools (to be found :doc:`here </how_to_guides/tools/index>`).

.. image:: /_static/gmd_ecosystem_small.png
    :width: 650

.. centered:: *The GENeSYS-MOD ecosystem and repositories.*

Mathematically, GENeSYS-MOD is a linear program (an option for use as a mixed-integer problem (MIP) exists, but is not commonly used) that optimizes the net-present value of the entire energy system across time. While the name suggests a global model setting, this is not mandatory and indeed, many regional and country-level case studies have been conducted with GENeSYS-MOD. The analyzed timeframe usually reaches until 2050 or 2060, with longer or shorter horizons being possible.
The framework is meant to be largely driven by the used data, meaning that it can be implemented very flexibly, ranging from broad, global analyses with several macro-regions and only a handful of time steps per year, to detailed local applications at high temporal resolution. The model core itself can be used to model almost any input-output relationship of energy-related technologies and fuels (e.g. power, natural gas, hydrogen,...), as well as their proxies (e.g. passenger kilometers, tons of steel,...).

The objective function of GENeSYS-MOD is as follows:

.. math::
    \mathrm{min}\; z &= \sum_r\sum_t \sum_y \mathit{DiscountedTechnologyCosts_{r,t,y}} \nonumber\\ 
    &+ \sum_r\sum_s \sum_y \mathit{DiscountedStorageCosts_{r,s,y}} \nonumber \\
    &+ \sum_r\sum_y \mathit{DiscountedTradeCosts_{r,y}} \\
    &- \sum_r\sum_t \sum_y \mathit{DiscountedTechnologySalvageValue_{r,t,y}} \nonumber\\
    &- \sum_r\sum_s \sum_y \mathit{DiscountedStorageSalvageValue_{r,s,y}} \nonumber

Where :math:`r` is the set of regions, :math:`t` the set of technologies, :math:`y` the set of modeled years, and :math:`s` is the set of storages. A full list of all sets can be found :doc:`here </mathematical_formulation/sets>`.
This leads to a cost-optimal system design, while maintaining relevant constraints such as the energy balances (to ensure that supply always meets demand), capacity restrictions (e.g. due to area limitations), emission targets (this can be modeled either as annual limits, an overall budget, an emission price, minimum renewable shares, or a combination), and political constraints (e.g. expansion stops or phase outs of certain technologies).

The following pages give an overview over the :doc:`sets </mathematical_formulation/sets>`, :doc:`parameters </mathematical_formulation/parameters>`, and :doc:`variables </mathematical_formulation/variables>` of GENeSYS-MOD.
An overview over some key equations will be added in the future.