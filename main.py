import os
import streamlit as st
import datetime
import time
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_k=os.getenv("GEMINI_API_KEY")
client=genai.Client(api_key=api_k)

st.title("Ai Travel  Planner  For  Students :airplane:")
 
with st.form("travel_form"):
    starting_point=st.text_input("starting point (city or landmark)")
    destination=st.text_input("Destination (City or landmark)")
    starting_date=st.date_input("start date",min_value=datetime.date.today())
    ending_date=st.date_input("ending date",min_value=starting_date)
    num_travellers=st.number_input("No of travellers",min_value=1)
    budget=st.number_input("Budget (in INR)",min_value=1000)
    trip_type=st.selectbox("Trip type",options=["Solo Trip",
        "Friends Trip",
        "College Group Trip",
        "Educational Tour",
        "Adventure Trip",
        "Weekend Getaway",
        "Cultural/Heritage Trip",
        "Beach Vacation",
        "Hill Station Trip",
        "City Exploration",
        "International Trip",
        "Road Trip"])
    
    submit_button=st.form_submit_button("Get Travel Plan",type="primary")

    if submit_button:
        if not all([starting_point,destination,starting_date,ending_date,budget,trip_type]):
            st.error(":warning: please fill all the fields")
        else:
            with st.spinner("Generating your trip plan .... it will take time",show_time=True):
                time.sleep(10)
                prompt=f"""You are an expert AI travel planner who specializes in creating fun, budget-friendly, and efficient itineraries for students.

                    Create a **detailed travel plan** for the following inputs:

                    - **Starting Point:** {starting_point}
                    - **Destination:** {destination}
                    - **Travel Dates:** {starting_date} to {ending_date}
                    - **Number of Travellers:** {num_travellers}
                    - **Budget:** ₹{budget}
                    - **Trip Type:** {trip_type}

                    The output should include:

                    1. 🗓️ **Overview** — brief description of the trip and ideal travel route.
                    2. 🏨 **Accommodation** — suggest budget stays (hostels, dorms, affordable hotels).
                    3. 🍴 **Food Options** — local and budget-friendly eating places.
                    4. 🚗 **Transport Plan** — how to travel from start to destination and local transport options.
                    5. 📍 **Day-wise Itinerary** — daily plan including major attractions and activities.
                    6. 💰 **Estimated Total Cost Breakdown** — show how the budget will be used.
                    7. 💡 **Tips for Students** — money-saving hacks, safety advice, and must-carry items.

                    Keep the tone **friendly and engaging**.
                    Highlight **educational value** if it’s an educational or cultural trip.
                    If the budget seems low for the distance, suggest how to make it affordable. """
                
                response=client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
                st.subheader("🧳 Your AI-Generated Trip Plan")
                st.markdown(response.text)  
               