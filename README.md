# New-old system global watch

**New-old system global watch** is an interactive web application developed with Python and Streamlit that implements a new timekeeping system based on geographic longitude.

Instead of using the conventional 24 time zones, this system divides the Earth into 1,440 meridians, spaced 0.25° of longitude apart, so that each meridian represents a one-minute difference in solar time. This provides a more geographically continuous representation of solar time, which was historically determined locally before the adoption of standardized time zones. As coordinating different local times became increasingly difficult, standardized time zones were introduced. This project does not intend to replace the current time standard, whose practical benefits are recognized; it is simply an experimental and educational project.

The application allows users to select a point directly on a map or search for a municipality to determine the time corresponding to that location according to this new time system.

## How does it work?

The system uses the 180° meridian as its reference meridian. In this proposed system, the 180° meridian also acts as the boundary between two consecutive calendar days. Therefore, locations on opposite sides of this meridian may have different dates, even when their geographical distance is very small.

Due to large areas of land sharing the same time zone, as is the case across much of Europe or big countries like China, sunrise and sunset can occur at very different times in places that share the same time zone. Looking for a way to "fix" this, I explored the idea of having one time zone for each minute of the day. As there are 60 minutes in an hour and 24 hours in a day, 60 * 24 = 1440 time zones. Dividing the Earth's 360° of longitude into 1,440 equal sections gives us intervals of 0.25°.

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

## Features

The application allows users to:

* Select a point on the map to obtain its corresponding time.
* Search for a municipality by name.
* Calculate the corresponding time based on geographic longitude.
* Automatically move the map to the selected municipality.
* Display the calculated time and date for the selected location.

## Technologies

The project is developed using:

* **Python**
* **Streamlit** — for building the web application.
* **Folium** — for creating the interactive map.
* **streamlit-folium** — for integrating Folium maps into Streamlit.
* **GeoPy** — for obtaining geographic coordinates from municipality names.
* **Nominatim / OpenStreetMap** — for geocoding municipalities.
* **datetime / zoneinfo** — for handling dates, times, and time zones.

## Installation

Clone this repository:

```bash
git clone https://github.com/ivange00/new_old_system_global_watch.git
```

Navigate to the project directory:

```bash
cd new_old_system_global_watch
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the application

Start the application with:

```bash
streamlit run global_watch_app.py
```

Or use it online in [(https://newoldsystemglobalwatch.streamlit.app/)]

## Usage

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

## Mathematical model

The main calculation used by the application is:

```python
minutes_difference = (180 - longitude) / 0.25
```

This difference is then applied to the time at the reference meridian:

```python
local_time = time_at_180 - timedelta(minutes=minutes_difference)
```

This approach directly converts geographic longitude into a time difference without requiring the 1,440 meridians to be stored in an array.

## License

This project is currently developed for educational and experimental purposes.

The project is licensed under the MIT License
