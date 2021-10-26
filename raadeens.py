import random, shortcuts

loop = True
kansen = 0
keerGespeeld = 0

def randomInt():
    rando = random.randint(0, 1000)
    return rando

print('''

,---.      .--.     .--.    ,'|"\      .-. .-.  ,---.    _______     ,--,    ,---.    _______   .--.   ,-.     
| .-.\    / /\ \   / /\ \   | |\ \     | | | |  | .-'   |__   __|  .' .'     | .-'   |__   __| / /\ \  | |     
| `-'/   / /__\ \ / /__\ \  | | \ \    | `-' |  | `-.     )| |     |  |  __  | `-.     )| |   / /__\ \ | |     
|   (    |  __  | |  __  |  | |  \ \   | .-. |  | .-'    (_) |     \  \ ( _) | .-'    (_) |   |  __  | | |     
| |\ \   | |  |)| | |  |)|  /(|`-' /   | | |)|  |  `--.    | |      \  `-) ) |  `--.    | |   | |  |)| | `--.  
|_| \)\  |_|  (_) |_|  (_) (__)`--'    /(  (_)  /( __.'    `-'      )\____/  /( __.'    `-'   |_|  (_) |( __.' 
    (__)                              (__)     (__)                (__)     (__)                       (_)     

''')

shortcuts.print_slow('Laden.........')
shortcuts.clearScreen(7.5)

score = 0
shortcuts.print_slow('Welkom bij raad het getal!\n')
shortcuts.clearScreen(5)
shortcuts.print_slow('Bij dit spel is het de bedoeling dat jij het getal raad wat het programma in gedachten heeft, succes!')
shortcuts.clearScreen(5)
guessed = 0

while  True:
    guessed += 1
    rando = randomInt()
    shortcuts.print_slow('Kies een willekeurig getal tussen de 0 en 1000')
    shortcuts.clearScreen(2.5)
    kansen = 0
    while kansen < 10:
        while True:
            try:
                gok = int(input('Kies en voer het getal in: '))
                break
            except:
                print('Kies een getal zonder kommas!')

        difference = rando - gok

        if difference == 0:
            shortcuts.print_slow('Je hebt het getal geraden!')
            shortcuts.clearScreen(5)
            shortcuts.print_slow('Gefeliciteerd!')
            shortcuts.clearScreen(5)
            score += 1
            break
        if difference >= -20 and difference <= 20:
            print('Je bent heel heet')
        elif difference >= -50 and difference <= 50:
            print('Je bent warm')
        else:
            print('Je zit er heel erg ver van af')
        if gok > rando:
            print('Het getal is lager')
        elif gok < rando:
            print('Het getal is hoger')
        kansen += 1
        print("\n")
        if kansen == 10:
            print('Goed geprobeerd, het getal was: ',rando)
    print('Jouw score: '+str(score))
    keerGespeeld+=1
    if keerGespeeld == 20:
        break
    
    while True:
        nogKeer = input('Wil je nog een ronde spelen? y/n: ')
        if nogKeer == "y":
            loop = True
            break
        elif nogKeer == "n":
            loop = False
            break
        else:
            print('y/n')
    if loop == False:
        break
shortcuts.print_slow('Eindscore: '+str(score))
shortcuts.clearScreen(7.5)

shortcuts.print_slow('Gemaakt door: Lucas van Pelt')
shortcuts.clearScreen(12.5)