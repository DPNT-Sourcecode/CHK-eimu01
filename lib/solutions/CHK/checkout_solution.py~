

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

def getSkuCounts(skus, items):
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
    
    multiItems = {
            'A': [0, 0, 130, 0, 2000],
            'B': [0, 45]}
    
    # check input integrity
    passTests = getPassTests(skus, items)
    if not passTests:
        return -1
    
    # build inventory
    skuCounts = getSkuCounts(skus, items)
    print('skuCounts: %s' % skuCounts)
    
    # calculate free items value
    free = 0
    if 'E' in skuCounts:
        free += items['E'] * (skuCounts['E'] // 2)
    print('free: %s' % free)
    
    # adjust inventory for discounts
    discounted = 0
    
    for sku in multiItems:
#        print('sku: %s' % sku)
        if sku in skuCounts:
            offers= multiItems[sku]
#            print('offers: %s' % offers)
            for i in range(len(offers)):
#                print('i: %s' % i)
                n = len(offers) - i
                pos = n - 1
                if multiItems[sku][pos] > 0:
                    discounted += multiItems[sku][pos] * (skuCounts[sku] // n)
#                    print('discounted: %s' % discounted)
                    skuCounts[sku] = skuCounts[sku] % n
#                    print('skuCounts: %s' % skuCounts)
    
#    return 'done'
    
    
    # no discounts total
    noDiscount = 0
    for sku, count in skuCounts.items():
        noDiscount += skuCounts[sku] * items[sku]
    print('noDiscount: %s' % noDiscount)
    
    # finalise total
    total = discounted + noDiscount + free
    
    return total

#checkout('AABCDABCABCDAAAAABCDEEE')







