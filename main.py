import tkinter as tk
from draw import Gasket

#window = tk.Tk()
#draw_button = tk.Button(window, text="Draw", command=Gasket(sku="001050", outside_diameter=883, inside_diameter=765, holes=32, hole_diameter=27, pcd=835))
gasket = Gasket(sku="000606", outside_diameter=270, inside_diameter=200, holes=6, hole_diameter=12, pcd=240, colour="grey")
gasket.draw()

#keep the window open if required
tk.mainloop()
