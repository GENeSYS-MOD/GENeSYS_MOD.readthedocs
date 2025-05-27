Parameters
==============


AnnualEmissionLimit 
--------------------
**Limits the maximum amount of Emissions in a year. Sets: [Emission, Year] Unit: [Megatonnes]**

Enables the user to set a maximum amount of emissions across all sectors for each model year. This can be used, for example, to gradually reduce emissions and reach a net-zero target in a specific year. `Carbon Budget Calculator <https://carbonbudgetcalculator.com/>`_  is a resource to generate different scenarios. 

AnnualExogenousEmission
--------------------------

**Amount of external Emissions for a year in a certain region. Sets: [Region, Year] Unit: [Megatonnes]**

This parameter allows the user to add exogenous emissions to the model that would otherwise not be captured but are intended to be accounted for in the model setup. These can include emissions from, for example, cement production, international air travel, and agriculture.

AnnualSectoralEmissionLimit
----------------------------
**Limits the maximum amount of Emissions for a specific sector and region in a year. Sets: [Emission, Sector, Year] Unit: [Megatonnes]**

This parameter enables the user to set specific emission targets for each sector in different regions per year. This allows for more precise control over sectoral emissions and their impact on model results.

AvailabilityFactor
---------------------
**Maximum time a technology may run for the whole year.  Sets: [Region, Technology, Year] Unit: [Fraction]**

Caps the maximum time a technology may run for the whole year and is often used to simulate planned outages. GENeSYS-MOD will choose when to run or not run. It can also be used to “turn off” technologies if they are not to be used by the model by setting their AvailabilityFactor to zero. 

BaseYearProduction
---------------------
**Describes how much of a fuel has to be produced by specific technologies in the base year across all regions. Sets: [Region, Technology, Year] Unit: [PJ]**

→ Currently not used.

.. _baseyearslack:

BaseYearSlack
--------------
**Slack for RegionalBaseYearProduction. Sets: [Fuel] Unit: [Fraction]**

Defines by how much the regional base year production can vary from its value given in :ref:`regionalbaseyearproduction`.

CapacityFactor
----------------
**Indicates the maximum time a technology may run in a given time slice. Sets: [Region, Technology, TimeSlice, Year] Unit: [Fraction]**

→ Not used, defined in model.

CapacityToActivityUnit
-----------------------
**Converts capacity to activity. Sets: [Technology] Unit: [PJ/GW-YR]**

For this parameter, a factor of 31.536 is used, representing the energy produced in PJ by 1 GW operating for one year:

:math:`\frac{1\,\text{GW} \times 8760\,\text{h} \times 3600\,\text{s}}{10^6} = 31.536\,\text{PJ}` 

For non-energetic activities, the value is 1.

CapitalCost
--------------
**Total capital cost (including interest paid during construction) per unit of capacity for new capacity additions. Sets: [Region, Technology, Year] Unit: [M€/GW]**

The capital costs are provided for each region, technology, and year, allowing the user to account for changes over time due to technological improvements.
For freight transport, values are given in million euros per gigatonne-kilometre per year (M€/Gtkm/year), and for passenger transport in million euros per gigapassenger-kilometre per year (M€/Gpkm/year).

CapitalCostStorage
--------------------
**Capital Cost of storages per energy content. Sets: [Region, Technology, Year] Unit: [M€/PJ]**

The capital costs for storages are provided per region, technology, and year, allowing for the consideration of changes over time due to technological improvements. Compared to the CapitalCost, this parameter is given in M€/PJ, as for storage technologies the amount of energy that can be stored is specified, not the power capacity in GW.

CommissionedTradeCapacity
--------------------------
**Planned capacity. Sets: [Refion,Region2,Fuel] Unit: [GW]**

Commissioned trade capacity will be built by the model; however, other than residual capacity, all costs are accounted for. This feature can primarily be used to implement policy plans and other planned capacity.

EmissionActivityRatio
----------------------
**Emissions factor per unit of activity. Sets: [Region, Technology, Mode_of_operation, Emission, Year] Unit: [Fraction]**

The value is typically 1, representing full emissions, but it can vary for carbon capture and storage (CCS) technologies, as not all emissions are released into the atmosphere. In some cases, the value can even be negative—such as with direct air capture (DAC) or bioenergy with carbon capture and storage (BECCS)—indicating net removal of CO₂.

EmissionContentPerFuel
-----------------------
**Emission content per unit of energy per fuel. Sets: [Fuel, Emission] Unit: [Megatonnes/PJ]**

It allows the model to translate fuel consumption into associated emissions by multiplying it with the fuel input used in technologies. For example, hard coal has a value of 0.0939 Mt/PJ, meaning burning 1 PJ of hard coal emits 0.0939 Mt of CO₂.

