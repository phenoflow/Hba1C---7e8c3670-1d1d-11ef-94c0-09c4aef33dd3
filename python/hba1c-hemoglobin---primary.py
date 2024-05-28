# Matthew J Carr, Alison K Wright, Lalantha Leelarantha, Hood Thabit, Nicola Milne, Naresh Kanumilli, Darren M Ashcroft, Martin K Rutter, 2024.

import sys, csv, re

codes = [{"code":"44TC.00","system":"readv2"},{"code":"42V2000","system":"readv2"},{"code":"44TB.00","system":"readv2"},{"code":"42VA.00","system":"readv2"},{"code":"44TB000","system":"readv2"},{"code":"42W..12","system":"readv2"},{"code":"44TB100","system":"readv2"},{"code":"42V2.00","system":"readv2"},{"code":"1.09871E+14","system":"readv2"},{"code":"1.29761E+14","system":"readv2"},{"code":"493590018","system":"readv2"},{"code":"404443010","system":"readv2"},{"code":"489331011","system":"readv2"},{"code":"493589010","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('hba1c-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["hba1c-hemoglobin---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["hba1c-hemoglobin---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["hba1c-hemoglobin---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
