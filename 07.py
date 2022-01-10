# Сортировка двумерного списка

# Функция, возвращающая двумерный список индексов двумерного списка
def getIndexArray(myList):
     ret = []
     for i in range(len(myList)):
          for j in range(len(myList[i])):
               ret.append([])
               ret[(i * len(myList)) + j].append(i)
               ret[(i * len(myList)) + j].append(j)
     return ret

# Функция, сортирующая двумерный список по индексам
def getSortedArray(myList, idx):
     for i in range(len(idx) - 1):
          for j in range(len(idx) - 1 - i):
               if myList[idx[j][0]][idx[j][1]] > myList[idx[j + 1][0]][idx[j + 1][1]]:
                    myList[idx[j][0]][idx[j][1]], myList[idx[j + 1][0]][idx[j + 1][1]] = \
                         myList[idx[j + 1][0]][idx[j + 1][1]], myList[idx[j][0]][idx[j][1]]
     return myList


a = [[16, 6, 11, 7],
     [5, 12, 13, 14],
     [3, 9, 15, 10],
     [1, 4, 8, 2]]

print(sorted(a))

idx = getIndexArray(a)
#for i in idx:
#     print(i)
print(f"Исходный список: \n{a}\n\nОтсортированный:\n{getSortedArray(a, idx)}")