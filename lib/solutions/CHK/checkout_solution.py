

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
    
    
    
    nSkus = len(skus)
    
    for sku in ['A', 'B', 'C', 'D']:
        skuCounts[sku] = list(skus).count(sku)
    
    
    return out


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

sum(skuCounts.values())




