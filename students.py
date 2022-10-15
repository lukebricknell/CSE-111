import csv

def main():
  stu_dict = read_dict("students.csv")

  ID = input("What is your student ID number?")
  ID = ID.replace("-", "")

  if not ID.isdigit():
    print("Invalid character in I-Number")
  elif ID in list(stu_dict.keys()) :
    print(f"Your name is {stu_dict[ID]}.")
  elif len(ID) < 9:
    print("Invalid I-Number: too few digits")
  elif len(ID) > 9:
    print("Invalid I-Number: too many digits")
  else:
    print("No such student")

def read_dict(filename):
  """Read the contents of a CSV file into a
  dictionary and return the dictionary.

  Parameters
      filename: the name of the CSV file to read.
  Return: a dictionary that contains
      the contents of the CSV file.
  """
  stu_dict = {} 

  with open(filename, "rt") as csv_file:

    reader = csv.reader(csv_file)
    next(reader)

    for row in reader: 

      key = row[0]
      row.remove(key)
      stu_dict[key] = row[0]

  return stu_dict


if __name__ == "__main__":
  main()