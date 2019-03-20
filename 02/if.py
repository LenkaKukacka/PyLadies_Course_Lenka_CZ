print("A ted zkus nejake desetinne...")

page = float(input("Strana ctverce je (zadej desetinne cislo):"))
numbercheck = page >= 0
if numbercheck:
       print("Obvod čtverce se stranou" , page , "je" , page*4 , "cm")
       print("Obsah čtverce se stranou" , page , "je" , page*page , "cm2")

else:
    print ("Haha ... Cislo musi byt kladne :D")
