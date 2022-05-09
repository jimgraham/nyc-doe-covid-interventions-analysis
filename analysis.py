import csv
import pdb 
import json
from subprocess import PIPE, Popen


def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0].decode("utf-8").strip()

NYC_DIR = "../nyc-doe-covid-interventions"
SCHOOL_FILE = "schoolcases.json"
DISTRICT_75_ID = "9748b1f5-eaf6-ea11-b883-24ee9a37d459"
DISTRICT_15_ID = "fdd7cf12-31f4-ea11-b882-24ee9a37d45c"
SCHOOL_IDS = [DISTRICT_15_ID, DISTRICT_75_ID]

# update github
print("Pulling all data\n")
pull_command = f"cd {NYC_DIR}; git pull"
cmdline(pull_command)

# get commits since then
list_command = f"cd {NYC_DIR}; git log --diff-filter=d --date-order --reverse --format=\"%ad %H\" --date=iso-strict \"{SCHOOL_FILE}\" | grep -v '^commit'"
output = cmdline(list_command).split("\n")
date_revs = list(map(lambda o: (o.split(" ")), output))

csv_header = [ "date", "District 15 students", "District 15 staff", "District 75 students", "District 75 staff",]
csv_rows = []
csv_rows.append(csv_header)

print("Finding schools in dataset\n")
for date, rev in date_revs:
    csv_row = []
    district_15_students = 0
    district_15_staff = 0
    district_75_students = 0
    district_75_staff = 0
    
    # git show
    show_command = f"cd {NYC_DIR}; git cat-file -p \"{rev}:{SCHOOL_FILE}\""
    file_contents = cmdline(show_command)
    file_json = json.loads(file_contents)
    schools = list(school for school in file_json if school["nycsr_locationsiteid"] in SCHOOL_IDS)
    if schools == []:
        continue

    csv_row.append(date)
    for school in schools:
        if school["nycsr_locationsiteid"] == DISTRICT_15_ID:
            district_15_students += school["StudentCases"]
            district_15_staff += school["EmployeeCases"]
        if school["nycsr_locationsiteid"] == DISTRICT_75_ID:
            district_75_students += school["StudentCases"]
            district_75_staff += school["EmployeeCases"]
        
    csv_row.append(district_15_students)
    csv_row.append(district_15_staff)
    csv_row.append(district_75_students)
    csv_row.append(district_75_staff)

    csv_rows.append(csv_row)

print("Writing 'cases.csv'")

with open('cases.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(csv_rows)
