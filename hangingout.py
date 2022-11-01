limit, events = input().split()
limit, events = int(limit), int(events)
current = 0
reject = 0
for i in range(events):
    motion, people = input().split()
    people = int(people)
    if motion == "enter":
        if people + current > limit:
            reject += 1
        else:
            current += people
    elif motion == "leave":
        current -= people
print(reject)
