#Empty list
alien_0 = {}
alien_0['color']='green'
alien_0['points']=5
print(alien_0)

#Changning variables in list
alien_0={'color':'green'}
print("The alien is "+alien_0['color']+".")
alien_0['color']='yellow'
print("The alien is now "+alien_0['color']+".")

#Speed of an alien
alien_0={'x_position':0,'y_position':25,'speed':'fast'}
print("Original x_postion:"+str(alien_0['x_position']))
#Aline moving to right
# Calculate the offset amount based on the current speed.”
if alien_0['speed'] == 'slow':
    x_increment =1
elif alien_0['speed'] == 'medium':
    x_increment = 2 
else:
    #Alien moving fast
    x_increment = 3
# The new position is equal to the sum of the old position and the increment.”          
alien_0['x_position']= alien_0['x_position']+x_increment
print("New x_position:" +str(alien_0['x_position']))

#Deleting pair "key-variable"
alien_0={'color':'green','points':5}
print(alien_0)
del alien_0['points']
print(alien_0)

print("Well done Denis")
