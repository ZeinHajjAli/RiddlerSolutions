states = ['AL','AK','AS','AZ','AR','CA','CO','CT','DE','DC','FM','FL','GA','GU','HI','ID','IL', 'IN','IA','KS','KY','LA','ME','MH','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','MP','OH','OK','OR','PW','PA','PR','RI','SC','SD','TN','TX','UT','VT','VI','VA','WA','WV','WI','WY']

maxLength = 0
maxRoute = []

def routeFinder():
    unusedStates = states[:]
    route = []
    everyOption(route, unusedStates, unusedStates)
    print("The maximum states that can be done in this way are {}\n".format(maxLength))
    print(stringBuilder(maxRoute))

def everyOption(route, unusedStates, nextStates):
    newUnusedStates = []
    newRoute = []
    print(route)
    for nextState in nextStates:
        newUnusedStates = unusedStates[:]
        newUnusedStates.remove(nextState)
        newRoute = route[:]
        newRoute.append(nextState)
        routeBuilder(newRoute, newUnusedStates)

def routeBuilder(route, unusedStates):
    global maxLength
    global maxRoute
    last = route[-1]
    lastLetter = last[-1]
    nextStates = []
    for state in unusedStates:
        if state.startswith(lastLetter):
            nextStates.append(state)
            if len(nextStates) > 0:
                everyOption(route, unusedStates, nextStates)
            else:
                if len(route) > maxLength:
                    maxLength = length
                    maxRoute = route


def stringBuilder(codeArray):
    firstCode = codeArray[0]
    outputString = firstCode[0]
    for code in codeArray:
        outputString = outputString + code[-1]
    return outputString

routeFinder()
