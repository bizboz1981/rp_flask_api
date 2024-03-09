import people

# create a new person by passing a dictionary to the create() function. returns a tuple where the first element is the created person's dictionary and the second element is the HTTP status code.
new_person = {
    "lname": "Doe",
    "fname": "John"
}
result, status_code = create(new_person)

# Call the update function
updated_person = {
    "fname": "Jane"
}
result = update("Ruprecht", updated_person)