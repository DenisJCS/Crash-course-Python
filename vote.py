info_0 = {
    'first_name':'Lester',
    'last_name':'Sumrall',
    'DOB':'1958',
    'birthed_in':'Florida',
    'age':'72',
}
print(info_0)
info_0['first_preaching']='Luisiana'
print(info_0)

print(info_0)
if info_0['DOB'] == '1928':
    print("It is Lester Sumral")
elif info_0['DOB']== '1930':
    print("It is not Lester Sumrall")
else:
    print("Error")

year_service = ('1937')
print("Frirs service of "+ info_0['first_name']+ "was in "
      +str(year_service) +" in state of "+ info_0['first_preaching']+".")
#Exercise 6-2
numbers = {'Denis':'7',
           'Jessica':'23',
           'Alex':'5',
           'Vadeam':'15',
           'Rita':'10'
           }
print(numbers)
numbers['Jane']='17'
print(numbers)
del numbers['Denis']
print(numbers)
print("Favorite number of Vadeam is "+ numbers['vadeam'.title()]+".")
number = numbers['Rita']
print(" Favorite number of Rita is " + str(number.upper())+".")
