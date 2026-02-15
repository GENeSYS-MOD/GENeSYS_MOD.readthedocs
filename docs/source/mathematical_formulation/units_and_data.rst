Units and data
==============

Units
-----

The following units are being used throughout GENeSYS-MOD:

+---------------------+----------------------+------------------+
| **Type**            | **Unit**             | **Abbreviation** |
+=====================+======================+==================+
| Capacity            | Gigawatt             | GW               |
+---------------------+----------------------+------------------+
| Energy              | Petajoule            | PJ               |
+---------------------+----------------------+------------------+
| Passenger transport | Billion kilometers   | gpkm             |
+---------------------+----------------------+------------------+
| Freight transport   | Billion kilometers   | gpkm             |
+---------------------+----------------------+------------------+
| Monetary units      | Million Euro         | M€               |
+---------------------+----------------------+------------------+
| Emissions (CO₂)     | Megatonnes           | Mt               |
+---------------------+----------------------+------------------+

List of technologies
--------------------

The following technologies are included in the current main version of GENeSYS-MOD (other technologies might be included in specific versions used for case studies etc.). Please refer to :ref:`the set documentation <technology>` for an explanation of the naming convention.

.. list-table::
   :header-rows: 1
   :widths: 28 72

   * - Name
     - Description
   * - A_Air
     - Dummy fuel for use in Direct Air Capture (DAC)
   * - A_Rooftop_Commercial
     - Surface area of commercial rooftops
   * - A_Rooftop_Residential
     - Surface area of residential rooftops
   * - CHP_Biomass_Solid
     - Combined-heat-and-power plant using solid biomass
   * - CHP_Biomass_Solid_CCS
     - Combined-heat-and-power plant using solid biomass with CCS
   * - CHP_Coal_Hardcoal
     - Combined-heat-and-power plant using hard coal
   * - CHP_Coal_Hardcoal_CCS
     - Combined-heat-and-power plant using hard coal with CCS
   * - CHP_Coal_Lignite
     - Combined-heat-and-power plant using lignite coal
   * - CHP_Coal_Lignite_CCS
     - Combined-heat-and-power plant using lignite coal with CCS
   * - CHP_Gas_CCGT_Biogas
     - Combined-heat-and-power plant using biogas
   * - CHP_Gas_CCGT_Biogas_CCS
     - Combined-heat-and-power plant using biogas with CCS
   * - CHP_Gas_CCGT_Natural
     - Combined-heat-and-power plant using natural gas
   * - CHP_Gas_CCGT_Natural_CCS
     - Combined-heat-and-power plant using natural gas with CCS
   * - CHP_Gas_CCGT_SynGas
     - Combined-heat-and-power plant using synthetic natural gas
   * - CHP_Hydrogen_FuelCell
     - Combined-heat-and-power plant using hydrogen in a fuel cell
   * - CHP_Oil
     - Combined-heat-and-power plant using crude oil
   * - CHP_WasteToEnergy
     - Combined-heat-and-power plant using waste
   * - D_Battery_Li-Ion
     - Storage dummy technology / grid link for Lithium-Ion Batteries
   * - D_Battery_Redox
     - Storage dummy technology / grid link for Redox-Flow Batteries
   * - D_CAES
     - Storage dummy technology / grid link for Compressed-Air Electricity Storage
   * - D_Gas_H2
     - Storage dummy technology / grid link for Redox-Flow Batteries
   * - D_Gas_Methane
     - Storage dummy technology / grid link for Redox-Flow Batteries
   * - D_HB_Tank_Small
     - Storage dummy technology / grid link for Redox-Flow Batteries
   * - D_HD_Pit
     - Storage dummy technology / grid link for large-scale heat storage (e.g. aquifer)
   * - D_HLI_Tank_Large
     - Storage dummy technology / grid link for Redox-Flow Batteries
   * - D_PHS
     - Storage dummy technology / grid link for Redox-Flow Batteries
   * - FRT_Rail_Conv
     - Freight railroad technology using conventional (petro-) fuels
   * - FRT_Rail_Electric
     - Freight railroad technology using electricity
   * - FRT_Road_BEV
     - Freight trucks using battery-electric technology
   * - FRT_Road_H2
     - Freight trucks using hydrogen in a fuel cell
   * - FRT_Road_ICE
     - Freight trucks with an internal combustion engine, can use multiple fuels
   * - FRT_Road_LNG
     - Freight trucks using liquified natural gas (LNG)
   * - FRT_Road_OH
     - Freight trucks with overhead power lines (overhead trolley trucks)
   * - FRT_Road_PHEV
     - Freight trucks with plug-in hybrid technology (combination of ICE and BEV)
   * - FRT_Ship_Bio
     - Freight ships using biofuels
   * - FRT_Ship_Conv
     - Freight ships using conventional (petro-) fuels
   * - FRT_Ship_LNG
     - Freight ships using liquified natural gas (LNG)
   * - HB_Biomass
     - Building heating technology using biomass
   * - HB_Direct_Electric
     - Building heating technology using resistance heating
   * - HB_Gas_Boiler
     - Building heating technology using gas (incl. biogas and synth. methane)
   * - HB_Geothermal
     - Building heating technology using geothermal energy
   * - HB_H2_Boiler
     - Building heating technology using hydrogen (burning)
   * - HB_Hardcoal
     - Building heating technology using hard coal
   * - HB_Heatpump_Aerial
     - Building heating technology; air-sourced heat pump
   * - HB_Heatpump_Ground
     - Building heating technology; ground-sourced heat pump
   * - HB_Lignite
     - Building heating technology using lignite
   * - HB_Oil_Boiler
     - Building heating technology using petroleum products
   * - HB_Solar_Thermal
     - Building heating technology using solar thermal energy
   * - HD_Electric_Boiler
     - District heat supply technology using electric boilers
   * - HD_Geothermal
     - District heat supply technology using geothermal energy
   * - HD_Heatpump_Air
     - District heat supply technology using air-sourced heatpumps
   * - HD_Heatpump_ExcessHeat
     - District heat supply technology using excess heat from e.g. industrial processes
   * - HD_Solar_Thermal
     - District heat supply technology using solar termal energy
   * - HHI_BF_BOF
     - Blast oven furnace for steel-making (allows for multiple modes of operation and fuel mixes)
   * - HHI_BF_BOF_CCS
     - Blast oven furnace for steel-making with CCS (allows for multiple modes of operation and fuel mixes)
   * - HHI_Bio_BF_BOF
     - Blast oven furnace for steel-making (fully fueled by biomass)
   * - HHI_DRI_EAF
     - Direct reduction steelmaking with an electric arc furnace
   * - HHI_DRI_EAF_CCS
     - Direct reduction steelmaking with an electric arc furnace with CCS
   * - HHI_H2DRI_EAF
     - Direct reduction steelmaking with an electric arc furnace, using hydrogen
   * - HHI_Molten_Electrolysis
     - Steelmaking using molten electrolysis (electricity-powered)
   * - HHI_Scrap_EAF
     - Electric arc furnace for recycled (scrap) steel
   * - HLI_Biomass
     - Low-temperature boiler using biomass
   * - HLI_Direct_Electric
     - Resistance heater for low-temperature industrial process heat
   * - HLI_Gas_Boiler
     - Gas boiler for low-temperature industrial process heat
   * - HLI_Geothermal
     - Geothermal heater for low-temperature industrial process heat
   * - HLI_H2_Boiler
     - Hydrogen-fueled boiler for low-temperature industrial process heat
   * - HLI_Hardcoal
     - Hardcoal-fired boiler for low-temperature industrial process heat
   * - HLI_Lignite
     - Lignite-fueled boiler for low-temperature industrial process heat
   * - HLI_Oil_Boiler
     - Oil-fueled boiler for low-temperature industrial process heat
   * - HLI_Solar_Thermal
     - Solar-thermal generation of low-temperature industrial process heat
   * - HMHI_Biomass
     - Medium-temperature (100-1000°C) industrial process heating technology using biomass
   * - HMHI_Gas
     - Medium-temperature (100-1000°C) industrial process heating technology using gas (incl. biogas and synth. methane)
   * - HMHI_Gas_CCS
     - Medium-temperature (100-1000°C) industrial process heating technology using gas with CCS
   * - HMHI_H2
     - Medium-temperature (100-1000°C) industrial process heating technology using hydrogen
   * - HMHI_HardCoal
     - Medium-temperature (100-1000°C) industrial process heating technology using hard coal
   * - HMHI_HardCoal_CCS
     - Medium-temperature (100-1000°C) industrial process heating technology using hard coal with CCS
   * - HMHI_Oil
     - Medium-temperature (100-1000°C) industrial process heating technology using petroleum products
   * - HMHI_Steam_Electric
     - Medium-temperature (100-1000°C) industrial process heating technology using resistance heating for steam generation
   * - HMLI_Heatpump
     - Medium-low-temperature (100-400°C) industrial process heating technology using heat pumps
   * - Infeasibility_H2
     - Costly technology used to serve unmet demand; used for error handling
   * - Infeasibility_HHI
     - Costly technology used to serve unmet demand; used for error handling
   * - Infeasibility_HLI
     - Costly technology used to serve unmet demand; used for error handling
   * - Infeasibility_HMI
     - Costly technology used to serve unmet demand; used for error handling
   * - Infeasibility_HRI
     - Costly technology used to serve unmet demand; used for error handling
   * - Infeasibility_Mob_Freight
     - Costly technology used to serve unmet demand; used for error handling
   * - Infeasibility_Mob_Passenger
     - Costly technology used to serve unmet demand; used for error handling
   * - Infeasibility_Natural_Gas
     - Costly technology used to serve unmet demand; used for error handling
   * - Infeasibility_Power
     - Costly technology used to serve unmet demand; used for error handling
   * - P_Biomass
     - Thermal power generation using biomass
   * - P_Biomass_CCS
     - Thermal power generation using biomass with CCS
   * - P_Coal_Hardcoal
     - Thermal power generation using hard coal
   * - P_Coal_Hardcoal_CCS
     - Thermal power generation using hard coal with CCS
   * - P_Coal_Lignite
     - Thermal power generation using lignite
   * - P_Coal_Lignite_CCS
     - Thermal power generation using lignite with CCS
   * - P_CSP
     - Concentrated solar power plant
   * - P_Gas_CCGT
     - Combined-cycle gas turbine (can use nat. gas, biogas, synth. methane)
   * - P_Gas_CCS
     - Gas turbine with CCS
   * - P_Gas_Engines
     - Engine-based gas turbine
   * - P_Gas_OCGT
     - Open-cycle gas turbine
   * - P_Geothermal
     - Geothermal power plant
   * - P_H2_OCGT
     - Open-cycle gas turbine for hydrogen gas
   * - P_Hydro_Reservoir
     - Large-scale (reservoir) hydropower plant
   * - P_Hydro_RoR
     - Small-scale (run of river) hydropower plant
   * - P_Nuclear
     - Thermal power generation using nuclear power
   * - P_Ocean
     - Wave and tidal electricity generation
   * - P_Oil
     - Thermal power generation using petroleum products
   * - P_PV_Rooftop_Commercial
     - Rooftop-PV installations for electricity generation on commercial buildings
   * - P_PV_Rooftop_Residential
     - Rooftop-PV installations for electricity generation on residential buildings
   * - P_PV_Utility_Avg
     - Utility-scale PV installations, average placements
   * - P_PV_Utility_Inf
     - Utility-scale PV installations, below-average placements
   * - P_PV_Utility_Opt
     - Utility-scale PV installations, optimal placements
   * - P_PV_Utility_Tracking
     - Utility-scale PV installations, with single-axis tracking mechanism
   * - P_Wind_Offshore_Deep
     - Deep (floating) offshore wind turbine
   * - P_Wind_Offshore_Shallow
     - Offshore wind turbine in shallow water (close to coast)
   * - P_Wind_Offshore_Transitional
     - Offshore wind turbine in medium deep water
   * - P_Wind_Onshore_Avg
     - Onshore wind turbine, average placement
   * - P_Wind_Onshore_Inf
     - Onshore wind turbine, below-average placement
   * - P_Wind_Onshore_Opt
     - Onshore wind turbine, optimal placement
   * - PSNG_Air_Bio
     - Bio-fueled passenger plane
   * - PSNG_Air_Conv
     - Petroleum-fueled passenger plane
   * - PSNG_Air_H2
     - Hydrogen-fueled passenger plane
   * - PSNG_Rail_Conv
     - Petroleum-fueled passenger train
   * - PSNG_Rail_Electric
     - Electric passenger train
   * - PSNG_Road_BEV
     - Battery electric vehicle for passenger transport
   * - PSNG_Road_H2
     - Fuel-cell electric vehicle for passenger transport
   * - PSNG_Road_ICE
     - Internal combustion engine car for passenger transport
   * - PSNG_Road_LNG
     - Liquified natural gas fueled car for passenger transport
   * - PSNG_Road_PHEV
     - Plug-In hybrid vehicle for passenger transport
   * - R_Biogas
     - Renewable resource source technology: biogas
   * - R_Coal_Hardcoal
     - Resource source technology: hard coal
   * - R_Coal_Lignite
     - Resource source technology: lignite coal
   * - R_Gas
     - Resource source technology: natural gas
   * - R_Grass
     - Renewable resource source technology: grass waste for biomass generation
   * - R_Nuclear
     - Resource source technology: nuclear material
   * - R_Oil
     - Resource source technology: crude oil
   * - R_Paper_Cardboard
     - Renewable resource source technology: paper and cardboard waste for biomass generation
   * - R_Residues
     - Renewable resource source technology: organic residues for biomass generation
   * - R_Roundwood
     - Renewable resource source technology: roundwood potentials for biomass generation
   * - R_Waste
     - Renewable resource source technology: Waste-based energy
   * - R_Wood
     - Renewable resource source technology: wood potentials for biomass generation
   * - X_Alkaline_Electrolysis
     - Alkaline electrolysis
   * - X_ATR_CCS
     - Autothermal methane reforming with CCS, converting natural gas to hydrogen
   * - X_Biofuel
     - Conversion technology, converts biomass to biofuel
   * - X_Convert_HD
     - Conversion technology for district heat to industrial process or building heat
   * - X_DAC_HT
     - Direct air capture technology, high temperature
   * - X_DAC_LT
     - Direct air capture technology, low temperature
   * - X_Electrolysis
     - Electrolyzer for hydrogen generation
   * - X_Gasifier
     - Conversion technology, converts liquid hydrogen or natural gas to their gaseous forms
   * - X_Liquifier
     - Conversion technology, converts gaseous hydrogen or natural gas to their liquid forms
   * - X_Methanation
     - Conversion technology for methanation of biogas and hydrogen
   * - X_PEM_Electrolysis
     - PEM electrolysis
   * - X_Powerfuel
     - Conversion technology, creates powerfuels out of hydrogen
   * - X_SMR
     - Conversion technology, Steam-methane reforming, generated hydrogen out of natural gas
   * - X_SOEC_Electrolysis
     - SOEC electrolysis
   * - Z_ETS_Buy
     - Dummy technology for CO2 trading system (only relevant if country-level emission limits are used)
   * - Z_ETS_Sell
     - Dummy technology for CO2 trading system (only relevant if country-level emission limits are used)
   * - Z_Import_Gas
     - Import technology for natural gas from outside of the model scope
   * - Z_Import_H2
     - Import technology for hydrogen from outside of the model scope
   * - Z_Import_Hardcoal
     - Import technology for hard coal from outside of the model scope
   * - Z_Import_LNG
     - Import technology for liquified natural gas from outside of the model scope
   * - Z_Import_Oil
     - Import technology for crude oil from outside of the model scope

