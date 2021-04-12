app = input("Which app:")
print("Launching: " + app)

income_tax = {"CA": {"0" : 15, "97069": 26, "150473":29, "214368":33},
            "CAQC": {"0": 15, "44545": 20, "89080": 24, "108000": 25.75},
            "CABC": {"0": 5.06, "42184": 7.70, "84369" : 10.5, "96866": 12.29, "117623": 14.7, "159483": 16.8, "222420": 20.5}}

capgain_tax = 

prov = {"CA": {"BC","QC"}, "US":{"TX":0,"CA": {} }

if app == "Test":
    paygrowth =	0.03
    stock_return = 0.1
    bond_return = 0.05
    tax_cred = 200000
    tax_cred_used = 0	
    salary= 90000
    country= "CA"
    province = "QC"
    perf_bonus = 0.15
    sign_bonus = 15000
    gross_pay = perf_bonus * salary + sign_bonus + salary
else:
    title = input("What is your job title?")
    paygrowth =	infer_growth(title)
    risk_profile = input("How much risk would you like?")
    stock_return = infer_stock_return(risk_profile)
    bond_return = 0.05
    tax_cred = input("How much tax credit do you have?")
    salary= input("What is your current salary")
    bonus = input("How much bonus do you receive?")
    country= input("Which country do you live in?")
    if country == "CA" or country =="US":
        province = input("Which state/province do you live in?")
    city = input("Which city do you live in?")
    
def infer_pay_growth(title):
    pass

def infer_stock_return(risk_profile):
    pass
    



def net_worth(gross_pay, paygrowth, stock_return, bond_return, loc):
    if gross_pay > taxes[]


