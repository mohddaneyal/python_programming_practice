def max_visited_speciality(patient_list):
    # Dictionary containing medical specialities
    speciality_dict = {
        "P": "Pediatrics",
        "O": "Orthopedics",
        "E": "ENT"
    }

    # Dictionary to keep count of visits to each speciality
    speciality_count = {"P": 0, "O": 0, "E": 0}

    # Loop through the patient_list to count visits to each speciality
    for i in range(1, len(patient_list), 2):
        speciality = patient_list[i]
        speciality_count[speciality] += 1

    # Find the speciality with the maximum visits
    max_speciality = max(speciality_count, key=speciality_count.get)

    # Return the name of the speciality using the dictionary
    return speciality_dict[max_speciality]

# Example usage:
patient_list1 = [101, "P", 102, "O", 302, "P", 305, "P"]
print(max_visited_speciality(patient_list1))  # Expected Output: "Pediatrics"

patient_list2 = [101, "O", 102, "O", 302, "P", 305, "E", 401, "O", 656, "O"]
print(max_visited_speciality(patient_list2))  # Expected Output: "Orthopedics"

