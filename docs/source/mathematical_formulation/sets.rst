Sets
==============
Sets serve as the index domains over which all parameters, decision variables and constraints are defined. They also facilitate scalability, as expanding the model to include more regions or years simply involves extending the relevant sets without modifying the core model logic.

.. _region:

Region
------

.. rubric:: Region [r/rr/r_full/rr_full]
    
The Region set defines the geographical scope over which the energy system is modelled and is fully flexible to the user's needs. 
Each element in the Region set could for example correspond to a country, a subnational area (e.g. a federal state), or an aggregated zone (such as "EU27"). 
It enables the model to capture region-specific demand, supply, costs, emissions, and energy flows, as well as inter-regional trade.

The list of regions usually includes a "World" region which provides generic data for some parameters, that is used by the model if no region specific data is defined. However, this "World" region is only used in the pre-processing phase of the model run and then excluded from the actual computation.

**Aliases:** The aliases for region are r and rr (if multiple regions are needed, see also :ref:`region2`), while r_full and rr_full mark the full list of regions prior to eventual filtering (e.g. before removal of the "World" region).

**Naming convention:** The name of regions usually includes the country ISO2 code (e.g. "DE","NO","FR",...) and then potentially sub-regions separated by a "_" (e.g. "DE_BE","NO_1",...). *The macro-regions currently do not have a naming convention.*


Technology
-----------

.. rubric:: Technology [t]

The Technology set defines all processes that can convert, move, store, or use energy (or materials, areas, and energy proxies such as driven kilometers). What counts as a “technology” is deliberately broad and user-configurable to allow for any kind of input-output relationship that is supposed to be modeled.
Typically these types of technologies are included:

- Power and heat generation
- Industrial processes
- Transportation
- Storages
- Energy conversion
- Resource supply

**Aliases:** The alias for the Technology set is t.

**Naming convention:** The technologies in GENeSYS-MOD are each given a prefix dependent on their sector. Below is a list of the prefixes of different technologies:

+---------------------------------+--------------------------------------------------------------------------------------------------------------------+
| **Prefix**                      | **Technology Group**                                                                                               |
+=================================+====================================================================================================================+
| A\_                             | Area / Dummy input source                                                                                          |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------+
| CHP\_                           | Combined-heat-and-power plants                                                                                     |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------+
| D\_                             | Storage dummy technologies / grid links                                                                            |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------+
| FRT\_                           | Freight transport technologies                                                                                     |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------+
| HB\_                            | Decentral building heat supply technologies (space heat and warm water)                                            |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------+
| HLI\_                           | Low-temperature industrial process heat (<100°C)                                                                   |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------+
| HMLI\_                          | Medium-low-temperature industrial process heat (100-400°C)                                                         |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------+
| HMHI\_                          | Medium-high-temperature industrial process heat (400-1000°C)                                                       |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------+
| HHI\_                           | High-temperature industrial process heat (>1000°C)                                                                 |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------+
| HD\_                            | District heat generation technologies                                                                              |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Infeasibility\_                 | Infeasibility technologies (to capture lost load)                                                                  |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------+
| P\_                             | Power generation technologies                                                                                      |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------+
| PSNG\_                          | Passenger transport technologies                                                                                   |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------+
| R\_                             | Resource generation technologies                                                                                   |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------+
| X\_                             | Transformation technologies                                                                                        |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Z\_                             | Import / Export technologies                                                                                       |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------+


Storage
--------

.. rubric:: Storage [s]

Defines all energy storages. Storages are separate entities from Technologies and therefore have their own set, being subject to specific limitations and functionalities. Storages are usually linked to technologies via the :ref:`TechnologyToStorage` and :ref:`TechnologyFromStorage` parameters, either directly (e.g. by coupling a heat pump with a thermal storage) or via the grid (e.g. grid-scale battery systems). This grid link is created via a placeholder dummy-technology that serves as the grid link for the actual storage (see image below for reference).


.. image:: /_static/storage_dummies.png
    :width: 650

.. centered:: *Set-up of grid-level storage technologies via dummy technologies.*

**Aliases:** The alias for the Storage set is s.

**Naming convention:** Storages have the prefix "S\_" before their name (e.g. "S_Battery_Li-Ion").

Fuel
-----

.. rubric:: Fuel [f/ff]

Defines all inputs and outputs of technologies. This can include either energy carriers (e.g. power or coal), energy procies (e.g. kilometers traveled), or other units (e.g. surface area).

