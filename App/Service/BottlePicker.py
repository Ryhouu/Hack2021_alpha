def run(bottle, player, other) :
    if bottle is None :
            return
    if bottle.isMemory() :
        if player.memory < 5 :
            print ("picking bottle")
            
            player.memory += 1
            player.vision -= 1
            player.speed -= 1
            other.memory -= 1