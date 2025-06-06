Variables
==============
AccumulatedNewCapacity
----------------------
**Sets: [Year,Technology,Region] Unit: [GW]**

Represents the total amount of capacity that was built in previous years and remains operational in the current year. It is defined as the sum of all past new-capacity additions within their defined operational lifetime.

AccumulatedNewStorageCapacity
-----------------------------
**Sets: [Storage,Year,Region] Unit: [PJ]**

Represents the total amount of storage capacity that was built in previous years and remains operational in the current year; defined as the sum of all past new-storage-capacity additions within their defined operational lifetime.

AnnualCurtailmentCost
---------------------
**Sets: [Year,Fuel,Region] Unit: [M€]**

The yearly expense assigned to curtailing energy. It is computed by multiplying the curtailed-energy volume in year y by its per-unit curtailment cost factor.

AnnualEmissions
---------------
**Sets: [Year,Emission,Region] Unit: [Mt]**

Total emissions of pollutant in a specific region for one year, defined as the sum of all technology-specific emissions. This aggregated figure is then used to enforce regional and system-wide emission limits.

AnnualFixedOperatingCost
------------------------
**Sets: [Year,Technology,Region] Unit: [M€]**

The annual fixed operating cost for a given technology and location, calculated as the sum of fixed‐cost charges on all capacity still in service (both newly built and existing).

AnnualProductionChangeCost
--------------------------
**Sets: [Year,Technology,Region] Unit: [M€]**

The total cost over a year for adjusting a dispatchable generator’s output up or down, computed by summing all increases and decreases in output and multiplying by the per-unit production-change cost.

AnnualSectoralEmissions
-----------------------
**Sets: [Year,Emission,SECTOR,Region] Unit: [Mt]**

Represents the total emissions of a given pollutant from a specific sector in a particular region and year. It is calculated as the sum of all technology-level emissions assigned to that sector in that region and year, and is used to enforce the annual sectoral emission cap.

AnnualTechnologyEmission
------------------------
**Sets: [Year,Technology,Emission,Region] Unit: [Mt]**

Defined as the total emissions of a given pollutant from a specific technologyy in a particular region and year. 

AnnualTechnologyEmissionByMode
------------------------------
**Sets: [Year,Technology,Emission,Mode of Operation,Region] Unit: [Mt]**

Represents the annual mass of a specific pollutant emitted by a given technology when running in a particular operating mode within a region. It is computed by taking that technology’s total yearly activity in the chosen mode, multiplying by the mode’s fuel‐input ratios, and then applying the pollutant content per unit of each fuel.

.. _annualtechnologyemissionpenaltybyemission:

AnnualTechnologyEmissionPenaltyByEmission
-----------------------------------------
**Sets: [Year,Technology,Emission,Region] Unit: [M€]**

The penalty cost assigned to a technology for emitting a particular pollutant in a given year and location, calculated by multiplying its annual emissions of that pollutant by the applicable penalty rate.

AnnualTechnologyEmissionsPenalty
--------------------------------
**Sets: [Year,Technology,Region] Unit: [M€]**

:ref:`annualtechnologyemissionpenaltybyemission` summed over all emissions.

AnnualTotalTradeCosts
---------------------
**Sets: [Year,Region] Unit: [M€]**

The total yearly expense for importing fuels into a region, calculated by summing each imported fuel volume (across all routes and timeslices) multiplied by its per-unit trade cost.

AnnualVariableOperatingCost
---------------------------
**Sets: [Year,Technology,Region] Unit: [M€]**

The annual variable operating cost reflects what it costs to run a technology over the year. It takes each mode of operation, multiplies how much the technology was used in that mode by its per-unit running cost, and then adds those figures together.

CapitalInvestment
-----------------
**Sets: [Year,Technology,Region] Unit: [M€]**

The total money spent on adding new capacity in a given year and location, calculated by multiplying the per-unit capital cost by the amount of capacity built.

CapitalInvestmentStorage
------------------------
**Sets: [Storage,Year,Region] Unit: [M€]**

The total money spent on adding new storage capacity in a given year and location, calculated by multiplying the per-unit capital cost by the amount of capacity built.

