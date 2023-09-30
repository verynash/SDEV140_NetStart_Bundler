from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("NetStart Bundler")
root.geometry("600x600")

def fullPackageEstimate(num_lines, high_speed, hotspot, internet, cable):
    price = 155
    price += ((num_lines - 1) * 15)
    if high_speed == 1:
        price += (num_lines * 10)
    if hotspot == 1:
        price += 25
    if internet == "Advanced":
        price += 15
    if internet == "Premium":
        price += 30
    if cable == "Advanced":
        price += 30
    messagebox.showinfo("Estimate", "Your package is estimated at $" + str(price) + "/month.")

def phoneInternetEstimate(num_lines, high_speed, hotspot, internet):
    price = 110
    price += ((num_lines - 1) * 15)
    if high_speed == 1:
        price += (num_lines * 10)
    if hotspot == 1:
        price += 25
    if internet == "Advanced":
        price += 15
    if internet == "Premium":
        price += 30
    messagebox.showinfo("Estimate", "Your package is estimated at $" + str(price) + "/month.")

def phoneCableEstimate(num_lines, high_speed, hotspot, cable):
    price = 115
    price += ((num_lines - 1) * 15)
    if high_speed == 1:
        price += (num_lines * 10)
    if hotspot == 1:
        price += 25
    if cable == "Advanced":
        price += 30
    messagebox.showinfo("Estimate", "Your package is estimated at $" + str(price) + "/month.")

def internetCableEstimate(internet, cable):
    price = 85
    if internet == "Advanced":
        price += 15
    if internet == "Premium":
        price += 30
    if cable == "Advanced":
        price += 30
    messagebox.showinfo("Estimate", "Your package is estimated at $" + str(price) + "/month.")

def familyPhonePlanEstimate(num_lines, high_speed, hotspot):
    price = 70
    price += ((num_lines - 1) * 15)
    if high_speed == 1:
        price += (num_lines * 10)
    if hotspot == 1:
        price += 25
    messagebox.showinfo("Estimate", "Your package is estimated at $" + str(price) + "/month.")

def internetEstimate(internet):
    price = 40
    if internet == "Advanced":
        price += 15
    if internet == "Premium":
        price += 30
    messagebox.showinfo("Estimate", "Your package is estimated at $" + str(price) + "/month.")

def cableEstimate(cable):
    price = 45
    if cable == "Advanced":
        price += 30
    messagebox.showinfo("Estimate", "Your package is estimated at $" + str(price) + "/month.")

def phoneOptions():
    phone_frame = LabelFrame(top, text="Cellular Options - $70", padx=10, pady=10)
    phone_frame.pack()

    options = [1,2,3,4,5]
    global num_lines
    num_lines = IntVar()
    num_lines.set(options[0])

    global high_speed
    high_speed = IntVar()
    global hotspot
    hotspot = IntVar()

    line_lbl = Label(phone_frame, text="Number of Lines")
    high_speed_lbl = Label(phone_frame, text="High Speed")
    hotspot_lbl = Label(phone_frame, text="HotSpot")
    price1_lbl = Label(phone_frame, text="+ $15/addt. line")
    price2_lbl = Label(phone_frame, text="+ $10/line")
    price3_lbl = Label(phone_frame, text="+ $25")
    drop = OptionMenu(phone_frame, num_lines, *options)
    speed_check = Checkbutton(phone_frame, variable=high_speed)
    speed_check.deselect()
    hotspot_check = Checkbutton(phone_frame, variable=hotspot)
    hotspot_check.deselect()

    line_lbl.grid(row=0, column=0)
    high_speed_lbl.grid(row=1, column=0)
    hotspot_lbl.grid(row=2, column=0)
    price1_lbl.grid(row=0, column=1)
    price2_lbl.grid(row=1, column=1)
    price3_lbl.grid(row=2, column=1)
    drop.grid(row=0, column=2)
    speed_check.grid(row=1, column=2)
    hotspot_check.grid(row=2, column=2)

