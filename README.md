🍵 Chai App — Brew Heavenly Tea

A fun interactive web app built with Streamlit where users can vote for their favourite chai, customize their brew, and see live vote counts backed by a real SQL database.

🔗 Live App: my-chai-app.streamlit.app


What it does


Vote for your favourite chai — Masala, Adrak, or Lemon
One vote per session (no spam voting)
Live vote counts updated in real time
Bar chart visualization of votes
Customize your brew — chai base, extra flavour, sugar level, number of cups
Sidebar with home delivery info and brewing instructions



Tech Stack

ToolPurposePythonCore languageStreamlitFrontend and deploymentSQLitePersistent vote storagePandasData handling for chart


What I learned building this


Connecting a SQLite database to a live Streamlit app
Using st.session_state to prevent duplicate votes
Reading SQL query results into a Pandas DataFrame for visualization
Deploying a Python app with a live URL on Streamlit Cloud
