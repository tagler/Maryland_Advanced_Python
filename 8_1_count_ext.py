import os
from collections import Counter

# Get filenames in current directory.
files = os.listdir('.')

# Extract filename extensions.
file_exts = []
for each_file in files:
    if '.' in each_file:
        split_filename = each_file.split('.')
        each_ext = split_filename[1]
        file_exts.append(each_ext)

# Count frequencies.
freq = Counter(file_exts)
print(freq)
