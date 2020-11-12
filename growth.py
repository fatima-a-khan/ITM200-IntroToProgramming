#growth.py
#Author: Fatima Khan 500766544


growthrate = 0
s = input("Enter the investment duration: \n");
duration = float(s);

s = input("Enter the investment amount: \n");
investment = float(s);

s = input("Enter the prime rate: \n");
primerate = float(s);

if (investment <= 500000) and (duration <=1):
    growthrate = primerate

elif (investment <=500000) and (duration > 1):
    growthrate = (1.5*primerate)

elif (investment > 500000) and (duration <=1):
    growthrate= (25000*primerate) +(2*primerate)*(investment-25000)

elif (investment > 500000) and (duration > 1):
    growthrate= (25000*2.5*primerate) + ((3.5*primerate)*(investment-25000))


print("Growth rate: "+str(growthrate))