CurtailedCapacity
-----------------
**Sets: [Region,Timeslice,Technology,Year] Unit: [GW]**

Represents the portion of installed capacity at a given site and timeslot that remains idle even though it is technically able to operate. In other words, although that capacity could generate energy, it is held back—often because there is more supply than demand, grid limitations, or economic reasons.

CurtailedEnergy
---------------
**Sets: [Year,Timeslice,Fuel,Region] Unit: [PJ]**

Represents the quantity of energy in a single timeslice that was withheld even though capacity was available, calculated by converting each unit of idle capacity into its equivalent energy output.

CurtailedEnergyAnnual
---------------------
**Sets: [Year,Fuel,Region] Unit: [PJ]**

Represents the yearly total of energy not produced despite available capacity, obtained by summing all curtailed-energy values across every timeslice for a given fuel and region.

DemandNeedingReserveMargin
--------------------------
**Sets: [Year,Timeslice,Region] Unit: [PJ]**

Represents, for each time slice and region, the amount of demand that must be backed by generators tagged as reserve-eligible. It is calculated by summing all reserve-capable output (weighted by conversion factors, time-slice shares, and reserve tags) to ensure the required reserve margin is met.

DemandSplitByModalType
----------------------
**Sets: [ModalType,Timeslice,Region,Fuel,Year] Unit: [gpkm/gtkm]**

Denotes the portion of a region’s specified fuel demand allocated to each transport mode and time slice. It is obtained by multiplying the annual demand for that fuel by the mode-specific share and the time-slice profile.

DiscountedAnnualCurtailmentCost
-------------------------------
**Sets: [Year,Fuel,Region] Unit: [M€]**

Represents the present‐value cost of energy curtailment in a given year for a specific fuel and region, calculated by taking the undiscounted annual curtailment cost and dividing it by the appropriate discount factor for that year and location.

.. _discountedannualproductionchangecost:

DiscountedAnnualProductionChangeCost
------------------------------------
**Sets: [Year,Technology,Region] Unit: [M€]**

Reflects the discounted value of all ramp‐up and ramp‐down costs for a particular generation technology in a given region over a year, obtained by applying the technology-specific discount rate to the annual production-change cost.

DiscountedAnnualTotalTradeCosts
-------------------------------
**Sets: [Year,Region] Unit: [M€]**

Denotes the present‐value of the total cost of importing fuels into a region during the year, calculated by discounting the sum of its undiscounted annual trade costs by the regional discount rate.

.. _discountedcapitalinvestment:

DiscountedCapitalInvestment
---------------------------
**Sets: [Year,Technology,Region] Unit: [M€]**

Represents the discounted total spending on new capacity additions for a given technology and region in a year, found by applying the capital‐cost discount factor to that year’s undiscounted capital investment.


.. _discountedcapitalinvestmentstorage:

DiscountedCapitalInvestmentStorage
----------------------------------
**Sets: [Storage,Year,Region] Unit: [M€]**

Captures the present‐value of all capital spending on new storage capacity of a particular storage technology in a region and year, computed by dividing the year’s undiscounted storage investment by the region’s discount factor.

DiscountedNewTradeCapacityCosts
-------------------------------
**Sets: [Year,Fuel,Region,Region] Unit: [M€]**

Represents the discounted cost of expanding cross‐region trade capacity for a given fuel pair in a particular year, obtained by applying the appropriate discount rate to that year’s undiscounted investment in new trade infrastructure.

.. _discountedoperatingcost:

DiscountedOperatingCost
-----------------------
**Sets: [Year,Technology,Region] Unit: [M€]**

Denotes the present‐value of all variable and fixed operating costs for a given technology in a region over the year, calculated by discounting the sum of its undiscounted annual operating costs.

.. _discountedsalvagevalue:

DiscountedSalvageValue
----------------------
**Sets: [Year,Technology,Region] Unit: [M€]**

Reflects the present‐value benefit of retiring remaining capacity for a particular technology and region in a given year, computed by applying the discount factor to that year’s undiscounted salvage value for the retired capacity.

DiscountedSalvageValueStorage
-----------------------------
**Sets: [Storage,Year,Region] Unit: [M€]**

