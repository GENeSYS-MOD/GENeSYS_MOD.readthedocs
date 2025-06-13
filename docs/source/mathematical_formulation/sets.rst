Sets
==============
Sets serve as the index domains over which all parameters, decision variables and constraints are defined. They also facilitate scalability, as expanding the model to include more regions or years simply involves extending the relevant sets without modifying the core model logic.

.. _region:

Region
--------
The Region set defines the geographical scope over which the energy system is modelled and is fully flexible to the user's needs. 
Each element in the Region set could for example correspond to a country, a subnational area (e.g. a federal state), or an aggregated zone (such as "EU27"). 
It enables the model to capture region-specific demand, supply, costs, emissions, and energy flows, as well as inter-regional trade.
The region set usually includes a "World" region which provides generic data for some parameters, that is used by the model if no region specific data is defined.

Technology
-----------
The Technology set defines all processes that can convert, move, store, or use energy (or materials). What counts as a “technology” is deliberately broad and user-configurable.
Typically these types of technologies are included:

- Power and heat generation
- Industrial Processes
- Transportation
- Storages
- Energy-carrier conversion
- Ressource supply

Storage
--------
Defines all technologies that can store energy.

Fuel
-----
Defines all inputs (e.g. coal) and outputs (e.g. power) of technologies. 

Mode_of_operation
------------------
Defines the number of different modes of operations for technologies. It gives a structure to represent internal technological behaviour: for example a gas power plant could use conventional gas in mode of operation 1 and biogas in mode of operation 2.

Emission
---------
Defines the types of emissions tracked within the model's framework (e.g. CO2).

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

Region2
--------
Contains the same elements as :ref:`region`, but is used specifically to distinguish between origin and destination regions in inter-regional energy trade or transmission.
