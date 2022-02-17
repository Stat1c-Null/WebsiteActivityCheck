import csv, subprocess, time, os
import pandas as pd

#Variables
website = []
status_code = []
web_count = 0
empty = True
size = os.path.getsize("log.txt")
nameplace = 'copy_of_'

def copy_csv(filename):
  global nameplace
  df = pd.read_csv(filename)
  name = nameplace + filename
  if os.path.exists(name) and os.path.isfile(name):
    os.remove(name)
    df.to_csv(name)
  else:
    df.to_csv(name)

#Check if file was previously empty or not
if size > 0:
  print("Log file is not empty")
  empty = False
else:
  print("Log file is empty")
  empty = True
#Clear out old logs
with open('log.txt', 'w'):
    pass

#Read data from csv
with open('data.csv', 'r') as csv_file:
  csv_reader = csv.reader(csv_file)

  #Save all the websites to array
  for x in csv_reader:
    website.append("https://" + x[0] + "/")

  #Test the websites 
  for z in website:
    web_count += 1#Add 1 for each new website
  
    test_input = 'curl -s -o /dev/null -w "%{http_code}" ' + str(z)
    #Run CMD prompt and write the result into a file
    try:
      subprocess.Popen(test_input + ' >> log.txt'.format(z),shell=True)
      time.sleep(1)#Wait 1.5 seconds before testing next one, so processes won't overlap
      print("Done with " + str(web_count) + " websites")
    except:
      with open("log.txt", 'a') as f:
        f.write('nul')

  
  #Read output from file and save it in the array
  file = open('log.txt', 'r')
  while True:
    char = file.read(3)#Read only first 3 characters
    if not char:
      break
    status_code.append(char)
  file.close()

#Copy old data, so we can add it to new one
copy_csv('new_data.csv')

if empty:
  file_path = 'data.csv'
else:
  file_path = nameplace + 'new_data.csv'

#Write results into csv file
with open(file_path, 'r') as file:
  csv_reader = csv.reader(file)
  with open('new_data.csv', 'w') as data_file:
    csv_writer = csv.writer(data_file, delimiter=",")
    counter = 0

    for line in csv_reader:
      #Write down all 3 exit codes
      line.append(status_code[counter])
      counter += 1
      csv_writer.writerow(line) 
    print("This execution status codes: ")
    print(status_code)
print("Done with all the websites")
