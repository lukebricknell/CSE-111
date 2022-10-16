import csv
from datetime import datetime
from datetime import date

from numpy import number

def main():
  index_number = 0;
  
  products_dict = read_dict("products.csv", index_number)

  print(products_dict)
  
  try: 

    filename = "request.csv"
    with open(filename, "rt") as csv_file:

      sub_total = 0;
      number_of_items = 0;

      reader = csv.reader(csv_file)
      next(reader)

      print("--Checkers Hyper by the Sea--")

      print("Products:")
      print("")

      for row in reader:

        key = row[0]
        product_price = float(products_dict[key][2]) * float(row[1])
        name = products_dict[key][1]
        
        number_of_items += int(row[1])
        
        sub_total += product_price
        sales_tax = round(sub_total * 0.06, 2)
        total_amt = round(sub_total + sales_tax, 2)
        current_date_and_time = datetime.now()
        day = current_date_and_time.weekday()


        if "oz" in name or "cup" in name:
          name = name.replace("oz", "")
          name = name.replace("cup", "")
          new_name = ''.join([i for i in name if not i.isdigit()])
          new_name = new_name.strip().capitalize()

          print(new_name)

        else: 
          print(name.capitalize())
      
      print("")
      print(f"---ORDER SUMMARY---")
      print("")
      print(f"Number of items ordered: {number_of_items} ")
      print(f"Subtotal: ${round(sub_total, 2)}")
      print(f"Sales tax: ${sales_tax}")
      print(f"Total Amount: ${total_amt}")
      print("Thank you so much for shopping at Checkers today!")
      print("")

      if day == 1 or day == 2:
        total_amt = round(total_amt * 0.9, 2)
        print(f"Today is your lucky day! You get a 10% discount. Your new total is: ${total_amt}")
      else:
        print("I'm so sorry, but you don't qualify for a discount today.")
      
      print("")

      print(f"{current_date_and_time:%A %I:%M %p}")


  except FileNotFoundError as not_found_err:
    print(not_found_err)
    print(f"Error: cannot open {filename} because it doesn't exist.")
  except PermissionError as perm_err:
    print(perm_err)
    print(f"Error: cannot open {filename} because you don't have permission.")
  except KeyError as key_err:
    print(f"Error: Unkown product ID in the {filename} file {key_err}")



def read_dict(filename, index_number):
  """Read the contents of a CSV file into a
  dictionary and return the dictionary.

  Parameters
      filename: the name of the CSV file to read.
  Return: a dictionary that contains
      the contents of the CSV file.
  """
  products_dict = {} 

  try:
    with open(filename, "rt") as csv_file:

      reader = csv.reader(csv_file)
      next(reader)

      for row in reader: 

        key = row[index_number]
        # row.remove(key)
        products_dict[key] = row

  except FileNotFoundError as not_found_err: 
    print(f"Error: cannot open {filename} because it doesn't exist.")
  except PermissionError as perm_err:
    print(f"Erro: cannot open {filename} because you don't have permission.")
  except KeyError as key_err:
    print(type(key_err))

  return products_dict


if __name__ == "__main__":
  main()
