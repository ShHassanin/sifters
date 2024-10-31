import streamlit as st

p= [
st.Page("home.py", title="Home"),
st.Page("app\streamlit_dashboard.py", title="Dashboards"),
st.Page("sentiment.py", title="Sentiment", icon="🔥")]
#pa = pages.nav_pages()
ng = st.navigation(pages= p, position='sidebar', expanded=False)
#ng= st.navigation([ st.Page("home.py"), st.Page("dashboard.py") , st.Page("sentiment.py")])
ng.run()
