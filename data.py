import json
from datetime import datetime
from pathlib import Path
STUDENT_DATA_FILE_NAME = "studentData.json"
STUDENT_DATA_FILE_PATH = Path(STUDENT_DATA_FILE_NAME)

def getFileContents():
    fileContents = []
    if STUDENT_DATA_FILE_PATH.is_file(): # Checks if the file exists
        if STUDENT_DATA_FILE_PATH.stat().st_size != 0: # Checks if the file is not empty
            with open(STUDENT_DATA_FILE_NAME, "r") as file:
                fileContents = json.load(file)
    return fileContents

def generateStudentID():
    data = getFileContents()
    return (datetime.now().year, 1000+len(data)+1)

def getStudentDictionary(studentNameParam, studentProgramParam):    
    return {
        "Name": studentNameParam,
        "Student ID": generateStudentID(),
        "Program": studentProgramParam,
    }

def addToFile(studentParam):
    data = getFileContents()
    data.append(studentParam)
    with open("studentData.json", "w") as file:
        json.dump(data, file, indent=4)