EmissionPenaltyTagTech
-----------------------
**Tags all technologies which produce emissions. Sets: [Technology] Unit: [Binary]**

This is a binary parameter that tags technologies which produce emissions (e.g. CO₂). A value of 1 indicates the technology emits and may be subject to penalties or carbon pricing.

EmissionsPenalty
-----------------
**Externality cost per unit of emission. Sets: [Region, Emission, Year] Unit: [M€/Megatonnes]**

This represents the carbon price and can be used instead of an emissions target to explore how different carbon prices influence scenario outcomes.

FixedCost
--------------
**The annual cost per unit of capacity of a technology. Sets: [Region, Technology, Year] Unit: [M€/GW]**

Represents the annual fixed cost associated with maintaining and operating one gigawatt (GW) of installed capacity for a given technology. It is measured in million euros per gigawatt per year (M€/GW) and includes costs that do not vary with output, such as maintenance, insurance, and administrative expenses.
For freight transport, values are given in million euros per gigatonne-kilometre per year (M€/Gtkm/year), and for passenger transport in million euros per gigapassenger-kilometre per year (M€/Gpkm/year).

.. _generaldiscountrate:

GeneralDiscountRate
---------------------
**Discount rate used in the model. Sets: [Region] Unit: [Fraction]**

All fiscal units are handled in 2018 (or base year if different from 2018) terms (with amounts in other years being discounted towards the base year). The general discount rate used is 5%.

GrowthRateTradeCapacity
----------------------------
**Defines by how much the trade capacity between two regions can grow. Sets: [Region, Region2, Fuel, Year] Unit: [Factor]**

Defines the maximum rate at which trade capacity between two regions can grow each year, expressed as a factor of the previous year's total capacity, thereby limiting how much new capacity can be added annually. So, if the growth rate is 0.1 (10%), and the capacity last year was 100 MW, then at most 10 MW of new capacity can be added this year.

.. _inputactivityratio:

InputActivityRatio
---------------------
**The input (use) of fuel per unit of activity for each technology. Describes, in combination with the OutputActivityRatio, the efficiency of the technology.  Sets:[Region ,Technology ,Fuel ,Mode_of_operation, Year] Unit: [Fraction]**

Let's take an example of a Power producing technology P_Gas_CCGT. The table below shows the Fuels the technology can use, these correspond to the mode_of_operation. For each of the fuel, the InputActivityRatio is specified which is the amount of Gas that is needed to produce one unit of output. The efficiency therefore is :math:`\frac{1}{\text{InputActivityRatio}}` (see right column). The value can change over the years if an efficiency increase (or decrease) is expected.

.. figure:: /_static/parameter/InputActivityRatio_1.png
   :width: 650
   :align: center

   Excerpt from InputActivityRatio for P_Gas_CCGT

We then go into the OutputActivityRatio. There we can see that for each of the mode_of_operations, the output is exactly 1 unit of power. 

.. figure:: /_static/parameter/InputActivityRatio_2.png
   :width: 650
   :align: center

   Excerpt from OutputActivityRatio for P_Gas_CCGT

CHPs make up a special case as they can produce power and heat simultaneously in one mode of operation.  
**Example:**  

.. figure:: /_static/parameter/InputActivityRatio_3.png
   :width: 650
   :align: center

   InputActivityRatio values for CHP_Biomass_Solid

For CHP_Biomass_Solid the value for the year 2018 is 2.890173 for the fuel Biomass in Mode_of_operation 1. This means the efficiency is :math:`\frac{1}{\text{2.890173}}= 0.346` so around 34.6%. If we want to know what Mode_of_operation 1 means, we can look it up in the OutputActivityRatio.  

.. figure:: /_static/parameter/InputActivityRatio_4.png
   :width: 650
   :align: center

   OutputActivityRatio values for CHP_Biomass_Solid

This means that we produce one unit of power from the 2.890173 Units of Biomass we put in.

For mode of operation 2, we find the following InputActivityRatio 3.571428572. The technology produces 1 Unit of power and 2.568 Units of Heat_District from the 3.571428572 Units of Biomass (OutputActivityRatio). The model can decide which mode_of_operation to use. Total CHP system efficiency would equate to 

:math:`\frac{\text{Power Output} + \text{Heat Output}}{\text{Input}} = \frac{1 + 2.568}{3.571428571} = 0.999` 

so around 99%. The fact that the excess heat is used greatly improves the efficiency of the technology.

MinStorageCharge 
---------------------
**Lower bound of total storage capacity which always has to be charged. Sets: [Region, Storage, Year] Unit: [Fraction]**

