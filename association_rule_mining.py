# %% import dataframe from pickle file
import pandas as pd

df = pd.read_pickle("UK.pkl")

df.head()

# %% convert dataframe to invoice-based transactional format

import pandas as pd


invoice_df = df.groupby('InvoiceNo')['Description'].apply(list).reset_index()

print(invoice_df.head())

# %% apply apriori algorithm to find frequent items and association rules

import pandas as pd
df = pd.read_pickle("UK.pkl")

df = df[df['Description'].notna()]
df['Description'] = df['Description'].astype(str)

invoice_df = df.groupby('InvoiceNo')['Description'].apply(list).reset_index()



from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

te = TransactionEncoder()
te_array = te.fit_transform(invoice_df['Description'])


df = pd.DataFrame(te_array, columns=te.columns_)
print(df.shape) 

frequent_itemsets = apriori(df, min_support=0.01, use_colnames= True)

frequent_itemsets

## Association rules
rules = association_rules(frequent_itemsets, min_threshold=0.01)
rules

# %% count of frequent itemsets that have more then 1/2/3 items,
# and the frequent itemsets that has the most items

frequent_1_items = frequent_itemsets[frequent_itemsets['itemsets'].apply(lambda x: len(x)>1)] # more than 1 item
frequent_1_items

frequent_2_items = frequent_itemsets[frequent_itemsets['itemsets'].apply(lambda x: len(x)>2)] #more than 2 items
frequent_2_items

frequent_3_items = frequent_itemsets[frequent_itemsets['itemsets'].apply(lambda x: len(x)>3)] # more than 3 items
frequent_3_items

frequent_4_items = frequent_itemsets[frequent_itemsets['itemsets'].apply(lambda x: len(x)>=4)] # has more items
frequent_4_items

# %% top 10 lift association rules

rules.sort_values('lift', ascending=False)
rules.head(10)


# %% scatterplot support vs confidence
import seaborn as sns
import matplotlib.pyplot as plt

sns.scatterplot(x=rules["support"], y=rules["confidence"], alpha=0.5)
plt.xlim(0.000,0.040)
plt.ylim(0.60,0.95)
plt.xlabel("Support")
plt.ylabel("Confidence")
plt.title("Support vs Confidence")


# %% scatterplot support vs lift

import seaborn as sns
import matplotlib.pyplot as plt

sns.scatterplot(x=rules["support"], y=rules["lift"], alpha=0.5)
plt.xlim(0.000,0.040)
plt.ylim(10,90)
plt.xlabel("Support")
plt.ylabel("Lift")
plt.title("Support vs lift")
