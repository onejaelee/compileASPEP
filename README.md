# compileASPEP
Compiles ASPEP (Annual Survey of Public Employment &amp; Payroll) into DataFrame and csv and joins with Census Bureau Fed, State, and Local Revenue and Expenditure data

ASEP_generator.py is used to clean and convert ASPEP data that is given in two different Census Bureau formats (exclusive to ASPEP)
into a DataFrame or csv. Also contains code to compare imputation data to nonimputed data to see how accurate it is and code to
utilize additional imputation provided by the US Census Bureau

aspepformat.py converts the DataFrame created by ASEP_generator to a DataFrame that is formatted to match the format of another project that
creates a DataFrame from the Census of Government that pertains to Federal, State, and Local Revenue and Expenditures so that both data sets of
disparate format can be merged to combine government payroll data to government revenue and expenditure data to draw conclusions between
pay of government workers and changes to revenue and expenditure structures (specifically when the government runs a deficit).
