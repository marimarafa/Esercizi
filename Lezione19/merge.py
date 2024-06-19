def mergeSort(input_list:list) -> list:

    if len(input_list) == 1:
        return input_list

    mid_point :int = len(input_list) // 2

    list1 :list[int] = mergeSort(input_list= input_list[:mid_point])
    list2 :list[int] = mergeSort(input_list=input_list[mid_point:])

    return merge(list1,list2)

def merge(list1:list[int],list2:list[int])->list[int]:
    i, j = 0,0
    result :list[int] = [None for _ in range(len(list1 + list2)) ]
    #result = []
    #aggiungere gli elementi con l'append alla lista result
    #result.append()

    for k in range(len(result)):
        if len(list1) < 1 :
            return result 
        elif len(list2) < 1:
            return result 
        else:
            if list1[i] > list2[j]:
                result[k] = list2[j]
                j += 1
            else:
                result[k] = list1[i]
                i += 1
    return result




if __name__ == "__main__":

    input_list:list[int] = [0,1,2,3,4,5,6,7]

    print(mergeSort(input_list))