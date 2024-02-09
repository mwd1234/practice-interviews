def can_place_flowers(flowerbed: list[int], n: int) -> bool:
    counter = 0
    for idx, pot in enumerate(flowerbed):
        if idx > 0 and idx < len(flowerbed) -1: 
            if pot == 0: 
                if flowerbed[idx - 1] == 0: 
                    if flowerbed[idx + 1] == 0: 
                        counter += 1
                        flowerbed[idx] = 1

    if counter >= n:
        return True
    
    return False

flowerbed = [1,0,0,0,1]
n = 1

flowerbed = [0,0,1,0,1]
n = 2
print(can_place_flowers(flowerbed, n))