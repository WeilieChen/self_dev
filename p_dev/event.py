import math
import os
import random
import re
import sys
import json
import pandas as pd


def extract_events(text_list):
    event_output = []
    if len(text_list) ==0:
        event_output["events"] = []
    else:
        # looping with the list, use  the event as break point
        event_list=[]
        current_list = []
        for item in text_list:
            if item.startswith('Event:') and current_list:
                event_list.append(current_list)
                current_list = []

            current_list.append(item)

        # last list
        if current_list:
            event_list.append(current_list)
    
    for event in event_list:
        event_items={}
        for e  in event:
            if e.startswith('Event:'):
                event_items['Event'] = e.split(': ')[-1]

            if e.startswith('Date:'):
                event_items['Date'] = e.split(': ')[-1]

            if e.startswith('Time:'):
                event_items['Time'] = e.split(': ')[-1]

            if e.startswith('Location:'):
                event_items['Location'] = e.split(': ')[-1]

            if e.startswith('Tags:'):
                tag_str = (e.split(': ')[1:])[0].split(', ')
                event_items['Tags'] = tag_str
        event_output.append(event_items)

        # find the patten
    return event_output

def write_df(text_list):
    data = extract_events(text_list)
    ## convert away of dict to df
    df = pd.DataFrame(data)
    print(df)

def df_delta_table(text_list):
    df = write_df (text_list)
    
    
    # Initialize Spark session with Delta support
    # assuming spark section been build
    # spark = SparkSession.builder \
    # .appName("pandas-to-delta") \
    # .config("spark.jars.packages", "io.delta:delta-core_2.12:2.4.0") \
    # .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    # .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    # .getOrCreate()

    ## convert to spark dataframe
    pydf= spark.createDataFrame(df)
    delta_table_path = "/path/to/delta-table"

    # Write to Delta Table
    sdf.write.format("delta").mode("overwrite").save(delta_table_path)
    
    ## in databricks :
    pydf.write.format("delta").mode("append").partitionBy("Date").saveAsTable("user_nebula_prod.wchen2_sbx.testwrite")



input_value = ['Event: Birthday Party', 'Date: 2024-02-20', 'Time: 15:00', 'Location: My House', 'Tags: Celebration, Friends', 
               'Event: 2nd Party', 'Date: 2024-02-20', 'Time: 15:00', 'Location: My House', 'Tags: Celebration, Friends',
               'Event: 3nd Party', 'Date: 2024-02-20', 'Time: 15:00', 'Location: My House', 'Tags: Celebration, Friends',
               ]


print(write_df(input_value))