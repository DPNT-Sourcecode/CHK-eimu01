

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
    if not set(skus).issubset(items):
        return -1
    
    # build inventory
    skuCounts = {}
    for sku in items:
        skuCounts[sku] = list(skus).count(sku)
    
    # adjust inventory for discounts
    total = 0
    if 'A' in skuCounts:
        total +=  multiItems['A'] * (skuCounts['A'] // 3)
        skuCounts['A'] = skuCounts['A'] % 3
    
    if 'B' in skuCounts:
        total += multiItems['B'] * (skuCounts['B'] // 2)
        skuCounts['B'] = skuCounts['B'] % 2
    
    # no discounts total
    noDiscount = 0
    for sku, count in skuCounts.items():
        noDiscount += skuCounts[sku] * items[sku]
    
    # finalise total
    total += noDiscount
    
    return total





