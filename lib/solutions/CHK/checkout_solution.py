

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

def adjustForDiscounts(skuCounts, multiItems):
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
    
    return discounted, skuCounts

def getNoDiscounts(skuCounts, items):
    noDiscount = 0
    for sku, count in skuCounts.items():
        noDiscount += skuCounts[sku] * items[sku]
    print('noDiscount: %s' % noDiscount)
    
    return noDiscount


def checkout(skus):
    items = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
        'F': 10,
        'G': 20,
        'H': 10,
        'I': 35,
        'J': 60,
        'K': 80,
        'L': 90,
        'M': 15,
        'N': 40,
        'O': 10,
        'P': 50,
        'Q': 30,
        'R': 50,
        'S': 30,
        'T': 20,
        'U': 40,
        'V': 50,
        'W': 20,
        'X': 90,
        'Y': 10,
        'Z': 50}
    
    multiItems = {
            'A': [0, 0, 130, 0, 200],  # 3A for 130, 5A for 200
            'B': [0, 45],  # 2B for 45
            'H': [0, 0, 0, 0, 45, 0, 0, 0, 0, 80],  # 5H for 45, 10H for 80
            'K': [0, 150],  # 2K for 150
            'P': [0, 0, 0, 0, 200],  # 5P for 200
            'Q': [0, 0, 80], # 3Q for 80
            'V': [0, 90, 130]}  # 2V for 90, 3V for 130
    
    # check input integrity
    passTests = getPassTests(skus, items)
    if not passTests:
        return -1
    
    # build inventory
    skuCounts = getSkuCounts(skus, items)
    print('skuCounts: %s' % skuCounts)
    
    # deduct offers
    if 'E' in skuCounts:  # 2E get one B free
        offers = skuCounts['E'] // 2
        if offers > 0:
            skuCounts['B'] -= offers
            if skuCounts['B'] < 0:
                skuCounts['B'] = 0
    print('E skuCounts: %s' % skuCounts)
    
    if 'F' in skuCounts:  # 2F get one F free
        if skuCounts['F'] >= 3:
            offers = skuCounts['F'] // 3
            if offers > 0:
                skuCounts['F'] -= offers
                if skuCounts['F'] < 0:
                    skuCounts['F'] = 0
    print('F skuCounts: %s' % skuCounts)
    
    if 'F' in skuCounts:  # 2F get one F free
        if skuCounts['F'] >= 3:
            offers = skuCounts['F'] // 3
            if offers > 0:
                skuCounts['F'] -= offers
                if skuCounts['F'] < 0:
                    skuCounts['F'] = 0
    print('F skuCounts: %s' % skuCounts)
    
    # TODO
    # 3N get one M free 
    # 3R get one Q free
    # 3U get one U free
    
    
    
    
    
    
    
    
    
    
    
    # adjust inventory for discounts
    discounted, skuCounts = adjustForDiscounts(skuCounts, multiItems)
    
    # no discounts total
    noDiscount = getNoDiscounts(skuCounts, items)
    
    # finalise total
    total = discounted + noDiscount
    
#    return('done')
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
#a = checkout("F")
#a
#----------------
#a = checkout("FF")
#a
#----------------
#a = checkout("FFF")
#a
#----------------
a = checkout("FFFFF")
a






