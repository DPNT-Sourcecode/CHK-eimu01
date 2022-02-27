

# noinspection PyUnusedLocal
# skus = unicode string

def passTests(skus, items):
    passTest = False
    
    # check string
    if not isinstance(skus, str):
        passTest = False
    
    # check valid skus
    if not set(skus).issubset(items):
        passTest = False
    
    return passTest

def checkout(skus):
    """
    3A = 130
    5A = 200
    2B = 45
    2E = extra B
    """
    items = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40}
    
    multiItems = {
            'A': 130,
            'B': 45}
    
    
    
    
    
    
    if not passTests:
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







