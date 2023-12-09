itemset_type = list[object]
dataset_type = list[list[object]]


def support(itemsets: dataset_type, data_set: itemset_type) -> float:
    """
    To find the frequency of itemsets in the dataset.
    """

    return support_value

dataset = [
        ['bread', 'milk'],
        ['bread', 'diaper', 'beer', 'eggs'],
        ['milk', 'diaper', 'beer', 'cola'],
        ['bread', 'milk', 'diaper', 'beer'],
        ['bread', 'milk', 'diaper', 'cola']
    ]
itemset = ['bread', 'milk']

"""
       ensuring the dataset is not empty before proceeding
    """

if len(dataset) != 0:

        occurrence = 0
        for index in range(len(dataset)):
            """
             comparing each value in the itemset to those in each index of the dataset 
            """

            if itemset[0] in dataset[index] and itemset[1] in dataset[index]:
                occurrence = occurrence + 1

else:
        print(f"error:{dataset} is empty")

support_value = occurrence / len(dataset)

support(itemsets=itemset, data_set=dataset)

print(f"support value for: {itemset} is {support_value}")



