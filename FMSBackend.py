import pandas as pd 

def addDriverToDB():

    return 0
def readCard():
    id = 0 
    info = 0

    return (id, info)

def updateDriverList(report):
    """
    Args:
        Report: Dictionary with the pre-specified format Driver_data.csv
            (Same header names) 
    """
    df_new = pd.DataFrame(report)
    df1 = pd.read_csv("logs/Driver_data.csv",index_col =  False)
    df = df1.append(df_new, ignore_index = True
          )
    df.to_csv("logs/Driver_data.csv", index = False)
    
def updateVehicleList(report):
    """
    Args:
        Report: Dictionary with the pre-specified format of Vehicle_data.csv
            (Same header names) 
    """
    df_new = pd.DataFrame(report)
    df1 = pd.read_csv("logs/Vehicle_data.csv",index_col =  False)
    df = df1.append(df_new, ignore_index = True
          )
    df.to_csv("logs/Vehicle_data.csv", index = False)