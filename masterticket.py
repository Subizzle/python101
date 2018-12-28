TICKET_PRICE = 10
SERVICE_CHARGE = 2
tickets_remaining = 100  
def calculate_price(TICKET_PRICE, number_of_tickets):
    return (TICKET_PRICE * number_of_tickets) + SERVICE_CHARGE


while tickets_remaining >= 1:
    print("Hello Python fans! Welcome to the secret ticket site!\nThere are currently {} tickets remaining for purchase!".format(tickets_remaining))
    name = input("With whom am I typing with today? ")
    num_tickets = input("{} how many tickets would you like to purchase? ".format(name))
    try:
        num_tickets = int(num_tickets)
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining for purchase.".format(tickets_remaining))
    except ValueError as err:
        print("{} we have an issue! {}".format(name, err))
    else:
        amount_due = calculate_price(TICKET_PRICE,num_tickets)
        print("{} the total price would come to ${}.".format(name, amount_due))
        confirm = input("At this time {} can I confirm you want to purchase {} tickets for ${}?\nPlease respond yes or no. ".format(name, num_tickets, amount_due))
        if  confirm.lower() == "y":
            print("{} tickets for ${} SOLD to {}!".format(num_tickets, amount_due, name))
            tickets_remaining -= num_tickets
        else:
            print("Thank you for your interest {}!".format(name))
print("We're sorry, all tickets for this event have been SOLD OUT!")
