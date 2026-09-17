import numpy as np
import pandas as pd

def generate_retention_data(seed=42,n_customers=600):
    rng=np.random.default_rng(seed)
    regions=["North America","Europe","Asia Pacific","Middle East & Africa"]
    products=["Core","Analytics","Operations","Optimization"]
    rows=[]
    for i in range(1,n_customers+1):
        start=float(rng.uniform(20000,500000))
        move=rng.choice(["renew_flat","expansion","contraction","churn"],p=[.58,.20,.14,.08])
        expansion=contraction=churn=0
        if move=="renew_flat": ending=start*rng.normal(1,.01)
        elif move=="expansion": expansion=start*rng.uniform(.08,.45); ending=start+expansion
        elif move=="contraction": contraction=start*rng.uniform(.08,.40); ending=start-contraction
        else: churn=start; ending=0
        rows.append([f"CUST-{i:04d}",rng.choice(regions),rng.choice(products),start,expansion,contraction,churn,ending,move])
    return pd.DataFrame(rows,columns=["customer_id","region","product_suite","starting_arr","expansion","contraction","churn","ending_arr","movement"])
