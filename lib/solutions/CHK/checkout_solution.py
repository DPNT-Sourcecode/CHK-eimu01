

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
    
    # check valid skus
    if set(skus) != set(items):
        return -1
    
    # build inventory
    skuCounts = {}
    for sku in items:
        skuCounts[sku] = list(skus).count(sku)
    
    # adjust inventory for discounts
    if 'A' in 
    
    
    return total


skus = "AABCDABCABCDAAABCDE"

items = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15}

multiItems = {
        'A': 130,
        'B': 45}

skuCounts = {}
for sku in items:
    skuCounts[sku] = list(skus).count(sku)

skuCounts
#{'A': 7, 'B': 4, 'C': 4, 'D': 3}

total = 0
if 'A' in skuCounts:
    total = total + (multiItems['A'] * (skuCounts['A'] // 3))
    skuCounts['A'] = skuCounts['A'] % 3
elif 'B' in skuCounts:
    total = total + (multiItems['B'] * (skuCounts['B'] // 3))
    skuCounts['B'] = skuCounts['B'] % 2










