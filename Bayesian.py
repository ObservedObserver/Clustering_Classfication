from PIL import Image
import math
INF = 2147483647
class Words():
    def __init__(self, imgs, results, resultSet):
        self.imgs = imgs
        self.results = results
        self.resultSet = resultSet
        tmp = Image.open(self.imgs[0])
        self.width = tmp.size[0]
        self.height = tmp.size[1]
        self.total = len(imgs) #size of training data
        self.count_result = [0 for i in range(0,len(resultSet))] #statistic of result(to get P(5), P(4),...)
        for result in self.results:
            self.count_result[result] += 1
        for val in self.count_result:
            val /= self.total
        self.resultNum = len(resultSet) #num of all kinds of result
        self.pb = [[0 for i in range(0,self.width*self.height)] for j in range(0,self.resultNum)]

    #get the probility matrix
    def statistic(self):
        index = 0
        for item in self.imgs:
            img = Image.open(item)
            width = img.size[0]
            height = img.size[1]
            pix = img.load()
            i = 0
            for x in range(0,width):
                for y in range(0,height):
                    if pix[x,y] != (255,255,255):
                        self.pb[self.results[index]][i] += 1
                    i += 1
            index += 1
        print(self.resultNum)
        for i in range(0,self.resultNum):
            for j in range(0,self.width*self.height):
                self.pb[i][j] = self.pb[i][j]/self.count_result[i]
        return self.pb

    def judge(self, image):
        img = Image.open(image)
        width = img.size[0]
        height = img.size[1]
        pix = img.load()
        ans = [math.log(val) for val in self.count_result]
        for x in range(0,width):
            for y in range(0,height):
                for i in range(0,self.resultNum):
                    if pix[x,y] == (255,255,255):
                        if (1-self.pb[i][x*self.width+y]) != 0:
                            ans[i] += math.log((1-self.pb[i][x*self.width+y]))
                        else:
                            ans[i] += -INF
                    else:
                        if self.pb[i][x*self.width+y] != 0:
                            ans[i] += math.log(self.pb[i][x*self.width+y])
                        else:
                            ans[i] += -INF
        # return ans
        return self.resultSet[str(ans.index(max(ans)))]

# ["4-1.png","4-2.png","4-3.png","4-4.png","5-1.png","5-2.png","5-3.png","5-4.png"],
#[0,0,0,0,1,1,1,1],
test = Words(
    ["4-1.png","4-2.png","4-3.png","4-4.png","5-1.png","5-2.png","5-3.png","5-4.png"],
    [0,0,0,0,1,1,1,1],
    {"0":4,"1":5}
    )
print(test.statistic())
print("---"*8)
print("It is more likely to be: "+str(test.judge("4-1.png")))
