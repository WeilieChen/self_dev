# Id of the order placed
# Area where the order was delivered
# Name of the product
# Quantity of the product delivered in that order
# Brand of the ordered product

# 0_input_file_name - In the first column, list the product Name.  The second column should contain the average quantity of the product purchased per order.
# 1_input_file_name -  In the first column, list the product Name. The second column should be the most popular Brand for that product. Most popular is defined as the brand with the most total orders for the item, not the quantity purchased. 
# If two or more brands have the same popularity for a product, include any one.

import pandas as pd

def generateFiles(input_file_name):
    
    ## define schema
    column_names = ['row_id', 'location', 'product_name','quantity','brand']

    ## reading data without hearder and assign to predefinde schema
    df = pd.read_csv(input_file_name, header=None, names =column_names) 
    
    ## file 1 , product_name, avg quantity

    df1 = df[["product_name","quantity"]]
    df1final = df1.groupby('product_name').agg(avg_quantity = ('quantity','mean'))
    df1final.to_csv('file1.csv', index=False)
    
    ## file 2 ,  product Name , most popular Brand 
    df2 = df[["product_name","brand","row_id"]].reset_index()
    df2_count = df2.groupby(['product_name','brand']).agg(ct = ('row_id','count'))
    df2_count['rk'] =  df2_count.groupby('product_name')['ct'].rank(method='first', ascending=False)
    df_result = df2_count[df2_count['rk']==1].reset_index()
    df2final  = df_result[["product_name","brand"]]
    df2final.to_csv('file1.csv', index=False)

generateFiles('data.csv')