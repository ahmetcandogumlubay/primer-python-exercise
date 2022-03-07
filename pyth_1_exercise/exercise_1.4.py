meters = float(input("Enter the meters: "))
cm = meters*100
inches = 2.54
feets = 12*inches
yards = 3*feets
b_miles = 1760*yards

print("%.1f meters is %.1f inches." %(meters,cm/inches)\
      ,"\n%.1f meters is %.1f feets." %(meters,cm/feets)\
          ,"\n%.1f meters is %.1f yards." %(meters,cm/yards)\
              ,"\n%.1f meters is %.1f british miles." %(meters,cm/b_miles))
    