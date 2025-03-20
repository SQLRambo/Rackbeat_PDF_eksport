import os
import requests
from tkinter import Tk, filedialog

# Function to download and save the PDF
def download_pdf(order_number, bearer_token):
    # API endpoint
    url = f"https://app.rackbeat.com/api/orders/{order_number}.pdf"
    
    # Headers with the bearer token
    headers = {
        "Authorization": f"Bearer {bearer_token}"
    }
    
    # Make the request
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Open a folder selection dialog
        Tk().withdraw()  # Hide the root window
        folder_path = filedialog.askdirectory(title="Select Folder to Save PDF")
        
        if folder_path:
            # Save the PDF to the selected folder
            file_path = os.path.join(folder_path, f"{order_number}.pdf")
            with open(file_path, "wb") as pdf_file:
                pdf_file.write(response.content)
            print(f"PDF saved to: {file_path}")
        else:
            print("No folder selected. PDF not saved.")
    else:
        print(f"Failed to download PDF. Status code: {response.status_code}, Response: {response.text}")

# Example usage
if __name__ == "__main__":
    order_number = input("Enter the order number: ")
    bearer_token = input("Enter your bearer token: ")
    download_pdf(order_number, bearer_token)