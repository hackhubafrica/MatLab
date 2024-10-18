from pysolar.solar import get_altitude, get_azimuth
import datetime

# Location details
latitude = 37.7749  # Example latitude (San Francisco)
longitude = -122.4194  # Example longitude

# Time of interest
time = datetime.datetime.now(datetime.timezone.utc)

# Calculate the sun's altitude and azimuth
altitude = get_altitude(latitude, longitude, time)
azimuth = get_azimuth(latitude, longitude, time)

print(f"Sun Altitude: {altitude} degrees")
print(f"Sun Azimuth: {azimuth} degrees")
