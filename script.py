import os
import pandas as pd

# Paths to your image folders
real_art_folder = "RealArt"
ai_art_folder = "AiArtData"

# Output CSV file
csv_filename = "dataset.csv"

# Function to rename and store file details
def rename_and_store(folder_path, prefix):
    image_data = []
    files = sorted(os.listdir(folder_path))  # Sort to maintain order
    for i, filename in enumerate(files, start=1):
        file_ext = os.path.splitext(filename)[-1].lower()  # Get file extension
        if file_ext in [".jpg", ".jpeg", ".png"]:  # Process only images
            new_filename = f"{prefix}_{i:03d}{file_ext}"  # Format: real_001.jpg, ai_001.jpg
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_filename)
            
            # Rename the file
            os.rename(old_path, new_path)
            
            # Store info (Modify URL part if using Google Drive)
            image_data.append([new_filename, new_path])
    
    return image_data

# Rename files and get data
real_data = rename_and_store(real_art_folder, "real")
ai_data = rename_and_store(ai_art_folder, "ai")

# Create DataFrame and save to CSV
df = pd.DataFrame(real_data + ai_data, columns=["File Name", "Local Path"])
df.to_csv(csv_filename, index=False)

print(f"✅ Renaming Done! {len(df)} images processed. Dataset saved as '{csv_filename}'.")
