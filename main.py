# Define the text to be replaced and the replacement text
text_to_replace = "Hello, world!"
replacement_text = "Goodbye, world!"

# Read the content of the file
with open("example.txt", "r") as file:
    file_content = file.read()

# Replace the text
updated_content = file_content.replace(text_to_replace, replacement_text)

# Write the updated content back to the file
with open("example.txt", "w") as file:
    file.write(updated_content)


with open("example.txt", "r") as file:
    file_content = file.read()
    print(file_content)
