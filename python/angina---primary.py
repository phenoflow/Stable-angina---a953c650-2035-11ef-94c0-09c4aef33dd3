# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"G33z700","system":"readv2"},{"code":"26863","system":"readv2"},{"code":"29902","system":"readv2"},{"code":"1414","system":"readv2"},{"code":"28554","system":"readv2"},{"code":"9555","system":"readv2"},{"code":"54535","system":"readv2"},{"code":"15349","system":"readv2"},{"code":"7696","system":"readv2"},{"code":"45960","system":"readv2"},{"code":"15373","system":"readv2"},{"code":"1430","system":"readv2"},{"code":"14782","system":"readv2"},{"code":"25842","system":"readv2"},{"code":"19542","system":"readv2"},{"code":"18125","system":"readv2"},{"code":"20095","system":"readv2"},{"code":"13185","system":"readv2"},{"code":"39546","system":"readv2"},{"code":"24540","system":"readv2"},{"code":"12804","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('stable-angina-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["angina---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["angina---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["angina---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