Defines the minimum fraction of total storage capacity that must remain charged at all times. It is applied as a lower bound on the storage level at the start of each time slice, ensuring that storage units are not completely depleted. This fraction is calculated based on the sum of newly installed and still-operational residual storage capacity. The parameter helps reflect technical constraints or policy requirements that require a certain minimum level of stored energy to always be available.

.. _modalsplitbyfuel:

ModalSplitByFuel 
---------------------
**Describes the distribution of technologies within a specific modal type. Sets: [Region, Fuel, ModalType] Unit: [Fraction]**

This parameter defines the distribution of technologies across different modal types. There are two fuels: Passenger Transport and Freight Transport, each with a specified annual demand. Both fuel categories have different technologies (ModalTypes) that can meet this demand. The ModalSplitByFuel parameter defines the minimum share of each technology.
**Example:** For the fuel Mobility Passenger, there are three main Modal Types (MT_PSNG_ROAD, MT_PSNG_RAIL, MT_PSNG_AIR), meaning that passenger transport can be carried out via road, rail, or air. The values indicate that 91.3% of Passenger Transport in 2018 was done via Road (e.g., cars), 7.6% via Rail, and 1% via Air transport. The total for 2018 is 100%, meaning the model has no remaining capacity to allocate any additional shares.

.. figure:: /_static/parameter/ModalSplitByFuel_1.png
   :width: 650
   :align: center

   Example ModalSplit for Passenger Transport

For the three main Modal Types, there are also subtypes that can be defined by the user. For MT_PSNG_RAIL, for example, there are two Modal Types: CONV (Conventional - Fossil Fuel) and RE (Renewable - Power). These subtypes contribute 6.47% and 1.09%, respectively, to make up MT_PSNG_RAIL (7.6%), leaving a small margin for the model to decide which one to use.

.. figure:: /_static/parameter/ModalSplitByFuel_2.png
   :width: 650
   :align: center

   Example ModalSplit for Passenger Transport Subtypes

As the years progress, the model is typically given more flexibility in selecting the technologies used. The ModalSplitByFuel parameter then establishes a lower limit for the share that a technology must maintain. In our example, the total share is at 92% in 2030, meaning the remaining 8% can be allocated by the model. This parameter allows the model to incorporate political plans or scenarios (e.g., 30% BEV by 2035 for passenger transport).

.. figure:: /_static/parameter/ModalSplitByFuel_3.png
   :width: 650
   :align: center

   Example ModalSplit for Passenger Transport in 2030

The principle of this example applies to all Fuels and Modal Types for ModalSplitByFuel. In general, this data serves as a guide for the model, and the user can decide how much flexibility to allow the model, considering that everything beyond the base year is based on assumptions.

Overview of ModalTypes and Technologies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Mobility Fright**

+------------+------------------------+------------------------+------------------------+
| Modaltype  | ROAD                   | RAIL                   | SHIP                   |
+============+========================+========================+========================+
| _CONV      | | FRT_Road_ICE         | | FRT_Rail_Conv        | | FRT_Ship_Conv        |
|            | | FRT_Road_PHEV        | | FRT_Rail_Conv(2)     | | FRT_Ship_LNG         |
|            | | FRT_Road_LNG         | | FRT_Rail_Conv(3)     |                        |
|            | | FRT_Road_LNG         |                        |                        |
|            | | FRT_Road_ICE(2)      |                        |                        |
|            | | FRT_Road_ICE(3)      |                        |                        |
+------------+------------------------+------------------------+------------------------+
| _RE        | | FRT_Road_BEV         | | FRT_Rail_Electric    | | FRT_Ship_Bio         |
|            | | FRT_Road_H2          |                        | | FRT_Ship_Conv(2)     |
|            | | FRT_Road_OH          |                        | | FRT_Ship_LNG         |
|            | | FRT_Road_PHEV(2)     |                        |                        |
|            | | FRT_Road_PHEV(3)     |                        |                        |
+------------+------------------------+------------------------+------------------------+

**Mobility Passenger**

+----------+------------------------+------------------------+------------------------+
| Subtype  | ROAD                   | RAIL                   | AIR                    |
+==========+========================+========================+========================+
| _CONV    | | PSNG_Road_ICE        | | PSNG_Rail_Conv       | | PSNG_Air_Conv        |
|          | | PSNG_Road_PHEV       |                        | | PSNG_Air_Conv(2)     |
|          | | PSNG_Road_LNG        |                        |                        |
+----------+------------------------+------------------------+------------------------+
| _RE      | | PSNG_Road_BEV        | | PSNG_Rail_Electric   | | PSNG_Air_Bio         |
|          | | PSNG_Road_H2         | | PSNG_Rail_Conv(2)    | | PSNG_Air_H2          |
|          | | PSNG_Road_ICE(2)     | | PSNG_Rail_Conv(3)    |                        |
|          | | PSNG_Road_PHEV(2)    |                        |                        |
|          | | PSNG_Road_ICE(3)     |                        |                        |
|          | | PSNG_Road_PHEV(3)    |                        |                        |
+----------+------------------------+------------------------+------------------------+

