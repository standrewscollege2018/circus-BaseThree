#Benoit Wynn-Williams
#03 / 08 / 18 (START)
#07 / 08 / 18 (FINISH) (expected inputs only)

### Concert Tickets###

#################
#create TK window               (root can be called anything)
from tkinter import *
root = Tk()

root.title("Concert Booking System M1")
root.resizable(width=False, height=False)
root.geometry('400x647')


##################
#Object Orientation
class Concert:
    def __init__(self, name, capacity, availability, cost):
        
        self._name         = name       # underscore means encapsulated. so belongs (and is private) to the class.
        self._capacity     = capacity
        self._availability = availability
        self._cost         = cost

        concerts.append(self)
        concert_names.append(self._name)

concerts = []
concert_names = []

Concert("Blood Brothers 7PM"   , 220, 220, 20)
Concert("Dance Revue 6PM"      , 220, 220, 10)
Concert("Film Fest 5PM"        , 220, 220, 5)
Concert("Drowsy Chaperone 7PM" , 220, 220, 15)
Concert("Cultural Showcase 6PM", 220, 220, 1)

#concert name and price overview in a dunction
def update_concert_overview():
    concert_overview_name.set("")
    concert_overview_capacity.set("")
    concert_overview_availability.set("")
    concert_overview_cost.set("")
    for c in concerts:
        concert_overview_name.set(concert_overview_name.get() + c._name + "\n")
        concert_overview_capacity.set(concert_overview_capacity.get() + str(c._capacity) + "\n")
        concert_overview_availability.set(concert_overview_availability.get() + str(c._availability) + "\n")
        concert_overview_cost.set(concert_overview_cost.get() + "$" + str(c._cost) + "\n")

###################
#title label
concert_name_lbl = Label(root, text="Current Concerts", font="avenir 16 bold", justify=LEFT)
concert_name_lbl.grid(row=0, column = 0, columnspan = 4)

#sub headings
concert_name_lbl = Label(root, text="Concert Name", font="avenir 12 bold underline").grid(row=1, column = 0)
concert_cap_lbl  = Label(root, text="Capacity",  font="avenir 12 bold underline").grid(row=1, column = 1)
concert_aval_lbl = Label(root, text="Available", font="avenir 12 bold underline").grid(row=1, column = 2)
concert_cost_lbl = Label(root, text="Cost",      font="avenir 12 bold underline").grid(row=1, column = 3)

#set up the undynamic label
concert_overview_name = StringVar()
concert_overview_capacity = StringVar()
concert_overview_availability = StringVar()
concert_overview_cost = StringVar()

concert_name_lbl = Label(root, textvariable=concert_overview_name, justify=LEFT)
concert_name_lbl.grid(row=2, column = 0)

concert_capacity_lbl = Label(root, textvariable=concert_overview_capacity, justify=RIGHT)
concert_capacity_lbl.grid(row=2, column = 1)

concert_availability_lbl = Label(root, textvariable=concert_overview_availability, justify=RIGHT)
concert_availability_lbl.grid(row=2, column = 2)

concert_cost_lbl = Label(root, textvariable=concert_overview_cost, justify=RIGHT)
concert_cost_lbl.grid(row=2, column = 3)

#####################
#set up the whole drop down menu

#variables to store TODAY's sale information

tickets_sold_today = 0
earnings_today = 0