def internetOptions():
    internet_frame = LabelFrame(top, text="Internet Options - $40", padx=10, pady=10)
    internet_frame.pack()
    
    global internet_package
    internet_package = StringVar()
    internet_package.set("Basic")

    basic_lbl = Label(internet_frame, text="Basic")
    advanced_lbl = Label(internet_frame, text="Advanced")
    premium_lbl = Label(internet_frame, text="Premium")
    i_price1_lbl = Label(internet_frame, text="+ $15")
    i_price2_lbl = Label(internet_frame, text="+ $30")
    basic_radio = Radiobutton(internet_frame, variable=internet_package, value="Basic")
    advanced_radio = Radiobutton(internet_frame, variable=internet_package, value="Advanced")
    premium_radio = Radiobutton(internet_frame, variable=internet_package, value="Premium")

    basic_lbl.grid(row=0, column=0)
    advanced_lbl.grid(row=1, column=0)
    premium_lbl.grid(row=2, column=0)
    i_price1_lbl.grid(row=1, column=1)
    i_price2_lbl.grid(row=2, column=1)
    basic_radio.grid(row=0, column=2)
    advanced_radio.grid(row=1, column=2)
    premium_radio.grid(row=2, column=2)
    
def cableOptions():
    cable_frame = LabelFrame(top, text="Cable Options - $45", padx=10, pady=10)
    cable_frame.pack()

    global cable_package
    cable_package = StringVar()
    cable_package.set("Basic")

    c_basic_lbl = Label(cable_frame, text="Basic")
    c_advanced_lbl = Label(cable_frame, text="Advanced")
    c_price_lbl = Label(cable_frame, text="+ $30")
    c_basic_radio = Radiobutton(cable_frame, variable=cable_package, value="Basic")
    c_advanced_radio = Radiobutton(cable_frame, variable=cable_package, value="Advanced")
    
    c_basic_lbl.grid(row=0, column=0)
    c_advanced_lbl.grid(row=1, column=0)
    c_price_lbl.grid(row=1, column=1)
    c_basic_radio.grid(row=0, column=2)
    c_advanced_radio.grid(row=1, column=2)

def fullPackageWindow():
    phoneOptions()
    internetOptions()
    cableOptions()

    b = Button(top, text="Submit for Estimate", command=lambda: fullPackageEstimate(num_lines.get(), 
                                                                                      high_speed.get(), 
                                                                                      hotspot.get(), 
                                                                                      internet_package.get(), 
                                                                                      cable_package.get()))
    b.pack()

def phoneInternetWindow():
    phoneOptions()
    internetOptions()

    b = Button(top, text="Submit for Estimate", command=lambda: phoneInternetEstimate(num_lines.get(), 
                                                                                      high_speed.get(), 
                                                                                      hotspot.get(), 
                                                                                      internet_package.get()))
    b.pack()

def familyPhonePlanWindow():
    phoneOptions()

    b = Button(top, text="Submit for Estimate", command=lambda: familyPhonePlanEstimate(num_lines.get(), 
                                                                                      high_speed.get(), 
                                                                                      hotspot.get()))
    b.pack()

def openBundleWindow(bundle):
    bundle_proceed_button["state"] = "disabled"
    alternate_button["state"] = "disabled"
    bundle_reset_button["state"] = "normal"
    global top
    top = Toplevel()
    top.title(bundle)
    lbl = Label(top, text="Customize your package").pack()
    if bundle == "Full Package":
        fullPackageWindow()
        top.geometry("400x380")
    elif bundle == "Phone & Internet":
        phoneInternetWindow()
        top.geometry("400x290")
    else:
        familyPhonePlanWindow()   
        top.geometry("400x175")

def displayCustomServiceOptions(phone_service, internet_service, cable_service):
    window.destroy()
    global top
    top = Toplevel()
    top.title("Custom Package")
    if phone_service == 1:
        phoneOptions()
    if internet_service == 1:
        internetOptions()
    if cable_service == 1:
        cableOptions()

    if phone_service == 1 and internet_service == 1 and cable_service == 1:
        b = Button(top, text="Submit for Estimate", command=lambda: fullPackageEstimate(num_lines.get(), 
                                                                                        high_speed.get(), 
                                                                                        hotspot.get(), 
                                                                                        internet_package.get(), 
                                                                                        cable_package.get()))
        b.pack()
    elif phone_service == 1 and internet_service == 1:
        b = Button(top, text="Submit for Estimate", command=lambda: phoneInternetEstimate(num_lines.get(), 
                                                                                      high_speed.get(), 
                                                                                      hotspot.get(), 
                                                                                      internet_package.get()))
        b.pack()
    elif phone_service == 1 and cable_service == 1:
        b = Button(top, text="Submit for Estimate", command=lambda: phoneCableEstimate(num_lines.get(), 
                                                                                      high_speed.get(), 
                                                                                      hotspot.get(), 
                                                                                      cable_package.get()))
        b.pack()
    elif internet_service == 1 and cable_service == 1:
        b = Button(top, text="Submit for Estimate", command=lambda: internetCableEstimate(internet_package.get(), 
                                                                                      cable_package.get()))
        b.pack()
    elif phone_service == 1:
        b = Button(top, text="Submit for Estimate", command=lambda: familyPhonePlanEstimate(num_lines.get(), 
                                                                                      high_speed.get(), 
                                                                                      hotspot.get()))
        b.pack()
    elif internet_service == 1:
        b = Button(top, text="Submit for Estimate", command=lambda: internetEstimate(internet_package.get()))
        b.pack()
    else:
        b = Button(top, text="Submit for Estimate", command=lambda: cableEstimate(cable_package.get()))
        b.pack()
        
