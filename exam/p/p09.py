def p09(citations=[]):
    h=None
    # ↓程式區域↓
    citations.sort(reverse=True)
    for i, c in enumerate(citations):
        if i >= c:
            return i
    # ↑程式區域↑
    return h