**Aliases:** The alias for the Storage set is f or ff in cases where multiple fuels are used cojointly.

**Naming convention:** Fuels have no clear naming convention, but follow the general rule of containing the respective names (e.g. Power, H2, Mobility_Passenger,...).

Mode of Operation
------------------

.. rubric:: Mode of Operation [m]

Defines the number of different modes of operations for technologies. The  gives a structure to represent multiple input-output combinations for technologies (e.g. fuel switching): for example a gas power plant could use either natural gas in mode of operation 1 and biogas in mode of operation 2.

**Aliases:** The alias for the Mode of Operation set is m.

**Naming convention:** Modes of operation are simply numbered (e.g. 1,2,3,4). At the moment, GENeSYS-MOD includes up to four modes of operation.

Emission
---------

.. rubric:: Emission [e]

Defines the types of emissions tracked within the model's framework (e.g. CO\ :sub:`2`).

**Aliases:** The alias for the Emission set is e.

**Naming convention:** Currently, only CO\ :sub:`2` is modeled within GENeSYS-MOD.

ModalType
----------

.. rubric:: ModalType [mt]

The ModalType set is used to group shares of the total transport demand into different categories or modal types. These are based on the purpose of the transport (passenger or freight transport), the transport medium (road, rail, air, ship), and also to distinguish between conventional and renewable options.

**Aliases:** The alias for the ModalType set is mt.

**Naming convention:** All modal types start with the prefix "MT\_" and are then followed by either "PSNG" or "FRT" depending on their purpose. They can then be further classified by using the transport medium (e.g. "ROAD") and type. A full example for this would be *"MT\_PSNG\_ROAD\_CONV"*, representing the share of road-based passenger transportation by conventional technologies (e.g. combustion-based vehicles).


Sector
-------

.. rubric:: Sector [se]

GEPNeSYS-MOD classifies technologies into different sectors to assign sectoral emission limits and sector specific constraints. Sectors included are typically Power, Industry, Buildings, Transportation, Resources, Storages, Transformation and CHP.

**Aliases:** The alias for the Sector set is se.

**Naming convention:** Sectors are simple descriptions of the respective sectors (e.g. "Power", "Industry", ...).

Year
-----

.. rubric:: Year [y/yy/y_full/yy_full]

Defines the temporal resolution of the model on an annual basis. Each element in the Year set represents one modelled year within the planning horizon (e.g., 2020, 2025, 2030).
It is used to track all time-dependent variables, such as investments, energy production, demand, emissions, and system costs over time, enabling the model to simulate long-term energy system developments and transitions.

**Aliases:** The aliases for the Year set is y (or yy if multiple years need to be indexed simultaneously). The set y_full / yy_full is used for processing only and includes every year between 1980 and 2100.

**Naming convention:** Years are simple numbers (e.g. 2018,2030,...).

TimeSlice
----------

.. rubric:: TimeSlice [l/ll/l_full/ll_full]

Defines the intra-annual temporal resolution of the model. While input data (e.g., renewable generation profiles or demand) is expected to be provided in hourly resolution, a timeseries reduction algorithm (based on `Gerbaulet and Lorenz (2017)  <https://www.diw.de/documents/publikationen/73/diw_01.c.558112.de/diw_datadoc_2017-088.pdf>`_) aggregates this data into a smaller number of consecutive timeslices to reduce computational complexity. There are plans to also include a choice of multiple timeseries reduction methods in the model.
The number of timeslices can be configured flexibly in the model settings and is taken into the account by the timeseries reduction algorithm. A higher number of timeslices allows for a more accurate representation of diurnal and seasonal variability in energy demand and supply, which is especially important for modelling variable renewable energy sources.

**Aliases:** The aliases for the TimeSlice set is l (or ll if multiple time slices need to be indexed simultaneously). The set l_full / ll_full is used for processing only and includes every hour of the year (always assumes 8760 hours, in case of leap years, the last 24 hours are cut off).

**Naming convention:** The TimeSlice always represents the respective hour of the year (e.g. 8, 81, 154, 8695, ...).


.. _region2:

Region2
--------

.. rubric:: Region2 [rr/rr_full]

Contains the same elements as :ref:`region`, but is used specifically to distinguish between origin and destination regions in inter-regional energy trade or transmission. This distinct naming of the set Region is only found in data tables and the GENeSYS-MOD.data repository. Within the model, the simple aliases of Region (r/rr) will be used.
