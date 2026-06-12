import streamlit as st 
import pandas as pd

st.title("Chai App")
st.subheader("Brew Heavenly Tea ")
st.text("Welcome to my first interactive app brewed with streamlit")

import sqlite3

@st.cache_resource
def get_connection():
    return sqlite3.connect("votes.db", check_same_thread=False)

conn = get_connection()
cursor = conn.cursor()

# Create table once
cursor.execute("""
    CREATE TABLE IF NOT EXISTS votes (
        chai_name TEXT PRIMARY KEY,
        vote_count INTEGER DEFAULT 0
    )
""")
conn.commit()

chai_list = ["Masala","Adrak","Lemon"]

for chai in chai_list:
    cursor.execute(
    """
    INSERT OR IGNORE INTO votes (chai_name, vote_count) VALUES (?,0)
    """,
    (chai,)
    )
conn.commit()


st.markdown('### Vote for your favourite Chai')

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.header("Masala Chai")
    st.image("https://images.pexels.com/photos/10377676/pexels-photo-10377676.jpeg")
    vote1 = st.button("Vote Masala Chai",width=200)

with col2:
    st.header("Adrak Chai")
    st.image("https://images.pexels.com/photos/20270270/pexels-photo-20270270.jpeg",width=200)
    vote2 = st.button("Vote Adrak Chai")

with col3:
    st.header("Lemon Chai")
    st.image("https://images.pexels.com/photos/28617425/pexels-photo-28617425.jpeg",width=200)
    vote3 = st.button("Vote Lemon Chai")


if "voted" not in st.session_state:
    st.session_state.voted = False

def cast_vote(chai):
    if not st.session_state.voted:
        cursor.execute(
            "UPDATE votes SET vote_count = vote_count + 1 WHERE chai_name=?",(chai,)
        )
        conn.commit()

        st.session_state.voted = True
        st.success("Vote recorded !")

    else:
        st.warning("Already voted")


if vote1:
    cast_vote("Masala")

if vote2:
    cast_vote("Adrak")

if vote3:
    cast_vote("Lemon")

with col4:
    
    cursor.execute("""
    SELECT * FROM votes
    """)

    results = cursor.fetchall()
    st.markdown("### 🗳️ Live Vote Count")
    for row in results:
        st.write(f"{row[0]} : {row[1]} votes")

    df = pd.DataFrame(
        results,columns=["Chai","Votes"]
    )
    st.bar_chart(df.set_index("Chai"),height=200)

chai = st.selectbox("Select Today's Chai",["Masala","Adrak","Lemon"])


tea_type = st.radio("pick your chai base :",['Milk','Water','Almond Milk'])

flavour = st.selectbox("Add Extra flavour: ",["Cinnamon","Kesar","Tulsi","None"])

if flavour == "None":
    st.write("Okay Lets keep it simple this time")
else:
    st.write(f"Selected Flavour ( {flavour} ) Good Choice !!")

add_masala = st.checkbox(f"Add Masala to your {chai}")
if add_masala:
    st.success("Masala Added")



sugar = st.slider("Sugar Level (tbsp)",0,5,0)

if sugar==0:
    st.write("None")
elif sugar<4:
    st.success("Okay Gotcha !!")
else:
    st.success("Sweet Tooth ! ")

cups  = st.number_input("How many Cups? ",min_value=1,max_value=10,step=1)

st.write(f"Okay so {cups} Cups . Fine !")




if st.button("Brew"):
    st.success("Your chai has been brewed")



name = st.sidebar.text_input("Enter Your Name")

if name:
    st.sidebar.write(f"Welcome! {name}, Like some tea ?")

address = st.sidebar.text_input(("Your Address ?"))

if address:
    st.sidebar.write("Free Home Delivery Available at your address ")

with st.sidebar.expander("How We make our Chai"):
    st.write("""
    1.Boil Water with tea leaves
             
    2.Add Milk and Spices
             
    3.Serve Hot """)

