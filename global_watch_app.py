# %%
# Import libraries
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from geopy.geocoders import Nominatim
import folium
from streamlit_folium import st_folium
import streamlit as st

# %%
# Initialize geolocator, a variable to get the location of a place using its name
geolocator = Nominatim(user_agent="new_old_time_standard")

# Define a function to get the time at a specific longitude
def get_location_time(longitude):
    time_180 = datetime.now(ZoneInfo("Etc/GMT-12"))
    min_diff = (180 - longitude) / 0.25
    location_time = time_180 - timedelta(minutes=min_diff)
    fixed_location_time = location_time.strftime("%H:%M %d-%m-%Y")
    return fixed_location_time

# %%
# Initialize session state variables for map center, zoom level, place name, and location time
if "center" not in st.session_state:
    st.session_state.center = [40, 0]

if "zoom" not in st.session_state:
    st.session_state.zoom = 2

if "place" not in st.session_state:
    st.session_state.place = None

if "location_time" not in st.session_state:
    st.session_state.location_time = None

# %%
# Set the title of the Streamlit app and provide instructions for the user
st.title("Global Watch for the new-old time standard")

st.markdown(
    """
    Select a place directly on the map or search for a location.
    """
)


# %%
# Create a text input for the user to search for a location
place = st.text_input(
    "Search location",
    placeholder="Type a city..."
)

if st.button("Search"):

    # Get the location of the place using geopy
    location = geolocator.geocode(place)

    if location is not None:

        # Get the coordinates of the location
        lat = location.latitude
        lng = location.longitude

        # Get the time at the location using the longitude
        st.session_state.location_time = get_location_time(lng)

        # Store the place name in session state
        st.session_state.place = location.address

        # Update the map center and zoom level in the location
        st.session_state.center = [lat, lng]
        st.session_state.zoom = 12

    else:
        st.warning("Location not found.")


# %%
# Display the location and time if they are available in the session state
if st.session_state.location_time is not None:

    st.write(
        f"Location: {st.session_state.place}"
    )

    st.write(
        f"Time: {st.session_state.location_time}"
    )
# %%
# Create a folium map centered at the specified coordinates and zoom level
m = folium.Map(
    location=st.session_state.center,
    zoom_start=st.session_state.zoom
)

# Show the map on the Streamlit app
map_data = st_folium(
    m,
    center=st.session_state.center,
    zoom=st.session_state.zoom
)

# %%
# Display the time at the selected place on the map if a location has been clicked
if map_data["last_clicked"] is not None:

    lng = map_data["last_clicked"]["lng"]
    
    location_time = get_location_time(lng)

    st.write(f"Time at the selected place: {location_time}")