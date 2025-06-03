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

DemandSplitByModalType
----------------------
**Sets: [ModalType,Timeslice,Region,Fuel,Year] Unit: [gpkm/gtkm]**

DiscountedAnnualCurtailmentCost
-------------------------------
**Sets: [Year,Fuel,Region] Unit: [M€]**

DiscountedAnnualProductionChangeCost
------------------------------------
**Sets: [Year,Technology,Region] Unit: [M€]**

DiscountedAnnualTotalTradeCosts
-------------------------------
**Sets: [Year,Region] Unit: [M€]**

DiscountedCapitalInvestment
---------------------------
**Sets: [Year,Technology,Region] Unit: [M€]**

DiscountedCapitalInvestmentStorage
----------------------------------
**Sets: [Storage,Year,Region] Unit: [M€]**

DiscountedNewTradeCapacityCosts
-------------------------------
**Sets: [Year,Fuel,Region,Region] Unit: [M€]**

DiscountedOperatingCost
-----------------------
**Sets: [Year,Technology,Region] Unit: [M€]**

DiscountedSalvageValue
----------------------
**Sets: [Year,Technology,Region] Unit: [M€]**

DiscountedSalvageValueStorage
-----------------------------
**Sets: [Storage,Year,Region] Unit: [M€]**

DiscountedSalvageValueTransmission
----------------------------------
**Sets: [Year,Region] Unit: [M€]**

DiscountedTechnologyEmissionsPenalty
------------------------------------
**Sets: [Year,Technology,Region] Unit: [M€]**

Export
------
**Sets: [Year,Timeslice,Fuel,Region,Region] Unit: [PJ]**

Import
------
**Sets: [Year,Timeslice,Fuel,Region,Region] Unit: [PJ]**

ModelPeriodCostByRegion
-----------------------
**Sets: [Region] Unit: [M€]**

ModelPeriodEmissions
--------------------
**Sets: [Region,Emission] Unit: [Mt]**

NetTrade
--------
**Sets: [Year,Timeslice,Fuel,Region] Unit: [PJ]**

NetTradeAnnual
--------------
**Sets: [Year,Fuel,Region] Unit: [PJ]**

NewCapacity
-----------
**Sets: [Year,Technology,Region] Unit: [GW]**

NewStorageCapacity
------------------
**Sets: [Storage,Year,Region] Unit: [PJ]**

NewTradeCapacity
----------------
**Sets: [Year,Fuel,Region,Region] Unit: [GW]**

NewTradeCapacityCosts
---------------------
**Sets: [Year,Fuel,Region,Region] Unit: [M€]**

OperatingCost
-------------
**Sets: [Year,Technology,Region] Unit: [M€]**

Production
----------
**Sets: [Year,Timeslice,Fuel,Region] Unit: [PJ]**

ProductionAnnual
----------------
**Sets: [Year,Fuel,Region] Unit: [PJ]**

ProductionByTechnology
----------------------
**Sets: [Year,Timeslice,Technology,Fuel,Region] Unit: [PJ]**

ProductionByTechnologyAnnual
----------------------------
**Sets: [Year,Technology,Fuel,Region] Unit: [PJ]**

ProductionDownChangeInTimeslice
-------------------------------
**Sets: [Year,Timeslice,Fuel,Technology,Region] Unit: [PJ]**

ProductionSplitByModalType
--------------------------
**Sets: [ModalType,Timeslice,Region,Fuel,Year] Unit: [%]**

ProductionUpChangeInTimeslice
-----------------------------
**Sets: [Year,Timeslice,Fuel,Technology,Region] Unit: [PJ]**

RateOfActivity
--------------
**Sets: [Year,Timeslice,Technology,Mode of Operation,Region] Unit: [GW]**

RateOfProduction
----------------
**Sets: [Year,Timeslice,Fuel,Region] Unit: [GW]**

