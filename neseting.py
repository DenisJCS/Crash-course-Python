#Dictionary is below
alien_0 = {'color':"green",'points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}
#Now will nest it in list
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

aliens = []
#Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color':'green','points':5, 'speed':'slow'}
    aliens.append(new_alien)

#Show first five aliens    
for alien in aliens[:5]:
    print(alien)

#Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

#Change some aliens in the list
#Make an empty list for storing aliens
for alien_number in range(30):
    new_alien = {'color':'green','points':5, 'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien ['color'] == 'green':
       alien ['color'] = 'yellow'
       alien ['speed'] = 'medium'
       alien ['points'] = 10

#Show the first five aliens    
for alien in aliens[:5]:
    print(alien)
print(f"Total number of aliens: {len(aliens)}")
