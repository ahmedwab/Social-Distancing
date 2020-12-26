def calculateIntersection(a0, a1, b0, b1):
    if a0 >= b0 and a1 <= b1: # Contained
        intersection = a1 - a0
    elif a0 < b0 and a1 > b1: # Contains
        intersection = b1 - b0
    elif a0 < b0 and a1 > b0: # Intersects right
        intersection = a1 - b0
    elif a1 > b1 and a0 < b1: # Intersects left
        intersection = b1 - a0
    else: # No intersection (either side)
        intersection = 0

    return intersection
    

def IsIntersected(x,y,width,height,x1,y1,width1,height1):
   
    Area = ((x1+width1)-x1) *((y1+height1)-y1)
    width = calculateIntersection(x, x+width, x1, x1+width1)        
    height = calculateIntersection(y, y+height, y1, y1+height1)          
    area = width * height
    percent = area / Area

    if (percent >= 0):
        return True
    else:
        return False
 
def findIntersections(detected):
    for item1 in detected:
        for item2 in detected:
            if item1!=item2:
                if IsIntersected(item1[0],item1[1],item1[2],item1[3],item2[0],item2[1],item2[2],item2[3])!=True:
                    return False

    return True


    # credits to https://stackoverflow.com/questions/48477130/find-area-of-overlapping-rectangles-in-python-cv2-with-a-raw-list-of-points

