class planet:

    planets = dict()
    def __init__(self, name,  orbiter):
        self.orbiters = []
        self.orbits = None
        if orbiter != None:
            self.orbiters.append(orbiter)
            orbiter.addOrbits(self)
        self.planets[name] = self
        self.name = name

    def addOrbiter(self, orbiter):
        self.orbiters.append(orbiter)
        orbiter.addOrbits(self)

    def addOrbits(self, orbits):
        self.orbits = orbits

    def printPlanet(self, depth):
        print(self.name.rjust(depth, '#'))
        for p in self.orbiters:
            p.printPlanet(depth + 1)


    def countOrbits(self, depth):
        #print(self.name.rjust(depth, '#'))
        #print("counting orbits for: " + self.name)
        orbitCount = 0
        if self.orbits != None:
            orbitCount = self.orbits.countOrbits(depth+1)
        else:
            #print("Nonea pukkaa")
            return depth
        #print(" there are orbits: " + str(orbitCount))
        return orbitCount

    def printInfo(self):
        print("name: " + self.name + " orbiters: " + str(self.orbiters) + " orbits: " + str(self.orbits))


path = "input.txt"


with open(path) as fl:
    for line in fl:
        line = line.strip()
        pl = line.split(')')
        #print(pl)
        if pl[0] in planet.planets and pl[1] in planet.planets:
            planet.planets[pl[0]].addOrbiter(planet.planets[pl[1]])
            #print("both existed:")
            #planet.planets[pl[0]].printPlanet(1)
            #planet.planets[pl[1]].printPlanet(1)
        elif pl[0] in planet.planets:
            newPlanet = planet(pl[1], None)
            planet.planets[pl[0]].addOrbiter(newPlanet)
            #print("0 existed:")
            #newPlanet.printPlanet(1)
        elif pl[1] in planet.planets:
            newPlanet = planet(pl[0], planet.planets[pl[1]])
        else:
            newPlanet = planet(pl[1], None)
            #print("none existet new planet:")
            #newPlanet.printPlanet(1)
            newPlanet2 = planet(pl[0], newPlanet)
            #print("none existet new planet 2:")
            #newPlanet2.printPlanet(1)
    planet.planets["COM"].printPlanet(1)
    totalDepth = 0
    for key in planet.planets:
        planet.planets[key].printInfo()
        totalDepth += planet.planets[key].countOrbits(0)
    print("syvyydet: " + str(totalDepth))

