aw = input("je wekker gaat af wat doe opstaan of liggen? ")
aw1 = False
aw2 = False
aw3 = False
aw4 = False
aw5 = False
aw6 = False
aw7 = False

if aw == "opstaan" :
    print("je staat op en gaat eten")
    aw1 = True
elif aw == "liggen" :
    print("je moeder word boos op je dat je niet optijd opstaat en schreeuwt je wakker jij gaat maar naar beneden")
    aw2 = True
else:
    print("geen geldige keuze")

if aw1 == True : 
    aw = input("je staat in de keuken en weet niet wat je wilt eten je kan kiezen uit brood of cornflakes jij kiest?: ")

    if aw == "brood" :
        print("je pakt je brood en gaat smeren")
        aw3 = True
    elif aw ==  "cornflakes" :
        print("je pakt een bakje en je gaat je cornfalkes maken")
        aw4 = True
    else:
        print("geen geldige keuze")

if aw2 == True : 
    aw = input("je stampt boos naar beneden en je gaat eten maken je kan kiezen uit brood of cornflakes jij kiest?: ")

    if aw == "brood" :
        print("je pakt je brood en gaat smeren")
        aw3 = True
    elif aw ==  "cornflakes" :
        print("je pakt een bakje en je gaat je cornfalkes maken")
        aw4 = True
    else:
        print("geen geldige keuze")

if aw3 == True :
    aw = input("je weet niet of je pindakaas of chocopasta wilt jij kiest?: ")

    if aw == "pindakaas": 
        print("je laat de pot flikkeren omdat je te moe bent")
        aw5 = True
    elif aw == "chocopasta":
        print("je laat de pot flikkeren omdat je te moe bent")
        aw5 = True
    else:
        print("geen geldige keuze")

if aw4 == True :
    aw = input("bij je cornflakes doe je melk of water jij kiest: ")

    if aw == "water": 
        print("jij kiest water omdat je te moe bent om na te denken en je dom bent GAME OVER")
    elif aw == "melk":
        print("je laat het bakje met melk flikkeren")
        aw6 = True
    else:
        print("geen geldige keuze")
if aw5 == True :
    aw = input("je bent boos op je zelf dat je het laat flikeren jij kan het laten liggen of opruimen jij kiest: ")

    if aw == "liggen": 
        print("je laat het liggen voor je moeder daar zal ze niet blij mee zijn maar je gaat naar school voordat ze iets kan zeggen")
        aw7 = True
    elif aw == "opruimen":
        print("je ruimt het op en je gaat gehaast naar school")
        aw7 = True
    else:
        ("geen geldige keuze")

if aw7 == True:
    aw = input("je sprint de deur uit en je moet kiezen uit de bus of fiets jij kiest: ")

    if aw == "bus":
        print("jij sprint naar het bus hokje maar de bus heeft vertraging dus je komt te laat")
    elif aw == "fiets":
        print("jij pakt je fiets en je fietst o hard mogelijk en je komt nog net uitgeput de les in maar je bent optijd")
    else:
        ("geen geldige keuze")


print("einde verhaal")