Captures the present‐value of salvaging any remaining storage capacity of a given storage technology in a region during that year, calculated by discounting the undiscounted salvage value by the regional discount rate.

DiscountedSalvageValueTransmission
----------------------------------
**Sets: [Year,Region] Unit: [M€]**

Represents the present‐value gain from retiring transmission assets within a region in a given year, obtained by applying the appropriate discount factor to the undiscounted salvage value of those transmission lines.

.. _discountedtechnologyemissionspenalty:

DiscountedTechnologyEmissionsPenalty
------------------------------------
**Sets: [Year,Technology,Region] Unit: [M€]**

Denotes the present‐value cost of all emissions penalties incurred by a specific generation technology in a region over the year, calculated by discounting the sum of its emission-based penalties.

Export
------
**Sets: [Year,Timeslice,Fuel,Region,Region] Unit: [PJ]**

Amount of a fuel exported from one region to another in a specific timeslice.

Import
------
**Sets: [Year,Timeslice,Fuel,Region,Region] Unit: [PJ]**

Amount of a given fuel imported into a region from another region during a specific timeslice. The model enforces that exports from Region A to Region B exactly match imports into Region B from Region A, ensuring a balanced trade flow.

ModelPeriodCostByRegion
-----------------------
**Sets: [Region] Unit: [M€]**

Represents the cumulative present‐value cost incurred in each region over the entire model period, calculated by summing that region’s :ref:`totaldiscountedcost` across all years.

ModelPeriodEmissions
--------------------
**Sets: [Region,Emission] Unit: [Mt]**

Represents the cumulative emissions a pollutant in a specific region over the entire model horizon, including exougenous emissions. It is used to add emission limits overthe entire model period. 

NetTrade
--------
**Sets: [Year,Timeslice,Fuel,Region] Unit: [PJ]**

Net trade measures, for each region, fuel, and time slice, the difference between exports (adjusted upward to account for trade losses) and imports into that region. Specifically, every unit exported is multiplied by (1 + loss factor) to reflect the extra amount that had to be shipped out before losses occur, and then imports are subtracted. 

NetTradeAnnual
--------------
**Sets: [Year,Fuel,Region] Unit: [PJ]**

Represents the yearly net volume of a specific fuel traded by a region , calculated as the sum of net trade across all time slices. A positive value indicates the region overall sends more fuel out (net exporter), while a negative value means it receives more than it ships (net importer). 

NewCapacity
-----------
**Sets: [Year,Technology,Region] Unit: [GW]**

Represents the amount of new generation capacity added in a given year and location, measured in gigawatts.

NewStorageCapacity
------------------
**Sets: [Storage,Year,Region] Unit: [PJ]**

Represents the amount of new generation capacity added in a given year and location, measured in petajoules.

NewTradeCapacity
----------------
**Sets: [Year,Fuel,Region,Region] Unit: [GW]**

Represents the additional inter‐regional transport capacity installed in a given year for moving a specific fuel between two regions, measured in gigawatts.

NewTradeCapacityCosts
---------------------
**Sets: [Year,Fuel,Region,Region] Unit: [M€]**

Represents the annual cost of building additional trade capacity for a fuel between two regions, calculated as the new capacity amount multiplied by the per-unit growth cost and the distance of that trade route.

OperatingCost
-------------
**Sets: [Year,Technology,Region] Unit: [M€]**

Represents the total annual expense to run a technology at a location, computed by summing its fixed and variable operating costs.

Production
----------
**Sets: [Year,Timeslice,Fuel,Region] Unit: [PJ]**

Represents the energy output of a given fuel in a particular region during a specific timeslice, calculated by summing each technology’s slice‐level production of that fuel.

ProductionAnnual
----------------
**Sets: [Year,Fuel,Region] Unit: [PJ]**

Denotes the total yearly energy output of a given fuel in a region, obtained by summing all timeslice‐level production values for that fuel across the entire year.

ProductionByTechnology
----------------------
**Sets: [Year,Timeslice,Technology,Fuel,Region] Unit: [PJ]**

