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
