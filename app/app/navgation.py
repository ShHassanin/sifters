import streamlit as st

p= [
st.Page("home.py", title="Home"),
st.Page("streamlit_dashboard.py", title="Dashboards"),
st.Page("sentiment.py", title="Sentiment", icon="🔥")]
ng = st.navigation(pages= p, position='sidebar', expanded=False)
ng.run()
