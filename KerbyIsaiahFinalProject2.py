"""
Program: KerbyIsaiahFinalProject.py
Author: Isaiah Kerby
Last date modified: 2/25/2025 

This final project program provides a GUI interface for customers of a car customization shop to 
select customization options for their car. The interface keeps track of the customer's selections and 
and a running subtotal, tax, and total amount for purchase.
"""

# import the breezypythongui and tkinkter
from breezypythongui import EasyFrame
from tkinter import *
from tkinter import PhotoImage
from tkinter.font import Font


class CarCustomization(EasyFrame):
    # The  __init__ methodd definition
    # Definisitions of event handling methods

    def __init__(self):
        # Set up the main window and the widgets.
        EasyFrame.__init__(self, title = "Car Customization Calculator")
        self.setResizable(False);
        imageLabel = self.addLabel(text = "", row = 0, column = 0, sticky = "NSEW", columnspan = 5)
        textLabel = self.addLabel(text = "Car Customization Calculator", row = 1, column = 0, sticky = "NSEW", columnspan = 5)

        # load the top of window image and associate it with the image label
        self.image = PhotoImage(file="racecar3.png")
        imageLabel["image"] = self.image
            # set the font for the image caption
        font = Font(family ="Verdana", size = 30, slant = "italic")
        textLabel["font"] = font
        textLabel["foreground"] = "red"

        # set the main window background color to light yellow
        self["background"] = "yellow"
        

        # Create a top level window for checkout display of items selected in main window..
        def checkout_window():
            global chromeWheelLabel
            top_window = Toplevel()
            top_window.geometry("600x800")
            top_window.title('Checkout Window')
            top_window['background']='yellow'
            
            # List all of the items that were checked along with their prices.
            if self.chromeWheelCB.isChecked():
                Label(top_window, text = "Chrome Wheels: $" + str("%.2f" % wheelPrices.get("Chrome")), bg='yellow', padx=20, pady=5).pack()
            if self.bronzeWheelCB.isChecked():
                Label(top_window, text = "Bronze Wheels: $" + str("%.2f" % wheelPrices.get("Bronze")), bg='yellow', padx=20, pady=5).pack()
            if self.carbonFiberWheelCB.isChecked():
                Label(top_window, text = "Carbon Fiber Wheels: $" + str("%.2f" % wheelPrices.get("Carbon Fiber")), bg='yellow', padx=20, pady=5).pack()
            if self.matteWhiteWheelCB.isChecked():
                Label(top_window, text = "Matte White Wheels: $" + str("%.2f" % wheelPrices.get("Matte White")), bg='yellow', padx=20, pady=5).pack()
            
            if self.regularSeatCB.isChecked():
                Label(top_window, text = "Regular Seats: $" + str("%.2f" % seatPrices.get("Regular")), bg='yellow', padx=20, pady=5).pack()
            if self.racingSeatCB.isChecked():
                Label(top_window, text = "Racing Seats: $" + str("%.2f" % seatPrices.get("Racing")), bg='yellow', padx=20, pady=5).pack()

            if self.spoilerAeroCB.isChecked():
                Label(top_window, text = "Spoiler: $" + str("%.2f" % aeroPrices.get("Spoiler")), bg='yellow', padx=20, pady=5).pack()
            if self.wingAeroCB.isChecked():
                Label(top_window, text = "Wing: $" + str("%.2f" % aeroPrices.get("Wing")), bg='yellow', padx=20, pady=5).pack()

            if self.bluePaintCB.isChecked():
                Label(top_window, text = "Blue Paint $" + str("%.2f" % paintPrices.get("Blue")), bg='yellow', padx=20, pady=5).pack()
            if self.greenPaintCB.isChecked():
                Label(top_window, text = "Green Paint $" + str("%.2f" % paintPrices.get("Green")), bg='yellow', padx=20, pady=5).pack()
            if self.pinkPaintCB.isChecked():
                Label(top_window, text = "Pink Paint $" + str("%.2f" % paintPrices.get("Pink")), bg='yellow', padx=20, pady=5).pack()
            if self.purplePaintCB.isChecked():
                Label(top_window, text = "Purple Paint $" + str("%.2f" % paintPrices.get("Purple")), bg='yellow', padx=20, pady=5).pack()
            if self.blackPaintCB.isChecked():
                Label(top_window, text = "Black Paint $" + str("%.2f" % paintPrices.get("Black")), bg='yellow', padx=20, pady=5).pack()
            if self.goldPaintCB.isChecked():
                Label(top_window, text = "Gold Paint $" + str("%.2f" % paintPrices.get("Gold")), bg='yellow', padx=20, pady=5).pack()
            if self.whitePaintCB.isChecked():
                Label(top_window, text = "White Paint $" + str("%.2f" % paintPrices.get("White")), bg='yellow', padx=20, pady=5).pack()

            if self.whiteBrakeCB.isChecked():
                Label(top_window, text = "White Brake $" + str("%.2f" % brakePrices.get("White")), bg='yellow', padx=20, pady=5).pack()
            if self.blueBrakeCB.isChecked():
                Label(top_window, text = "Blue Brake $" + str("%.2f" % brakePrices.get("Blue")), bg='yellow', padx=20, pady=5).pack()
            if self.blackBrakeCB.isChecked():
                Label(top_window, text = "Black Brake $" + str("%.2f" % brakePrices.get("Black")), bg='yellow', padx=20, pady=5).pack()
            if self.greyBrakeCB.isChecked():
                Label(top_window, text = "Grey Brake $" + str("%.2f" % brakePrices.get("Grey")), bg='yellow', padx=20, pady=5).pack()
            if self.redBrakeCB.isChecked():
                Label(top_window, text = "Red Brake $" + str("%.2f" % brakePrices.get("Red")), bg='yellow', padx=20, pady=5).pack()

            # Create a space and list the subtotal, tax, and total in the checkout window
            Label(top_window, text = "", bg='yellow', padx=20, pady=10).pack()
            Label(top_window, text = "Subtotal: $" + str("%.2f" % round(self.subtotal,2)), bg='yellow', padx=20, pady=5).pack()
            Label(top_window, text = "Tax (7%): $" + str("%.2f" % round(self.tax,2)), bg='yellow', padx=20, pady=5).pack()
            Label(top_window, text = "Total: $" + str("%.2f" % round(self.total,2)), bg='yellow', padx=20, pady=5).pack()
            
            # create a space and a close button to close the checkout window
            Label(top_window, text = "", bg='yellow', padx=20, pady=10).pack()
            closeButton = Button(top_window, text = "Close Window", font=("Arial", 12), bg="red", pady=10, command=top_window.destroy).pack()
            # closeButton.pack(top_window,side=BOTTOM, padx=20, pady=20)


        # Establish price lists for each selection option
        wheelPrices = {"Chrome":70.00, "Bronze":85.99, "Carbon Fiber":109.75, "Matte White":107.00}
        seatPrices = {"Regular": 100.00, "Racing": 100.00}
        aeroPrices = {"Spoiler": 53.75, "Wing": 70.00}
        paintPrices = {"Blue": 67.75, "Green": 37.70, "Pink": 40.15, "Purple": 61.00, "Black": 57.30, "Gold": 80.57, "White": 30.99}
        brakePrices = {"White": 64.00, "Blue": 64.00, "Black": 64.00, "Grey": 64.00, "Red": 64.00}
        
        # Set up the instance variables for subtotal, tax, and total
        subtotal = float(0.0)
        taxRate = float(0.07)
        tax = float(0.0)
        total = float(0.0)

        self.subtotal = subtotal
        self.tax = tax
        self.total = total

        
        # update totals
        def updateTotals():
            global subtotal, tax, total
            subtotal = 0.00
            tax = 0.00
            total = 0.00

            # sum the selected checkbox options
            if self.chromeWheelCB.isChecked():
                subtotal += wheelPrices.get("Chrome")
            if self.bronzeWheelCB.isChecked():
                subtotal += wheelPrices.get("Bronze")
            if self.carbonFiberWheelCB.isChecked():
                subtotal += wheelPrices.get("Carbon Fiber")
            if self.matteWhiteWheelCB.isChecked():
                subtotal += wheelPrices.get("Matte White")
                
            if self.regularSeatCB.isChecked():
                subtotal += seatPrices.get("Regular")
            if self.racingSeatCB.isChecked():
                subtotal += seatPrices.get("Racing")

            if self.spoilerAeroCB.isChecked():
                subtotal += aeroPrices.get("Spoiler")
            if self.wingAeroCB.isChecked():
                subtotal += aeroPrices.get("Wing")

            if self.bluePaintCB.isChecked():
                subtotal += paintPrices.get("Blue")
            if self.greenPaintCB.isChecked():
                subtotal += paintPrices.get("Green")
            if self.pinkPaintCB.isChecked():
                subtotal += paintPrices.get("Pink")
            if self.purplePaintCB.isChecked():
                subtotal += paintPrices.get("Purple")
            if self.blackPaintCB.isChecked():
                subtotal += paintPrices.get("Black")
            if self.goldPaintCB.isChecked():
                subtotal += paintPrices.get("Gold")
            if self.whitePaintCB.isChecked():
                subtotal += paintPrices.get("White")

            if self.whiteBrakeCB.isChecked():
                subtotal += brakePrices.get("White")
            if self.blueBrakeCB.isChecked():
                subtotal += brakePrices.get("Blue")
            if self.blackBrakeCB.isChecked():
                subtotal += brakePrices.get("Black")
            if self.greyBrakeCB.isChecked():
                subtotal += brakePrices.get("Grey")
            if self.redBrakeCB.isChecked():
                subtotal += brakePrices.get("Red")

            # Calculate tax and total
            tax = round(subtotal * taxRate, 2)
            total = round(subtotal + tax, 2)

            # Update the labels
            self.subtotal = subtotal
            self.subtotalField.setNumber(self.subtotal)
            self.tax = tax
            self.taxField.setNumber(self.tax)
            self.total = total
            self.totalField.setNumber(self.total)

        # Create option images as headers above each option category
        wheelimageLabel = self.addLabel(text = "custom wheel", row = 2, column = 0, sticky = "NSEW")
        self.wheelImage = PhotoImage(file="chromewheel.png")
        wheelimageLabel["image"] = self.wheelImage
        seatsimageLabel = self.addLabel(text = "custom seats", row = 2, column = 1, sticky = "NSEW")
        self.seatsImage = PhotoImage(file="racingseats.png")
        seatsimageLabel["image"] = self.seatsImage
        aeroimageLabel = self.addLabel(text = "custom aero", row = 2, column = 2, sticky = "NSEW")
        self.aeroImage = PhotoImage(file="spoiler.png")
        aeroimageLabel["image"] = self.aeroImage
        paintimageLabel = self.addLabel(text = "custom paint", row = 2, column = 3, sticky = "NSEW")
        self.paintImage = PhotoImage(file="carpaint.png")
        paintimageLabel["image"] = self.paintImage
        brakesimageLabel = self.addLabel(text = "custom brakes", row = 2, column = 4, sticky = "NSEW")
        self.brakesImage = PhotoImage(file="brakes.png")
        brakesimageLabel["image"] = self.brakesImage

        # set up labels and fields for the selections window.j
        self.addLabel(text = "Wheel Options", font=12, row = 3, column = 0)
        self.addLabel(text = "Seat Options", font=12, row = 3, column = 1)
        self.addLabel(text = "Aero Options", font=12, row = 3, column = 2)
        self.addLabel(text = "Paint Options", font=12, row = 3, column = 3)
        self.addLabel(text = "Brake Options", font=12, row = 3, column = 4)

        # add wheel selection checkboxes
        self.chromeWheelCB = self.addCheckbutton(text = "Chrome: $" + str("%.2f" % wheelPrices.get("Chrome")), row = 4, column = 0, sticky="W", command=updateTotals)
        self.bronzeWheelCB = self.addCheckbutton(text = "Bronze: $" + str("%.2f" % wheelPrices.get("Bronze")), row = 5, column = 0, sticky="W", command=updateTotals)
        self.carbonFiberWheelCB = self.addCheckbutton(text = "Carbon Fiber: $" + str("%.2f" % wheelPrices.get("Carbon Fiber")), row = 6, column = 0, sticky="W", command=updateTotals)
        self.matteWhiteWheelCB = self.addCheckbutton(text = "Matte White: $" + str("%.2f" % wheelPrices.get("Matte White")), row = 7, column = 0, sticky="W", command=updateTotals)

        # add seat selection checkboxes
        self.regularSeatCB = self.addCheckbutton(text = "Regular: $" + str("%.2f" % seatPrices.get("Regular")), row = 4, column = 1, sticky="W", command=updateTotals)
        self.racingSeatCB = self.addCheckbutton(text = "Racing: $" + str("%.2f" % seatPrices.get("Racing")), row = 5, column = 1, sticky="W", command=updateTotals)

        # add Aerodynamic selection checkboxes
        self.spoilerAeroCB = self.addCheckbutton(text = "Spoiler: $" + str("%.2f" % aeroPrices.get("Spoiler")), row = 4, column = 2, sticky="W", command=updateTotals)
        self.wingAeroCB = self.addCheckbutton(text = "Wing: $" + str("%.2f" % aeroPrices.get("Wing")), row = 5, column = 2, sticky="W", command=updateTotals)

        # add Paint selection checkboxes
        self.bluePaintCB = self.addCheckbutton(text = "Blue: $" + str("%.2f" % paintPrices.get("Blue")), row = 4, column = 3, sticky="W", command=updateTotals)
        self.greenPaintCB = self.addCheckbutton(text = "Green: $" + str("%.2f" % paintPrices.get("Green")), row = 5, column = 3, sticky="W", command=updateTotals)
        self.pinkPaintCB = self.addCheckbutton(text = "Pink: $" + str("%.2f" % paintPrices.get("Pink")), row = 6, column = 3, sticky="W", command=updateTotals)
        self.purplePaintCB = self.addCheckbutton(text = "Purple: $" + str("%.2f" % paintPrices.get("Purple")), row = 7, column = 3, sticky="W", command=updateTotals)
        self.blackPaintCB = self.addCheckbutton(text = "Black: $" + str("%.2f" % paintPrices.get("Black")), row = 8, column = 3, sticky="W", command=updateTotals)
        self.goldPaintCB = self.addCheckbutton(text = "Gold: $" + str("%.2f" % paintPrices.get("Gold")), row = 9, column = 3, sticky="W", command=updateTotals)
        self.whitePaintCB = self.addCheckbutton(text = "white: $" + str("%.2f" % paintPrices.get("White")), row = 10, column = 3, sticky="W", command=updateTotals)

        # add brake caliper color selection checkboxes
        self.whiteBrakeCB = self.addCheckbutton(text = "White: $" + str("%.2f" % brakePrices.get("White")), row = 4, column = 4, sticky="W", command=updateTotals)
        self.blueBrakeCB = self.addCheckbutton(text = "Blue: $" + str("%.2f" % brakePrices.get("Blue")), row = 5, column = 4, sticky="W", command=updateTotals)
        self.blackBrakeCB = self.addCheckbutton(text = "Black: $" + str("%.2f" % brakePrices.get("Black")), row = 6, column = 4, sticky="W", command=updateTotals)
        self.greyBrakeCB = self.addCheckbutton(text = "Grey: $" + str("%.2f" % brakePrices.get("Grey")), row = 7, column = 4, sticky="W", command=updateTotals)
        self.redBrakeCB = self.addCheckbutton(text = "Red: $" + str("%.2f" % brakePrices.get("Red")), row = 8, column = 4, sticky="W", command=updateTotals)

        # add labels for subtotal, tax, and total
        self.addLabel(text = "Subtotal: ", row = 11, column = 1)
        self.subtotalField = self.addFloatField(value = subtotal, row = 11, column = 2, precision=2, state="readonly")
        self.addLabel(text = "Tax (7%): ", row = 12, column = 1)
        self.taxField = self.addFloatField(value = tax, row = 12, column = 2, precision=2, state="readonly")
        self.addLabel(text = "Total: ", row = 13, column = 1)
        self.totalField = self.addFloatField(value = total, row = 13, column = 2, precision=2, state="readonly")

        # create a nested, contrasting background panel for buttons
        buttonPanel = self.addPanel(row = 14, column = 0, columnspan=5, background = "black")
        
        # add buttons to start over, check out, or exit
        buttonPanel.addButton (text = "Check Out", row = 0, column = 1, command=checkout_window)
        buttonPanel.addButton (text = "Exit", row = 0, column = 3, command=quit)

CarCustomization().mainloop()