Specifies the energy of a particular fuel produced by a single technology in a region during one timeslice, computed by converting the technology’s instantaneous activity (in GW) into PJ using the mode‐specific output ratios and the timeslice’s fraction of the year.

ProductionByTechnologyAnnual
----------------------------
**Sets: [Year,Technology,Fuel,Region] Unit: [PJ]**

Gives the annual total energy of a particular fuel produced by a single technology in a region, calculated as the sum of that technology’s timeslice‐level fuel production (in PJ) over all timeslices in the year.

ProductionDownChangeInTimeslice
-------------------------------
**Sets: [Year,Timeslice,Fuel,Technology,Region] Unit: [PJ]**

Measures the decrease in energy production of a given fuel by a specific technology from the previous timeslice to the current one, capturing downward ramping.

ProductionSplitByModalType
--------------------------
**Sets: [ModalType,Timeslice,Region,Fuel,Year] Unit: [%]**

Indicates the percentage share of a fuel’s production in a region and timeslice that is allocated to a particular transport mode, determined by tagging each technology‐mode pair and dividing its fuel output by the total fuel production in that slice.

ProductionUpChangeInTimeslice
-----------------------------
**Sets: [Year,Timeslice,Fuel,Technology,Region] Unit: [PJ]**

Measures the increase in energy production of a given fuel by a specific technology from the previous timeslice to the current one, capturing upward ramping.

.. _rateofactivity:

RateOfActivity
--------------
**Sets: [Year,Timeslice,Technology,Mode of Operation,Region] Unit: [GW]**

Represents the actual power output of a given technology running in a specific mode and region during a single timeslice. The sum of all mode‐specific RateOfActivity values for that technology equals its total available capacity (after applying availability, minus any reserved or curtailed capacity).

RateOfProduction
----------------
**Sets: [Year,Timeslice,Fuel,Region] Unit: [GW]**

Denotes the instantaneous generation rate of a particular fuel in a region during one timeslice, calculated by adding up each technology’s combined mode‐specific production rates for that fuel.

RateOfProductionByTechnology
----------------------------
**Sets: [Year,Timeslice,Technology,Fuel,Region] Unit: [GW]**

Specifies the instantaneous production rate (in GW) of a particular fuel by one technology in a region during a timeslice, obtained by summing that technology’s mode‐specific production rates for the fuel.

RateOfProductionByTechnologyByMode
----------------------------------
**Sets: [Year,Timeslice,Technology,Mode of Operation,Fuel,Region] Unit: [GW]**

Gives the instantaneous production rate (in GW) of a particular fuel by a specific technology operating in one mode and region during a timeslice.

RateOfTotalActivity
-------------------
**Sets: [Year,Timeslice,Technology,Region] Unit: [GW]**

Represents the total capacity (in GW) of a technology running in a region during a timeslice, summed across all its operating modes.

RateOfUse
---------
**Sets: [Year,Timeslice,Fuel,Region] Unit: [GW]**

Denotes the instantaneous fuel consumption rate for a given fuel in a region and timeslice, obtained by summing all technologies’ mode‐specific usage rates for that fuel.

RateOfUseByTechnology
---------------------
**Sets: [Year,Timeslice,Technology,Fuel,Region] Unit: [GW]**

Specifies the instantaneous consumption rate of a particular fuel by one technology in a region during a timeslice, calculated by summing that technology’s mode‐specific usage rates for the fuel (including time‐dependent efficiencies).

RateOfUseByTechnologyByMode
---------------------------
**Sets: [Year,Timeslice,Technology,Mode of Operation,Fuel,Region] Unit: [GW]**

Gives the instantaneous consumption rate of a specific fuel by a technology running in a certain mode and region during a timeslice.

RETargetMin
-----------
**Sets: [Year,Region] Unit: [PJ]**

RETotalDemandOfTargetFuelAnnual
-------------------------------
**Sets: [Year,Region,Fuel] Unit: [PJ]**

.. _salvagevalue:

SalvageValue
------------
**Sets: [Year,Technology,Region] Unit: [M€]**

