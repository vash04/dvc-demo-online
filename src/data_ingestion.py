import pandas as pd
import numpy as np
import os

df=pd.read_csv("https://raw.githubusercontent.com/araj2/customer-database/refs/heads/master/Ecommerce%20Customers.csv")

df=df.iloc[:, 4:]

df=df[df["Length of Membership"]>2]

df.to_csv(os.path.join('data', 'customer.csv'))