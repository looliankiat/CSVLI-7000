import csv

with open('C:\Users\Loo\Desktop\SMART\LI-7000.txt','r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line for line in stripped if line)
    grouped = [line.split() for line in lines]              #converts list into csv format with ',' as delimiter
    print grouped[0]
    with open('updated.csv', 'a+') as out_file:
        out_file.seek(0)                                    #goes to first line of csv file
        first_char=out_file.read(1)                         #reads first character in 'updated.csv'
        if not first_char:                                  #checking if csv file is empty
            if "DATAH" not in grouped[0]:                   #checking for presence of header in in_file and adds header
                writer = csv.writer(out_file)
                writer.writerow(['DATAH','Aux1','Aux2','CO2 AGC','CO2A abs','CO2A um/m','CO2B abs','CO2B um/m',
                                 'CO2D um/m',',Diag','Flow V','H2O AGC','H2OA abs','H2OA dpC','H2OA mm/m','H2OB abs',
                                 'H2OB dpC','H2OB mm/m','H2OD mm/m','Integral','P kPa','Peak','RH %','T C'])
                writer.writerows(grouped)
            else:
                writer=csv.writer(out_file)
                writer.writerows(grouped)
        else:                                               #appending data into existing file
            out_file.seek(0)
            if "DATAH" not in grouped[0]:                   #checking of header in in_file
                writer = csv.writer(out_file)
                writer.writerows(grouped)
            else:
                grouped.remove(grouped[0])                  #removing header from in_file
                writer = csv.writer(out_file)
                writer.writerows(grouped)
