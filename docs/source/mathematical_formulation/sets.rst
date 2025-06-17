Sets
==============
Sets serve as the index domains over which all parameters, decision variables and constraints are defined. They also facilitate scalability, as expanding the model to include more regions or years simply involves extending the relevant sets without modifying the core model logic.

.. _region:

Region [r/rr/r_full/rr_full]
----------------------------
The Region set defines the geographical scope over which the energy system is modelled and is fully flexible to the user's needs. 
Each element in the Region set could for example correspond to a country, a subnational area (e.g. a federal state), or an aggregated zone (such as "EU27"). 
It enables the model to capture region-specific demand, supply, costs, emissions, and energy flows, as well as inter-regional trade.

The list of regions usually includes a "World" region which provides generic data for some parameters, that is used by the model if no region specific data is defined. However, this "World" region is only used in the pre-processing phase of the model run and then excluded from the actual computation.

**Aliases:** The aliases for region are r and rr (if multiple regions are needed, see also :ref:`region2`), while r_full and rr_full mark the full list of regions prior to eventual filtering (e.g. before removal of the "World" region).

**Naming convention:** The name of regions usually includes the country ISO2 code (e.g. "DE","NO","FR",...) and then potentially sub-regions separated by a "_" (e.g. "DE_BE","NO_1",...). *The macro-regions currently do not have a naming convention.*


Technology [t]
--------------
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


Storage [s]
-----------
Defines all energy storages. Storages are separate entities from Technologies and therefore have their own set, being subject to specific limitations and functionalities. Storages are usually linked to technologies via the :ref:`TechnologyToStorage` and :ref:`TechnologyFromStorage` parameters, either directly (e.g. by coupling a heat pump with a thermal storage) or via the grid (e.g. grid-scale battery systems). This grid link is created via a placeholder dummy-technology that serves as the grid link for the actual storage (see image below for reference).


.. image:: /_static/storage_dummies.png
    :width: 650

.. centered:: *Set-up of grid-level storage technologies via dummy technologies.*

**Aliases:** The alias for the Storage set is s.

**Naming convention:** Storages have the prefix "S\_" before their name (e.g. "S_Battery_Li-Ion").

Fuel [f/ff]
-----------
Defines all inputs and outputs of technologies. This can include either energy carriers (e.g. power or coal), energy procies (e.g. kilometers traveled), or other units (e.g. surface area).

**Aliases:** The alias for the Storage set is f or ff in cases where multiple fuels are used cojointly.

**Naming convention:** Fuels have no clear naming convention, but follow the general rule of containing the respective names (e.g. Power, H2, Mobility_Passenger,...).

Mode of Operation [m]
---------------------
Defines the number of different modes of operations for technologies. The  gives a structure to represent multiple input-output combinations for technologies (e.g. fuel switching): for example a gas power plant could use either natural gas in mode of operation 1 and biogas in mode of operation 2.

**Aliases:** The alias for the Mode of Operation set is m.

**Naming convention:** Modes of operation are simply numbered (e.g. 1,2,3,4). At the moment, GENeSYS-MOD includes up to four modes of operation.

Emission [e]
------------
Defines the types of emissions tracked within the model's framework (e.g. CO\ :sub:`2`).

**Aliases:** The alias for the Emission set is e.

**Naming convention:** Currently, only CO\ :sub:`2` is modeled within GENeSYS-MOD.

ModalType
----------
The ModalType set classifies transport-demand into different categories, based on the transport pupose (passenger or freight), the transport medium (road, rail, air, ship), and the fuel or drivetrain (renewable vs. conventional).

Sector
-------
GEPNeSYS-MOD classifies technologies into different sectors to assign sectoral emission limits and sector specific constraints. Sectors included are typically Power, Industry, Buildings, Transportation, Resources, Storages, Transformation and CHP.

Year
-----
Defines the temporal resolution of the model on an annual basis. Each element in the Year set represents one modelled year within the planning horizon (e.g., 2020, 2025, 2030).
It is used to track all time-dependent variables, such as investments, energy production, demand, emissions, and system costs over time, enabling the model to simulate long-term energy system developments and transitions.

TimeSlice
----------
Defines the intra-annual temporal resolution of the model. While input data (e.g., renewable generation profiles or demand) is typically provided in hourly resolution, a timeseries reduction script aggregates this data into a smaller number of representative timeslices to reduce computational complexity.
The number of timeslices can be configured in the model settings. A higher number of timeslices allows for a more accurate representation of diurnal and seasonal variability in energy demand and supply, especially important for modelling variable renewable energy sources.

.. _region2:

Region2 [rr/rr_full]
--------------------
Contains the same elements as :ref:`region`, but is used specifically to distinguish between origin and destination regions in inter-regional energy trade or transmission. This distinct naming of the set Region is only found in data tables and the GENeSYS-MOD.data repository. Within the model, the simple aliases of Region (r/rr) will be used.
