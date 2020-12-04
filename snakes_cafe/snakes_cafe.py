
orders=[]

def menu():
    print("""
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************

    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls

    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden

    Desserts
    --------
    Ice Cream
    Cake
    Pie

    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears

    ***********************************
    ** What would you like to order? **
    ***********************************
    """)
menu()


    


if __name__ == "__main__":
    order=""
    while order != "quit":
        order=input('> ')
        if order!='quit':
            orders.append(order)
            print(f'** {orders.count(order)} order of {order} have been added to your meal **')
            
  
    print("Thanks for ordering!")



