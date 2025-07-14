import pandas as pd

# Id of the order placed
# Area where the order was delivered
# Name of the product
# Quantity of the product delivered in that order
# Brand of the ordered product

# 0_input_file_name - In the first column, list the product Name.  The second column should contain the average quantity of the product purchased per order.
# 1_input_file_name -  In the first column, list the product Name. The second column should be the 
# most popular Brand for that product. Most popular is defined as the brand with the most total orders for the item, not the quantity purchased. 
# If two or more brands have the same popularity for a product, include any one.


def generete_file (filename):
## define schema
    column_names = ['row_id', 'location', 'product_name','quantity','brand']

    df =pd.read_csv(filename, header = None, names=column_names)

    ## first file

    df1 = df[["product_name",'quantity']]
    df1final = df1.groupby('product_name').agg(avg_quan = ('quantity','mean')).reset_index()
    
    ## 2nd files 
    df2 = df[["product_name",'brand','row_id']]
    df2ct = df2.groupby(["product_name",'brand']).agg(ct =('row_id', 'count')).reset_index()
    df2ct['rk'] = df2ct.groupby("product_name")['ct'].rank(method= 'first', ascending= False)
    df2result = df2ct[df2ct['rk']==1].reset_index()
    df2final = df2result[["product_name",'brand']]
    return df2final


print(generete_file('data.csv'))