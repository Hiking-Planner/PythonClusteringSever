from haversine import haversine

def cal_dist(path):
    total_dist = 0
    for i in range(1,len(path)):
        total_dist += haversine(path[i-1],path[i],unit='m')

    return total_dist