Represents the remaining undepreciated value of newly built capacity at the end of the model horizon, for each technology and region. For any unit of capacity added in year y, if its operational lifetime extends beyond the final model year, that leftover portion is considered a “salvage” asset with some resale or secondary‐use value. Two depreciation methods determine how much of the original capital cost survives at the horizon:

- **Annuitized:**
When a technology’s discount rate is positive and the asset’s full operational life extends past the last model year, the model computes salvage as follows:

.. math::

    {\small
    SalvageValue_{y,t,r} 
    = \; CapitalCost_{r,t,y}\;\cdot\;  NewCapacity_{y,t,r} 
      \;\left(\,
        1 \;-\; 
        \frac{ 
          \bigl(1 + DiscountRate_{r,t}\bigr)^{\,\bigl(\max(\mathcal{Y}) - y + 1\bigr)} \;-\; 1 
        }{ 
          \bigl(1 + DiscountRate_{r,t}\bigr)^{\,\bigl(OperationalLife_t\bigr)} \;-\; 1 
        }
      \right)
    }

- **Straight‐Line:**
If a technology’s discount rate is zero (so Method 1 would divide by zero) the salvage calculation falls back to straight‐line depreciation:

.. math::

    {\small
    SalvageValue_{y,t,r} 
    = \; CapitalCost_{r,t,y}\;\cdot\;  NewCapacity_{y,t,r} 
      \;\left(\,
        1 \;-\; 
        \frac{ 
          \bigl(\max(\mathcal{Y}) - y + 1\bigr)
        }{ 
          \bigl(OperationalLife_{t}\bigr)
        }
      \right)
    }

SalvageValueStorage
-------------------
**Sets: [Storage,Year,Region] Unit: [M€]**

Represents the remaining undepreciated value of storage capacity at the end of the model horizon, analogous to how :ref:`salvagevalue` captures undepreciated value for generation technologies.

StorageLevelTSStart
-------------------
**Sets: [Storage,Year,Timeslice,Region] Unit: [PJ]**

Represents the state-of-charge at the beginning of each timeslice for a given storage asset in a region. For any slice beyond the first, it equals the previous slice’s start level plus the net charging minus discharging, all scaled by the timeslice fraction. For the first slice, it is initialized from the year-start level. It is also constrained not to exceed the sum of available storage capacity.

StorageLevelYearFinish
----------------------
**Sets: [Storage,Year,Region] Unit: [PJ]**

The state-of-charge at the end of each year for a given storage asset and region, which by construction equals the level at the start of the same year (ensuring a cyclical, year-to-year accounting of stored energy).

StorageLevelYearStart
---------------------
**Sets: [Storage,Year,Region] Unit: [PJ]**

The state-of-charge at the beginning of each year for a storage asset and region, which must lie between storage-specific upper and lower bounds based on available capacity and residual inventory.

StorageLowerLimit
-----------------
**Sets: [Storage,Year,Region] Unit: [PJ]**

Defines the minimum allowable storage level for each asset, year, and region, set as a fixed fraction of total available storage capacity to ensure a required minimum reserve of stored energy.

StorageUpperLimit
-----------------
**Sets: [Storage,Year,Region] Unit: [PJ]**

Defines the maximum allowable storage level for each asset, year, and region expressed as a fraction of total available storage capacity so that storage holdings cannot exceed physical capacity.

TotalActivityInReserveMargin
----------------------------
**Sets: [Region,Year,Timeslice] Unit: [GW]**

Represents, for each region and timeslice, the total energy‐equivalent output from all generators that qualify as reserve‐eligible. It is calculated by summing each technology’s slice‐level generation only for those technologies and fuels tagged to provide reserves, thereby measuring the amount of capacity available to meet the reserve‐margin requirement.

TotalActivityPerYear
--------------------
**Sets: [Region,Timeslice,Technology,Year] Unit: [PJ]**

Represents the total potential energy a technology could generate in a region during a specific timeslice and year.

TotalAnnualTechnologyActivityByMode
-----------------------------------
**Sets: [Year,Technology,Mode of Operation,Region] Unit: [PJ]**

Denotes the actual annual energy output of a given technology in a particular operating mode and region, obtained by summing its activity over all timeslices in the year.