.. note::

   The number in () denotes the mode of operation, if different from 1.  
   See :ref:`inputactivityratio` for more information on the mode of operation.

Some general points:

- To find all technologies linked to the ModelTypes, check the Parameter 
- Ship usually accounts for all transport done on water within a country
- Air usually accounts for all inland flights 

ModelPeriodActivityMaxLimit 
-----------------------------
**Maximum total activity for the complete model period per region. Sets: [Region, Technology] Unit: [PJ]**

This parameter defines the maximum values for Resource Technologies (e.g., R_Coal_Hardcoal, R_Gas, etc.), which represent the extraction of resources. It indicates the maximum potential of a resource in a specific region, essentially reflecting the reserves that can potentially be accessed.
To calculate this, one might take the resource reserves and multiply them by the energy content specific to the fuel to get the value in PJ as required for GENeSYS-MOD.
A potential source for 2018 could be: `BP Statistical Review of World Energy <https://www.bp.com/content/dam/bp/business-sites/en/global/corporate/pdfs/energy-economics/statistical-review/bp-stats-review-2018-full-report.pdf>`_

ModelPeriodEmissionLimit 
-------------------------
**Total model period upper limit for a specific emission generated in the whole modelled region.  Sets: [Emission] Unit: [Megatonnes]**

The ModelPeriodEmissionLimit sets a maximum allowed amount of a specific emission across all regions over the entire model period, ensuring total emissions stay within a defined global limit.

ModelPeriodExogenousEmission 
------------------------------
**Additional emissions over the entire modelled period, on top of those computed endogenously by the model. Sets: [Region, Emission] Unit: [Megatonnes]**

ModelPeriodExogenousEmission defines the total amount of external (exogenous) emissions—such as from cement, agriculture, or international travel—that are not captured by the modeled technologies but must still be included in the overall emission accounting for the model period. These emissions are added to the model’s total emissions and count against the ModelPeriodEmissionLimit.

.. _operationallife:

OperationalLife 
-----------------
**Operational lifespan of a process in years. Sets: [Technology] Unit: [Years]**

OperationalLife defines the number of years a technology remains operational after installation. It determines how long newly installed capacity contributes to the system before it retires.

OperationalLifeStorage 
-------------------------
**Operational Life of Storages. Sets: [Storage] Unit: [Years]**

Defines the number of years a storage remains operational after installation. It determines how long newly installed capacity contributes to the system before it retires.

OutputActivityRatio 
---------------------
**Ratio of output to activity. Describes, together with the InputActivityRatio, the efficiency of the technology Sets: [Region, Technology] Unit: [Fraction]**

See :ref:`inputactivityratio` for further information.

ProductionChangeCost 
----------------------
**Production change cost. Sets: [Technology, Year] Unit: [M€]**

Cost associated with increasing or decreasing the output of a dispatchable technology within a year, measured in million euros (M€). It reflects operational costs like fuel ramping penalties, wear and tear, or market balancing charges.
For example, if CHP_Coal_Hardcoal has a value of 13.8889 M€, and its production ramps up or down by 1 PJ across timeslices, the model will assign 13.8889 M€ in ramping cost for that change.

ProductionGrowthLimit 
----------------------
**This parameter controls the maximal increase between two years of a specific fuel production from renewable energy sources. Sets: [Fuel, Year] Unit: [Fraction]**

ProductionGrowthLimit defines the maximum allowed annual increase in the production of a specific fuel from renewable energy technologies, expressed as a fraction of the previous year’s production, to ensure a gradual and realistic scale-up.

.. _rampingdownfactor:

RampingDownFactor 
------------------
**RampingDownFactor. Sets: [Technology, Year] Unit: [Fraction]**

Limits the rate at which a dispatchable technology can decrease its output during a given timeslice, in this case, per hour. It is a unitless factor that represents a fraction of the technology’s available capacity.
This factor ensures that the model reflects the physical constraints of power plants, which typically cannot abruptly reduce their output due to operational limits like thermal inertia.
Example: For a coal plant with a ramping down factor of 0.02, the maximum reduction in output allowed per hour is 2% of the plant’s available capacity. This prevents rapid shutdowns, ensuring that power plants follow a more gradual decrease in output over time.

