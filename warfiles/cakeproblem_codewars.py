"""
*Most Liked Answer

def cakes(recipe, available):
    return min(available.get(k, 0)/recipe[k] for k in recipe)

"""

def cakes(recipe, available):
    topcount = []
    if recipe.keys():
        for ingname in recipe.keys():
            if ingname not in available.keys():
                topcount.append(0)
                continue
            else:
                tempcount = available[ingname] // recipe[ingname]
                topcount.append(tempcount)
                continue
    else:
        return 0
    return min(topcount)