List of fuels
-------------

The following fuels are included in the current main version of GENeSYS-MOD (other fuels might be included in specific versions used for case studies etc.).

.. list-table::
   :header-rows: 1
   :widths: 28 72

   * - Name
     - Description
   * - Air
     - Dummy fuel used to calculate CO2 contents of air in DAC
   * - Area_Rooftop_Commercial
     - Surface area for rooftop installations (commercial buildings)
   * - Area_Rooftop_Residential
     - Surface area for rooftop installations (residential buildings)
   * - Biofuel
     - Biofuels (e.g. bio-diesel)
   * - Biomass
     - Solid biomass
   * - ETS
     - Dummy fuel used to emulate an emission-trading-system
   * - ETS_Source
     - Dummy fuel used to emulate an emission-trading-system
   * - Gas_Bio
     - Methane (from biological origin)
   * - Gas_Natural
     - Methane (from geological origin)
   * - Gas_Synth
     - Methane (from synthetic origin / hydrogen-derivative)
   * - H2
     - Hydrogen (gaseous)
   * - H2_Blend
     - Hydrogen-methane blend
   * - Hardcoal
     - Steam / hard coal
   * - Heat_Buildings
     - Space heating and warm water in buildings
   * - Heat_District
     - Heat feed-in into the district heating network
   * - Heat_High_Industrial
     - High-temperature industrial process heat (>1000°C)
   * - Heat_Low_Industrial
     - Low-temperature industrial process heat (<100°C)
   * - Heat_MediumLow_Industrial
     - Medium-temperature industrial process heat (100-400°C)
   * - Heat_MediumHigh_Industrial
     - Medium-temperature industrial process heat (400-1000°C)
   * - LBG
     - Liquid biogas / liquid form of Gas_Bio
   * - LH2
     - Liquid hydrogen (H2)
   * - Lignite
     - Lignite coal
   * - LNG
     - Liquefied natural gas / liquid form of Gas_Natural
   * - LSG
     - Liquefied synthetic gas / liquid form of Gas_Synth
   * - Mobility_Freight
     - Freight mobility services
   * - Mobility_Passenger
     - Passenger mobility services
   * - Nuclear
     - Nuclear fuel (e.g. fuel rods)
   * - Oil
     - Petroleum products
   * - Power
     - Electricity / power
   * - Powerfuel
     - E-fuels (e.g. synthetically derived diesel or gasoline)
   * - Waste
     - Waste energy resource