RampingUpFactor 
----------------
**RampingUpFactor. Sets: [Technology, Year] Unit: [Fraction]**

Same as :ref:`rampingdownfactor`, but for increasing output.

RegionalAnnualEmissionLimit 
----------------------------
**Limits the maximum amount of Emissions for a certain region in a year. Sets: [Region, Emission, Year] Unit: [PJ]**

RegionalAnnualEmissionLimit sets an upper limit on the amount of a specific emission (in megatonnes) that can be released in a given region during a single year, helping enforce regional environmental or regulatory targets.

.. _regionalbaseyearproduction:

RegionalBaseYearProduction 
----------------------------
**Describes how much of a fuel has to be produced by specific technologies in the base year per region. Sets: [Region, Technology, Fuel, Year] Unit: [PJ]**

Based on historical data, helps to calibrate the model in the base year primarily for the power sector but should also be applied to the heating sector. In the base year, the model will generate the exact amount of power given for each region and technology, using existing capacities only, as it cannot build new ones to ensure accurate historical representation. Therefore, it's crucial to provide sufficient residual capacities to match the regional production of the base year (for heat, the technology can be built endogenously by doing a model run). To allow for some flexibility, the model can vary production within a set range, given via the Parameter :ref:`baseyearslack` (Fraction).

RegionalCCSLimit 
-----------------
**Describes how much carbon can be stored per region. Sets: [Region, Value] Unit: [Megatonnes]**

RegionalCCSLimit sets the maximum amount of CO₂ that can be stored via carbon capture and storage technologies in a given region over the entire model period, ensuring storage remains within regional capacity limits.

RegionalModelPeriodEmissionLimit 
----------------------------------
**Total model period upper limit for a specific emission generated in a certain modelled region. Sets: [Region, Emission] Unit: [Megatonnes]**

RegionalModelPeriodEmissionLimit sets an upper limit, in megatonnes, on the total amount of a specific emission that can be released in a particular region over the entire model period, ensuring long-term regional emission targets are met.

REMinProductionTarget 
----------------------
**Minimal production target for renewable energy sources. Sets: [Region, Fuel, Year] Unit: [PJ]**

REMinProductionTarget defines the minimum amount of energy (in PJ) that must be produced from renewable sources for a specific fuel in a given region and year, ensuring that the modeled energy system meets predefined renewable production targets.

ReserveMargin 
--------------
**The reserve (installed) capacity required relative to the peak demand. Sets: [Region, Year] Unit: [Ratio]**

Specifies the required ratio of reserve capacity relative to peak demand, ensuring that the system has enough extra capacity to maintain reliability during high-demand periods or unexpected outages.

ReserveMarginTagFuel 
---------------------
**Indicates if the output fuel has a reserve margin associated with it. Sets: [Fuel] Unit: [Binary]**

A binary indicator that defines whether a specific fuel type should be included in the calculation of demand requiring reserve capacity.

ReserveMarginTagTechnology 
---------------------------
**Amount the technology contributes to the reserve margin. Sets: [Technology] Unit: [Fraction]**

Indicates the fraction of a technology’s capacity that can contribute to the reserve margin, reflecting its suitability for reliably providing backup capacity  1=100%  0.2=20%.

.. _residualcapacity:

ResidualCapacity 
-----------------
**The capacity left over from periods prior to the modeling period. Sets: [Region, Technology, Year] Unit: [GW]**

Residual Capacity is the existing capacity that the model can utilize. It essentially represents the current capabilities/capacities of the region under consideration. It is important to take into account the lifespan of the technologies and/or any planned decommissions.

.. note::

   For Transport there is usually no data, as this will be done by running the model once and allowing the model to build new capacities based on the modal split. For heating, this can also be done, but if you have information on capacities, it is more realistic to use the existing data.


**Example:** A coal power plant of 2MW that will be decommissioned in 2030 will be available for the model in the base year 2018 and in 2025. In 2030, however, the model would need to build new capacities (including capital costs etc.). 

.. figure:: /_static/parameter/ResidualCapacity_1.png
   :width: 650
   :align: center

   Example Capacities for P_Coal_Hardcoal from 2020 to 2030

Residual Capacity for Heating and Transport
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The capacities for the heating and transport sectors in the baseyear are generated by the model based on information from the :ref:`modalsplitbyfuel` and the :ref:`regionalbaseyearproduction`. The main issue with this approach is that all capacities are assumed to be built in 2018. The model then applies the :ref:`operationallife` to these capacities, which would lead to a large number of technologies being decommissioned simultaneously at the end of their lifespan. This results in an unrealistic, abrupt drop in capacity.

