#Benoit Wynn-Williams
#03 / 08 / 18 (START)

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

def order_tickets():
    concert_name.set(selected_concert.get())
    

    for c in concerts:
        if concert_name.get() == c._name:
            c._availability = c._availability - tickets_entered.get()

    order_confirmation.set(str(tickets_entered.get()) + " ticket(s) ordered for \n'" + concert_name.get() + "' \n at $" + "each. Total")

    update_concert_overview()

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

#dynamic label

order_confirmation = StringVar()
order_confirmation.set("---Not Selected---")
order_confirmation_lbl = Label(root, textvariable=order_confirmation, font="avenir 14").grid(row=6)

concert_name = StringVar()

#################################################################


#########################
update_concert_overview()

#this is needed at the end
root.mainloop()


