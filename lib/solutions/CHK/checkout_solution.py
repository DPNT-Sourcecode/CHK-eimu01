

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """
    3A 130
    2B 45
    """
    items = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15}
    multiItems = {
            'A': 130,
            'B': 45}
    
    # check string
    if not isinstance(skus, str):
        return -1

    
    
    
    nSkus = len(skus)
    
    for sku in ['A', 'B', 'C', 'D']:
        skuCounts[sku] = list(skus).count(sku)
    
    
    return ret


skus = "ABCDABCABCDAAABCDE"

items = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15}


nSkus = len(skus)

skuCounts = {}
for sku in ['A', 'B', 'C', 'D']:
    skuCounts[sku] = list(skus).count(sku)

total = sum(skuCounts.values())


if nSkus != total:
    return -1


{'A': 6, 'B': 4, 'C': 4, 'D': 3}

