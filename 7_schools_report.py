"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten, and SEC divisons.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 75%
Display report for all universities that have a total price for in-state 
students living off campus over $65,000

"""
import json

infile = open('school_data.json','r')
schools = json.load(infile)

conferece_schools = [372,108,107,130]

print (len(schools))

for school in schools:
    #print(type(school))
    conf_number = school["NCAA"]["NAIA conference number football (IC2020)"]
    #print(conf_number)
    if conf_number in conferece_schools:
        grad_rate = school['Graduation rate  women (DRVGR2020)']
        if grad_rate > 75:
            print(f"University Name: {school['instnm']}")
            print(f"Graduation rate for Women: {grad_rate}%")
            print()
            print()

#Report 2

for school in schools:
    #print(type(school))
    conf_number = school["NCAA"]["NAIA conference number football (IC2020)"]
    #print(conf_number)
    if conf_number in conferece_schools:
        tuition = school ["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"]
        if tuition: #if there is a value in tuition
            if tuition > 60_000:
                print(f"University Name: {school['instnm']}")
                print(f"Tuition Cost {tuition:,.2f}")
                print()
                print()


#Report 3

for school in schools:
    #print(type(school))
    conf_number = school["NCAA"]["NAIA conference number football (IC2020)"]
    #print(conf_number)
    if conf_number in conferece_schools:
        off_camp = school["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)": 63285,
   "Total price for out-of-state students living off campus (not with family)  2020-21 (DRVIC2020)":]