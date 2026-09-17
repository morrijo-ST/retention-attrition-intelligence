import streamlit as st
import plotly.express as px
import pandas as pd
from core import load_data,metrics

st.set_page_config(page_title="Retention Attrition Intelligence",layout="wide")
st.title("Retention & Attrition Intelligence")
st.caption("Synthetic recurring-revenue retention, churn, contraction, expansion, GRR/NRR, and health scoring.")
df=load_data()
regs=st.sidebar.multiselect("Region",sorted(df.region.unique()),default=sorted(df.region.unique()))
prods=st.sidebar.multiselect("Product",sorted(df.product_suite.unique()),default=sorted(df.product_suite.unique()))
f=df[df.region.isin(regs)&df.product_suite.isin(prods)]
m=metrics(f)
c=st.columns(6)
c[0].metric("GRR",f"{m['grr']:.1%}")
c[1].metric("NRR",f"{m['nrr']:.1%}")
c[2].metric("Logo Attrition",f"{m['logo_attrition']:.1%}")
c[3].metric("Revenue Attrition",f"{m['revenue_attrition']:.1%}")
c[4].metric("Health Score",f"{m['health_score']:.0f}")
c[5].metric("Grade",m['grade'])
moves=f.groupby("movement",as_index=False)["starting_arr"].sum()
st.plotly_chart(px.bar(moves,x="movement",y="starting_arr",title="Starting ARR by movement"),use_container_width=True)
water=pd.DataFrame({"component":["Starting ARR","Expansion","Contraction","Churn","Ending ARR"],"value":[m["starting_arr"],m["expansion"],-f.contraction.sum(),-f.churn.sum(),m["ending_arr"]]})
st.plotly_chart(px.bar(water,x="component",y="value",title="Retention movement bridge"),use_container_width=True)
byreg=f.groupby("region").apply(lambda x: metrics(x),include_groups=False).apply(pd.Series).reset_index()
st.plotly_chart(px.scatter(byreg,x="grr",y="nrr",size="starting_arr",text="region",title="Regional retention health"),use_container_width=True)
st.dataframe(f.sort_values("starting_arr",ascending=False),use_container_width=True)
