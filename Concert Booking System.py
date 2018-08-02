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
        
        self._name        = name       # underscore means encapsulated. so belongs (and is private) to the class.
        self._capacity    = capacity
        self._availablity = availability
        self._cost        = cost

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
    concert_overview_cost.set("")
    for c in concerts:
        concert_overview_name.set(concert_overview_name.get() + c._name + "\n")
        concert_overview_capacity.set(concert_overview_capacity.get() + str(c._capacity) + "\n")
        concert_overview_availability.set(concert_overview_availability.get() + "$" + str(c._availability) + "\n")
        concert_overview_cost.set(concert_overview_cost.get() + "$" + str(c._cost) + "\n")

###################
#title label
concert_name_lbl = Label(root, text="Current Concerts", font="avenir 16 bold", justify=LEFT)
concert_name_lbl.grid(row=0, column = 0, columnspan = 4)
        
#set up the undynamic label
concert_overview_name = StringVar()
concert_overview_cost = StringVar()

concert_name_lbl = Label(root, textvariable=concert_overview_name, justify=LEFT)
concert_name_lbl.grid(row=1, column = 0)

concert_capacity_lbl = Label(root, textvariable=concert_overview_capacity, justify=RIGHT)
concert_capacity_lbl.grid(row=1, column = 1)

concert_availability_lbl = Label(root, textvariable=concert_overview_availability, justify=RIGHT)
concert_availability_lbl.grid(row=1, column = 1)

concert_cost_lbl = Label(root, textvariable=concert_overview_cost, justify=RIGHT)
concert_cost_lbl.grid(row=1, column = 1)

#####################
#set up the drop down menu

def select_concert():
    text_selected = selected_concert.get()
    concert_name.set(text_selected)
    

    concert_cost = StringVar()

    for c in concerts:
        if concert_name.get() == c._name:
            concert_cost.set(str(c._cost))
    combined_output.set(concert_name.get() + "   $" + concert_cost.get())


selected_concert = StringVar()
selected_concert.set(concert_names[0])

concert_menu = OptionMenu(root, selected_concert, *concert_names)
concert_menu.grid(row=1)

#enter button
button_enter = Button(root, text="OK-GO", width=10, font="avenir", command=select_concert).grid(row=2, column=0)

#dynamic label

combined_output = StringVar()
combined_output.set("---Not Selected---")
combined_output_lbl = Label(root, textvariable=combined_output, font="avenir 14").grid(row=3)

concert_name = StringVar()
'''
#################################################################
#add a new object and display

#function
def add_new_concert():
    global concert_menu

    if new_name.get() !="Enter concert Name" and new_cost.get() != "Cost":
        concert(new_name.get(), new_cost.get()) #add info into the Object Orientation Class
        update_concert_overview() #update the concert overview label

        concert_menu.grid_forget() #delete the drop down menu
        concert_menu = OptionMenu(root, selected_concert, *concert_names) #reinstate the drop down menu
        concert_menu.grid(row=1)

new_name = StringVar()
new_cost = StringVar() #for various reasons....

new_name.set("Enter concert Name")
new_cost.set("Cost")

add_new_title_seperator_lbl = Label(root, text="---------------------------------------------------", font="avenir 12").grid(row=4)
add_new_title_lbl = Label(root, text="Add a new concert", font="avenir 16 bold").grid(row=5)

new_title_name_entry = Entry(root, textvariable = new_name, width=20).grid(row=6, column=0)
new_title_cost_entry = Entry(root, textvariable = new_cost, width=6 ).grid(row=6, column=1)

new_title_button = Button(root, text="OK-GO", width=10, font="avenir", command=add_new_concert).grid(row=6, column=2)


#################################################################
#edit / update a new object and display

#FUNCTION
def edit_concert():
    global concert_menu

    if edit_name.get() !="Enter concert Name" and edit_cost.get() != "Cost":
        concert(edit_name.get(), edit_cost.get()) #add info into the Object Orientation Class
        update_concert_overview() #update the concert overview label

        concert_menu.grid_forget() #delete the drop down menu
        concert_menu = OptionMenu(root, selected_concert, *concert_names) #reinstate the drop down menu
        concert_menu.grid(row=1)

#UNDYNAMIC LABELS

edit_title_seperator_lbl = Label(root, text="---------------------------------------------------", font="avenir 12").grid(row=7)
edit_title_lbl = Label(root, text="Update a concert's info", font="avenir 16 bold").grid(row=8)

#DROP DOWN
selected_concert_edit = StringVar()
selected_concert_edit.set(concert_names[0])

concert_menu_edit = OptionMenu(root, selected_concert_edit, *concert_names)
concert_menu_edit.grid(row=9)
edit_title_button = Button(root, text="OK-GO", width=10, font="avenir", command=edit_concert).grid(row=9, column=2)


#ENTRY FIELDS
edit_name = StringVar()
edit_cost = StringVar() #for various reasons....

edit_name.set("New concert Name")
edit_cost.set("New $")



edit_name_entry = Entry(root, textvariable = edit_name, width=20).grid(row=10, column=0)
edit_cost_entry = Entry(root, textvariable = edit_cost, width=6 ).grid(row=10, column=1)

edit_title_button = Button(root, text="OK-GO", width=10, font="avenir", command=edit_concert).grid(row=10, column=2)




'''
#########################
update_concert_overview()

#this is needed at the end
root.mainloop()


