year_list = ["jan", "feb", "march", "april", "may", "jun", "july", "aug", "sep", "oct", "nov", "dec"]


print("Month Codes==>\n jan, feb, march, april, may, jun, \n july, aug, sep, oct, nov, dec")
date = int(input("Date: "))
month = str(input("Month: "))
year = input("Year: ")
year_2 = int(str(year)[-2:])
year_3 = year_2 / 4
year_len = len(str(year))

if 1000 < int(year) < 1099:
    centuery_code = 2
if 1100 < int(year) < 1199:
    centuery_code = 0
if 1200 < int(year) < 1299:
    centuery_code = 6
if 1300 < int(year) < 1399:
    centuery_code = 4
if 1400 < int(year) < 1499:
    centuery_code = 2
if 1500 < int(year) < 1599:
    centuery_code = 0
if 1600 < int(year) < 1699:
    centuery_code = 6
if 1700 < int(year) < 1799:
    centuery_code = 4
if 1800 < int(year) < 1899:
    centuery_code = 2
if 1900 < int(year) < 1999:
    centuery_code = 0
if 2000 < int(year) < 2099:
    centuery_code = 6
if 2100 < int(year) < 2199:
    centuery_code = 4
if 2200 < int(year) < 2299:
    centuery_code = 2
if 2300 < int(year) < 2399:
    centuery_code = 0
if 2400 < int(year) < 2499:
    centuery_code = 6
if 2500 < int(year) < 2599:
    centuery_code = 4
if 2600 < int(year) < 2699:
    centuery_code = 2
if 2700 < int(year) < 2799:
    centuery_code = 0
if 2800 < int(year) < 2899:
    centuery_code = 6
if 2900 < int(year) < 2999:
    centuery_code = 4
if 3000 < int(year) < 3099:
    centuery_code = 2
if 3100 < int(year) < 3199:
    centuery_code = 0
if 3200 < int(year) < 3299:
    centuery_code = 6
if 3300 < int(year) < 3399:
    centuery_code = 4
if 3400 < int(year) < 3499:
    centuery_code = 2
if 3500 < int(year) < 3599:
    centuery_code = 0
if 3600 < int(year) < 3699:
    centuery_code = 6
if 3700 < int(year) < 3799:
    centuery_code = 4
if 3800 < int(year) < 3899:
    centuery_code = 2
if 3900 < int(year) < 3999:
    centuery_code = 0
if 4000 < int(year) < 4099:
    centuery_code = 0


if date > 31:
    print("Cant Accept That Sorry.")
elif month not in year_list:
    print("Cant Accept That Sorry.")
elif year_len > 4:
    print("Cant Accept That Sorry.")

if month == year_list[0]:
    month_code = 1
if month == year_list[1]:
    month_code = 4
if month == year_list[2]:
    month_code = 4
if month == year_list[3]:
    month_code = 0
if month == year_list[4]:
    month_code = 2
if month == year_list[5]:
    month_code = 5
if month == year_list[6]:
    month_code = 0
if month == year_list[7]:
    month_code = 3
if month == year_list[8]:
    month_code = 6
if month == year_list[9]:
    month_code = 1
if month == year_list[10]:
    month_code = 4
if month == year_list[11]:
    month_code = 6

cal = date + int(month_code) + centuery_code + year_2 + int(year_3)
final_cal = cal % 7

final_day = ""

if final_cal == 1:
    final_day = "Sunday"
if final_cal == 2:
    final_day = "Monday"
if final_cal == 3:
    final_day = "Tuesday"
if final_cal == 4:
    final_day = "Wednesday"
if final_cal == 5:
    final_day = "Thursday"
if final_cal == 6:
    final_day = "Friday"
if final_cal == 0:
    final_day = "Saturday"

print("It was " + final_day)
