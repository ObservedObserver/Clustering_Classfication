import math
class KNN():
    #points contains all the attribute info
    #result contains the training data's result(only int supported)
    def __init__(self, points, results):
        self.points = points
        self.results = results
        self.matrix = [ [] for item in points ]
        #Normalization of Variables
        max_dict = {}
        for att in points[0]:
            if type(points[0][att]) == str:
                continue
            else:
                max_dict[att] = max([point[att] for point in points])
        for point in points:
            for att in point:
                if type(points[0][att]) == str:
                    continue
                else:
                    point[att] /= max_dict[att]
    #calcute dis between two point
    def distance(self, point1, point2):
        dis = 0
        for item in point1.items():
            if type(item[1]) == str:
                continue
            else:
                dis += (item[1]-point2[item[0]])*(item[1]-point2[item[0]])
        dis = math.sqrt(dis)
        return dis
    #adj_matrix contains all the distance
    def adjacency_matrix(self):
        i = 0
        for point1 in self.points:
            for point2 in self.points:
                self.matrix[i].append(self.distance(point1,point2))
            i += 1
        return self.matrix
    #point is the prediction data and k is the size of k nearest.
    def classify(self, point, k):
        if len(self.matrix[0]) == 0:
            self.adjacency_matrix()
        dis = []
        for i in range(0,len(self.points)-1):
            dis.append( (self.distance(self.points[i], point), self.results[i]) )
        dis.sort()
        ans = 0
        for i in range(0,k-1):
            ans += dis[i][1]
        ans /= k
        return int(round(ans))
#examples:
people = [
    {"name":"John","Age":35,"Income":35000,"ncc":3},
    {"name":"Rechel","Age":22,"Income":50000,"ncc":2},
    {"name":"Hannah","Age":63,"Income":200000,"ncc":1},
    {"name":"Tom","Age":59,"Income":170000,"ncc":1},
    {"name":"Nellie","Age":25,"Income":40000,"ncc":4},
    {"name":"David","Age":37,"Income":50000,"ncc":2},
]
Response = [0,1,0,0,1]
test = KNN(people,Response)
print(test.adjacency_matrix())
print(test.classify(people[5],3))
print(test.points)