RateOfProductionByTechnology
----------------------------
**Sets: [Year,Timeslice,Technology,Fuel,Region] Unit: [GW]**

RateOfProductionByTechnologyByMode
----------------------------------
**Sets: [Year,Timeslice,Technology,Mode of Operation,Fuel,Region] Unit: [GW]**

RateOfTotalActivity
-------------------
**Sets: [Year,Timeslice,Technology,Region] Unit: [GW]**

RateOfUse
---------
**Sets: [Year,Timeslice,Fuel,Region] Unit: [GW]**

RateOfUseByTechnology
---------------------
**Sets: [Year,Timeslice,Technology,Fuel,Region] Unit: [GW]**

RateOfUseByTechnologyByMode
---------------------------
**Sets: [Year,Timeslice,Technology,Mode of Operation,Fuel,Region] Unit: [GW]**

RETargetMin
-----------
**Sets: [Year,Region] Unit: [PJ]**

RETotalDemandOfTargetFuelAnnual
-------------------------------
**Sets: [Year,Region,Fuel] Unit: [PJ]**

SalvageValue
------------
**Sets: [Year,Technology,Region] Unit: [M€]**

SalvageValueStorage
-------------------
**Sets: [Storage,Year,Region] Unit: [M€]**

StorageLevelTSStart
-------------------
**Sets: [Storage,Year,Timeslice,Region] Unit: [PJ]**

StorageLevelYearFinish
----------------------
**Sets: [Storage,Year,Region] Unit: [PJ]**

StorageLevelYearStart
---------------------
**Sets: [Storage,Year,Region] Unit: [PJ]**

StorageLowerLimit
-----------------
**Sets: [Storage,Year,Region] Unit: [PJ]**

StorageUpperLimit
-----------------
**Sets: [Storage,Year,Region] Unit: [PJ]**

TotalActivityInReserveMargin
----------------------------
**Sets: [Region,Year,Timeslice] Unit: [GW]**

TotalActivityPerYear
--------------------
**Sets: [Region,Timeslice,Technology,Year] Unit: [PJ]**

TotalAnnualTechnologyActivityByMode
-----------------------------------
**Sets: [Year,Technology,Mode of Operation,Region] Unit: [PJ]**

TotalCapacityAnnual
-------------------
**Sets: [Year,Technology,Region] Unit: [GW]**

TotalDiscountedCost
-------------------
**Sets: [Year,Region] Unit: [M€]**

TotalDiscountedCostByTechnology
-------------------------------
**Sets: [Year,Technology,Region] Unit: [M€]**

TotalDiscountedStorageCost
--------------------------
**Sets: [Storage,Year,Region] Unit: [M€]**

TotalREProductionAnnual
-----------------------
**Sets: [Year,Region,Fuel] Unit: [PJ]**

TotalTechnologyAnnualActivity
-----------------------------
**Sets: [Year,Technology,Region] Unit: [PJ]**

TotalTechnologyModelPeriodActivity
----------------------------------
**Sets: [Technology,Region] Unit: [PJ]**

TotalTradeCapacity
------------------
**Sets: [Year,Fuel,Region,Region] Unit: [GW/PJ]**

TotalTradeCosts
---------------
**Sets: [Year,Timeslice,Region] Unit: [M€]**

Use
---
**Sets: [Year,Timeslice,Fuel,Region] Unit: [PJ]**

UseAnnual
---------
**Sets: [Year,Fuel,Region] Unit: [PJ]**

UseByTechnology
---------------
**Sets: [Year,Timeslice,Technology,Fuel,Region] Unit: [PJ]**

UseByTechnologyAnnual
---------------------
**Sets: [Year,Technology,Fuel,Region] Unit: [PJ]**

VariableOperatingCost
---------------------
**Sets: [Year,Timeslice,Technology,Region] Unit: [M€]**

WeightedAnnualEmissions
-----------------------
**Sets: [Year,Emission,Region] Unit: [Mt]**
