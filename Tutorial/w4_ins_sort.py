# insertion sort

def find_ins_idx(r, v):
    for i in range(0, len(r)):
        if v < r[i]:
            return i

    return len(r)  #적절한 위치를 못찾은 경우, 맨뒤에 삽입

def ins_sort(a):
    result = []
    while a:
        value = a.pop(0)
        ins_idx = find_ins_idx(result, value)
        result.insert(ins_idx, value)
    return result

if __name__ == '__main__':
    d = [2,4,5,1,3]
    print(ins_sort(d))


