

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
            'A': [0, 0, 130, 0, 200],
            'B': [0, 45]}
    
    # check input integrity
    passTests = getPassTests(skus, items)
    if not passTests:
        return -1
    
    # build inventory
    skuCounts = getSkuCounts(skus, items)
    print('skuCounts: %s' % skuCounts)
    
    # deduct offers
    if 'E' in skuCounts:
        offers = skuCounts['E'] // 2
        if offers > 0:
            skuCounts['B'] -= offers
            if skuCounts['B'] < 0:
                skuCounts['B'] = 0
    print('skuCounts: %s' % skuCounts)
    
    # adjust inventory for discounts
    discounted = 0
    
    for sku in multiItems:
        print('sku: %s' % sku)
        if sku in skuCounts:
            offers= multiItems[sku]
            print('offers: %s' % offers)
            for i in range(len(offers)):
                print('i: %s' % i)
                n = len(offers) - i
                pos = n - 1
                if multiItems[sku][pos] > 0:
                    discounted += multiItems[sku][pos] * (skuCounts[sku] // n)
                    print('discounted: %s' % discounted)
                    skuCounts[sku] = skuCounts[sku] % n
                    print('skuCounts: %s' % skuCounts)
    
#    return('done')
    
    # no discounts total
    noDiscount = 0
    for sku, count in skuCounts.items():
        noDiscount += skuCounts[sku] * items[sku]
    print('noDiscount: %s' % noDiscount)
    
    # finalise total
    total = discounted + noDiscount
    
    return total


# - {"method":"checkout","params":["EE"],"id":"CHK_R2_023"}, expected: 80, got: 120
# - {"method":"checkout","params":["EEB"],"id":"CHK_R2_024"}, expected: 80, got: 150
# - {"method":"checkout","params":["EEEB"],"id":"CHK_R2_025"}, expected: 120, got: 190

#a = checkout('EE')
#a
#----------------
#a = checkout("EEB")
#a
#----------------
#a = checkout("EEEB")
#a
#----------------




