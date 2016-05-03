Colour_Names = {"AliceBlue":"#f0f8ff", "BlanchedAlmond":"ffebcd", "BlueViolet":"#8a2be2", "CornflowerBlue":"#6495ed", "DarkGreen":"#006400", "DarkKhaki":"#bdb76b", "DarkSalmon":"#e9967a", "DarkTurquoise":"#00ced1", "DarkViolet":"9400d3", "DimGray":"#696969"}

colourName = input("Enter name of colour: ")

while len(colourName) != 0:
    if colourName in Colour_Names:
        print("Colour code is", Colour_Names[colourName])
    else:
        print("Invalid colour name. Try again.")
    colourName = input("Enter name of colour: ")
