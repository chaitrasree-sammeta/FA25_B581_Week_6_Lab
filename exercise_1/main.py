import hl7                         # Import the python-hl7 library for parsing HL7 messages
from pathlib import Path           # Import Path to handle file paths in a clean, cross-platform way

# Define the path to the "data" directory relative to the current working directory
data_dir = Path.cwd() / "data"

# Open the HL7 message file and read its contents
with open(data_dir / "message.txt", "r") as file:
    hl7_message = file.read().strip()  # Read and remove any leading/trailing whitespace

# Replace newline characters with carriage return, as HL7 segments are separated by '\r'
hl7_message = hl7_message.replace('\n', '\r')

# Parse the HL7 message into a structured object
parsed = hl7.parse(hl7_message)

# Extract the PID (Patient Identification) segment
pid = parsed.segment('PID')

# Extract patient name from PID-5 field: [LastName, FirstName, MiddleName, ...]
name_field = pid[5][0]
last_name = name_field[0]          # Last name: PID-5.1
first_name = name_field[1]         # First name: PID-5.2

# Extract gender from PID-8
gender = pid[8][0]
dob  = pid[7]
address = pid[11][0]
street = address[0]
city = address[2]
state = address[3]
zipcode = address[4]
phone =pid[13]

print(f"Name:{first_name} {last_name}")# Gender: PID-8
print(f"Gender:{gender}")
print(pid)


print(f"Name: {first_name} {last_name}")
print(f"DOB: {dob}")
print(f"Gender: {gender}")
print(f"Address: {street}, {city}, {state} {zipcode}")
print(f"Phone: {phone}")
