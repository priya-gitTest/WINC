# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line
def farm_action(weather, time_of_day,milk_cow, cow_location,season, slurry_tank_full,grass_long_status):
    farm_action_status = ''
    if time_of_day == 'night' and cow_location=='pasture':
        return  'take cows to cowshed'
    elif cow_location=='cowshed' and milk_cow==True:
        return  'milk cows'
    elif cow_location=='cowshed' and ((weather !='sunny' and weather!='windy')) and slurry_tank_full==True:
        return  'fertilize pasture'
    elif cow_location=='cowshed' and season=='spring' and grass_long_status==True and weather=='sunny':
        return  'mow grass'    
    elif  milk_cow == True  and cow_location=='pasture':
        return  'take cows to cowshed\n'+'milk cows'+'\ntake cows back to pasture'
    elif ((weather !='sunny' or weather!='windy')) and slurry_tank_full==True and cow_location=='pasture':
        return  'take cows to cowshed\n'+'fertilize pasture'+'\ntake cows back to pasture'
    elif grass_long_status==True and season=='spring' and weather=='sunny' and cow_location=='pasture':
        return 'take cows to cowshed\n'+'mow grass'+'\ntake cows back to pasture'
    else :
        return 'wait'
    #return farm_action_status    
#print(farm_action(time_of_day='night',cow_location='pasture'))#take cows to cowshed
#print(farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True))#'fertilize pasture'
#print(farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True))#'wait'
#print(farm_action('windy', 'night', True, 'cowshed', 'winter', True, True)) #'milk cows'
print(farm_action('sunny', 'day', True, 'pasture', 'spring', False, True))