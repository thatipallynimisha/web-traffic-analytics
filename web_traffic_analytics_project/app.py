
import pandas as pd

# Load website traffic dataset
df = pd.read_csv("website_traffic.csv")

print("\nWebsite Traffic Data:\n")
print(df)

# Basic Analytics
print("\n--- Web Traffic Analytics Report ---")

# Total page views
total_views = df["PageViews"].sum()
print(f"Total Page Views: {total_views}")

# Average session duration
avg_duration = df["SessionDuration"].mean()
print(f"Average Session Duration: {avg_duration:.2f} minutes")

# Drop-off pages
drop_off = df[df["Bounce"] == "Yes"]

print(f"\nTotal Drop-off Sessions: {len(drop_off)}")

print("\nPages with High Drop-offs:")
print(drop_off["Page"].value_counts())

# User journey analysis
print("\n--- User Journey Analysis ---")
journey = df.groupby("UserID")["Page"].apply(list)

for user, pages in journey.items():
    print(f"User {user}: {' -> '.join(pages)}")

# Suggestions
print("\n--- Suggestions to Improve Engagement ---")
print("1. Improve content on pages with high bounce rates.")
print("2. Simplify navigation for better user flow.")
print("3. Increase interactive elements on landing pages.")
print("4. Optimize slow-loading pages.")
