with open('requirements.txt', 'r') as f:
    lines = f.readlines()

# Remove duplicates
lines = list(set(lines))

with open('output_file.txt', 'w') as f:
    for line in lines:
        f.write(line)
