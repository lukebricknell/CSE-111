import csv

def main():
  index_number = 0; 
  products_dict = read_dict("products.csv", index_number)

  print(products_dict)

  with open("request.csv", "rt") as csv_file:

    reader = csv.reader(csv_file)
    next(reader)



    for row in reader:

      key = row[0]

      name = products_dict[key][1]
        
      if "oz" in name or "cup" in name:
        name = name.replace("oz", "")
        name = name.replace("cup", "")
        new_name = ''.join([i for i in name if not i.isdigit()])
        new_name = new_name.strip().capitalize()

        print(f""" 
        Product Name: {new_name}
        Product Quantity: {row[1]}
        Product Price = {products_dict[key][2]}
        """)
      else: 
        print(f""" 
        Product Name: {name}
        Product Quantity: {row[1]}
        Product Price = {products_dict[key][2]}
        """)



def read_dict(filename, index_number):
  """Read the contents of a CSV file into a
  dictionary and return the dictionary.

  Parameters
      filename: the name of the CSV file to read.
  Return: a dictionary that contains
      the contents of the CSV file.
  """
  products_dict = {} 

  with open(filename, "rt") as csv_file:

    reader = csv.reader(csv_file)
    next(reader)

    for row in reader: 

      key = row[index_number]
      # row.remove(key)
      products_dict[key] = row

  return products_dict


if __name__ == "__main__":
  main()


order = range(0,9)