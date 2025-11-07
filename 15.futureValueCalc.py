principal = float(input("What is your initial deposit?: "))
contribCheck = bool(input("Will you be making regular contributions?: ")=="Y"or"y")
contribAmt = 0.0
contribTime = "M"
contribMult = 1
contribStartCheck = True
contribSeries = 0

if contribCheck:
    contribAmt = float(input("How much per contribution?: "))
    contribTime = input("How often will you contribute? Daily, Weekly, Monthly, Annually? D/W/M/A: ")
    contribTime=contribTime.upper()
    contribMult = 0
    contribStartCheck = bool(input("Will these contributions occur at the beginning of the period (Y) or at the end(N)? Y/N: ")=="Y"or"y")
    contribSeries = 0

rate = float(input("What is the interest rate?: "))/100
yrs = int(input("How many years will you wait?: "))
compounds = int(input("How many compounding periods per year?: "))

match contribTime:
    case "D":
        contribMult = 365/compounds
    case "W":
        contribMult = 52/compounds
    case "M":
        contribMult = 12/compounds
    case "A":
        contribMult = 1/compounds

if contribCheck and not contribStartCheck:
    contribSeries = (contribAmt*contribMult)*((1+(rate/compounds))**(yrs*compounds)-(1+rate))/(rate/compounds)
    
elif contribCheck:
    contribSeries = (contribAmt*contribMult)*((1+(rate/compounds))**(yrs*compounds)-1)/(rate/compounds)
    
futureValue = principal*(1+(rate/compounds))**(yrs*compounds)+contribSeries

print(f"The future value of ${principal:,.2f} in {yrs:,} years will be ${futureValue:,.2f}")