sub_dataset_type = tuple[object]
support_type = float
strong_rules = list[object], list[object]
confidence_type = float


def apriori(transactions: list[list[object]], min_support: float = 0.7, min_confidence: float = 0.5) \
        -> tuple[dict[sub_dataset_type, support_type], dict[strong_rules, confidence_type]]:
    """
    To find all frequent itemsets in a dataset and generate strong association rules.
    """
sub_dataset_type = tuple[object]
support_type = float
strong_rules = list[object], list[object]
confidence_type = float

dataset = [
        ['bread', 'milk'],
        ['bread', 'diaper', 'beer', 'eggs'],
        ['milk', 'diaper', 'beer', 'cola'],
        ['bread', 'milk', 'diaper', 'beer'],
        ['bread', 'milk', 'diaper', 'cola']
    ]
longlist = []
item1= []
item2 = []
item3 = []
item4 = []
item5 = []
final = []
def apriori():

    """
    To find all frequent item sets in a dataset and generate strong association rules.
    """

    for index1 in range(len(dataset)) :
        for index2 in range(len(dataset)):
            longlist.append((dataset[index1]))

    first = longlist[0]

    for index in range(len(longlist)):
        if first == longlist[index]:
            item1.append(first)
        elif first != longlist[index]:
            item2.append(first)

    second = item2[0]

    for index in range(len(item2)):
        if second == longlist[index]:
            item2.append(second)
        elif second != longlist[index]:
            item3.append(second)
    third = item3[0]

    for index in range(len(item3)):
        if third == longlist[index]:
            item2.append(third)
        elif third != longlist[index]:
            item4.append(third)

    fourth = item4[0]

    for index in range(len(item3)):
        if fourth == longlist[index]:
            item2.append(fourth)
        elif third != longlist[index]:
            item5.append(fourth)

    support1 = len(item1)
    support2 = len(item2)
    support3 = len(item3)
    support4 = len(item4)
    support5 = len(item5)
    p = 2
    for i in range(1, 6):

     if support1 / len(dataset) >= 0.7:
        value = item1[0]

        for l in range(len(dataset)):
            if value in dataset[l] and len(dataset[l]) == p:
                final.append(tuple(dataset[l]))
        if len(final) == 1 and len(dataset) == 5:
            break
        else:
            continue
     p = p+1
    for i in range(len(dataset)):
        if value in (dataset[i]):
            count = count+1

    return {tuple(final)}

print(apriori())

         return {}, {}
