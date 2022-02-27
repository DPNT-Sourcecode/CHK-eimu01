

# noinspection PyUnusedLocal
# skus = unicode string

def getPassTests(skus, items):
    """Input tests"""
    passTest = True
    
    # check string
    if not isinstance(skus, str):
        passTest = False
    
    # check valid skus
    if not set(skus).issubset(items):
        passTest = False
    
    return passTest

def getSkuCounts(skus):
    """Build inventory dictionary"""
    skuCounts = {}
    for sku in items:
        skuCounts[sku] = list(skus).count(sku)
    
    return skuCounts

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
    
    # TODO: structure
    multiItems = {
            'A': 130,
            'B': 45}
    
    
    
    
    # check input integrity
    passTests = getPassTests(skus, items)
    if not passTests:
        return -1
    
    # build inventory
    skuCounts = getSkuCounts(skus)
    print('skuCounts: %s' % skuCounts)
    
    
    
    
    
    # adjust inventory for discounts
    discounted = 0
    if 'A' in skuCounts:
        discounted +=  multiItems['A'] * (skuCounts['A'] // 3)
        skuCounts['A'] = skuCounts['A'] % 3
    
    if 'B' in skuCounts:
        discounted += multiItems['B'] * (skuCounts['B'] // 2)
        skuCounts['B'] = skuCounts['B'] % 2
    
    # no discounts total
    noDiscount = 0
    for sku, count in skuCounts.items():
        noDiscount += skuCounts[sku] * items[sku]
    print('noDiscount: %s' % noDiscount)
    
    
    # finalise total
    total = discounted + noDiscount
    
    return total

skus = 'AABCDABCABCDAAABCDE'
checkout('AABCDABCABCDAAABCDE')

items = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40}

# TODO: structure
multiItems = {
        'A': 130,
        'B': 45}


# check input integrity
passTests = getPassTests(skus, items)
if not passTests:
    return -1

# build inventory
skuCounts = getSkuCounts(skus)
print('skuCounts: %s' % skuCounts)




