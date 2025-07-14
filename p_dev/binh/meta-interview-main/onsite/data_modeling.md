When to have multiple different types of fact tables vs one fact with a 'type' column.
e.g. fact_share, fact_upload vs fact_activity with activity_type (share, upload)

Multiple fact table
Pros:
    Improved performance - smaller fact tables
    Granularity - actvity specific columns, different activity types can have differet attributes that don't overlap
    Scalability - easier to scale specific activity types

Cons:
    Increased complexity
    Reduced flexibility - when analyzing across activity types
    Storage 

One fact table
Pros:
    Flexibility - easy to add new activity types
    Unified - enables cross activity analysis
    Storage efficiency

Cons:
    Performance
    Data sparsity - will have multiple null columns with no relation to activity

Hybrid approach
Single fact table for activities with similiar attributes
Multiple fact tables for activitis with unique attributes on high volumnes



How to handle time zone?
Have seperate time dimension and date dimension
Store timestamp in unified format like utc.
Keep original time zone and time zone offset

dim_date (date_id, year, month, day, week)
dim_time (time_id, timestamp, hour, minute, second, time_zone)



Bridge table
Pros
    Handle many to many relationships
    Preserveres granularity in fact table, so fact table can contain measures
    Metadata attributes can also be in bridge table
    For example: allocation, role, status, rankings

Con
    Increased complexity in querying and performance overhead



SCD Type 2
Tracks full history
Simple for current data



Role playing dimension
Pros
    storage effiency
    maintence and consistency

Cons
    complexity in query
    differing attributes

Good for: date, location, time
Not good for: seperate entity (drivers and riders), many to many relationships