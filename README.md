# FHIR learnings
**Python support** hl7 and fhirclients avaialble

1. HL7 is older version and fhir is the newer version
2. HL7 is parsing. fhir is api driven

## Key HL7 Message Structure:
- Segments (MSH, PID, OBX, etc.): These define parts of a message.
- Fields & Delimiters: Data is separated by pipes (|), carets (^), and tildes (~).

- ==MSH== → Message Header (who sent it, where it’s going)
- ==PID== → Patient Identification (Name, DOB, Address, etc.)