In reality, technologies such as cars are decommissioned gradually over time. To better reflect this in the model, we convert the capacity built in 2018 from the results into residual capacity. This is done by taking the built capacities from the results file and entering them into ResidualCapacity. To make this more realistic, we then reduce the residual capacity incrementally in each model period. This ensures that, for example, by 2025 a portion of the capacity must be replaced, mimicking the continuous turnover observed in the real world.

**Example:**
The model builds the technology PSNG_Road_ICE in a specific region, with a total capacity of 100. This technology has an operational life of 20 years. If the model builds this capacity in 2018, it will all be decommissioned at once by 2040, resulting in an unrealistic, sudden drop in capacity. In reality, many of the cars currently in use will be decommissioned much earlier.

To address this, we use the model's built capacity as the basis for our ResidualCapacity in 2018. However, we apply a gradual reduction over time to better reflect real-world decommissioning. Specifically:

- In 2025, we reduce the residual capacity to 90% of the original 2018 value.
- By 2030, it will be reduced to 60% of the original capacity.
- In 2035, only 30% of the original capacity remains.
- After 2035, no residual capacity remains.

.. figure:: /_static/parameter/ResidualCapacity_2.png
   :width: 650
   :align: center

   Example of decreasing residual capacities for passenger transport

This can be repeated for all technologies in the Transport & Industry sector taking into account their :ref:`operationallife`. If the lifespan is longer, the reduction on technologies each year also needs to be adjusted.

This approach ensures that the model must replace decommissioned capacity in each model period, creating a more realistic trajectory. Where available, census or other national data can be used to refine these assumptions and improve accuracy.

ResidualStorageCapacity 
-------------------------
**The capacity left over from periods prior to the modeling period. Sets: [Region, Storage, Year] Unit: [GW]**

ResidualStorageCapacity defines the amount of existing storage capacity (in GW) available at the start of the modeling period, originating from installations made before the model's first year.

SelfSufficiency 
----------------
**Lower bound that limits the imports of fuels in a specific year and region. Sets: [Region, Fuel, Year] Unit: [Fraction]**

SelfSufficiency sets a lower bound on the share of domestic fuel production in a given region and year, limiting the extent to which fuels can be imported by requiring that a minimum fraction of total fuel supply be produced locally.

SocialDiscountRate 
-------------------
**Social Discount rate. Sets: [Region] Unit: [Fraction]**

See :ref:`generaldiscountrate`.

SpecifiedAnnualDemand 
-------------------------
**Total specified demand for a year. Sets: [Region, Fuel, Year] Unit: [PJ]**

GENeSYS-MOD models the Specified Annual Demand for all fuels and regions from the base year to the final year, covering electricity, heat, and mobility. Base year data typically comes from statistical sources, while future development is guided by scenario assumptions. The model then endogenously determines the technologies required to meet demand, ensuring a comprehensive energy system representation.

Final energy consumption is categorized into three main groups: electricity, heat, and mobility (If Cooking is added as fuel in the model it will also have to have a SpecifiedAnnualDemand). The heat sector is further divided into low-temperature heat (for water and space heating/cooling) and process heat (above 100°C). The mobility sector distinguishes between passenger transport, measured in billion passenger-kilometres (Gpkm), and freight transport, measured in billion tonnes-kilometres (Gtkm). All other energy data, including power and heat, is expressed in Petajoules (PJ).
The total industrial heat demand is divided in Heat_Low_Industrial (<100 degrees), Heat_Medium_Industrial (100-1000 degrees) and Heat_High_Industrial (>1000 degrees).

The specified annual demand data in GENeSYS-MOD represents the final demand for different fuels, meaning that the fuel will no longer undergo further conversion. Specifically, "Power demand" in specified annual demand refers to the actual use of power in applications such as appliances, lighting, and various operations. Power used in the Transport Sector, however, is classified differently: it appears as a demand for either "Mobility Passenger" or "Mobility Freight," depending on the context, rather than as a power demand. For example, for electric vehicles that require power, the demand will show-up in the fuel mobility_passenger (Gpkm) as power will be used to produce the fuel mobility_passenger (conversion of fuel power to fuel Mobility Passenger). Visualization of this concept: 

.. figure:: /_static/parameter/SpecifiedAnnualDemand_1.png
   :width: 650
   :align: center

   Concept of Fuel Conversion in SpecifiedAnnualDemand 

To ensure accuracy, data from official sources must be analyzed to exclude transport-related power consumption from the actual power demand in GENeSYS-MOD. Instead, such data should be recorded under mobility demand in units of Gpkm (billion passenger kilometres) or Gtkm (billion ton kilometres), rather than PJ (petajoules). The same concept applied to all other fuels. 

