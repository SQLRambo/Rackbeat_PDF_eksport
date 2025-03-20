import os
import requests
import csv
from tkinter import Tk, filedialog

# Function to download and save the PDF
def download_pdf(order_number, bearer_token, folder_path):
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
        # Save the PDF to the selected folder
        file_path = os.path.join(folder_path, f"{order_number}.pdf")
        with open(file_path, "wb") as pdf_file:
            pdf_file.write(response.content)
        print(f"PDF saved to: {file_path}")
    else:
        print(f"Failed to download PDF for order {order_number}. Status code: {response.status_code}, Response: {response.text}")

# Main function to handle CSV input and folder selection
def main():
    # Open a file selection dialog to choose the CSV file
    Tk().withdraw()  # Hide the root window
    csv_file_path = filedialog.askopenfilename(
        title="Select CSV File with Order Numbers",
        filetypes=[("CSV Files", "*.csv")]
    )
    
    if not csv_file_path:
        print("No CSV file selected. Exiting.")
        return
    
    # Open a folder selection dialog to choose the save location
    folder_path = filedialog.askdirectory(title="Select Folder to Save PDFs")
    
    if not folder_path:
        print("No folder selected. Exiting.")
        return
    
    # Read the CSV file and process each order number
    bearer_token = input("Enter your bearer token: ")
    try:
        with open(csv_file_path, newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for row in csv_reader:
                if row:  # Ensure the row is not empty
                    order_number = row[0].strip()
                    download_pdf(order_number, bearer_token, folder_path)
    except Exception as e:
        print(f"An error occurred while processing the CSV file: {e}")

# Run the script
if __name__ == "__main__":
    main()