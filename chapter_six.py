alien_o = {'color':'green','points':5}
print(alien_o['color'])
print(alien_o['points'])
#Running code to get information from list
new_points = alien_o['points']
print("You just eraned " + str(new_points)+" points!")
#Adding new key to list
alien_o['x_position']=0
alien_o['y_position']=25
print(alien_o)
