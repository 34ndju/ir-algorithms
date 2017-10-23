def edit_distance(s1,s2):
    m = []

    m.append([0])

    for i in range(1,len(s1) + 1):
        m.append([i])

    for j in range(1,len(s2) + 1):
        m[0].append(j)

    for i in range(1,len(s1) + 1):
        for j in range(1,len(s2) + 1):
            m[i].append(min(m[i-1][j-1] if (s1[i-1] == s2[j-1]) else (m[i-1][j-1] + 1), m[i-1][j] + 1, m[i][j-1] + 1))
            
    return m[len(s1)][len(s2)]

print edit_distance("cats", "fast")
