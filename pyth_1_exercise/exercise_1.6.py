A = float(input("Enter the initial money: "))
P = float(input("Enter the banks interest rate: "))
n = float(input("Enter the year: "))

n_a_o_m = A*(1 + P/100)**n #new_amount_of_money
gain = n_a_o_m - A

print("This bank gives %.1f euros in %d years with %.1f%% interest from %.1f euros." %(gain,n,P,A))
