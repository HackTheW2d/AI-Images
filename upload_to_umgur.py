import os
import requests
import pandas as pd
import time

# 🔹 REPLACE THIS with your actual Client ID from Imgur API
IMGUR_CLIENT_ID = "6afc3977325a023"

# 🔹 Folders containing images
FOLDERS = ["RealArt", "AiArtData"]  

# 🔹 Load existing dataset
df = pd.read_csv("dataset.csv")

# 🔹 Function to upload image and get Imgur URL
def upload_to_imgur(image_path):
    url = "https://api.imgur.com/3/upload"
    headers = {"Authorization": f"Client-ID {IMGUR_CLIENT_ID}"}
    
    with open(image_path, "rb") as file:
        response = requests.post(url, headers=headers, files={"image": file})
    
    if response.status_code == 200:
        return response.json()["data"]["link"]  # Get image URL
    else:
        print(f"❌ Failed to upload {image_path}: {response.json()}")
        return None

# 🔹 Upload all images and store URLs
image_urls = []
for index, row in df.iterrows():
    image_path = row["Local Path"]
    
    if os.path.exists(image_path):  # Ensure the file exists before upload
        print(f"⬆️ Uploading: {image_path} ...")
        imgur_url = upload_to_imgur(image_path)
        
        if imgur_url:
            image_urls.append(imgur_url)
        else:
            image_urls.append("UPLOAD_FAILED")
        
        time.sleep(1)  # Avoid rate limits
    else:
        print(f"⚠️ Missing file: {image_path}")
        image_urls.append("FILE_NOT_FOUND")

# 🔹 Add URLs to dataset and save new CSV
df["Imgur URL"] = image_urls
df.to_csv("dataset_with_urls.csv", index=False)

print("✅ Upload Complete! Check 'dataset_with_urls.csv' for image links.")
