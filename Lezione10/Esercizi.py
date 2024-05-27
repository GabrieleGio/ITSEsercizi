def rimbalzo() -> None:
    
    tempo: int = 0
    altezza: float = 0.0
    velocita: float = 100.0
    rimbalzi: int = 0

    print(f"Tempo: {tempo} Altezza {altezza} Velocità {velocita}")
    while rimbalzi < 5:
        altezza = altezza + velocita
        velocita = velocita - 96
        tempo += 1

        if altezza >= 0:
            print(f"Tempo: {tempo} Altezza {altezza} Velocità {velocita}")

        if altezza < 0:
            altezza=altezza*1/2
            velocita=velocita*1/2
            print(f"Tempo: {tempo} Rimbalzo!")
            rimbalzi = rimbalzi + 1
            tempo += 1
            if tempo != 29:
                print(f"Tempo: {tempo} Altezza {altezza}")
            else:
                break

        

print(rimbalzo())