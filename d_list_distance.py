import numpy
def distance_list(list_0):
### 第二种
    if len(list_0) <= 1:
        list00 =[0,0,0]
    else:
        list_0.sort()
        list1 = list_0[1:]
        list2 = list_0[:-1]
        list_dis = numpy.array(list1) - numpy.array(list2)
        mea = numpy.mean(list_dis)
        std = numpy.std(list_dis)
        med = numpy.median(list_dis)
        list00 = [ mea, med, std]
    list3 = [len(list_0),list00[0],list00[1],list00[2]]
    return (list3)

    # list = [26, 34, 70, 91, 143, 214, 261, 273, 274, 282, 311, 318, 332, 365, 374, 381, 4, 188, 191, 222, 225, 251, 253,
    #         287, 356, 358, 24, 57, 73, 85, 113, 126, 128, 296, 297, 364, 372, 378]
    # med=0
    # mea=0
    # std=0
    # if len(list_0) <= 1:
    #     dict1 = {"count":0,"mean":0,"med":0,"std":0}
    #     s1 = pd.Series(dict1)
    # else:
    #     list_0.sort()
    #     list1 = list_0[1:]
    #     list2 = list_0[:-1]
    #     list_dis = numpy.array(list1) - numpy.array(list2)
    #     mea=numpy.mean(list_dis)
    #     std=numpy.std(list_dis)
    #     med=numpy.median(list_dis)
    #
    #     dict1 = {"count": len(list_0), "mean": mea, "med": med, "std": std}
    #     list3 = (len(list_0),mea,med,std)
    #     s1 = pd.Series(list3, index=["count", "mean", "med", "std"])
    # # print(list_dis)
    # # print(list_dis)
    # return (s1)