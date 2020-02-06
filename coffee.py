class CoffeeMachine:
    possible_states = ["choosing an action", "choosing a variant of coffee", "filling the machine", "stop machine"]
    state = possible_states[0]
    resourses_needed = {
        '1': {'water': 250, 'milk': 0, 'coffee_beans': 16, 'price': 4},
        '2': {'water': 350, 'milk': 75, 'coffee_beans': 20, 'price': 7},
        '3': {'water': 200, 'milk': 100, 'coffee_beans': 12, 'price': 6},
    }

    def __init__(self, water=400, milk=540, coffee_beans=120, disposable_cups=9, money=550):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.disposable_cups = disposable_cups
        self.money = money
        self.filler = 0

    def handle_user_input(self, user_input):
        if self.state == CoffeeMachine.possible_states[0]:
            if user_input == "buy":
                self.state = CoffeeMachine.possible_states[1]
                print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ",
                      end='')
            elif user_input == "fill":
                self.state = CoffeeMachine.possible_states[2]
                self.fill_coffeemachine(user_input)
            elif user_input == "take":
                self.take_money()
            elif user_input == "remaining":
                self.print_remaining()
            elif user_input == "exit":
                self.state = CoffeeMachine.possible_states[3]
        elif self.state == CoffeeMachine.possible_states[1]:
            self.buy_coffee(user_input)
        elif self.state == CoffeeMachine.possible_states[2]:
            self.fill_coffeemachine(user_input)

    def print_remaining(self):
        print(f"""
The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee_beans} of coffee beans
{self.disposable_cups} of disposable cups
${self.money} of money
""")

    def check_resourses(self, coffee_type):
        if self.water < CoffeeMachine.resourses_needed[coffee_type]['water']:
            print("Sorry, not enough water!\n")
            return False
        if self.milk < CoffeeMachine.resourses_needed[coffee_type]['milk']:
            print("Sorry, not enough milk!\n")
            return False
        if self.coffee_beans < CoffeeMachine.resourses_needed[coffee_type]['coffee_beans']:
            print("Sorry, not enough coffee beans!\n")
            return False
        if self.disposable_cups < 1:
            print("Sorry, not enough disposable cups!\n")
            return False
        print("I have enough resources, making you a coffee!\n")
        return True

    def buy_coffee(self, coffee_type):
        if coffee_type not in CoffeeMachine.resourses_needed and coffee_type != "back":
            return
        if coffee_type == 'back':
            print()
            self.state = CoffeeMachine.possible_states[0]
            return
        if not self.check_resourses(coffee_type):
            self.state = CoffeeMachine.possible_states[0]
            return
        self.water -= CoffeeMachine.resourses_needed[coffee_type]['water']
        self.milk -= CoffeeMachine.resourses_needed[coffee_type]['milk']
        self.coffee_beans -= CoffeeMachine.resourses_needed[coffee_type]['coffee_beans']
        self.disposable_cups -= 1
        self.money += CoffeeMachine.resourses_needed[coffee_type]['price']
        self.state = CoffeeMachine.possible_states[0]

    def fill_coffeemachine(self, user_input):
        if self.filler == 0:
            print("\nWrite how many ml of water do you want to add: ")
        if self.filler == 1:
            self.water += int(user_input)
            print("Write how many ml of milk do you want to add: ")
        if self.filler == 2:
            self.milk += int(user_input)
            print("Write how many grams of coffee beans do you want to add: ")
        if self.filler == 3:
            self.coffee_beans += int(user_input)
            print("Write how many disposable cups of coffee do you want to add: ")
        if self.filler == 4:
            self.disposable_cups += int(user_input)
            self.filler = 0
            self.state = CoffeeMachine.possible_states[0]
            print()
            return
        self.filler += 1

    def take_money(self):
        print(f"I gave you ${self.money}\n")
        self.money = 0


my_machine = CoffeeMachine()

while my_machine.state != CoffeeMachine.possible_states[3]:
    if my_machine.state == CoffeeMachine.possible_states[0]:
        print("Write action (buy, fill, take, remaining, exit): ", end='')
    user_input = input()
    my_machine.handle_user_input(user_input)