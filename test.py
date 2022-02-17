import csv
import pandas as pd
fieldnames = []
#Check if csv file is empty
def is_empty_csv(path):
  with open(path) as csvfile:
    reader = csv.reader(csvfile)
    for i, _ in enumerate(reader):
      if i:  # found the second row
        print("Not empty file")
        return False
  print("Empty file")
  return True

#Get number of columns in file
def get_length(file_path):
  df = pd.read_csv(file_path)
  cols = len(df.axes[1])
  return cols

#Convert from csv into dictionary
def csv_conv_dict(file_path):
  global fieldnames
  data_dict = {}
  with open(file_path, 'r') as data:
    for line in csv.DictReader(data):
      data_dict = line
    return data_dict

def append_data(file_path, website, new_code):
  global fieldnames
  old_data = {}
  p1 = "'"
  p2 = "}"
  #Check if file is empty or not
  empty = is_empty_csv("testdata.csv")
  #If file is empty, fill it with new data
  if empty:
    fieldnames = ["website", "code"]#If file is empty, set default header
    with open(file_path, "a") as csvfile:
      writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
      writer.writeheader()
      writer.writerow({
        "website": website,
        "code": new_code
      })
  #If file is not empty, add new data on top
  else:
    #Write previous headers into array
    file = open(file_path, 'r')
    for line in file.readlines(1):
        fieldnames = line.rstrip().split(',') #using rstrip to remove the \n
    #Number of columns
    next_id = get_length(file_path)
    #Convert old data into dictionary
    old_data = csv_conv_dict(file_path)
    my_data = [old_data]
    #Convert into pandas DataFrame so we can insert new code
    col_name = "code"+str(next_id)
    data = pd.DataFrame.from_dict(my_data)
    print("Old data:")
    print(data)
    #Insert new data
    data.insert(next_id, col_name, str(new_code), True)
    fieldnames.append(col_name)#Add new value to header
    end_dict = data.to_dict(orient="dict")
    print("New data: ")
    #print(end_dict)
    #Extract specific data from weird dictionary
    for i in range (len(fieldnames)):
      placehold = str(end_dict[fieldnames[i]])
      id1 = placehold.index(p1)
      id2 = placehold.index(p2)
      res = ''
      for lol in range(id1 + len(p1), id2):
        res = res + placehold[lol]
      new = res.replace(res[len(res)-1], '')#Remove quote at the end
      print(new)
      end_dict[fieldnames[i]] = new
      
    with open(file_path, "w") as file:
      writer = csv.DictWriter(file, fieldnames=fieldnames)
      writer.writeheader()
      writer.writerow(end_dict)
    
append_data("testdata.csv", "google", 304)

