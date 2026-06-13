##import pandas as pd
##data = {
##    "name":["alica","bob","charlie"],
##    "age":[20,55,77],
##    "marks":[20,80,50]
##    }
##df = pd.DataFrame(data)
##print(df)

    
##import pandas as pd
##data = {
##    "name":["alica","bob","charlie"],
##    "age":[20,55,77],
##    "marks":[20,80,50]
##    }
##df = pd.DataFrame(data)
##print(df)
##print(df["name"])
##print(df[["name","marks"]])


##import pandas as pd
##data = {
##    "name":["alica","bob","charlie"],
##    "age":[20,55,77],
##    "marks":[20,80,50]
##    }
##df = pd.DataFrame(data)
##print(df)
###print(df["name"])
###print(df[["name","marks"]])
##print(df.iloc[0])
##print(df.iloc[0:2])
##print(df.iloc[1,2])

    
import pandas as pd
data = {
    "name":["alica","bob","charlie"],
    "age":[20,55,77],
    "marks":[20,80,50]
    }
df = pd.DataFrame(data)
print(df)
print(df.loc[0])
print(df.loc[0:2])
print(df.loc[0,"name"])
