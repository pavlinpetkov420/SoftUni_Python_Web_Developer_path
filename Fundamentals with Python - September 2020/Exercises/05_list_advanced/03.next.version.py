"""Last test is wrong!!!! Need to remake the algorithm!!!!"""
version = [int(x)
           for x in input().split('.')]
is_changed = False
next_version = version.copy()
for i in range(len(version) - 1, -1, -1):
    if is_changed:
        break
    if version[i] >= 9:
        next_version[i] = 0
        next_version[i - 1] += 1
        if next_version[i - 1] >= 9:
            next_version[i - 1] = 0
            next_version[0] += 1
            break
        is_changed = True
    else:
        next_version[i] += 1
        break

next_version = [str(i) for i in next_version]
print(".".join(next_version))

# v2.0
