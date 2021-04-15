#!/usr/bin/python

import pandas as pd
meal_info=pd.read_csv("data/meal_order_info.csv")
print("meal_order_info.csv:---------------------->>>",
        "\n\n", meal_info, "\n\n")
users=pd.read_excel( "./data/users.xlsx")
print("users.xlsx:------------------------------->>>",
        "\n\n", users, "\n\n")

pd.to_csv("tmp/orderinfor.csv")
