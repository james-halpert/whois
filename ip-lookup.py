import tkinter as tk
from tkinter import scrolledtext
import whois  # This library performs the WHOIS queries

def perform_whois(event=None):  # Allow binding to events
    # Get the input from the user
    target = entry.get()
    # Update the label with the entered IP or URL
    entered_ip.config(text=f"Entered: {target}")
    try:
        # Perform the WHOIS query
        whois_info = whois.whois(target)
        
        # Display the results in the scrolled text area
        results_text.delete(1.0, tk.END)  # Clear existing results
        results_text.insert(tk.INSERT, str(whois_info))
        
        # Update the labels for Name and Location
        name_text = f"Name: {whois_info.get('name', 'N/A')}"
        name.config(text=name_text)
        
        city = whois_info.get('city', '')
        state = whois_info.get('state', '')
        country = whois_info.get('country', 'N/A')
        location_str = f"{city}, {state} - {country}" if city or state else country
        location.config(text=f"Location: {location_str}")
        
    except Exception as e:
        results_text.delete(1.0, tk.END)  # Clear existing results
        results_text.insert(tk.INSERT, f"Error: {e}")

# Set up the GUI
root = tk.Tk()
root.title("WHOIS Lookup Tool")

entry_label = tk.Label(root, text="Enter IP Address or URL:")
entry_label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

search_button = tk.Button(root, text="Search", command=perform_whois)
search_button.pack()

# Label for the entered IP or URL
entered_ip = tk.Label(root, text="Entered: ")
entered_ip.pack()

# Labels for specific WHOIS details
name = tk.Label(root, text="Name: ")
name.pack()

location = tk.Label(root, text="Location: ")
location.pack()

# Scrolled text area for displaying the WHOIS lookup results
results_text = scrolledtext.ScrolledText(root, width=70, height=20)
results_text.pack()

# Bind the Enter key to the perform_whois function
root.bind('<Return>', perform_whois)

root.mainloop()
