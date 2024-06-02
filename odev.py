import math
points=[(1,2),(4,8),(10,20),(5,12)]

def euclideanDistance(a,b):
    return math.sqrt((a[0]-b[0])**2)+((a[1]-b[1])**2)
distances=[]
for i in range(len(points)):
    for j in range(i+1,len(points)):
        distance=euclideanDistance(points[i],points[j])
        distances.append(distance)
print(distances)
print("en kisa uzaklik:",min(distances))
