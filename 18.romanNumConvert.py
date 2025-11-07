def count(num, divisor):
    numCount = num//divisor
    modLeft = num%divisor
    return numCount, modLeft

def stringbuilder(count, str):
    rtstr = ""
    for i in range(count):
        rtstr += str
    return rtstr
  
def latinToRoman(num):
  I = 1
  V = 5
  X = 10
  L = 50
  C = 100
  D = 500
  M = 1000
  romanNum = ''

  mCount, rest = count(num, M)     #1000
  cmCount,rest = count(rest, M-C)  #900
  dCount, rest = count(rest, D)    #500
  cdCount,rest = count(rest, D-C)  #400
  cCount, rest = count(rest, C)    #100
  xcCount,rest = count(rest, C-X)  #90
  lCount, rest = count(rest, L)    #50
  xlCount,rest = count(rest, L-X)  #40
  xCount, iCount = count(rest, X)  #10
  
  romanNum += stringbuilder(mCount, "M")
  romanNum += stringbuilder(cmCount, "CM")
  romanNum += stringbuilder(dCount, "D")
  romanNum += stringbuilder(cdCount, "CD")
  romanNum += stringbuilder(cCount, "C")
  romanNum += stringbuilder(xcCount, "XC")
  romanNum += stringbuilder(lCount, "L")
  romanNum += stringbuilder(xlCount, "XL")
  romanNum += stringbuilder(xCount, "X")
  
  match iCount:
    case 9:
        romanNum +="IX"
    case 8:
        romanNum +="VIII"
    case 7:
        romanNum +="VII"
    case 6:
        romanNum +="VI"
    case 5:
        romanNum +="V"
    case 4:
        romanNum +="IV"
    case 3:
        romanNum +="III"
    case 2:
        romanNum +="II"
    case 1:
        romanNum +="I"
  return romanNum

def main ():
    for i in range (1001):
        romanNum = latinToRoman(i)
        print(f"The Roman equivalent of {i} is: {romanNum}")

if __name__ == "__main__":
    main()