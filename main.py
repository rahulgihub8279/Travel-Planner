import os
import streamlit as st
import datetime
import time
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_k = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_k)

st.title("Ai Travel  Planner  For  Students :airplane:")

with st.form("travel_form"):
    starting_point = st.text_input("starting point (city or landmark)")
    destination = st.text_input("Destination (City or landmark)")
    starting_date = st.date_input(
        "start date", min_value=datetime.date.today())
    ending_date = st.date_input("ending date", min_value=starting_date)
    num_travellers = st.number_input("No of travellers", min_value=1)
    budget = st.number_input("Budget (in INR)", min_value=1000)
    trip_type = st.selectbox("Trip type", options=["Solo Trip",
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

    submit_button = st.form_submit_button("Get Travel Plan", type="primary")

    if submit_button:
        if not all([starting_point, destination, starting_date, ending_date, budget, trip_type]):
            st.error(":warning: please fill all the fields")
        else:
            with st.spinner("Generating your trip plan .... it will take time", show_time=True):
                time.sleep(10)
                prompt = fprompt = f"""
You are an expert AI travel planner for students. Create a **fun, budget-friendly, detailed itinerary**:

- **From:** {starting_point} → **To:** {destination}
- **Dates:** {starting_date} to {ending_date}
- **Travellers:** {num_travellers}, **Budget:** ₹{budget}, **Trip Type:** {trip_type}

Include:

1. 🗓️ **Overview** — trip summary & route
2. 🏨 **Accommodation** — budget stays
3. 🍴 **Food** — local, affordable options
4. 🚗 **Transport** — to destination & local
5. 📍 **Day-wise Itinerary** — activities & attractions
6. 💰 **Estimated Costs** — budget breakdown
7. 💡 **Student Tips** — savings, safety, essentials

Keep it **friendly, engaging**, and highlight **educational/cultural value** if relevant. Suggest ways to make it affordable if budget is tight.
"""

                response = client.models.generate_content(
                    model="gemini-2.5-flash", contents=prompt)
                st.subheader("🧳 Your Trip Plan")
                st.markdown(response.text)
