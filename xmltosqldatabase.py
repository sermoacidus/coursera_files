import sqlite3
import re

create_new_db = sqlite3.connect('emaildb.sqlite')
processing_file_1 = create_new_db.cursor()
processing_file_1.execute('DROP TABLE IF EXISTS Counts')
processing_file_1.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

file_name_input = input(str('Enter file name: '))
if len(file_name_input) < 1: file_name_input = 'mbox.txt'

file_handle_1 = open(file_name_input)
for line in file_handle_1:
    line=line.strip()
    piece_of_text = re.findall('^From:.*@(\S+)',line)
    if len(piece_of_text) < 1: continue
    email = str(piece_of_text)
    email = email[2:len(email)-2]
    #print(email)
    processing_file_1.execute('SELECT count FROM Counts WHERE org = ?',(email,))
    row = processing_file_1.fetchone()
    if row is None:
        processing_file_1.execute('INSERT INTO Counts(org,count) VALUES(?,1)',(email,))
    else:
        processing_file_1.execute('UPDATE Counts SET count = count+1 WHERE org = ?',(email,))
create_new_db.commit()

for row in processing_file_1.execute('SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'):
    print(str(row[0]), row[1])

processing_file_1.close()
