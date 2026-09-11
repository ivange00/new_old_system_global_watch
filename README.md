# New-old system global watch

**New-old system global watch** is an interactive web application developed with Python and Streamlit that implements a new timekeeping system based on geographic longitude.

Instead of using conventional 24 time zones, this system divides the Earth into 1,440 meridians, spaced 0.25° of longitude apart, so that each meridian represents a difference of one minute. It is a more precise system according to sun hours in each place, as it was stablished before the current time standard. Due to the difficulties of coordination between different cities, that time standard was changed. This project has no intention on applying this system, recognizing the benefits of the current one, it's just a fun-to project. 

The application allows users to select a point directly on a map or search for a municipality to determine the time corresponding to that location according to this new time system.

## 🕐 How does it work?

The system uses the 180° meridian as its reference meridian. It keeps the same as the current time standard, so it's still the International Date Line. This meridian will still be the barrier with one day apart from each side.

Due to wide extensions of land sharing the same time zone, as it happens in a big part of Europe or big countries like China, sunrises and sunsets can be separated by several hours in places which share the same time zone. Looking for a way to "fix" this, I thought of getting more time zones, one for each minute of the day. As there are 60 minutes in an hour and 24 hours in a day, 60 * 24 = 1440 time zones. Separating the globe in 1440 parts is as easy as dividing 360° between 1440, what gives us earth portions of 0.25°

Given the longitude of a specific location, the difference in minutes from the reference meridian is calculated as follows:

```text
Time difference (minutes) = (180 - longitude) / 0.25
```

This difference is then applied to the time at the 180° meridian.

For example, for a location at the Greenwich meridian, wich is at 0° longitude:

```text
(180 - 0) / 0.25 = 720 minutes
```

Therefore, its time will be 720 minutes (12 hours) earlier than the time at the 180° meridian

## 🗺️ Features

The application allows users to:

* Select a point on the map to obtain its corresponding time.
* Search for a municipality by name.
* Calculate the corresponding time based on geographic longitude.
* Automatically move the map to the selected municipality.
* Display the calculated time and date for the selected location.

## 🛠️ Technologies

The project is developed using:

* **Python**
* **Streamlit** — for building the web application.
* **Folium** — for creating the interactive map.
* **streamlit-folium** — for integrating Folium maps into Streamlit.
* **GeoPy** — for obtaining geographic coordinates from municipality names.
* **Nominatim / OpenStreetMap** — for geocoding municipalities.
* **datetime / zoneinfo** — for handling dates, times, and time zones.

## 🚀 Installation

Clone this repository:

```bash
ivange00/new_old_system_global_watch
```

Navigate to the project directory:

```bash
cd REPOSITORY-NAME
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Running the application

Start the application with:

```bash
streamlit run app.py
```

Or use it online in AQUÍ PONER LA WEB CUANDO ESTÉ

## 📖 Usage

Once the application is open, there are two main ways to calculate the time.

### 1. Select a point on the map

Click anywhere on the map.

The application automatically retrieves the longitude of the selected point and calculates its corresponding time according to the proposed time system.

### 2. Search for a municipality

Enter the name of a municipality in the search box.

The application will:

1. Search for the municipality.
2. Retrieve its geographic coordinates.
3. Obtain its longitude.
4. Move the map to the selected location.
5. Calculate the corresponding time.
6. Display the calculated time.

## 🧮 Mathematical model

The main calculation used by the application is:

```python
minutes_difference = (180 - longitude) / 0.25
```

This difference is then applied to the time at the reference meridian:

```python
local_time = time_at_180 - timedelta(minutes=minutes_difference)
```

This approach directly converts geographic longitude into a time difference without requiring the 1,440 meridians to be stored in an array.

## 📄 License

This project is currently developed for **educational and experimental purposes**.

The project license is MIT.