This setup supports sector coupling, allowing the model to select technologies and fuels to best meet the final fuel demands. For the Base Year, regional production data is used to realistically represent the existing energy landscape in the base year.

StorageLevelStart 
------------------
**Defines the level of storage at the beginning of a year. Sets: [Region, Storage] Unit: [PJ]**

→ Currently not used

TagDemandFuelToSector 
----------------------
**Assigns final demand fuels to the different sectors. Sets: [Fuel, Sector] Unit: [Binary]**

This binary parameter assigns final demand fuels (e.g., electricity, heat, gasoline) to specific sectors such as transport, industry, or buildings. A value of 1 links the fuel to the sector, allowing sector-specific demand tracking and policy application.

TechnologyDiscountRate 
------------------------
**Discount Rate for Technologies. Sets: [Region, Technology] Unit: [Fraction]**

→ Currently not used

TagElectricTechnology 
-----------------------
**Indicates if a technology is considered to be "direct electrification". Sets: [Technology] Unit: [Binary]**

A binary indicator that marks whether a technology qualifies as direct electrification (e.g., electric vehicles or electric heating). A value of 1 allows the model to identify and group technologies that directly consume electricity, often for electrification targets or analysis.

TagTechnologyToModalType 
-------------------------
**Tags technologies which belong to a certain modal type. Sets: [Technology, ModalType] Unit: [Binary]**

This binary parameter tags each technology as belonging to a specific modal type (e.g., road, rail, shipping). A value of 1 indicates the technology is part of that mode, allowing the model to group and apply constraints or policies (such as efficiency targets or mode-specific emissions) to all technologies within that type.

TagTechnologyToSector 
-----------------------
**Assigns Technologies to the different sectors. Sets: [Technology, Sector] Unit: [Binary]**

This binary parameter assigns each technology to a particular sector (e.g., transport, industry, residential). A value of 1 indicates inclusion in that sector, enabling sector-based aggregation, analysis, and application of sector-specific targets or limits.

TechnologyFromStorage 
-----------------------
**Connects Storaged to their respective dummy technologies and describes the efficiency of storage discharging. Sets: [Technology, Storage, Mode_of_operation, Year] Unit: [Fraction]**

This fractional parameter connects storage technologies to their associated discharge dummy technologies, specifying the efficiency of discharging energy from storage. For example, a value of 0.9 means 90% of stored energy is delivered when discharged.

TechnologyToStorage 
--------------------
**Connects Storaged to their respective dummy technologies and describes the efficiency of storage charging. Sets: [Technology, Storage, Mode_of_operation, Year] Unit: [Fraction]**

This fractional parameter links storage technologies to their charging dummy technologies, defining the efficiency of storing energy. A value of 0.85 means only 85% of input energy is successfully stored, with the rest lost in the charging process.

.. _totalannualmaxactivity:

TotalAnnualMaxActivity 
-----------------------
**Maximum total activity each year. Sets: [Region, Technology, Year] Unit: [PJ]**

This Parameter is similar to the Parameter TotalAnnualMaxCapacity but is mainly used for Biomass. Biomass potentials are given in PJ, representing the maximum availability each year, effectively creating an upper limit. This is not the demand in Biomass, but the maximal amount available each year.

TotalAnnualMaxCapacity 
-----------------------
**Maximum total (residual and new) capacity each year. Sets: [Region, Technology, Year] Unit: [GW]**

Total Annual max capacity represents the maximum amount of capacity that can be built in a region. This is the upper limit for a technology and could be constrained in reality by, for example, available land in the case of wind onshore or solar pv. It is usually the same value each year as this upper limit does not change. 

This parameter can also be used to constrain capacity when necessary, ensuring that the model's early years remain within specific limits. For instance, if political plans require that capacity does not exceed a certain threshold in a given year (e.g., 2025), this parameter can be applied to restrict capacity expansion accordingly. However, users should apply this constraint cautiously, as it may prevent the model from selecting the most cost-effective solutions. It should only be used when necessary to enhance the model's realism.

TotalAnnualMinCapacity 
-------------------------
**Minimum total (residual and new) capacity each year. Sets: [Region, Technology, Year] Unit: [GW]**

Using the Parameter TotalAnnualMinCapacity, the minimum total capacity (residual and new capacity!) each year can be specified. This can be used to implement policy plans and include commissioned capacity.

TradeCapacity 
--------------
**Defines the capacities for trade between two regions in a specific year and for a specific fuel. Sets: [Region, Region.1, Fuel, Year] Unit: [GW]/[PJ]**

