from main import app
from database import db, Recording

# We must use the app context to connect to the SQLite database
with app.app_context():
    # Fetch the very first recording row from the database
    first_recording = db.get_or_404(Recording, 11)

    if first_recording:
        print("--- FIRST RECORDING ROW ---")
        print(f"ID:       {first_recording.id}")
        print(f"Title:    {first_recording.title}")
        print(f"Author:   {first_recording.author}")
        print(f"Date:     {first_recording.date}")
        print(f"Duration: {first_recording.duration}")

        # Only print a snippet of the data to avoid crashing the terminal
        if first_recording.data:
            print(f"Data:     {first_recording.data}")
        else:
            print("Data:     None")
    else:
        print("The database is currently empty. No recordings found.")