#function to order tickets
def order_tickets():

    #test for valid input
    order_error.set("\n\n")
    
    try:
        tickets_entered.set(int(tickets_entered.get()))

        if tickets_entered.get() == 0:
            order_error.set("Error: 'Tickets' is equal to 0\n\n")
        
        elif tickets_entered.get() < 0:
            order_error.set("Error: 'Tickets' is negative\n\n")
                    
        #if input is valid    
        else:
            concert_name.set(selected_concert.get())
            concert_cost = IntVar()
            concert_cost.set(0)

            for c in concerts:
                if concert_name.get() == c._name:
                    #check tickets against capacity
                    if c._availability <= tickets_entered.get():
                        order_error.set("Error: 'Tickets' > 'Capacity' \n\n")
                    else:
                        c._availability = c._availability - tickets_entered.get()
                        concert_cost.set(c._cost)

                        #update order confirmation
                        ticket_order_total_cost = concert_cost.get() * tickets_entered.get()
                        order_confirmation.set(str(tickets_entered.get()) + " ticket(s) ordered for \n'" + concert_name.get() + "' \n at $" + str(concert_cost.get()) + " each. Total $" + str(ticket_order_total_cost))

            global tickets_sold_today, earnings_today #global variables
            
            tickets_sold_today = tickets_sold_today + tickets_entered.get()
            earnings_today     = earnings_today     + ticket_order_total_cost
            
            update_concert_overview() #update the overview label
            ticket_summary()          #update the tickets summary
    except:
        order_error.set("Error: 'Tickets' is not an integer\n\n")

    
 

#sub headings
tickets_sub_title = Label(root, text="Tickets", font="avenir 10 bold").grid(row=3, column=1)


#physical drop down menu
selected_concert = StringVar()
selected_concert.set(concert_names[0])

concert_menu = OptionMenu(root, selected_concert, *concert_names)
concert_menu.grid(row=4)

#entry field for ticket count
tickets_entered = IntVar()
tickets_entered.set(0)
tickets_entry_field = Entry(root, textvariable = tickets_entered, width=6).grid(row=4, column=1)

#enter button
button_tickets = Button(root, text="OK-GO", width=10, font="avenir", command=order_tickets).grid(row=4, column=2)

#dynamic label, displays info about the bokking

order_confirmation = StringVar()
order_confirmation.set("---Not Selected--- \n\n")
order_confirmation_lbl = Label(root, textvariable=order_confirmation, font="avenir 14").grid(row=6)

#error Messages :)

order_error = StringVar()
order_error.set("\n\n")
order_error_lbl = Label(root, textvariable=order_error, font="avenir 14", fg="red").grid(row=6, column=1, columnspan=3, sticky=W)

concert_name = StringVar()

#################################################################
#text variables for labels

tickets_sold = StringVar()
profit_made = StringVar()
def ticket_summary():
    tickets_sold.set("Tickets sold today:   " + str(tickets_sold_today))
    profit_made.set("Earnings today:      $" + str(earnings_today))

#ticket summary for the day
ticket_summary_seperator_lbl = Label(root, text="------------------------------------", pady=10).grid(row=9, column = 0, columnspan=2, sticky=W)

ticket_summary_lbl = Label(root, text="Ticket Summary",    font="avenir 16 bold").grid(row=10, column = 0, columnspan=2, sticky=W)
tickets_sold_today_lbl = Label(root, textvariable=tickets_sold, font="avenir 12").grid(row=11, column = 0, sticky=W)
profit_made_today_lbl  = Label(root, textvariable=profit_made,  font="avenir 12").grid(row=12, column = 0, sticky=W)

#####################
#reseting the day

def reset_today():
    global tickets_sold_today, earnings_today #global variables
    tickets_sold_today = 0
    earnings_today = 0

    for c in concerts:
        c._availability = c._capacity
    
    ticket_summary() #reload the summary label
    update_concert_overview() #reload the overview label
    order_error.set("\n\n") #reset the error
    order_confirmation.set("---Not Selected--- \n\n") #reset the order confirmation


    
        

reset_day_seperator = Label(root, text="------------------------------------", pady=15).grid(row=19, column = 0, columnspan=2, sticky=W)

reset_day_lbl = Button(root, text="RESET", font="avenir 14 bold", fg="red", bg="black", pady=5, command=reset_today).grid(row=20, column = 0, columnspan=1, sticky=W)




#################################################################
update_concert_overview()
ticket_summary()

#this is needed at the end
root.mainloop()