Trade capacities for power are given in GW and trade capacity for Gas, H2 etc. are given in PJ. They are defined for each year and represent the currently available trade capacities and take into account their expected life-time. The model is able to build new trade capacities if it needs to, taking into account the associated costs.

.. _tradecapacitygrowthcosts:

TradeCapacityGrowthCosts 
-------------------------
**Costs of expanding trade capacity. Sets: [Region, Region2, Fuel] Unit: [M€/GW]**

TradeCapacityGrowthCosts defines the cost, in million euros per gigawatt (M€/GW), of expanding trade capacity (e.g., transmission lines) between regions, and is used to account for investment costs in cross-regional infrastructure.

TradeCosts 
--------------
**Costs for trading a fuel from one region to another. Sets: [Fuel, Region, Region2] Unit: [M€/PJ]**

Specifies the costs for trading a fuel between two different regions in M€ per PJ. To generate the trade costs, the distance of TradeRoute is multiplied with the costs of Transporting a fuel in M€/PJ per km. 
Assumptions must be made regarding the most common mode of transport for a given fuel between two countries, e.g., by ship, pipeline, or road. For the selected mode of transport, the trade costs in M€/PJ per km need to be calculated.

**Example:**
Let’s calculate the costs for LH2 transport by truck per km:

.. figure:: /_static/parameter/TradeCosts_1.png
   :width: 650
   :align: center

   Example Transport Data from `Technology Data for Transport of Energy <https://ens.dk/en/analyses-and-statistics/technology-data-transport-energy>`_

To get a simplified value in M€/(PJ·km), we need the average transport distance for LH₂. We get this by adding up all the transport distances in :ref:`traderoute` and dividing them by the total number of trade routes. For this example, we use the value for Europe: 528.82 km.

We further need to convert tons of LH₂ into PJ. After a quick search, we find the energy density of LH₂ to be 33.3 kWh/kg, which is equivalent to 0.00011988 PJ/t.

From the table, we take the fixed and variable costs:

- Fixed cost: 37 €/t = 0.000037 M€/t
- Variable cost: 1.1 €/(t·km) = 0.0000011 M€/(t·km)`

Now we can calculate the trade costs in M€/(PJ·km):

:math:`\left( \frac{\text{Fixed Cost}}{\text{Average Trade Distance}} + \text{Variable Cost} \right) \cdot \frac{1}{\text{Energy Density}}`

Substituting the values:

:math:`\left( \frac{0.000037\,\text{M€}/\text{t}}{528.82\,\text{km}} + 0.0000011\,\text{M€}/(\text{t} \cdot \text{km}) \right) \cdot \frac{1}{0.00011988\,\text{PJ}/\text{t}} = 0.009759485\,\text{M€}/(\text{PJ} \cdot \text{km})`

The trade costs are now determined by multiplying this factor with the trade distance between two regions.
For fuels that are primarily transported via pipeline, such as natural gas, the cost of constructing new pipelines is accounted for under :ref:`tradecapacitygrowthcosts`. As a result, construction costs should not be factored in again for these fuels, only the O&M costs.

TradeLossFactor 
----------------
**Percentage loss of traded fuel from one region to another. Used to model losses in power transmission networks. Sets: [Fuel, Year] Unit: [Fraction]**

TradeLossFactor represents the fraction of energy lost when trading a fuel (typically power) between regions, accounting for transmission losses in the network and reducing the amount of energy delivered relative to what was sent.

.. _traderoute:

TradeRoute 
--------------
**Defines lenght of a trade link between regions for specific fuels. Sets: [Region, Region.1, Fuel] Unit: [km]**

The trade route is defined by taking the distance (in km) from the centre point of one region to another. In general, there can only be connections between regions that are directly connected to each other. The flow always goes from Region1 to Region2. This means that a connection between two regions needs to be defined both ways (Region1 → Region2 & Region2 → Region 1)

Variable Costs 
---------------
**Cost per unit of activity of the technology. Sets: [Region, Technology, Mode_of_operation, Year] Unit: [M€/PJ]**

This parameter is used to define the variable costs for each technology in each year and region. 
There are some specific variable cost for technologies that serve a specific purpose:

Z_Technologies are used to represent Import from outside the regions used in the model.
Z_Import_H2, as an example, represents the variable costs or market price associated with importing hydrogen (H2). This technology serves as a supply option that provides hydrogen at the cost specified in its variable cost parameter. If the model cannot produce hydrogen more cheaply through domestic technologies, it will choose to import it—provided that imports are allowed. A maximum import volume can be enforced by setting the :ref:`totalannualmaxactivity` parameter, which limits the total annual import activity for this technology.
