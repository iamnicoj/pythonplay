import variables as v

print(v.daftpunk)
print(v.qotsa)

months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

for month in months:
  print(month)
  if month == "September":
    print(v.daftpunk)
  elif month == "May":
    print(v.qotsa)  
    