TotalCapacityAnnual
-------------------
**Sets: [Year,Technology,Region] Unit: [GW]**

Denotes the total available capacity of a given technology in a region during a year, calculated as the sum of its residual capacity and the accumulated new capacity still within its operational life.

.. _totaldiscountedcost:

TotalDiscountedCost
-------------------
**Sets: [Year,Region] Unit: [M€]**

Represents the overall net present‐value expenditure for a region in a specific year, obtained by summing:

- :ref:`totaldiscountedcostbytechnology` across all technologies

- :ref:`totaldiscountedstoragecost` across all storage assets.

.. _totaldiscountedcostbytechnology:

TotalDiscountedCostByTechnology
-------------------------------
**Sets: [Year,Technology,Region] Unit: [M€]**

Represents the net present‐value cost of operating and investing in a specific technology and region during a given year. It is calculated as the sum of:

- :ref:`discountedoperatingcost` (annual fixed + variable operating costs)

- :ref:`discountedcapitalinvestment` (new capacity expenditure)

- :ref:`discountedtechnologyemissionspenalty` (emissions fines)

- :ref:`discountedannualproductionchangecost` (ramp‐up/ramp‐down costs)

minus :ref:`discountedsalvagevalue` (residual value recovered at horizon).

.. _totaldiscountedstoragecost:

TotalDiscountedStorageCost
--------------------------
**Sets: [Storage,Year,Region] Unit: [M€]**

Denotes the net present‐value cost of adding and operating storage capacity in a region during a given year. It equals the :ref:`discountedcapitalinvestmentstorage` minus the :ref:`discountedsalvagevalue` of that storage at the end of the model horizon.

TotalREProductionAnnual
-----------------------
**Sets: [Year,Region,Fuel] Unit: [PJ]**

Represents the total annual energy output (in PJ) from all renewable technologies producing a given fuel in a region and year. It is used to enforce both minimum renewable‐production targets and year‐to‐year growth paths based on specified demand ratios.

TotalTechnologyAnnualActivity
-----------------------------
**Sets: [Year,Technology,Region] Unit: [PJ]**

Represents the total annual energy output of a given technology in a region and year, calculated by summing its annual production across all fuels.

TotalTechnologyModelPeriodActivity
----------------------------------
**Sets: [Technology,Region] Unit: [PJ]**

Represents the  sum of a technology’s annual output over the entire model horizon. It is then subject to any model‐period upper or lower activity limits. 

TotalTradeCapacity
------------------
**Sets: [Year,Fuel,Region,Region] Unit: [GW/PJ]**

Represents the total available transport capacity for a specific fuel between two regions in a given year. It equals the preset trade capacity plus any newly added and commissioned trade capacity that comes online that year.

TotalTradeCosts
---------------
**Sets: [Year,Timeslice,Region] Unit: [M€]**

Use
---
**Sets: [Year,Timeslice,Fuel,Region] Unit: [PJ]**

Represents the total energy consumption of a given fuel in a region during a specific timeslice.

UseAnnual
---------
**Sets: [Year,Fuel,Region] Unit: [PJ]**

Represents the total annual energy consumption of a given fuel in a region.

UseByTechnology
---------------
**Sets: [Year,Timeslice,Technology,Fuel,Region] Unit: [PJ]**

Represents the energy content of a fuel consumed by a technology per region and timeslice.

UseByTechnologyAnnual
---------------------
**Sets: [Year,Technology,Fuel,Region] Unit: [PJ]**

Represents the total yearly energy of a fuel consumed by a technology in a specific region, calculated by summing the timeslice‐level fuel use (in PJ) across all timeslices.

VariableOperatingCost
---------------------
**Sets: [Year,Timeslice,Technology,Region] Unit: [M€]**

WeightedAnnualEmissions
-----------------------
**Sets: [Year,Emission,Region] Unit: [Mt]**

For each region and pollutant, weighted emissions for year y are defined so that they lie halfway between that year’s actual emissions and the next year’s, except in the final year where they simply equal that year’s emissions. This approach ensures that when you integrate (sum) emissions over the multi‐year intervals you approximate the area under a linear interpolation between those two years. 








