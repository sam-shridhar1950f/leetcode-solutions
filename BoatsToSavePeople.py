def BoatsToSave(people, limit):
    pointer1 = 0
    pointer2 = len(people) - 1
    people.sort()
    boats_number = 0


    while (pointer1 <= pointer2):
        
        if pointer1 == pointer2:
            boats_number += 1
            break

        elif people[pointer1] + people[pointer2] <= limit:
            boats_number += 1
            pointer2 -= 1
            pointer1 += 1
        else:
            boats_number += 1
            pointer2 -= 1



    return boats_number