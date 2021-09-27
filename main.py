# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

import datetime 

import plotly.graph_objects as go



items = pd.read_csv('Data Files/items.csv')

item_categories = pd.read_csv('Data Files/item_categories.csv')

shops = pd.read_csv('Data Files/shops.csv')

sales_train = pd.read_csv('Data Files/sales_train.csv')

items_with_categories = items.join(item_categories,on='item_category_id',how='left',lsuffix="it")


items_with_categories_field_subset = items_with_categories[['item_id','item_name','item_category_name']]


sales_refined_with_items_categories = sales_train.join(items_with_categories_field_subset, 
                                                       on='item_id',how='left',lsuffix='sls')


sales_refined_with_items_categories_shop = sales_refined_with_items_categories.join(shops,on='shop_id',how='left',lsuffix='sls')

sales_refined_field_subset = sales_refined_with_items_categories_shop[['date','date_block_num','item_idsls','item_price','item_cnt_day','item_name','item_category_name','shop_name']]

sales_refined_field_subset['weekday'] = pd.to_datetime(sales_refined_field_subset['date']).dt.day_name()

sales_refined_field_subset['dayofweek'] = pd.to_datetime(sales_refined_field_subset['date']).dt.dayofweek

sales_refined_field_subset['weekend_flag'] = sales_refined_field_subset['dayofweek'] // 5





## fig = go.Figure()


## fig.add_trace(go.Bar(x=sales_refined_with_items_categories['item_category_name'],y=sales_refined_with_items_categories['item_cnt_day'], name='Rest of world', marker_color='rgb(55, 83, 109)' ))














