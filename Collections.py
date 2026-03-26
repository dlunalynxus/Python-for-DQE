import random  
import string  

# Step 1: Create a random list of dictionaries
num_dicts = random.randint(2, 10)  # Randomly decide how many dicts to create (between 2 and 10)
list_of_dicts = []  # empty list for all dictionaries

for i in range(num_dicts):
    num_keys = random.randint(1, 5)  # Each dict will have between 1 and 5 keys
    keys = random.sample(string.ascii_lowercase, num_keys)  # Randomly choose letters for keys
    values = [random.randint(0, 100) for _ in range(num_keys)]  # Generate random values (0-100) for each key
    d = dict(zip(keys, values))  # Create dictionary from keys and values
    list_of_dicts.append(d)  # Add dictionary to the list

print("Generated list of dictionaries:")
print(list_of_dicts)  # Print the generated list for reference

# Step 2: Combine all dicts into a single dict
combined_dict = {}  # Initialize empty dict for final result

for idx, d in enumerate(list_of_dicts, start=1):  # Loop through each dict with index starting at 1
    for key, value in d.items():
        if key not in combined_dict:
            # If key not yet in combined_dict, add it as is with original key
            combined_dict[key] = (value, idx)  # Store value and dict index as a tuple
        else:
            # If key exists, compare values
            current_value, current_idx = combined_dict[key]
            if value > current_value:
                # If current dict has a larger value, replace and keep index of max
                combined_dict[key] = (value, idx)

# Step 3: Rename keys where needed (only if max value came from a specific dict)
final_dict = {}
for key, (value, idx) in combined_dict.items():
    # If key appeared in multiple dicts (detected by index not equal to 1 and key reused), rename
    occurrences = sum(1 for d in list_of_dicts if key in d)
    if occurrences > 1:
        final_dict[f"{key}_{idx}"] = value  # Rename key with dict number where max value came from
    else:
        final_dict[key] = value  # Keep key as is if it only appears once

print("\nCombined dictionary with max values:")
print(final_dict)  # Print the final combined dictionary