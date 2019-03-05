from tkinter import *

def colourswitch(window, colourbutton):
    global colour
    colour = colourbutton["bg"]
    window.destroy()

def colourselect():
    window = Tk()
    window.title("Select Colour")
    window.grid()

    colourslist = ['snow', 'ghostwhite', 'whitesmoke', 'gainsboro', 'floralwhite', 'oldlace', 'linen', 'antiquewhite', 'papayawhip', 'blanchedalmond', 'bisque', 'peachpuff', 'navajowhite', 'lemonchiffon', 'mintcream', 'azure', 'aliceblue', 'lavender', 'lavenderblush', 'mistyrose', 'darkslategray', 'dimgray', 'slategray', 'lightslategray', 'gray', 'lightgrey', 'midnightblue', 'navy', 'cornflowerblue', 'darkslateblue', 'slateblue', 'mediumslateblue', 'lightslateblue', 'mediumblue', 'royalblue', 'blue', 'dodgerblue', 'deepskyblue', 'skyblue', 'lightskyblue', 'steelblue', 'lightsteelblue', 'lightblue', 'powderblue', 'paleturquoise', 'darkturquoise', 'mediumturquoise', 'turquoise', 'cyan', 'lightcyan', 'cadetblue', 'mediumaquamarine', 'aquamarine', 'darkgreen', 'darkolivegreen', 'darkseagreen', 'seagreen', 'mediumseagreen', 'lightseagreen', 'palegreen', 'springgreen', 'lawngreen', 'mediumspringgreen', 'greenyellow', 'limegreen', 'yellowgreen', 'forestgreen', 'olivedrab', 'darkkhaki', 'khaki', 'palegoldenrod', 'lightgoldenrodyellow', 'lightyellow', 'yellow', 'gold', 'lightgoldenrod', 'goldenrod', 'darkgoldenrod', 'rosybrown', 'indianred', 'saddlebrown', 'sandybrown', 'darksalmon', 'salmon', 'lightsalmon', 'orange', 'darkorange', 'coral', 'lightcoral', 'tomato', 'orangered', 'red', 'hotpink', 'deeppink', 'pink', 'lightpink', 'palevioletred', 'maroon', 'mediumvioletred', 'violetred', 'mediumorchid', 'darkorchid', 'darkviolet', 'blueviolet', 'purple', 'mediumpurple', 'thistle', 'snow2', 'snow3', 'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2', 'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2', 'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4', 'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3', 'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4', 'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3', 'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3', 'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4', 'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2', 'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4', 'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2', 'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3', 'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3', 'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2', 'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3', 'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3', 'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4', 'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3', 'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2', 'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4', 'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4', 'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2', 'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4', 'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4', 'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4', 'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4', 'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4', 'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2', 'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1', 'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1', 'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2', 'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2', 'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2', 'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4', 'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2', 'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4', 'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4', 'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1', 'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2', 'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4', 'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1', 'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3', 'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4', 'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2', 'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4', 'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10', 'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19', 'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28', 'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37', 'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47', 'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56', 'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65', 'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74', 'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83', 'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92', 'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']

    colourbutton = list()
    rowvar = 0
    
    for i in range(len(colourslist)):
        temp = i + 1
        colourbutton.append("")
        colourbutton[i] = Button(window, bg = colourslist[i], height = 1, width = 2, command = lambda i=i: colourswitch(window, colourbutton[i]))
        colourbutton[i].grid(row = rowvar, column = temp - 37 * rowvar)
        if temp % 37 == 0:
            rowvar = rowvar + 1

def onclick(self):
    global colour
    if self["bg"] == colour:
        self["bg"] = "ghostwhite"
    else:
        self["bg"] = colour

def Open(root2):
    openwindow = Tk()
    openwindow.title("Open")
    openwindow.grid()

    inputlabel = Label(openwindow, text = "Name of file:").grid(row = 1, column = 1)
    nameinput = Entry(openwindow)
    nameinput.grid(row = 1, column = 2)

    confirmbutton = Button(openwindow, text = "Open", command = lambda: openfile(nameinput, root2, openwindow))
    confirmbutton.grid(row = 2, column = 2)

