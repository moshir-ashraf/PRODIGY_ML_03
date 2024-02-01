import os
import csv

image_folder = 'dataset'
data = []
for filename in os.listdir(image_folder):
    if filename.startswith('cat'):
        label = 0  # Cat
    elif filename.startswith('dog'):
        label = 1  # Dog
    else:
        continue
    image_path = os.path.join(image_folder, filename)
    image_id = filename[0] + filename[4:]  # Remove the first 4 characters
    data.append({'ID': image_id, 'Label': label, 'Path': image_path})
csv_file_path = 'imageLabels.csv'
with open(csv_file_path, 'w', newline='') as csvfile:
    fieldnames = ['ID', 'Label', 'Path']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)
print(f"CSV file created at: {csv_file_path}")
