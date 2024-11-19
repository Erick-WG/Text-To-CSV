import csv
from datetime import datetime


# Defining the reader function with default format file = txt file.
# Future use and formatting of other file formats.
def Reader(filename, format='txt') -> str:
    try:
        with open(filename+'.'+format, 'r') as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        print("Please input a file")
        return FileNotFoundError

# Defining the data formatting function.
# think of a way to add formatting options, default will be tab separated values.
def Format(lines, fotmat_delimeter='\t', reversed=False)-> str:
    rows = []
    for line in lines:
        if not reversed:
            line = line.strip().split(fotmat_delimeter)
            rows.append(line)
        else:
            rows.append(line.strip().split(fotmat_delimeter)[::-1])
    return rows



# Defining the Converting function.
# The output file name accepts args and defaults to output + current date.
def Converter(rows, outputFilename=f'output {datetime.now().strftime('%d-%m-%Y %H-%M_%p')}') -> None:
    # Think of a way to define the output file.
    with open(outputFilename+'.csv', 'w', newline="") as output_file:
        writer = csv.writer(output_file, delimiter=",")
        writer.writerows(rows)
        print('Successfully converted txt -> csv')



# Main execution of the converter.
def main ():
    filename = input("Please input the file name (without extensions): ")
    lines = Reader(filename)
    
    print("")
    print("Input file format: ")
    print("")

    options = {
        "1": "Tab separated values",
        "2": "Comma separated values",
        "3": "Space separated values"
    }
    
    # Displaying options
    for option in options:
        print(f"{option}: {options[option]}")
    
    print("")
    # User input for output formatting.
    choice_format = input("Select the format of your text file: ").lower()
    print("")
    
    # input file format passed for reading to get key data.
    match (choice_format):
        case ('1' | "tab separated values"):
            rows = Format(lines)
        case ('2' | "comma separated values"):
            rows = Format(lines, ',')
        case ('3' | "space separated values"):
            rows = Format(lines, '\S')
        case (_):
            rows = Format(lines)
            Converter(rows)
            

    print('Reversed output: Yes | No')
    reversing = input("Would you like to reverse the order of columns in the file? ")
    
    # Reversing output by users choice.
    match (reversing):
        # Reversing output option.
        case ('yes'):
            rows = Format(lines, reversed=True)
        case ('no'):
            rows = Format(lines, reversed=False)
        case (_):
            rows = Format(lines)
            Converter(rows)

    print('Great 😎')
    
    output_file_name = input("How would you like to name your output file? ")
    if output_file_name:
        Converter(rows, output_file_name)
    else:
        Converter(rows)
    
if __name__ == "__main__":
    main()