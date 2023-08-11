import requests
import zipfile
import io
import csv

# URL of the zip file
zip_url = "https://www.football-data.co.uk/mmz4281/2324/data.zip"
latest_url = "https://www.football-data.co.uk/fixtures.csv"

# Download the zip file and store it in memory
response = requests.get(zip_url)
zip_contents = io.BytesIO(response.content)

# Extract and process each CSV file within the zip
with zipfile.ZipFile(zip_contents, "r") as zip_ref:
    for csv_info in zip_ref.infolist():
        if csv_info.filename.endswith(".csv"):
#            with zip_ref.open(csv_info) as csv_file:
#                csv_data = csv_file.read().decode("utf-8")
#                csv_rows = csv.reader(csv_data.splitlines())
                
                print(f"CSV file: {csv_info.filename}")
#                for row in csv_rows:
#                    print(row)
#                print("-" * 20)

