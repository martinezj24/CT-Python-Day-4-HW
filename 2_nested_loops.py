#Task 1: Meal Planner
import random

days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
foods = ['Chicken', 'Beef','Salmon']
meals = ['Breakfast','Lunch','Dinner']

for day in days:
    for meal in meals:
        food = random.choice(foods)
        print('On', day, 'for', meal, 'Im eating', food)
