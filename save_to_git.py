import pandas as pd

# 🔹 Replace with your actual GitHub username and repo name
GITHUB_USERNAME = "HackTheW2d"
REPO_NAME = "AI-Images"
FOLDER_NAME = "AiArtData"  # 🔹 Your image folder inside the repo

# 🔹 Read the dataset with filenames
df = pd.read_csv("dataset.csv")

# 🔹 Generate the GitHub raw content URLs
df["GitHub URL"] = df["File Name"].apply(lambda x: f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{REPO_NAME}/main/{FOLDER_NAME}/{x}")

# 🔹 Save new CSV with URLs
df.to_csv("dataset_with_github_urls.csv", index=False)

print("✅ URLs Generated! Check 'dataset_with_github_urls.csv'")
