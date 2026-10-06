name="Olya"
age=41
height=1.6
is_student=True
print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))



name=input("What's your name?")
year_of_birth=input("What year were you born?")
age=2026-int(year_of_birth)
print(f"Hello, {name}! Your approximate age is {age}.")



quantity=input("How many apples did you buy?")
price=input("What is the price of one apple?")
total_cost=float(quantity)*float(price)
print(f"You bought {quantity} apples at ${price}. The total price is ${total_cost:.2f}.")


price=0.99
quantity=5
item=str("Apple")
total=price*quantity
print()
print("=========================================")
print("                RECEIPT                  ")
print("=========================================")
print(f"Item:       {item.upper()}")
print(f"Price:      ${price:.2f}")
print(f"Quantity:   {quantity}")
print("-----------------------------------------")
print(f"Total:      ${total:.2f}")
print("=========================================")



first_name=input("What is your first name?")
surname=input("What is your surname?")
hometown=input("What is your hometown?")
hobby=input("What is your hobby?")
fun_fact=input("Tell me a fun fact about yourself:")
year_of_birth=input("What year were you born?")
age=2026-int(year_of_birth)
print("╔════════════════════════════════════════════╗")
print(f"  PROFILE:  {first_name} {surname}           ")
print("╚════════════════════════════════════════════╝")
print(f"Hometown:       {hometown}")
print(f"Hobby:          {hobby}")
print(f"Fun fact:       {fun_fact}")
print(f"Age:            {age}")