def pickServiceCustomOptions():
    picker_frame = LabelFrame(window, padx=25, pady=25)
    picker_frame.pack()

    phone_service = IntVar()
    internet_service = IntVar()
    cable_service = IntVar()

    phone_check = Checkbutton(picker_frame, text="Phone", variable=phone_service)
    internet_check = Checkbutton(picker_frame, text="Internet", variable=internet_service)
    cable_check = Checkbutton(picker_frame, text="Cable", variable=cable_service)

    phone_check.pack()
    internet_check.pack()
    cable_check.pack()    

    service_button = Button(window, text="Proceed", command=lambda: displayCustomServiceOptions(phone_service.get(), 
                                                                                                      internet_service.get(),
                                                                                                      cable_service.get()))
    service_button.pack()

def openCustomizeWindow():
    bundle_proceed_button["state"] = "disabled"
    alternate_button["state"] = "disabled"
    bundle_reset_button["state"] = "normal"
    global window
    window = Toplevel()
    window.title("Custom Package")
    window.geometry("200x225")
    lbl = Label(window, text="What services would you like?", pady=10).pack()
    pickServiceCustomOptions()
    
def reset():
    top.destroy()
    bundle_proceed_button["state"] = "normal"
    alternate_button["state"] = "normal"
    bundle_reset_button["state"] = "disabled"

header_label = Label(root, text="~NetStart Bundler~")
header_label.pack()

bundle_frame = LabelFrame(root, text="Bundle Deals!", padx=25, pady=25)
bundle_frame.pack()

bundle_header_lbl = Label(bundle_frame, text="Select your package and press 'Proceed' to continue.")
bundle_lbl_1 = Label(bundle_frame, text="Phone, Internet, and Cable")
bundle_lbl_2 = Label(bundle_frame, text="Phone and Internet")
bundle_lbl_3 = Label(bundle_frame, text="Family Phone Plan")

bundle_header_lbl.grid(row=0,column=0, pady=10)
bundle_lbl_1.grid(row=1, column=0, sticky=W, columnspan=2, pady=25)
bundle_lbl_2.grid(row=2, column=0, sticky=W, columnspan=2, pady=25)
bundle_lbl_3.grid(row=3, column=0, sticky=W, columnspan=2, pady=25)

bundle = StringVar()
bundle.set("Full Package")

PLANS = [
    ("Full Package","Full Package",1),
    ("Phone & Internet","Phone & Internet",2),
    ("Family Phone Plan","Family Phone Plan",3)
]

for text, plan, position in PLANS:
    Radiobutton(bundle_frame, variable=bundle, value=plan).grid(row=position, column=2, padx=25)

bundle_reset_button = Button(bundle_frame, text="Reset", command=reset, state="disabled")
bundle_proceed_button = Button(bundle_frame, text="Proceed", command=lambda: openBundleWindow(bundle.get()))
bundle_reset_button.grid(row=4, column=0)
bundle_proceed_button.grid(row=4, column=2)


alternate_frame = LabelFrame(root, text="Alternate Option", padx=25, pady=25)
alternate_frame.pack()

alternate_label = Label(alternate_frame, text="Click below to customize your own package!")
alternate_button = Button(alternate_frame, text="Customize", command=openCustomizeWindow)
alternate_label.grid(row=0, column=0, padx=33, pady=10)
alternate_button.grid(row=1, column=0, pady=10)


exit_lbl = Label(root, text="Click below to quit", pady=10)
exit_button = Button(root, text="Exit", command=root.quit)
exit_lbl.pack()
exit_button.pack()

root.mainloop()