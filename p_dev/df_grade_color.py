## student df
# name,age,favorite_color,grade
# Tim voss,19,red,91
# Nicole Johnson, 20, yellow, 95
# elsa williams, 21, green, 82
# John James, 20, blue, 75
# catherien Jones, 23, blue, 75

## write the function for the select only the roes where the student favorite
## color is green or red and their grade is above 90
## input df , return df with filter

import pandas as pd

student_df = pd.DataFrame(data)

def grade_color(df):
    student_df = df[(df['grade']>= 90) 
                    & (df['favorite_color'].isin(['green','red']))
                    ]
    return student_df