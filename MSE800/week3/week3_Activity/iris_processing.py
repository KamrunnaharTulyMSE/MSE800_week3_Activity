# Iris Dataset Processing

# Open the Iris dataset
with open("iris.data", "r") as file:

    # Read all records
    data = file.readlines()


# Remove empty lines
data = [line.strip() for line in data if line.strip()]


# Count the total number of records
total_records = len(data)


# Get the flower names
flowers = set()

for line in data:
    parts = line.split(",")
    flowers.add(parts[4])


# Display the results
print("Total number of records:", total_records)
print("Total number of different flowers:", len(flowers))
print("Names of the flowers:")

for flower in sorted(flowers):
    print("-", flower)