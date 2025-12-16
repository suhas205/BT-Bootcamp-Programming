total_land = 80
segments = 5
land_per_segment = total_land / segments 

tomato_land_30 = 0.30 * land_per_segment
tomato_land_70 = 0.70 * land_per_segment

tomato_yield = (tomato_land_30 * 10) + (tomato_land_70 * 12) 
tomato_sales = tomato_yield * 1000 * 7 


potato_yield = land_per_segment * 10  
potato_sales = potato_yield * 1000 * 20  

cabbage_yield = land_per_segment * 14  
cabbage_sales = cabbage_yield * 1000 * 24 

sunflower_yield = land_per_segment * 0.7 
sunflower_sales = sunflower_yield * 1000 * 200 

sugarcane_yield = land_per_segment * 45 
sugarcane_sales = sugarcane_yield * 4000 


total_sales = (tomato_sales + potato_sales + cabbage_sales + sunflower_sales + sugarcane_sales)


chemical_free_sales = (tomato_sales + potato_sales + cabbage_sales + sunflower_sales)

print("Overall Sales from 80 acres: Rs.", int(total_sales))
print("Chemical-free Sales at end of 11 months: Rs.", int(chemical_free_sales))
