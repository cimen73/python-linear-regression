#packages

import statsmodels.api as sm
import statsmodels.formula.api as smf
import seaborn as sns 
#data

houseprices_object = sm.datasets.get_rdataset(dataname="HousePrices",package="AER",cache=True)
houseprices =houseprices_object.data
print(houseprices_object.__doc__)

#chart

sns.regplot(x="lotsize" , y="price" , data=houseprices, ci=None,
            line_kws={"color" : "red"}) 


#model
slr =smf.ols(formula="price ~ lotsize", data=houseprices).fit()
print(slr.params)