def openfile(nameinput, root2, openwindow):
    colourslist = ['snow', 'ghostwhite', 'whitesmoke', 'gainsboro', 'floralwhite', 'oldlace', 'linen', 'antiquewhite', 'papayawhip', 'blanchedalmond', 'bisque', 'peachpuff', 'navajowhite', 'lemonchiffon', 'mintcream', 'azure', 'aliceblue', 'lavender', 'lavenderblush', 'mistyrose', 'darkslategray', 'dimgray', 'slategray', 'lightslategray', 'gray', 'lightgrey', 'midnightblue', 'navy', 'cornflowerblue', 'darkslateblue', 'slateblue', 'mediumslateblue', 'lightslateblue', 'mediumblue', 'royalblue', 'blue', 'dodgerblue', 'deepskyblue', 'skyblue', 'lightskyblue', 'steelblue', 'lightsteelblue', 'lightblue', 'powderblue', 'paleturquoise', 'darkturquoise', 'mediumturquoise', 'turquoise', 'cyan', 'lightcyan', 'cadetblue', 'mediumaquamarine', 'aquamarine', 'darkgreen', 'darkolivegreen', 'darkseagreen', 'seagreen', 'mediumseagreen', 'lightseagreen', 'palegreen', 'springgreen', 'lawngreen', 'mediumspringgreen', 'greenyellow', 'limegreen', 'yellowgreen', 'forestgreen', 'olivedrab', 'darkkhaki', 'khaki', 'palegoldenrod', 'lightgoldenrodyellow', 'lightyellow', 'yellow', 'gold', 'lightgoldenrod', 'goldenrod', 'darkgoldenrod', 'rosybrown', 'indianred', 'saddlebrown', 'sandybrown', 'darksalmon', 'salmon', 'lightsalmon', 'orange', 'darkorange', 'coral', 'lightcoral', 'tomato', 'orangered', 'red', 'hotpink', 'deeppink', 'pink', 'lightpink', 'palevioletred', 'maroon', 'mediumvioletred', 'violetred', 'mediumorchid', 'darkorchid', 'darkviolet', 'blueviolet', 'purple', 'mediumpurple', 'thistle', 'snow2', 'snow3', 'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2', 'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2', 'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4', 'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3', 'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4', 'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3', 'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3', 'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4', 'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2', 'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4', 'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2', 'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3', 'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3', 'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2', 'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3', 'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3', 'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4', 'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3', 'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2', 'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4', 'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4', 'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2', 'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4', 'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4', 'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4', 'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4', 'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4', 'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2', 'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1', 'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1', 'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2', 'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2', 'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2', 'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4', 'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2', 'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4', 'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4', 'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1', 'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2', 'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4', 'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1', 'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3', 'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4', 'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2', 'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4', 'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10', 'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19', 'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28', 'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37', 'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47', 'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56', 'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65', 'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74', 'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83', 'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92', 'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']
    try:
        filetoread = open(nameinput.get() + ".txt", "r")
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found! Please enter the name of a compatible text file")

    else:
        contents = filetoread.read()
        contents = contents.split()
        filetoread.close()
        verf = "Y"
        if len(contents) >= 2:
        
            if contents[0].isdigit() and contents[1].isdigit(): #This part of the program verifies that the file is compatible
                for i in range(len(contents) - 2):
                    
                    if i % 2 == 0:
                        if contents[i + 2].isdigit():
                            pass
                        else:
                            verf = "N"

                    else:
                        inlist = "N"
                        for x in range(len(colourslist)):
                            if contents[i + 2] == colourslist[x]:
                                inlist = "Y"

                        if inlist == "N":
                            verf = "N"
                            
            else:
                verf = "N"


        else:
            verf = "N"

        if verf == "N":
            messagebox.showerror("Invalid Format", "File is formatted incorrectly and cannot be opened")

        else:
            newfile = "N"
            height = int(contents[0])
            width = int(contents[1])
            buildgrid(height, width, newfile, contents, openwindow, root2)

def saveas(buttonslist, height, width):
    savewindow = Tk()
    savewindow.title("Save As")
    savewindow.grid()

    inputlabel = Label(savewindow, text = "Name of new file:").grid(row = 1, column = 1)
    nameinput = Entry(savewindow)
    nameinput.grid(row = 1, column = 2)

    confirmbutton = Button(savewindow, text = "Save as", command = lambda: createfile(buttonslist, nameinput, height, width, savewindow))
    confirmbutton.grid(row = 2, column = 2)

    savewindow.mainloop()

