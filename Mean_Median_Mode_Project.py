# ============================================
# PROJECT: Mean, Median and Mode of Weight Data
# ============================================

# Import required modules
import csv
from collections import Counter

# -----------------------------
# Step 1: Read the CSV file
# -----------------------------
with open("SOCR-HeightWeight.csv", "r") as file:
    reader = csv.reader(file)
    file_data = list(reader)

# Remove the header row
file_data.pop(0)

# -----------------------------
# Step 2: Extract Weight Data
# -----------------------------
weights = []

for row in file_data:
    weight = float(row[2])      # Weight is in the 3rd column (index 2)
    weights.append(weight)

# -----------------------------
# Step 3: Calculate Mean
# -----------------------------
total_weight = sum(weights)
number_of_weights = len(weights)

mean = total_weight / number_of_weights

# -----------------------------
# Step 4: Calculate Median
# -----------------------------
weights.sort()

n = len(weights)

if n % 2 == 1:
    # Odd number of values
    median = weights[n // 2]
else:
    # Even number of values
    middle1 = weights[(n // 2) - 1]
    middle2 = weights[n // 2]
    median = (middle1 + middle2) / 2


from collections import Counter

# Count the frequency of each weight
data = Counter(weights)

# Create class intervals
modeData = {
    "50-60": 0,
    "60-70": 0,
    "70-80": 0
}

# Count how many values fall in each interval
for weight, occurrence in data.items():
    if 50 <= float(weight) < 60:
        modeData["50-60"] += occurrence
    elif 60 <= float(weight) < 70:
        modeData["60-70"] += occurrence
    elif 70 <= float(weight) < 80:
        modeData["70-80"] += occurrence

# Find the interval with the highest frequency
modeRange = []
modeOccurrence = 0

for interval, occurrence in modeData.items():
    if occurrence > modeOccurrence:
        modeRange = [int(interval.split("-")[0]), int(interval.split("-")[1])]
        modeOccurrence = occurrence

# Calculate the midpoint of the modal class
mode = (modeRange[0] + modeRange[1]) / 2

print("Mode Weight :", mode, "kg")
# -----------------------------
# Step 6: Display Results
# -----------------------------
print("========== RESULTS ==========")
print(f"Mean Weight   : {mean:.2f} kg")
print(f"Median Weight : {median:.2f} kg")
print(f"Mode Weight   : {mode:.2f} kg")