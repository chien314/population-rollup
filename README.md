# population-rollup
 
##  Dataset
Following the instruction, I am using the dataset [2000 to 2010 Census Tract Population Change](https://www.census.gov/data/tables/time-series/dec/metro-micro/tract-change-00-10.html). Please execute the 'run.sh' file in the main directory. The code is written in Python 3. As indicated in the instruction, we are allowed to use I/O libraries, so I use only 'sys' and 'csv' libraries. If these are not allowed please let me know. 

## Details about how I calculate the average population percent change for census tracts in this Core Based Statistical Area?

The average population percent change is defined as 1/N(\sum_i (POP10- POP00)/POP00) for all rows (i) that have the same Core Based Statistical Area Code (i.e. CBSA09), where N is the sum of all selected rows. However, I exclude the cases with POP00 equal to zero, since it would cause the divergence. But when calculating total population in the CBSA in 2000 and 2010 I include all the data including rows with POP00 equal to zero.

I use the data structure hashtable (or dictionary in Python) to collect all data with the same CBSA09 and use it as the key of the dictionary.  Shown below is an example of the dictionary output using the test dataset.

{'28540': [4, ['000100', '000200', '000300', '000400'], ['Ketchikan, AK', '3801', '3484'], ['Ketchikan, AK', '4909', '4884'], ['Ketchikan, AK', '3054', '2841'], ['Ketchikan, AK', '2310', '2268']], '46900': [4, ['950300', '950500', '950600', '950700'], ['Vernon, TX', '2304', '1849'], ['Vernon, TX', '3172', '2955'], ['Vernon, TX', '6022', '5994'], ['Vernon, TX', '3181', '2737']]}

The values of the dictionary consists of total number of census tracts and the corresponding values in the column 'TRACT10' as well as Core Based Statistical Area Code Title (i.e., CBSA_T), the population in the CBSA in 2000 (POP00), and the population in the CBSA in 2010 (POP10). Using the information, I calculate the average population percent change and total populations in the CBSA in 2000 and 2010. The final result is sorted by key and then output to report.csv.