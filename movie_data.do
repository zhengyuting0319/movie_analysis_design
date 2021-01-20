**************************************************
** Data Analysis for Movie Data
** Business Analytics--Xiaoyu Zhou @ ShanghaiTech
** 20180711
***************************************************

set more off, perm

** change working dir
cd "/Users/zhengyuting/Desktop/数据与商业分析/Project3"

** read in data file
import excel "movie_data_with_oscar_actors.xls", firstrow clear

rename A ID
rename budget_millions budget

** destring some variable
destring budget, ignore("N/A") replace
destring IMDB_rating, ignore("NA" "-") replace
destring Metascore, ignore("NA") replace
destring  total_gross gross return_rate std_IMDB std_Meta rating release_month release_year mins MPAA_rating budgetmillions theatres totalweek  ,  replace


** summarize your data
sum

** use tabstat to summarize
tabstat total_gross  theatres totalweek, s(mean sd var count rang min max)

** graph your data
** (1) one-way graph
** graph pie var, over()
** for discrete var: histogram var, discrete
** for continuous var: histogram var
** graph bar var, over()
graph box var, over()

** (2) two-way graph
** graph twoway 
graph twoway scatter IMDB_rating Metascore
** graph twoway line var1 var
** graph twoway function y=2*x+8
** graph twoway lfit var1 var2 || scatter var1 var2

** set scheme style
** set scheme (s1mono s1manual s1color s1rcolor s2mono s2manual s2gmanual s2color economist sj)



