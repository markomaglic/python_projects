import re
x=re.search("^([1-9] |1[0-9]| 2[0-9]|3[0-1])(.|-)([1-9] |1[0-2])(.|-|)20[0-9][0-9]$",date)

def transform_date_format(dates):
    correct_date_format = ''
    return_dates = []
    # Sad u for petlji pretvoriti iz 2010/02/20 u 20100220
    for date in dates:
        print(date)
        #regex za provjeru 3 formata koja su prihvaćena i trebaju se vraćati u novu listu
        if (re.search("(/^\d{4}-\d{2}-\d{2}$/)||(/^\d{2}-\d{2}-\d{4}$/)"),date)
        numbers = date.split("/")
        correct_date_format += numbers[0] + numbers[1] + numbers[2]
        return_dates.append(correct_date_format)
        print(return_dates)
    return return_dates

if __name__ == "__main__":
    dates = transform_date_format(["2010/02/20", "2 016p 19p 12", "11-18-2012", "2018 12 24", "20130720"])
    print(*dates, sep='\n')

