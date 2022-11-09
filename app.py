
import pyrebase

# Set the configuration for your app
# TODO: Replace with your project's config object
config = {
    "apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": "",
    "appId": "",
    "measurementId": ""
}
firebase = pyrebase.initialize_app(config)

# Get a reference to the database service
db = firebase.database()

# Try pushing some sample data
