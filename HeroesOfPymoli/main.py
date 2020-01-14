# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
file_to_load = r"C:\Users\unhea\Documents\Bootcamp\My Repositories\pandas-challenge\HeroesOfPymoli\Resources\purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)

purchase_data = purchase_data.drop_duplicates(subset = "SN") 

genderSummary = purchase_data.groupby(["Gender"])

genderTotals = genderSummary["Purchase ID"].count()

uniqueItems = genderSummary["Item ID"].count()

avgPurchasePrice = genderSummary["Price"].mean()

totalAmount = genderSummary["Price"].sum()

avgTotalPurchase = totalAmount / genderTotals

finalSummary = pd.DataFrame ({"Purchase Count" : uniqueItems,
                                         "Average Purchase Price" : avgPurchasePrice, 
                                         "Total Purchase Value" : totalAmount,
                                         "Avg Total Purchase per Person" : avgTotalPurchase})

finalSummary["Average Purchase Price"] = finalSummary["Average Purchase Price"].map("${:.2f}".format)
finalSummary["Total Purchase Value"] = finalSummary["Total Purchase Value"].map("${:.2f}".format)
finalSummary["Avg Total Purchase per Person"] = finalSummary["Avg Total Purchase per Person"].map("${:.2f}".format)

finalSummary
