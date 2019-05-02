"""

"""

def sublists(l):
    chosen = []
    sublistsHelper(l, chosen)


def sublistsHelper(l, chosen):
    print("####  Current: l:", l, "### Chosen:", chosen)
    if l == []:
        print(chosen)
    else:
        s = l[0]
        l.pop(0)

        #choose/explore without s
        sublistsHelper(l, chosen)

        #choose/explore with s
        chosen.append(s)
        sublistsHelper(l, chosen)

        #unchoose
        l.insert(0, s)
        chosen.pop()

sublists(["Jane","Bob","Matt","Sara"])
