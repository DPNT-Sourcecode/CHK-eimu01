# noinspection PyUnusedLocal
# skus = unicode string

def getItems():
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
        'K': 70,
        'L': 90,
        'M': 15,
        'N': 40,
        'O': 10,
        'P': 50,
        'Q': 30,
        'R': 50,
        'S': 20,
        'T': 20,
        'U': 40,
        'V': 50,
        'W': 20,
        'X': 17,
        'Y': 20,
        'Z': 21}
    
    return items

def getMultiItems():
    multiItems = {
            'A': [0, 0, 130, 0, 200],  # 3A for 130, 5A for 200
            'B': [0, 45],  # 2B for 45
            'H': [0, 0, 0, 0, 45, 0, 0, 0, 0, 80],  # 5H for 45, 10H for 80
            'K': [0, 120],  # 2K for 120
            'P': [0, 0, 0, 0, 200],  # 5P for 200
            'Q': [0, 0, 80], # 3Q for 80
            'V': [0, 90, 130]}  # 2V for 90, 3V for 130
    
    return multiItems

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


def adjustForGroupOffers(skuCounts):
    """ X, S, T, Y, Z increasing prices"""
    
skuCounts = {'S': 1, 'T': 1, 'X': 1, 'Y': 1, 'Z': 1}
skuCounts

special = [skuCounts.get(sku, 0) for sku in ['S', 'T', 'X', 'Y', 'Z']]
special

n = sum(special)
if n >= 3:
    n // 3
    groupOffer
    
    
    skuCounts
    
    
    
    
    return groupOffer, skuCounts

def adjustForOffers(skuCounts):
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
    
    if 'N' in skuCounts:  # 3N get one M free
        if skuCounts['N'] >= 3:
            offers = skuCounts['N'] // 3
            if offers > 0:
                skuCounts['M'] -= offers
                if skuCounts['M'] < 0:
                    skuCounts['M'] = 0
    print('N skuCounts: %s' % skuCounts)
    
    if 'R' in skuCounts:  # 3R get one Q free
        if skuCounts['R'] >= 3:
            offers = skuCounts['R'] // 3
            if offers > 0:
                skuCounts['Q'] -= offers
                if skuCounts['Q'] < 0:
                    skuCounts['Q'] = 0
    print('R skuCounts: %s' % skuCounts)
    
    if 'U' in skuCounts:  # 3U get one U free
        if skuCounts['U'] >= 4:
            offers = skuCounts['U'] // 4
            if offers > 0:
                skuCounts['U'] -= offers
                if skuCounts['U'] < 0:
                    skuCounts['U'] = 0
    print('U skuCounts: %s' % skuCounts)
    
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

def getRegular(skuCounts, items):
    regular = 0
    for sku, count in skuCounts.items():
        regular += skuCounts[sku] * items[sku]
    print('regular: %s' % regular)
    
    return regular

def checkout(skus):
    items = getItems()
    multiItems =  getMultiItems()
    
    # check input integrity
    passTests = getPassTests(skus, items)
    if not passTests:
        return -1
    
    # build inventory
    skuCounts = getSkuCounts(skus, items)
    print('skuCounts: %s' % skuCounts)
    
    # adjust inventory for group offers
    groupOffer, skuCounts = adjustForGroupOffers(skuCounts)
    
    # adjust inventory for offers
    skuCounts = adjustForOffers(skuCounts)
    
    # adjust inventory for discounts
    discounted, skuCounts = adjustForDiscounts(skuCounts, multiItems)
    
    # no discounts total
    regular = getRegular(skuCounts, items)
    
    # finalise total
    total = groupOffer + discounted + regular
    
#    return('done')
    return total


#Result is: FAILED
#Some requests have failed (1/141). Here are some of them:
# - {"method":"checkout","params":["UUU"],"id":"CHK_R4_054"}, expected: 120, got: 80

a = checkout('UUU')
a
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
#a = checkout("FFFFF")
#a









