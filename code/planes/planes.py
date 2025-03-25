import math, random, time

def createPlane(r, c):
    return [[0]*c]*r

def createSchedule(): # (plane, time, has_seats_available)
    sched = []
    for i in range(3):
        sched.append([createPlane(32, 4), random.randint(1, 24), True])
    sched=sorted(sched, key=lambda y: y[1])
    return sched

def availableFlights(sched):
    times=[]
    for i in sched:
        if i[2] == True:
            if i[1] not in times:
                times.append(i[1])
    return times

def suggestAlt0(times, val): # suggest closest time when not available
    closest=1000
    for i in times:
        if abs(val-i)<closest or abs(i-val)<closest:
            closest=i
    return closest

def main():
    sched = createSchedule()
    passengers_sat = 0
    groups_split = 0
    num_split = 0
    
    # loop should start here
    available_times = availableFlights(sched)
    print("We have planes departing at: "+str(available_times))
    t = int(input("What time would you like to depart? [Select 1-24] "))
    if t not in available_times:
        s0 = input("That time is not available. The closest departing flight to that time is "+str(suggestAlt0(available_times, t))+". Would you like to switch over? [Select Y/N] ").lower()
        if s0 == "y" or s0 == "yes":
            t = suggestAlt0(available_times, t)
        # ELSE (END + COUNT)


    # print-pront
    time.sleep(2)
    for i in sched:
        print("Departs at: "+str(i[1]))
        print("Available seats: "+str(i[2]))
        for j in i[0]:
            print(j)
        print()
main()
