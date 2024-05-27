# Function to slice the email
def email_slicer(email):
    # Split the email using '@' as the delimiter
    username, domain = email.split('@')
    return username, domain

# Input email address
email = input("Enter your email address: ")

# Call the function and unpack the result
username, domain = email_slicer(email)

# Display the results
print(f"Username: {username}")
print(f"Domain: {domain}")