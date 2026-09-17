import pandas as pd
from synthetic import generate_retention_data

def load_data(path=None):
    return generate_retention_data() if path is None else pd.read_csv(path)

def metrics(df):
    start=df.starting_arr.sum()
    churn=df.churn.sum()
    contraction=df.contraction.sum()
    expansion=df.expansion.sum()
    end=df.ending_arr.sum()
    grr=(start-churn-contraction)/start if start else 0
    nrr=(start-churn-contraction+expansion)/start if start else 0
    logo_attr=(df.movement.eq("churn").sum()/len(df)) if len(df) else 0
    revenue_attr=(churn+contraction)/start if start else 0
    score=100*(0.45*grr+0.45*min(nrr,1.2)/1.2+0.10*(1-logo_attr))
    grade="A" if score>=90 else "B" if score>=80 else "C" if score>=70 else "D" if score>=60 else "F"
    return {"starting_arr":start,"ending_arr":end,"grr":grr,"nrr":nrr,"logo_attrition":logo_attr,"revenue_attrition":revenue_attr,"expansion":expansion,"health_score":score,"grade":grade}
