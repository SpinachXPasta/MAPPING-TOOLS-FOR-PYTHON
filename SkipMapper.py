



def rapidCounter(array, unique, count):
    import numpy as np
    ref = {}
    out = []
    for i in range(count):
        ref[unique[i]] = i
    #print (ref)
    for i in array:
        try:
            if np.isnan(i) == True:
                out.append(np.nan)
        except TypeError:
            out.append(ref[i])
    return out

def map(df):
    import pandas as pd
    c_names = list(df.columns.values)

    order = list(df.columns) #preserve the order of the d


    ##Avoid columns that are already numbers
    safe = []
    for i in c_names:
        num = ['int64','float64']
        if df[i].dtype in num:
            safe.append(i)

    coll = {}
    err = []
    import numpy as np
    for i in c_names:
        if i not in safe:
            C = (len(list(df[i].unique())))
            U = list(df[i].unique())
            if np.nan in U:
                C -= 1
                U.remove(np.nan)
            U.sort()
            #print (U)
            A = df[i]
            if C < 100:# was origignally < 100
                coll[i] = rapidCounter(A,U,C)
            else:
                err.append(i)

    train = df[safe]
    Gtrain = pd.concat([train, pd.DataFrame(coll)], axis=1)
    Xtrain = Gtrain[order]
    return Xtrain
