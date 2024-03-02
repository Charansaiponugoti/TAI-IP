from geopy.geocoders import Nominatim
def get_user_location():
    geolocator = Nominatim(user_agent="location_app")
    user_location = None
    while user_location is None:
        user_input = input("Please enter your location (city, country, etc.): ")
        try:
            user_location = geolocator.geocode(user_input)
        except Exception as e:
            print("Error occurred:", e)
            print("Please try again.")
    print("Your GPS coordinates:")
    print(f"Latitude: {user_location.latitude}")
    print(f"Longitude: {user_location.longitude}")
if __name__ == "__main__":
    get_user_location()