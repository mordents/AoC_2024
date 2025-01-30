#The notation X|Y means that if both page number X and page number Y are to be produced as part of an update
# page number X must be printed at some point before page number Y
# Which books adhere to these rules 
rules = []
reports = []

with open('AoC5input.txt') as f:
    rules_section = True
    for line in f:
        if line == '\n':
            rules_section = False
            continue
        if rules_section == True:
            rules.append([int(number) for number in line.strip().split('|')])
        if rules_section == False:
            reports.append([int(number) for number in line.strip().split(',')]) 
def valid_report(report):
    for rule in rules:
        if rule[0] not in report or rule[1] not in report:
            continue
        left = report.index(rule[0])
        right = report.index(rule[1])
        if left>right:         #if in the report the item found at 0 comes after the val found
            return False       #at index 1 , the rule is broken
    return True
def get_middle_number(report):
    idx = len(report)//2
    return report[idx]
ans = sum([get_middle_number(report) for report in reports if valid_report(report)])



#Part 2 
def corrected(report):
    idx = 0
    while idx<len(rules):
        rule = rules[idx]
        if rule[0] not in report or rule[1] not in report:
            idx+=1
            continue
        left = report.index(rule[0])
        right = report.index(rule[1])
        if left<right:
            idx+=1
            continue
        # left > right
        tmp = report[left]
        report[left] = report[right]
        report[right] = tmp
        idx = 0 
    return report
ans_pt_2 = sum([get_middle_number(corrected(report)) for report in reports if valid_report(report)==False])
print(ans_pt_2)