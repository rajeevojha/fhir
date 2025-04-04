import hl7

hl7_message = """MSH|^~\&|HOSPITAL_A|LAB|INSURANCE|20250402||ADT^A01|12345|P|2.3\rPID|1||987654^^^HOSPITAL_A||DOE^JOHN||19750525|M|||123 MAIN ST^^CITY^ST^ZIP||555-1234\r"""

# Parse HL7 message
parsed_hl7 = hl7.parse(hl7_message)

# Extract patient details
patient_id = parsed_hl7.segment('PID')[3][0]  # Patient ID
patient_name = parsed_hl7.segment('PID')[5][0][0]  # Last Name
dob = parsed_hl7.segment('PID')[7][0]  # Date of Birth

print(f"Patient ID: {patient_id}")
print(f"Name: {patient_name}")
print(f"DOB: {dob}")