from data import data

class Sd:
    """Sudoku solver"""
    def __init__(self) -> None:
        #self.result = [['_' for i in range(9)] for j in range(9)]
        self.result = None
        self.winner = True
        self.possible = [[[1,2,3,4,5,6,7,8,9] for i in range(9)] for j in range(9)]
        self.prev_hint = []

    def get_board(self):
        print("Enter number if current position have value.")
        print("Enter '0' if current position dont have value.")
        for i in range(9):
            for j in range(9):
                self.result[i][j] = int(input(f"provide value for pos{i}{j}:"))
            print('')

    def print_board(self):
        for i in range(9):
            print('|',end=' ')
            for j in range(9):
            
                print(self.result[i][j] ,end=' ')
                if j == 2 or j == 5 :
                    print('|', end=' ')
            print('|')
            if i == 2 or i == 5 or i==8:
                for k in range(9):
                    print('__', end=" ")    
                print("")
            print('')
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

    def print_possible_board(self):
        for i in range(9):
            print('|',end=' ')
            for j in range(9):
            
                print(self.possible[i][j] ,end=' ')
                if j == 2 or j == 5 :
                    print('|', end=' ')
            print('|')
            if i == 2 or i == 5 or i==8:
                for k in range(9):
                    print('__', end=" ")    
                print("")
            print('')
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

    def is_board_contains_zero(self):
        for i in range(9):
            for j in range(9):
                if self.result[i][j] == 0:
                    self.winner = True
                    return

        self.winner = False
    
    def add_possible_row(self, a,b):
        for m in range(9):
            if self.result[a][m] != 0:
                if self.result[a][m] in self.possible[a][b]:
                    self.possible[a][b].remove(self.result[a][m])
          

    def add_possible_column(self, a,b):
        
        for m in range(9):
            if self.result[m][b] != 0:
                if self.result[m][b] in self.possible[a][b]:
                    self.possible[a][b].remove(self.result[m][b])


    def add_possible_square(self,a,b):
        m = (a//3) *3
        n = (b//3) * 3
        for m in range(m, m+3):
            for n in range(n, n+3):
                if self.result[m][n] != 0:
                    if self.result[m][n] in self.possible[a][b]:
                        self.possible[a][b].remove(self.result[m][n])
            n = (b//3) * 3


    def is_empty_val(self,a,b):
        if self.result[a][b] == 0:
            return True
        else:
            return False
    
    def get_empty_row(self, a, b):
        row=list()
        for k in range(9):
                if self.is_empty_val(a,k):
                    row.append(k)
        return row

    def get_empty_col(self, a, b):
        col=list()
        for k in range(9):
                if self.is_empty_val(k,b):
                    col.append(k)
        
        return col
    
    def add_possible_row_col(self, a, b):
        row = list()
        col = list()
        row = self.get_empty_row(a,b)
        col = self.get_empty_col(a,b)
        
        for r in row:  # add possible in every empty row
            for m in range(9):
                if self.result[a][m] != 0:
                    if self.result[a][m] in self.possible[a][r]:
                        self.possible[a][r].remove(self.result[a][m])

        for c in col:
             for m in range(9):
                if self.result[m][b] != 0:
                    if self.result[m][b] in self.possible[c][b]:
                        self.possible[c][b].remove(self.result[m][b])
            
    def add_possible_grid(self, a, b):
        val = self.result[a][b]

        for m in range((a//3)*3, (a//3)*3 +3):
            for n in range((b//3)*3, (b//3)*3 +3):
                if self.result[m][n] ==0:
                    if val in self.possible[m][n]:
                        self.possible[m][n].remove(val)


    def check_possible_with_row(self, a, b=0, check_next=False, if_check=False):
        #E.g  board [6,7,0,9,0,0,4,2,3]
        # possible [[],[],[5,8],[],[1,5,8],[5,8],[],[],[]]
        #  index    [0,1,2,3,4,5,6,7,8] 
        # here 4th index col can only have value '1' 
        row=list()
        row=self.get_empty_row(a,b) # [2,4,5]
        
        valueRow = 0
        for col in row:
            for val in self.possible[a][col]:
                count =0
                for eachCol in row:
                        if val not in self.possible[a][eachCol]:
                            count = count + 1
                if count == len(row) - 1:
                    valueRow = val # val = 1
        for col in row:
            if valueRow in self.possible[a][col]:
                if check_next and (2,a,col,valueRow) not in self.prev_hint:
                    if if_check == False:
                        self.prev_hint.append((2,a,col,valueRow)) # For check_possible_with_row function first index should be '2'
                    return f"Hidden single in row{a+1},column{col+1} with value of {valueRow} "
                self.result[a][col] = valueRow
                self.add_possible_row_col(a,col)
                self.add_possible_grid(a,col)
                self.possible[a][col].clear()

    def check_possible_with_col(self, b, a=0, check_next=False, if_check=False):
        #E.g  board [6, possible  [[],      index  [0,      
        #            7,            [],              1,  
        #            0,            [5,8],           2,
        #            9,            [],              3,
        #            0,            [1,5,8],         4,
        #            0,            [5,8],           5,
        #            4,            [],              6,
        #            2,            [],              7,
        #            3]            []]              8]
        # here 4th index row can only have value '1' 
        col= list()
        col = self.get_empty_col(a,b)           
        
        valueCol = 0
        for row in col:
            for val in self.possible[row][b]:
                count=0
                for eachRow in col:
                    if val not in self.possible[eachRow][b]:
                        count = count + 1
                if count == len(col) - 1:
                    valueCol = val
        for row in col:
            if valueCol in self.possible[row][b]:
                if check_next and (3,row,b,valueCol) not in self.prev_hint:
                    if if_check == False:
                        self.prev_hint.append((3,row,b,valueCol)) # For check_possible_with_col function first index should be '3'
                    return f"Hidden single in row{row+1},column{b+1} with value of {valueCol} "
                self.result[row][b] = valueCol
                self.add_possible_row_col(row, b)
                self.add_possible_grid(row,b)
                self.possible[row][b].clear()

    def is_in_other_rows_of_grid(self,a,val,square):
        for i in range((a//3)*3, (a//3*3)+3):
            if i !=a:
                for j in range(square*3,(square*3) +3):
                    if val in self.possible[i][j]:
                        return True
        return False
    
    def is_in_other_cols_of_grid(self,b,val,square):
        for i in range(b//3*3, (b//3*3)+3):
            if i !=b:
                for j in range(square*3,(square*3) +3):
                    if val in self.possible[j][i]:
                        return True
        return False
    
    def add_possible_other_row(self,a,val, square):

        for s in range(3):
            if s!= square:
                for j in range(s*3,(s*3)+3):
                    if val in self.possible[a][j]:
                        self.possible[a][j].remove(val)

    def add_possible_other_col(self,b,val, square):

        for s in range(3):
            if s!= square:
                for j in range(s*3,(s*3)+3):
                    if val in self.possible[j][b]:
                        self.possible[j][b].remove(val)
            

    def check_intersection_row(self,a, check_next=False, if_check=False):
        row1 = list()
        rowCount = 0
        for square in range(3):
            for i in range(square*3,(square*3)+3):
                for val in self.possible[a][i]:
                    rowCount =0
                    for j in range(square*3,(square*3)+3):
                        if val in self.possible[a][j]:
                            rowCount= rowCount + 1
                    if rowCount == 2:
                        if val not in row1:
                            row1.append(val)
            

            for val in row1:
                if self.is_in_other_rows_of_grid(a,val,square):
                    pass
                else:
                    if check_next and (5,a,square,val) not in self.prev_hint:
                        if if_check == False:
                            self.prev_hint.append((5,a,square,val)) # For check_intersection_row function first index should be '5'
                        return f"There is intersection in row {a+1} in square {square+1}. with value of {val} "
                    self.add_possible_other_row(a,val,square)
            row1.clear()

    def check_intersection_col(self,b, check_next= False, if_check=False):
        col1 = list()
        colCount = 0
        for square in range(3):
            for i in range(square*3,(square*3)+3):
                for val in self.possible[i][b]:
                    colCount =0
                    for j in range(square*3,(square*3)+3):
                        if val in self.possible[j][b]:
                            colCount= colCount + 1
                    if colCount == 2:
                        if val not in col1:
                            col1.append(val)
                    

            for val in col1:
                if self.is_in_other_cols_of_grid(b,val,square):
                    pass
                else:
                    if check_next and (6,b,square,val) not in self.prev_hint:
                        if if_check == False:
                            self.prev_hint.append((6,b,square,val)) # For check_intersection_col function fist index should be '6'
                        return f"There is intersection claiming available in col{b+1} in square {square+1} with value of {val} "
                    self.add_possible_other_col(b,val,square)
            col1.clear()



    def check_intersection(self, check_next=False, if_check=False):
        for i in range(9):
            if check_next:
                if if_check:
                    return self.check_intersection_row(i, True, True)
                else:
                    return self.check_intersection_row(i, True)
            else:
                self.check_intersection_row(i)

        for j in range(9):
            if check_next:
                if if_check:
                    return self.check_intersection_col(j, True, True)
                else:
                    return self.check_intersection_col(j, True)
            else:
                self.check_intersection_col(j)
    
    def get_row_with_only_2_possible_hidden(self, a):
        rowPair = list()
        row = list()
        row = self.get_empty_row(a,0)
        hiddenPair = list()

        for i in row:
            for val1 in self.possible[a][i]:
                count =0
                pos1=i
                for j in row:
                    if i !=j:
                        if val1 in self.possible[a][j]:
                            count += 1
                            pos2 = j
                if count == 1:
                    if len(rowPair) ==0:
                        rowPair.append([val1,pos1,pos2])
                    else:
                        if [val1,pos1,pos2] not in rowPair and [val1,pos2,pos1] not in rowPair:
                            rowPair.append([val1,pos1,pos2])

        for i in range(len(rowPair)):
            for j in range(len(rowPair)):
                if i !=j:
                    if rowPair[i][1] == rowPair[j][1] and rowPair[i][2] == rowPair[j][2] or rowPair[i][1] == rowPair[j][2] and rowPair[i][2] == rowPair[j][1]:
                        # if [rowPair[i][0],rowPair[i][1],rowPair[i][2]] not in hiddenPair and [rowPair[i][0],rowPair[i][2],rowPair[i][1]] not in hiddenPair:
                            hiddenPair.append([rowPair[i][0],rowPair[i][1],rowPair[i][2]])

        row.clear()
        rowPair.clear()
        return hiddenPair
    
    def get_col_with_only_2_possible_hidden(self, b):
        colPair = list()
        col = list()
        col = self.get_empty_col(0,b)
        hiddenPair = list()

        for i in col:
            for val1 in self.possible[i][b]:
                count =0
                pos1=i
                for j in col:
                    if i !=j:
                        if val1 in self.possible[j][b]:
                            count += 1
                            pos2 = j
                if count == 1:
                    if len(colPair) ==0:
                        colPair.append([val1,pos1,pos2])
                    else:
                        if [val1,pos1,pos2] not in colPair and [val1,pos2,pos1] not in colPair:
                            colPair.append([val1,pos1,pos2])

        for i in range(len(colPair)):
            for j in range(len(colPair)):
                if i !=j:
                    if colPair[i][1] == colPair[j][1] and colPair[i][2] == colPair[j][2] or colPair[i][1] == colPair[j][2] and colPair[i][2] == colPair[j][1]:
                        # if [rowPair[i][0],rowPair[i][1],rowPair[i][2]] not in hiddenPair and [rowPair[i][0],rowPair[i][2],rowPair[i][1]] not in hiddenPair:
                            hiddenPair.append([colPair[i][0],colPair[i][1],colPair[i][2]])
        col.clear()
        colPair.clear()
        return hiddenPair

    def get_row_with_only_2_possible(self, a):
        rowPair = list()
        row = list()
        row = self.get_empty_row(a,0)

        for i in row:
            if len(self.possible[a][i]) == 2:
                rowPair.append(i)

        row.clear()
        return rowPair
    
    def get_col_with_only_2_possible(self, b):
        colPair = list()
        col = list()
        col = self.get_empty_col(0,b)

        for j in col:
            if len(self.possible[j][b]) ==2:
                colPair.append(j)

        col.clear()
        return colPair

    def add_possible_except_pair_row(self,a, b1, b2):
        row = list()
        row = self.get_empty_row(a,0)

        for val in self.possible[a][b1]:
            for col in row:
                if col !=b1 and col != b2:
                    if val in self.possible[a][col]:
                        self.possible[a][col].remove(val)

    def add_possible_except_pair_col(self, b, a1, a2):
        col = list()
        col = self.get_empty_col(0,b)

        for val in self.possible[a1][b]:
            for row in col:
                if row != a1 and row != a2:
                    if val in self.possible[row][b]:
                        self.possible[row][b].remove(val)
    

    def check_naked_pair(self, check_next=False, if_check=False):
        rowPair = list()
        sum1=0
        sum2=0

        for i in range(9): # check row
            rowPair = self.get_row_with_only_2_possible(i)
            for col1 in rowPair:
                    for col2 in rowPair:
                        if col1 != col2:
                            if len(self.possible[i][col2]) == 2 and len(self.possible[i][col1]) == 2 :
                                if self.possible[i][col1][0] == self.possible[i][col2][0] and self.possible[i][col1][1]==self.possible[i][col2][1]: # check row pair
                                    if check_next and (7,i,self.possible[i][col1]) not in self.prev_hint:
                                        if if_check == False:
                                            self.prev_hint.append((7,i,self.possible[i][col1])) #For check_naked_pair funtion fist index should be '7'
                                        return f"Naked pair in row {i+1}, cols{col1,col2} and values{self.possible[i][col1]} "
                                    self.add_possible_except_pair_row(i, col1, col2)
                    
            rowPair.clear()

        colPair = list()
        
        for j in range(9): # check col
            colPair = self.get_col_with_only_2_possible(j)
            for row1 in colPair:
                for row2 in colPair:
                    if row1 != row2:
                        if len(self.possible[row2][j]) == 2 and len(self.possible[row1][j]) == 2:
                            if self.possible[row1][j][0] == self.possible[row2][j][0] and self.possible[row1][j][1] == self.possible[row2][j][1]:
                                if check_next and (13,j,self.possible[row1][j]) not in self.prev_hint:
                                    if if_check == False:
                                            self.prev_hint.append((13,j,self.possible[row1][j])) #For check_naked_pair funtion fist index should be '7'
                                    return f"Naked pair in rows{row1,row2} col {j+1} and values{self.possible[row2][j]} "
                                self.add_possible_except_pair_col(j,row1,row2)
                   
            colPair.clear()           


    def check_hidden_pair(self, check_next=False, if_check=False):
        hiddenPair = list()

        for i in range(9): # check row
            hiddenPair = self.get_row_with_only_2_possible_hidden(i)
            if len(hiddenPair) > 1:
                for col1 in hiddenPair[0][1:]:
                    for val1 in self.possible[i][col1]:
                        if val1 != hiddenPair[0][0] and val1 !=hiddenPair[1][0]:
                            if check_next and (7,i,hiddenPair[0][0],hiddenPair[0][0]) not in self.prev_hint:
                                if if_check == False:
                                    self.prev_hint.append((7,i,hiddenPair[0][0],hiddenPair[0][0])) #For check_naked_pair funtion fist index should be '7'
                                return f"Hidden pair in row {i+1}, cols{hiddenPair[0][1:]} and values{hiddenPair[0][0]},{hiddenPair[1][0]}  "
                            self.possible[i][col1].remove(val1)
                    
            hiddenPair.clear()

        hiddenPair = list()
        
        for j in range(9): # check col
            hiddenPair = self.get_col_with_only_2_possible_hidden(j)
            if len(hiddenPair) > 1:
                for row1 in hiddenPair[0][1:]:
                    for val1 in self.possible[row1][j]:
                        if val1 != hiddenPair[0][0] and val1 !=hiddenPair[1][0]:
                            if check_next and (13,i,hiddenPair[0][0],hiddenPair[1][0]) not in self.prev_hint:
                                if if_check == False:
                                    self.prev_hint.append((13,j,hiddenPair[0][0],hiddenPair[1][0])) #For check_naked_pair col funtion fist index should be '13'
                                return f"Hidden pair in rows{hiddenPair[0][1:]}, col {j+1} and values{hiddenPair[0][0]}, {hiddenPair[1][0]} "
                            self.possible[row1][j].remove(val1)
                   
            hiddenPair.clear()         

    def check_pos_in_same_grid(self, b1, b2):

        if b1<3 and b2<3:
            return True
        elif b1>3 and b1<6 and b2>3 and b2<6:
            return True
        elif b1>6 and b1<9 and b2>6 and b2<9:
            return True
        else:
            return False

    def add_possible_grid_interscetion_claiming_row(self, val, a, b1, b2):

        for i in range((a//3)*3, (a//3*3)+3):
            if i != a:
                for j in range(b1//3*3,(b1//3*3)+3):
                    if self.result[i][j] == 0:
                        if val in self.possible[i][j]:
                            self.possible[i][j].remove(val)

    def add_possible_grid_interscetion_claiming_col(self, val, b, a1, a2):

        for i in range(a1//3*3, (a1//3*3)+3):
            for j in range(b//3*3,(b//3*3)+3):
                if j != b:
                    if self.result[i][j] == 0:
                        if val in self.possible[i][j]:
                            self.possible[i][j].remove(val)


    def check_intersection_claiming(self, check_next=False, if_check=False):
        row = list()
        col = list()

        for i in range(9): #check row
            row = self.get_empty_row(i,0)
            for col1 in row:
                for val1 in self.possible[i][col1]:
                    count=0
                    for col2 in row:
                        for val2 in self.possible[i][col2]:
                            if val1 == val2:
                                count = count +1
                    if count == 2: # assume only one value will be there in a row
                        val = val1
                        for col3 in row:
                            if col1 != col3:
                                if val in self.possible[i][col3]:
                                    if self.check_pos_in_same_grid(col1,col3):
                                        if check_next and (8,i,col1,col2, val) not in self.prev_hint:
                                            if if_check == False:
                                                self.prev_hint.append((8,i,col1,col2, val)) # For check_intersection_claiming function first index should be '8'
                                            return f"Intersection claiming in row {i+1}, cols {col1+1}, {col3+1}, val{val} "
                                        self.add_possible_grid_interscetion_claiming_row(val,i,col1,col3)

            row.clear()


        for j in range(9):
            col = self.get_empty_col(0,j)
            for row1 in col:
                for val1 in self.possible[row1][j]:
                    count=0
                    for row2 in col:
                        for val2 in self.possible[row2][j]:
                            if val1 == val2:
                                count= count +1        
                    if count ==2:
                        val= val1
                        for row3 in col:
                            if row1 !=row3:
                                if val in self.possible[row3][j]:
                                    if self.check_pos_in_same_grid(row1,row3):
                                        if check_next:
                                            return f"Intersection claiming in col {j+1}, rows {row1+1}, {row3+1} "
                                        self.add_possible_grid_interscetion_claiming_col(val,j,row1,row3)
            col.clear()

    def fact(self, n):
        fact= 1
        for i in range(1,n+1):
            fact = fact*i
        return fact

    def get_empty_row_less_than_4_possible(self,a):
        row=list()
        for k in range(9):
                if self.is_empty_val(a,k) and len(self.possible[a][k])<4 and len(self.possible[a][k])>1:
                    row.append(k)
        return row
    
    def get_empty_col_less_than_4_possible(self,b):
        col=list()
        for k in range(9):
                if self.is_empty_val(k,b) and len(self.possible[k][b])<4 and len(self.possible[k][b])>1:
                    col.append(k)
        return col
    
    def get_combination_3(self,arr,n,r):
        c = int(self.fact(n)/(self.fact(r)* self.fact(n-r)) )             
        combo = [[0 for i in range(r)]for j in range(c)]
        data= [0]*r
        i = 0
        k = 0
        n = r-1
        m = 1
        count= 0
        v=0

        while i <= len(arr):
            if k==r:
                combo[v].clear()
                for j in range(r):
                    #print(data[j], end=" ")
                    combo[v].append(data[j])
                #print()
                v = v + 1
                k=k-1

            if  n ==len(arr):
                    i=m
                    n=m+(r-1)
                    m = m+ 1
                    k=0
                    count = count + 1

            # if count == r-1:  for 2
            #      break
            if m>= len(arr)-1-(r-1)+2: # for 3
                break

            if i == len(arr):  
                i=n  
                n= n+1
                k=k-1       

            data[k] = arr[i]

            i = i+1
            k = k+1
        return combo
    
    def get_combination_2(self,arr,n,r):
        c = 3            
        combo = [[0 for i in range(r)]for j in range(c)]
        data= [0]*r
        i = 0
        k = 0
        n = r-1
        m = 1
        count= 0
        v=0

        while i <= len(arr):
            if k==r:
                combo[v].clear()
                for j in range(r):
                    #print(data[j], end=" ")
                    combo[v].append(data[j])
                #print()
                v = v + 1
                k=k-1

            if  n ==len(arr):
                    i=m
                    n=m+(r-1)
                    m = m+ 1
                    k=0
                    count = count + 1

            if count == r-1:  #for 2
                 break
            # if m>= len(arr)-1-(r-1)+2: # for 3
            #     break

            if i == len(arr):  
                i=n  
                n= n+1
                k=k-1       

            data[k] = arr[i]

            i = i+1
            k = k+1
        return combo    
    

    def is_naked_triple_row(self,a, row, DoubleList):
        count =0
        count2 = 0
        p=list()

        for k in range(3):
            for val in DoubleList[k]:
                if val not in p:
                    p.append(val)
        
        for col in row:
            if len(self.possible[a][col]) == 3:
                if p[0] in self.possible[a][col] and p[1] in self.possible[a][col] and p[2] in self.possible[a][col]:
                    count = count + 1
            elif len(self.possible[a][col]) == 2:
                count2 = 0
                for val in p:
                    if val in self.possible[a][col]:
                        count2 = count2 + 1
                if count2 ==2:
                    count = count + 1

        if count == 3:
            return True
        else:
            return False
        
    def is_naked_triple_col(self,b,col,DoubleList):
        count =0
        count2 = 0
        p=list()

        for k in range(3):
            for val in DoubleList[k]:
                if val not in p:
                    p.append(val)
        
        for row in col:
            if len(self.possible[row][b]) == 3:
                if p[0] in self.possible[row][b] and p[1] in self.possible[row][b] and p[2] in self.possible[row][b]:
                    count = count + 1
            elif len(self.possible[row][b]) == 2:
                count2 = 0
                for val in p:
                    if val in self.possible[row][b]:
                        count2 = count2 + 1
                if count2 ==2:
                    count = count + 1

        if count == 3:
            return True
        else:
            return False
        
    def is_naked_triple_square(self, sq, DoubleList):
        count =0
        count2 = 0
        p=list()

        for k in range(3):
            for val in DoubleList[k]:
                if val not in p:
                    p.append(val)
        
        for i,j in sq:
            if len(self.possible[i][j]) == 3:
                if p[0] in self.possible[i][j] and p[1] in self.possible[i][j] and p[2] in self.possible[i][j]:
                    count = count + 1
            elif len(self.possible[i][j]) == 2:
                count2 = 0
                for val in p:
                    if val in self.possible[i][j]:
                        count2 = count2 + 1
                if count2 ==2:
                    count = count + 1

        if count == 3:
            return True
        else:
            return False

    def get_naked_triple_row(self,a,row,DoubleList):
        rowTriple=list()
        count2=0
        p=list()
        for k in range(3):
            for val in DoubleList[k]:
                if val not in p:
                    p.append(val)

        for col in row:
            if len(self.possible[a][col]) == 3:
                if p[0] in self.possible[a][col] and p[1] in self.possible[a][col] and p[2] in self.possible[a][col]:
                    rowTriple.append(col)
            elif len(self.possible[a][col]) == 2:
                count2=0
                for val in p:
                    if val in self.possible[a][col]:
                        count2 = count2 + 1
                if count2 ==2:
                    rowTriple.append(col)

        return rowTriple
    
    def get_naked_triple_col(self,b,col,DoubleList):
        colTriple=list()
        count2=0
        p=list()
        for k in range(3):
            for val in DoubleList[k]:
                if val not in p:
                    p.append(val)

        for row in col:
            if len(self.possible[row][b]) == 3:
                if p[0] in self.possible[row][b] and p[1] in self.possible[row][b] and p[2] in self.possible[row][b]:
                    colTriple.append(row)
            elif len(self.possible[row][b]) == 2:
                count2=0
                for val in p:
                    if val in self.possible[row][b]:
                        count2 = count2 + 1
                if count2 ==2:
                    colTriple.append(row)

        return colTriple
        
    def add_possible_naked_triple_row(self, a, row, DoubleList):
        rowEmpty = self.get_empty_row(a,0)
        rowTriple = self.get_naked_triple_row(a,row,DoubleList)
        p=list()
        for k in range(3):
            for val in DoubleList[k]:
                if val not in p:
                    p.append(val)

        for col in rowEmpty:
            if col not in rowTriple:
                for val in p:
                    if val in self.possible[a][col]:
                        self.possible[a][col].remove(val)

    def add_possible_naked_triple_col(self, b, col, DoubleList):
        colEmpty = self.get_empty_col(0,b)
        colTriple = self.get_naked_triple_col(b,col,DoubleList)
        p=list()
        for k in range(3):
            for val in DoubleList[k]:
                if val not in p:
                    p.append(val)

        for row in colEmpty:
            if row not in colTriple:
                for val in p:
                    if val in self.possible[row][b]:
                        self.possible[row][b].remove(val)

    def get_empty_square_less_4_possible(self,a,b):
        sq = list()
        k=0
        for i in range(a*3,(a*3)+3):
            for j in range(b*3, (b*3)+3):
                if self.is_empty_val(i,j) and len(self.possible[i][j])<4 and len(self.possible[i][j])>1:
                    sq.append([i,j])
        return sq
    
    def get_naked_triple_square(self,a,b,sq,DoubleList):
        sqTriple=list()
        count2=0
        p=list()
        for k in range(3):
            for val in DoubleList[k]:
                if val not in p:
                    p.append(val)

        for i,j in sq:
            if len(self.possible[i][j]) == 3:
                if p[0] in self.possible[i][j] and p[1] in self.possible[i][j] and p[2] in self.possible[i][j]:
                    sqTriple.append([i,j])
            elif len(self.possible[i][j]) == 2:
                count2=0
                for val in p:
                    if val in self.possible[i][j]:
                        count2 = count2 + 1
                if count2 ==2:
                    sqTriple.append([i,j])

        return sqTriple

    def add_possible_naked_triple_square(self, a,b, sq, DoubleList):
        sqEmpty = self.get_empty_square(a,b)
        sqTriple = self.get_naked_triple_square(a,b,sq,DoubleList)
        p=list()
        for k in range(3):
            for val in DoubleList[k]:
                if val not in p:
                    p.append(val)

        for i,j in sqEmpty:
            if [i,j] not in sqTriple:
                for val in p:
                    if val in self.possible[i][j]:
                        self.possible[i][j].remove(val)

    def check_possible_square_each_naked_triple(self,a,b, check_next=False, if_check=False):
        sq = list()
        sqPoss =list()
        sq = self.get_empty_square_less_4_possible(a,b)

        if len(sq)>=3:
            for i,j in sq:
                for val in self.possible[i][j]:
                    count = 0
                    for k,l in sq:
                        if val in self.possible[k][l]:
                                count = count + 1
                    if count >= 2:
                        if val not in sqPoss:
                                sqPoss.append(val)   # add possibles occur more than 2 time 
            
            if len(sqPoss) >= 3:
                    if len(sqPoss) >3:
                        TripleList = self.get_combination_3(sqPoss,len(sqPoss), 3)
                        for T in TripleList:
                            DoubleList = self.get_combination_2(T,len(T), 2)
                            if self.is_naked_triple_square(sq,DoubleList):
                                if check_next:
                                    return f"Naked triple in sq {sq+1}, row {a+1}, col {b+1}, double list{DoubleList} "
                                self.add_possible_naked_triple_square(a,b,sq,DoubleList)
                            DoubleList.clear()
                        TripleList.clear()
                    elif len(sqPoss) ==3:
                        DoubleList = self.get_combination_2(sqPoss,len(sqPoss), 2)
                        if self.is_naked_triple_square(sq,DoubleList):
                                if check_next:
                                    return f"Naked triple in sq {sq+1}, row {a+1}, col {b+1}, double list{DoubleList} "
                                self.add_possible_naked_triple_square(a,b,sq,DoubleList)
                        DoubleList.clear()        
            sqPoss.clear()


    def check_naked_triple(self, check_next=False, if_check=False):
        row=list()
        rowPoss= list()
        col=list()
        colPoss = list()
        for a in range(9): #check row
            row = self.get_empty_row_less_than_4_possible(a)
            if len(row)>=3: 
                for col1 in row:
                    for val in self.possible[a][col1]:
                        count=0
                        for col2 in row:
                            if val in self.possible[a][col2]:
                                count = count +1
                        
                        if count >=2:
                            if val not in rowPoss:
                                rowPoss.append(val)   # add possibles occur more than 2 time 

                if len(rowPoss) >= 3:
                    if len(rowPoss) >3:
                        TripleList = self.get_combination_3(rowPoss,len(rowPoss), 3)
                        for T in TripleList:
                            DoubleList = self.get_combination_2(T,len(T), 2)
                            if self.is_naked_triple_row(a,row,DoubleList):
                                if check_next and (9,a,row,DoubleList) not in self.prev_hint:
                                    if if_check == False:
                                        self.prev_hint.append((9,a,row,DoubleList)) # For check_naked_triple function double possible row, first index should be '9'
                                    return f"Naked triple in row {a+1}, col {row+1}, combination {DoubleList} "
                                self.add_possible_naked_triple_row(a,row,DoubleList)
                            DoubleList.clear()
                        TripleList.clear()
                    elif len(rowPoss) ==3:
                        DoubleList = self.get_combination_2(rowPoss,len(rowPoss), 2)
                        if self.is_naked_triple_row(a,row,DoubleList):
                                if check_next and (10,a, row,DoubleList) not in self.prev_hint:
                                    if if_check == False:
                                        self.prev_hint.append((10,a, row,DoubleList)) # For check_naked_triple function triple possible row, fist index should be '10'
                                    return f"Naked triple in row {a+1}, col {row+1}, combination {DoubleList} "
                                self.add_possible_naked_triple_row(a,row,DoubleList)
                        DoubleList.clear()        
            rowPoss.clear()
            
        for b in range(9):  #check col
            col = self.get_empty_col_less_than_4_possible(b)
            if len(col)>=3:
                for row1 in col:
                    for val in self.possible[row1][b]:
                        count=0
                        for row2 in col:
                            if val in self.possible[row2][b]:
                                count = count +1
                        if count >=2:
                            if val not in colPoss:
                                colPoss.append(val)   # add possibles occur more than 2 time 
                
                if len(colPoss) >= 3:
                    if len(colPoss) >3:
                        TripleList = self.get_combination_3(colPoss,len(colPoss), 3)
                        for T in TripleList:
                            DoubleList = self.get_combination_2(T,len(T), 2)
                            if self.is_naked_triple_col(b,col,DoubleList):
                                if check_next and (11,b,col,DoubleList) not in self.prev_hint:
                                    if if_check == False:
                                        self.prev_hint.append((11,b,col,DoubleList)) # For check_naked_triple function double possible col, first index should be '11'
                                    return f"Naked triple in col {b+1}, row {col+1}, combination {DoubleList} "
                                self.add_possible_naked_triple_col(b,col,DoubleList)
                            DoubleList.clear()
                        TripleList.clear()
                    elif len(colPoss) ==3:
                        DoubleList = self.get_combination_2(colPoss,len(colPoss), 2)
                        if self.is_naked_triple_col(b,col,DoubleList):
                                if check_next and (12, b, col, DoubleList) not in self.prev_hint:
                                    if if_check == False:
                                        self.prev_hint.append((12, b, col, DoubleList)) # For check_naked_triple function triple possible col, fist index should be '12'
                                    return f"Naked triple in col {b+1}, row {col+1}, combination {DoubleList} "
                                self.add_possible_naked_triple_col(b,col,DoubleList)
                        DoubleList.clear()        
            colPoss.clear()

        for i in range(3): # check square
            for j in range(3):
                self.check_possible_square_each_naked_triple(i,j, check_next)

    def check_possible(self,check_next=False, if_check=False):
        for i in range(9):
            if check_next:
                if if_check:
                    return self.check_possible_with_row(i, True, True)
                else:
                    return self.check_possible_with_row(i, True)
            else:
                self.check_possible_with_row(i)

        for j in range(9):
            if check_next:
                if if_check:
                    return self.check_possible_with_col(j, True, True)
                else:
                    return self.check_possible_with_col(j, True)
            else:
                self.check_possible_with_col(j)

    def get_empty_square(self,a,b):
        sq = list()
        k=0
        for i in range(a*3,(a*3)+3):
            for j in range(b*3, (b*3)+3):
                if self.result[i][j] ==0:
                    sq.append([i,j])
        return sq


    def check_possible_square_each(self, a, b, check_next=False, if_check=False):
        # if possible 1 available only one time in a square, value '1' can be on that cell only
        sq = list()
        sq = self.get_empty_square(a,b)
        val=0
        for i,j in sq:
            for val1 in self.possible[i][j]:
                count = 0
                for k,l in sq:
                   for val2 in self.possible[k][l]:
                       if val1 == val2:
                           count = count + 1
                if count < 2:
                    val = val1
        
        for i,j in sq:
            if val in self.possible[i][j]:
                if check_next and (4,i,j,val) not in self.prev_hint:
                    if if_check == False:
                        self.prev_hint.append((4,i,j,val)) # For check_possible_square_each function first index should be '4'
                    return f"Hidden single in square contains row {i+1}, column {j+1}. with value of {val} "
                self.result[i][j] = val
                self.add_possible_row_col(i,j)
                self.add_possible_grid(i,j)
                self.possible[i][j].clear()
    

    def check_possible_square(self, check_next=False, if_check=False):
        for i in range(3):
            for j in range(3):
                if check_next:
                    if if_check:
                        return self.check_possible_square_each(i,j, True, True)
                    else:
                        return self.check_possible_square_each(i,j, True)
                else:
                    self.check_possible_square_each(i,j)

    def add_possible(self): # removes possible candidates for each row, col and square
        for i in range(9):
                for j in range(9):
                    if self.result[i][j] == 0:
                        self.add_possible_row(i,j) #
                        self.add_possible_column(i,j)
                        self.add_possible_square(i,j)
                    else:
                        self.possible[i][j].clear()
                            

    def add_values(self, check_next=False, if_check=False): # add values to the board if one possible available in the cell
        for i in range(9):
            for j in range(9):
                if len(self.possible[i][j]) != 9:
                    if len(self.possible[i][j]) == 1:
                        val = self.possible[i][j]
                        if check_next and (1,i,j,val) not in self.prev_hint:
                            if if_check == False:
                                self.prev_hint.append((1,i,j,val)) # add_valued function first index should be '1'
                            return f"There is only one possible value in row {i+1}, column {j+1}. with value of {val} "
                        val = self.possible[i][j].pop()
                        self.result[i][j] = val
                        self.add_possible_row_col(i,j)
                        self.add_possible_grid(i,j)
                        self.possible[i][j].clear()



                
            
    def play(self):
        self.add_possible()
        while True:
            self.add_values()
            self.check_possible()
            self.check_possible_square()
            self.check_intersection()
            self.check_naked_pair()
            self.check_hidden_pair()
            self.check_intersection_claiming()
            self.check_naked_triple()
            self.is_board_contains_zero()
            self.print_board()
            

            if self.winner == False:
                self.print_board()
                print("You have won")
                break
            


if __name__ == "__main__":
    player = Sd()
    #player.get_board()
    # player.print_board()
    player.play() # this code will solve till challenging sudoku