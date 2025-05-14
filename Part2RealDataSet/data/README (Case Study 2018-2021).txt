**** Task Allocation Input 2018-2021.xlsx ****

Authors: M. Witteman, Q. Deng, B.F. Santos
Air Transport and Operations, Faculty of Aerospace Engineering, 
Delft University of Technology

Corresponding Author: Q. Deng
Contact Information: Q.Deng@tudelft.nl



** General Introduction **
This dataset contains aircraft maintenance data collected for the AIRMES Project (www.airmes-project.eu). 

It is being made public both to act as supplementary data for publications of the paper:
A Bin Packing Approach to Solve the Aircraft Maintenance Task Allocation Problem 



** Purpose **
The maintenance data is the input for maintenance task allocation for 2018-2021.



** Methodology **
The research proposed a bin-packing approach for aircraft maintenance task allocation. 



** Description**

-- Tasks --	

A/C TAIL:  Aircraft tail number
ITEM:  Maintenance task item number
Description: Description of the maintenance task
BLOCK: It indicates where a maintenance task should be performed
SKILL: Skill type needed for performing the maintenance task
Mxh EST.: Estimated labor-hours
PER FH: Maintnenace interval of the task in terms of flight hours (FH)
PER FC: Maintnenace interval of the task in terms of flight cycles (FC)
PER CALEND: Maintnenace interval of the task in terms of calendar days (D), months (M) or years (Y)
TASK BY BLOCK: It indicates whether the task can be performed in an A-/C-check or at line maintenance (A-check tasks can be performed in C-checks)
LAST EXEC INSP: The maintenance check number of its previous execution
LAST EXEC FH: Cumulative FH at its previous execution
LAST EXEC FC: Cumulative FC at its previous execution
LAST EXEC DT: The end date of its previous execution
LIMIT INSP: The maintenance task has to be performed no later than the check given by the LIMIT INSP column
LIMIT FH: The maintenance task has to be performed no later than the cumulative FH limit given by the LIMIT FH column
LIMIT FC: The maintenance task has to be performed no later than the cumulative FC limit given by the LIMIT FC column	
LIMIT EXEC DT: The maintenance task has to be performed no later than the calendar day/month/year limit given by the LIMIT EXEC DT column



-- Delivery --
Phase-in date of each aircraft



-- Skill_Type --
GR1 – Engines and Fuel Systems + Landing Gears and Flight Controls Systems
GR2 – Cabin, Cargo and Air Conditioning Systems
GR4 – Avionics
ESHS – Aircraft Metallic Structure
ICH – Aircraft Composite Structure
PINT – Painting
MAP – Technical Cleaning
NDT – Non Destructive Testing



-- A-Check_NRs_Ratio --		
SKILL GI: Primary skill type
BLOCK: It indicates where a maintenance task should be performed
SKILL MDO: Additional skill type needed for performing the task
RATIO: Non-routine ratio for the additional skill type



-- C-Check_NRs_Ratio -- 		
SKILL GI: Primary skill type
BLOCK: It indicates where a maintenance task should be performed
SKILL MDO: Additional skill type needed for performing the task
RATIO: Non-routine ratio for the additional skill type


-- Number_of_Technicians --
Indicate how many technicians available per skill type per week


