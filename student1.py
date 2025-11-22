import sys
if len(sys.argv) == 3:
    script_name = sys.argv[0]
    name = sys.argv[1]
    rollno = sys.argv[2]
    print("User provided input values:")
else:
    script_name = sys.argv[0]
    name = "Satish"
    rollno = "018"
    print("No input given - using default values:")

print("Script Name:", script_name)
print("Name:", name)
print("Roll No:", rollno)
