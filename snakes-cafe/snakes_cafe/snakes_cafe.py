
orders=[]

def menu():
    print('**************************************')
    print('**    Welcome to the Snakes Cafe!   **')
    print('**    Please see our menu below.    **')
    print('**')
    print('** To quit at any time, type "quit" **')
    print('**************************************')

    print('Appetizers')
    print('----------')
 
    print('Wings')
    print('Cookies')
    print('Spring Rolls')

    print('Entrees')
 

    print('-------')
    print('Salmon')
    print('Steak')
    print('Meat Tornado')
    print('A Literal Garden')

    print('Desserts')
    print('--------')
    print('Ice Cream')
    print('Cake')
    print('Pie')

    print('Drinks')
    print('------')
    print('Coffee')
    print('Tea')
    print('Unicorn Tears')
    print('***********************************')
    order=input('** What would you like to order? **\n***********************************\n>')
    orders.append(order)

    
    print(f'** {orders.count(order)} order of {order} have been added to your meal **')


if __name__ == "__main__":

    response = ""
    while response != "quit":
        menu()
        response = input("Are you done ordering? type 'quit' to exit")

    print("Thanks for ordering!")



