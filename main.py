import csv, subprocess, time


#Variables
website = []
status_code = []
web_count = 0

#Clear out old logs before testing
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
    for x in range(3):#Rerun 3 times for testing
      test_input = 'curl -s -o /dev/null -w "%{http_code}" ' + str(z)
      #Run CMD prompt and write the result into a file
      subprocess.Popen(test_input + ' >> log.txt'.format(z),shell=True)
      time.sleep(1)#Wait 1.5 seconds before testing next one, so processes won't overlap
    print("Done with " + str(web_count) + " websites")
  
  #Read output from file and save it in the array
  file = open('log.txt', 'r')
  while True:
    char = file.read(3)#Read only first 3 characters
    if not char:
      break
    status_code.append(char)
  file.close()

#Write results into csv file
with open('data.csv', 'r') as file:
  csv_reader = csv.reader(file)
  with open('new_data.csv', 'w') as data_file:
    csv_writer = csv.writer(data_file, delimiter=",")
    counter = 0
    for line in csv_reader:
      #Write down all 3 exit codes
      for l in range(3):
        line.append(status_code[counter])
        counter += 1
      csv_writer.writerow(line)
print("Done with all the websites")
