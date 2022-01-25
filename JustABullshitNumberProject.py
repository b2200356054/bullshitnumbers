import sys
stringlist = [x for x in sys.argv[1].split(",")]
allnumbers = []
evenlist = []
totaleven = 0
totalall = 0
quote = ""

for allof in stringlist:
    if int(allof) < 0:
        continue
    allnumbers.append(allof)
    
for number in allnumbers:
    number = int(number)
    totalall = totalall + number
    if number%2 == 0:
        evenlist.append(number)
    else:
        continue
    
for sumnum in evenlist:
    totaleven = int(sumnum) + totaleven


for count in range(len(evenlist)):
    quote = "{}".format(quote+str(evenlist[count]))
    if count+1 == len(evenlist):
        continue
    quote = quote + ","
    
evenrate = round(totaleven/totalall, 3)

print("Even Numbers: \"{}\"".format(quote))
print("Sum of Even Numbers: {}".format(totaleven))
print("Even Number Rate = {}".format(evenrate))
