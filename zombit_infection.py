def answer(population, x, y, strength):
    # x = The X-Coordinate (column) 
    # y = The Y-Coordinate (row)
    # population[row][column]
    if population[y][x] != -1 and population[y][x] <= strength:
        # Any infected cells value has been replaced with -1.
        population[y][x] = -1 
        
        # Infect any uninfected neighbors 
        if x > 0:
            population = answer(population, x - 1, y, strength)
        if x < len(population[0]) - 1:
            population = answer(population, x + 1, y, strength)
        if y > 0:
            population = answer(population, x, y - 1, strength)
        if y < len(population) - 1:
            population = answer(population, x, y + 1, strength)
            
    return population