temp=[[255, 255, 255], [255, 255, 0], [255, 165, 0], [0, 128, 0], [255, 0, 0], [0, 0, 255]]
swap=[[255, 255, 0], [255, 0, 0]]

print('org - ' + str(temp))
a = palette.index(swap[0])
b = palette.index(swap[1])

palette[a] = swap[1]
palette[b] = swap[0]

print('mod - ' + str(temp))