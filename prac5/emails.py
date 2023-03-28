
# Dictionary to store emails and names
emails_names = {}

# Function to extract name from email 
def extract_name(email): 
    name = email.split('@')[0].split('.')
    name = ' '.join(name).title()
    return name

# While loop to ask for emails
while True: 
    email = input('Email: ')
    if email == '': 
        break
    name = extract_name(email)
    confirmation = input(f'Is your name {name}? (Y/n) ')
    if confirmation.lower() != 'y':
        name = input('Name: ')
    emails_names[email] = name

# Print the emails and names 
for email, name in emails_names.items():
    print(f'{name} ({email})')
    