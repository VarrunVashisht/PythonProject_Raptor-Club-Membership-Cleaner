📘 Project Overview

The local Raptors Fan Club keeps a list of members in a .txt file.
Each month, they mark active members with “yes” and inactive ones with “no” in an Active column.

Your job as a Python beginner 🐍 is to:

Read the list of current members

Remove those who are inactive (Active = "no")

Append them to another file called inactive.txt

Keep the file format and header intact

It’s a small automation task that teaches you file handling and data cleaning basics.

📂 Folder Structure
raptor-club-cleaner/
├── README.md
├── main.py
├── members.txt
└── inactive.txt

🧠 What You’ll Learn

✅ How to open, read, and write files using with open()
✅ How to loop through file lines
✅ How to filter and move data between files
✅ How to preserve file headers and formatting
✅ How to automate repetitive tasks

main.py
Here’s a simple working version of your project. It automatically creates sample data, cleans inactive members, and prints both files.

from random import randint as rnd

# File paths
members_file = 'members.txt'
inactive_file = 'inactive.txt'
status = ('yes', 'no')

# Generate random sample files for testing
def generate_files(current, old):
    with open(current, 'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active\n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for _ in range(20):
            date = f"{rnd(2015,2020)}-{rnd(1,12)}-{rnd(1,28)}"
            writefile.write(data.format(rnd(10000,99999), date, status[rnd(0,1)]))

    with open(old, 'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active\n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for _ in range(3):
            date = f"{rnd(2015,2020)}-{rnd(1,12)}-{rnd(1,28)}"
            writefile.write(data.format(rnd(10000,99999), date, 'no'))

# ✨ Function to clean files
def cleanFiles(currentMem, exMem):
    with open(currentMem, 'r+') as current, open(exMem, 'a+') as old:
        members = current.readlines()
        header = members[0]
        members = members[1:]

        # Separate active and inactive members
        active_members = []
        inactive_members = []

        for member in members:
            if 'no' in member:
                inactive_members.append(member)
            else:
                active_members.append(member)

        # Write only active members back to current file
        current.seek(0)
        current.write(header)
        for member in active_members:
            current.write(member)
        current.truncate()  # Remove leftover old data

        # Append inactive members to the inactive file
        old.write(''.join(inactive_members))

# Generate sample data
generate_files(members_file, inactive_file)

# Run the cleaner
cleanFiles(members_file, inactive_file)

# Show results
print("\n✅ Active Members:\n")
with open(members_file, 'r') as file:
    print(file.read())

print("\n🛑 Inactive Members:\n")
with open(inactive_file, 'r') as file:
    print(file.read())


📄 Sample Output
🟢 Active Members (members.txt)
Membership No  Date Joined  Active
   82531        2016-6-18   yes
   48294        2018-3-12   yes
   91237        2017-9-27   yes

🔴 Inactive Members (inactive.txt)
Membership No  Date Joined  Active
   23451        2019-8-22   no
   67219        2020-1-14   no

🧪 How It Works

1️⃣ Open both files using Python’s with open() (in r+ and a+ modes)
2️⃣ Read all lines from the current member file
3️⃣ Split data into active and inactive lists
4️⃣ Rewrite the active list back into the original file
5️⃣ Append inactive members to the old members file

🧰 File Modes Used
Mode	Meaning	Used For
'r+'	Read + Write	To update the members.txt file
'a+'	Append + Read	To add to the inactive.txt file
🧩 How to Run

Make sure Python (3.8 or newer) is installed.
Save the files as shown above.
Open a terminal in your project folder.

Run:
python main.py

💡 Ideas to Expand
Want to make it more advanced? Try:

Add a menu to add or remove members manually
Log the date of each cleanup
Count how many members were removed
Save reports like cleanup_log.txt
Visualize member data using matplotlib

👩‍💻 Author

Your Name
Varrun Vashisht
  

