import cv2 as cv
import sqlite3
import customtkinter as ctk


def load_cameras(camera_dropdown):
    camera_devices = []
    for i in range(8):
        cap = cv.VideoCapture(i)
        if cap.isOpened():
            camera_devices.append(i)
        cap.release()

    # Connect to the SQLite database
    conn = sqlite3.connect('cameras.db')
    c = conn.cursor()

    # Create a table for the camera devices
    c.execute('''CREATE TABLE IF NOT EXISTS cameras (id INTEGER PRIMARY KEY, device_id INTEGER)''')

    # Clear the existing rows from the table
    c.execute("DELETE FROM cameras")

    # Insert the camera devices into the table
    for device_id in camera_devices:
        c.execute("INSERT INTO cameras (device_id) VALUES (?)", (device_id,))

    # pull new option box list and refresh
    camera_options = get_cameras()
    camera_dropdown.configure(values=camera_options)

    # Commit the changes and close the connection
    conn.commit()

    # Close the connection
    conn.close()


def get_cameras():
    # Connect to the SQLite database
    conn = sqlite3.connect('cameras.db')
    c = conn.cursor()

    # Retrieve the camera devices from the table and convert ID to string for option box type match
    c.execute("SELECT device_id FROM cameras")
    camera_devices = [str(row[0]) for row in c.fetchall()]

    # Close the connection
    conn.close()

    return camera_devices



