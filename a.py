import pandas as pd
import numpy as np
def common_elements(list1, list2):
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    return result


df1=pd.read_csv("./2013.csv",sep=',',low_memory=False)
df2=pd.read_csv("./2014.csv",sep=',',low_memory=False)
df3=pd.read_csv("./2015.csv",sep=',',low_memory=False)
df4=pd.read_csv("./2016.csv",sep=',',low_memory=False)
df5=pd.read_csv("./2017.csv",sep=',',low_memory=False)
df6=pd.read_csv("./2018.csv",sep=',',low_memory=False)
df7=pd.read_csv("./2019.csv",sep=',',low_memory=False)

sirve=['X','Y','Fecha','Hora','Comuna','Tipo_Accid','Tipo___CONA','Ubicación','Causa__CON','Causa_Acci','Calzada','Tipo_Calza','Estado_Cal','Condición','Estado_Atm','Fallecidos','Graves','Menos_Grav','Leves']
dataframes=[df1,df2,df4,df5,df6,df7]
juntos=pd.concat(dataframes)
nosirve=list(set(juntos) - set(sirve))
juntos.drop(nosirve, axis=1, inplace=True)
juntos.to_csv('juntos.csv',index=False)













# frames = [df1, df2]
# common_cols = list(set.intersection(*(set(df.columns) for df in frames)))
# pd.concat([df[common_cols] for df in frames], ignore_index=True).to_csv("./2018-2019.csv",index=False)





