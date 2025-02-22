import pandas as pd
import requests


def DataProcessIDB():
    # API Call
    f_censo = requests.get("https://api.census.gov/data/timeseries/idb/5year?get=NAME,GENC,POP,BIRTHS,DEATHS,NIM&YR=2010:2050&for=genc+standard+countries+and+areas:PR")
    f_censo = f_censo.json()
    
    # Turn API call to Pandas DataFrame
    headers = ["NAME", "GENC", "population", "births", "deaths", "net_migration", "YR",
               "genc standard countries and areas"]
    f_y = pd.DataFrame(f_censo, columns=headers)
    
    # As a list of lists, the first row contains headers that must be removed
    f_y = f_y.drop(index=0)
    
    # Remove unnecessary rows and columns
    f_y = f_y.drop("GENC", axis=1)
    f_y = f_y.drop("YR", axis=1)
    f_y = f_y.drop("NAME", axis=1)
    f_y = f_y.drop("genc standard countries and areas", axis=1)
    
    # Reindex due to dropped rows
    f_y = f_y.reset_index(drop=True)
    
    # Remove commas in numbers and change to numeric
    f_y["population"] = pd.to_numeric(f_y["population"], errors="coerce")
    f_y["births"] = pd.to_numeric(f_y["births"], errors="coerce")
    f_y["deaths"] = pd.to_numeric(f_y["deaths"], errors="coerce")
    f_y["net_migration"] = pd.to_numeric(f_y["net_migration"], errors="coerce")
    
    # Change index to yearly
    index_y = pd.date_range(start="2010", end="2051", freq="YE")
    f_y.set_index(index_y, inplace=True)
    
    # Create column with years
    f_y["year"] = f_y.index.year
    
    # Calculate product of population equation
    f_y["pop_change"] = f_y["births"] - f_y["deaths"] + f_y["net_migration"]
    f_y["pop_equation"] = f_y["population"] + f_y["pop_change"]
    
    # Calculate difference between interpolation and result of equation
    f_y["pop_diff"] = f_y["population"] - f_y["pop_equation"]
    f_y["diff_percentage"] = (f_y["pop_diff"]/f_y["population"])*100
    
    # Reformat dataframe into final format
    f_y = f_y[["year", "population", "births", "deaths", "net_migration", "pop_change", "pop_equation", "pop_diff", "diff_percentage"]]
    
    # Create monthly DataFrame and remove unnecessary columns
    f_m = f_y.copy()
    f_m = f_m.drop("year", axis=1)
    
    # Change Frequency to monthly
    index_m = pd.date_range(start="2010-01-31", end="2050-12-31", freq="ME")
    f_m = f_m.resample("M").mean().reindex(index_m)
    
    # Convert to monthly with cubic spline interpolation then round results
    f_m = f_m.interpolate(method="spline", order=3, limit_direction="both")
    f_m = f_m.round(0)
    f_m["deaths"] = f_m["deaths"].div(12).round(0)
    f_m["births"] = f_m["births"].div(12).round(0)
    f_m["net_migration"] = f_m["net_migration"].div(12).round(0)
    f_m["date"] = pd.PeriodIndex(f_m.index, freq="M")
    
    # Calculate product of population equation
    f_m["pop_change"] = f_m["births"] - f_m["deaths"] + f_m["net_migration"]
    f_m["pop_equation"] = f_m["population"] + f_m["pop_change"]
    
    # Calculate difference between interpolation and result of equation
    f_m["pop_diff"] = f_m["population"] - f_m["pop_equation"]
    f_m["diff_percentage"] = (f_m["pop_diff"]/f_m["population"])*100
    
    # Reformat dataframe into final format
    f_m = f_m[["date", "population", "births", "deaths", "net_migration", "pop_change", "pop_equation", "pop_diff", "diff_percentage"]]
    
    # Convert monthly data to quarterly with sum and population mean
    f_q = f_m.copy()
    q_pop = f_m.resample("Q")["population"].mean().round(0)
    f_q = f_q.resample("Q")["births", "deaths", "net_migration"].sum()
    f_q.insert(0, "population", q_pop, True)
    f_q["date"] = pd.PeriodIndex(f_q.index, freq="QE")
    
    # Calculate product of population equation
    f_q["pop_change"] = f_q["births"] - f_q["deaths"] + f_q["net_migration"]
    f_q["pop_equation"] = f_q["population"] + f_q["pop_change"]
    
    # Calculate difference between interpolation and result of equation
    f_q["pop_diff"] = f_q["population"] - f_q["pop_equation"]
    f_q["diff_percentage"] = (f_q["pop_diff"]/f_q["population"])*100
    
    # Reformat dataframe into final format
    f_q = f_q[["date", "population", "births", "deaths", "net_migration", "pop_change", "pop_equation", "pop_diff", "diff_percentage"]]
    
    # Copy monthly DataFrame to new DataFrame
    f_fy = f_m.copy()
    f_fy = f_fy.reset_index(drop=True)
    
    # Drop last 6 and first 6 months to enable conversion to fiscal year
    f_fy = f_fy.drop(index=[0, 1, 2, 3, 4, 5, 486, 487, 488, 489, 490, 491])
    
    # Generate new index with updated dates
    f_fy = f_fy.drop("date", axis=1)
    index_fy = pd.date_range(start="07-2010", end="07-2050", freq="ME")
    f_fy = f_fy.set_index(index_fy)
    
    # Aggregate births, deaths and net migration in 12-month intervals
    f_fy["births"] = f_fy["births"].rolling(window=12).sum()
    f_fy["deaths"] = f_fy["deaths"].rolling(window=12).sum()
    f_fy["net_migration"] = f_fy["net_migration"].rolling(window=12).sum()
    
    # Filter by the end-month of the fiscal year starting on June 2011
    f_fy = f_fy[f_fy.index.month == 6]
    
    # Create new column with fiscal years
    f_fy["fyear"] = f_fy.index.year - 1
    f_fy["fyear"] = "FY" + f_fy["fyear"].astype(str) + "-" + (f_fy["fyear"] + 1).astype(str)
    
    # Calculate product of population equation
    f_fy["pop_change"] = f_fy["births"] - f_fy["deaths"] + f_fy["net_migration"]
    f_fy["pop_equation"] = f_fy["population"] + f_fy["pop_change"]
    
    # Calculate difference between interpolation and result of equation
    f_fy["pop_diff"] = f_fy["population"] - f_fy["pop_equation"]
    f_fy["diff_percentage"] = (f_fy["pop_diff"]/f_fy["population"])*100
    
    # Reformat dataframe into final format
    f_fy = f_fy[["fyear", "population", "births", "deaths", "net_migration", "pop_change", "pop_equation", "pop_diff", "diff_percentage"]]
    
    # Export DataFrames to csvs
    f_y.to_parquet("data/processed/yearly_idb.parquet", index=False)
    f_m.to_parquet("data/processed/monthly_idb.parquet", index=False)
    f_q.to_parquet("data/processed/quarterly_idb.parquet", index=False)
    f_fy.to_parquet("data/processed/fiscal_year_idb.parquet", index=False)
