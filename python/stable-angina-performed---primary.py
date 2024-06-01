# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"68139","system":"readv2"},{"code":"42304","system":"readv2"},{"code":"60753","system":"readv2"},{"code":"38813","system":"readv2"},{"code":"33471","system":"readv2"},{"code":"44561","system":"readv2"},{"code":"67761","system":"readv2"},{"code":"37719","system":"readv2"},{"code":"61310","system":"readv2"},{"code":"737","system":"readv2"},{"code":"19046","system":"readv2"},{"code":"22828","system":"readv2"},{"code":"12734","system":"readv2"},{"code":"36011","system":"readv2"},{"code":"72780","system":"readv2"},{"code":"86071","system":"readv2"},{"code":"70185","system":"readv2"},{"code":"93618","system":"readv2"},{"code":"66664","system":"readv2"},{"code":"92927","system":"readv2"},{"code":"5744","system":"readv2"},{"code":"48767","system":"readv2"},{"code":"22647","system":"readv2"},{"code":"18249","system":"readv2"},{"code":"42708","system":"readv2"},{"code":"33718","system":"readv2"},{"code":"7609","system":"readv2"},{"code":"56990","system":"readv2"},{"code":"70755","system":"readv2"},{"code":"11610","system":"readv2"},{"code":"28837","system":"readv2"},{"code":"68123","system":"readv2"},{"code":"34963","system":"readv2"},{"code":"66236","system":"readv2"},{"code":"19413","system":"readv2"},{"code":"7134","system":"readv2"},{"code":"8312","system":"readv2"},{"code":"86773","system":"readv2"},{"code":"18670","system":"readv2"},{"code":"66921","system":"readv2"},{"code":"32651","system":"readv2"},{"code":"5703","system":"readv2"},{"code":"8679","system":"readv2"},{"code":"7137","system":"readv2"},{"code":"61208","system":"readv2"},{"code":"7634","system":"readv2"},{"code":"55598","system":"readv2"},{"code":"45886","system":"readv2"},{"code":"20903","system":"readv2"},{"code":"57241","system":"readv2"},{"code":"41547","system":"readv2"},{"code":"31556","system":"readv2"},{"code":"43939","system":"readv2"},{"code":"96537","system":"readv2"},{"code":"96804","system":"readv2"},{"code":"55092","system":"readv2"},{"code":"22020","system":"readv2"},{"code":"42462","system":"readv2"},{"code":"732","system":"readv2"},{"code":"69776","system":"readv2"},{"code":"59423","system":"readv2"},{"code":"60067","system":"readv2"},{"code":"70111","system":"readv2"},{"code":"64923","system":"readv2"},{"code":"62608","system":"readv2"},{"code":"37682","system":"readv2"},{"code":"10209","system":"readv2"},{"code":"3159","system":"readv2"},{"code":"67591","system":"readv2"},{"code":"31519","system":"readv2"},{"code":"19193","system":"readv2"},{"code":"51515","system":"readv2"},{"code":"85947","system":"readv2"},{"code":"8942","system":"readv2"},{"code":"9414","system":"readv2"},{"code":"51507","system":"readv2"},{"code":"33735","system":"readv2"},{"code":"7442","system":"readv2"},{"code":"92419","system":"readv2"},{"code":"45370","system":"readv2"},{"code":"87849","system":"readv2"},{"code":"19402","system":"readv2"},{"code":"733","system":"readv2"},{"code":"93828","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('stable-angina-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["stable-angina-performed---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["stable-angina-performed---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["stable-angina-performed---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
