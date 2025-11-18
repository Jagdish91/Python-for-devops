def update_config_file(file_path, key, value):
    key_found = False
    updated_lines = []

    # Read lines
    with open(file_path, "r") as file:
        for line in file:
            # Strip whitespace and newline for accurate key check
            stripped = line.strip()
            if stripped.startswith(key + "="):
                updated_lines.append(f"{key}={value}\n")
                key_found = True
            else:
                updated_lines.append(line)

    # If key was not found, add it at the end
    if not key_found:
        updated_lines.append(f"{key}={value}\n")

    # Write back
    with open(file_path, "w") as file:
        file.writelines(updated_lines)
