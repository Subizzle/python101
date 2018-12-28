import math
     
TICKET_PRICE = 10

tickets_remaining = 100  

# Run this code continually until we run out of tickets. 

while tickets_remaining >= 1:

    # Output how many tickets are remaining using the tickets_remaining variable. 
    
    print("Hello Python fans! Welcome to the secret ticket site!\nThere are currently {} tickets remaining for purchase!".format(tickets_remaining))
    
    # Gather the users name and assign it to a new variable.
    
    user_name = input("With whom am I typing with today? ")
    
    # Prompt the user by name and ask them how many tickets they would like.
    
    tickets_requested = int(input("{} how many tickets would you like to purchase? ".format(user_name)))
    
    # Calculate the price (number of tickets multiplied by the price) and assign it to a variable.
    
    def amount_due(TICKET_PRICE, tickets_requested):
        if tickets_requested < 1:
            raise ValueError("At least 1 should be entered")
        return math.ceil(TICKET_PRICE * tickets_requested)  
    
    # Output the price to the screen.
    
    total_cost = amount_due(TICKET_PRICE, tickets_requested)
    
    print("{} the total price would come to ${}.".format(user_name, total_cost))
    
    # Prompt the user if they want to proceed Y/N
    
    confirm = input("At this time {} can I confirm you want to purchase {} tickets for ${}?\nPlease respond yes or no. ".format(user_name, tickets_requested, total_cost))
    
    # If they want to proceed...
    
    if  confirm.lower() == "y":
    
        # Print out to screen "SOLD!" to confirm purchase
        
        print("{} tickets for ${} SOLD to {}!".format(tickets_requested, total_cost, user_name))
        
        # And then dedeuct from the total ticket amount
        
        tickets_remaining -= tickets_requested
    
    # Otherwise ...
    
    else:
        
        print("Thank you for your interest {}!".format(user_name))
    
        # Thank them by name.
        
# Notify user that the tickets are currently sold out.

print(" We're sorry, all tickets for this event have been SOLD OUT!")
