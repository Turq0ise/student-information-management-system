import json
import uuid
from pathlib import Path
STUDENT_DATA_FILE_NAME = "studentData.json"
STUDENT_DATA_FILE_PATH = Path(STUDENT_DATA_FILE_NAME)

def generateStudentID(studentNameParam):
    return(uuid.uuid5(uuid.NAMESPACE_DNS, studentNameParam))

def getStudentDictionary(studentNameParam, studentProgramParam):
    return {
        "Name": studentNameParam,
        "Student ID": str(generateStudentID(studentNameParam)),
        "Program": studentProgramParam,
    }

def addToFile(studentParam):
    existingData = []
    if STUDENT_DATA_FILE_PATH.is_file(): # Checks if the file exists
        if STUDENT_DATA_FILE_PATH.stat().st_size != 0: # Checks if the file is not empty
            with open(STUDENT_DATA_FILE_NAME, "r") as file:
                existingData = json.load(file)
    existingData.append(studentParam)
    with open("studentData.json", "w") as file:
        json.dump(existingData, file, indent=4)