def createfile(buttonslist, nameinput, height, width, savewindow):
    Clear = open(nameinput.get() + ".txt", "w")
    Clear.close()

    append = open(nameinput.get() + ".txt", "a+")
    append.write(height + " " + width)

    appendarray = list()
    for i in range(len(buttonslist)):
        for x in range(len(buttonslist[i])):
            appendarray.append(buttonslist[i][x]["bg"])

    completed = "N"
    repeated = 1
    finalappendarray = list()
    for i in range(len(appendarray) - 1):
        if appendarray[i] == appendarray[i + 1]:
            repeated = repeated + 1
        else:
            finalappendarray.append(repeated)
            finalappendarray.append(appendarray[i])
            repeated = 1

    finalappendarray.append(repeated)
    finalappendarray.append(appendarray[i + 1])

    for i in range(len(finalappendarray)):
        append.write(" " + str(finalappendarray[i]))
        
    append.close()
    savewindow.destroy()

def buildgrid(height, width, newfile, contents, openwindow, root2):
    global colour
    colour = "gray1"

    decompressedcontents = list()

    if newfile == "N":
        for i in range(len(contents) - 2):
            if contents[i + 2].isdigit():
                for x in range(int(contents[i + 2])):
                   decompressedcontents.append(contents[i + 3])
    
    root = Tk()
    root.title("Canvas")
    root.grid()

    menu = Menu(root)
    root.config(menu = menu)
    filemenu = Menu(menu) #This part creates the menu
    menu.add_cascade(label = "File", menu = filemenu)
    
    filemenu.add_command(label = "Open", command = lambda: Open(root))
    filemenu.add_command(label = "New", command = lambda: setup())
    filemenu.add_command(label = "Save As", command = lambda: saveas(buttonslist, height, width))

    buttonslist = list()

    cleanser = Frame(root)
    
    for i in range(int(height)):
        buttonslist.append([])
        
        for x in range(int(width)):
            buttonslist[i].append("")
            buttonslist[i][x] = Button(cleanser, bg = "ghostwhite",width = 2, height = 1, command = lambda i=i, x=x: onclick(buttonslist[i][x]))
            if newfile == "N":
                temp = i * width
                temp = temp + x
                
                buttonslist[i][x]["bg"] = decompressedcontents[temp]
            buttonslist[i][x].grid(row = i, column = x)

    cleanser.grid(row = 1, column = 1)

    placeholderlabel = Label(root, text = "").grid(row = 2)
    
    ColourButton = Button(root, text = "Change Colour", command = lambda: colourselect()).grid(row = 3, column = 1, sticky = "W")

    if newfile == "N":
        openwindow.destroy()

    if root2 != 0:
        root2.destroy()

def verification(heightentry, widthentry, setupwindow):
    width = widthentry.get()
    height = heightentry.get()
    newfile = "Y"
    openwindow = 0
    root2 = 0
    contents = list()
    
    if width.isdigit() and height.isdigit():
        if int(width) <= 80 and int(height) <= 35 and int(width) >= 2 and int(height) >= 2:
            setupwindow.destroy()
            buildgrid(height, width, newfile, contents, openwindow, root2)

        else:
            messagebox.showerror("Invalid", "Width must be between 2 and 80 and height must be between 2 and 35")

    else:
        messagebox.showerror("Invalid", "Width and Height must be integers!")


def setup():
    setupwindow = Tk()
    setupwindow.title("Setup")
    setupwindow.grid()

    menu = Menu(setupwindow)
    setupwindow.config(menu = menu)
    filemenu = Menu(menu) #This part creates the menu
    menu.add_cascade(label = "File", menu = filemenu)
    
    filemenu.add_command(label = "Open", command = lambda: Open(setupwindow))
    
    heightlabel = Label(setupwindow, text = "       Height:       ").grid(row = 1, column = 1)
    heightentry = Entry(setupwindow)
    heightentry.grid(row = 1, column = 2)

    widthlabel = Label(setupwindow, text = "       Width:       ").grid(row = 2, column = 1)
    widthentry = Entry(setupwindow)
    widthentry.grid(row = 2, column = 2)

    nextbutton = Button(setupwindow, text = "Continue", command = lambda: verification(heightentry, widthentry, setupwindow)).grid(row = 4, column = 2)

    setupwindow.mainloop()

if __name__ == "__main__":
    setup()
    quit()
