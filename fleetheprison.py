print("Hej du ska försöka fly från fängelset,du är i din cell och du börjar tänka hur man kan fly från galret.")
prisoncell={
    "Stage1": False,
    "Stage2": False,
    "Stage3": False
    
}
if prisoncell("Stage1"):
    print("Du planerar hur man kan fly från din cell, du ser en vakt som tappat sin nyckel")
elif prisoncell("Stage1"):
    print("Du tar vaktens nyckel och smyger ut från din cell, sedan du hittar lunchrummet välkommen till stage2")
else: 
    prisoncell("Stage1")
    print("du väljer inte nyckeln och sitter fast hela ditt livstid!")
