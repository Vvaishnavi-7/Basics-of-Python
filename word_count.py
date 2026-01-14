import os
import re

# Get the folder where this script is located
folder = os.path.dirname(os.path.abspath(__file__))

input_file = os.path.join(folder, "input.txt")
output_file = os.path.join(folder, "output.txt")

def frequency(input_file, output_file):
    # Ask the user for a paragraph every time
    paragraph = input("Enter a paragraph:\n")
    
    # Write the paragraph to the input file (UTF-8 encoding to handle all characters)
    with open(input_file, "w", encoding="utf-8") as file:
        file.write(paragraph)

    count = {}

    # Read the input file and count word frequency
    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            line = line.lower()  # Convert to lowercase
            # Use regex to extract words (ignores punctuation)
            words = re.findall(r'\b\w+\b', line)

            for w in words:
                if w in count:
                    count[w] += 1
                else:
                    count[w] = 1

    # Write the results to the output file (UTF-8 encoding)
    with open(output_file, "w", encoding="utf-8") as output:
        for w in sorted(count):
            output.write(f"{w}: {count[w]}\n")

    print("Word frequency count completed!")
    print("Input file:", input_file)
    print("Output file:", output_file)

# Run the function
frequency(input_file, output_file)