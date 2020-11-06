def tallest_people(**heights):
    max_height = max(heights.values())
    res = []
    for person in heights:
        if heights[person] == max_height:
            res.append(person)

    res.sort()

    for person in res:
        print(f"{person} : {max_height}")
