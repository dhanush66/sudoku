class Sd:
    def __init__(self) -> None:
        #self.board = [['_' for i in range(9)] for j in range(9)]
        self.board = [[8,0,0,0,0,0,5,0,3],
                      [0,7,3,1,0,8,0,2,0],
                      [2,0,4,0,7,5,1,6,0],
                      [0,5,9,0,0,0,0,8,0],
                      [0,0,2,0,0,0,7,0,0],
                      [0,4,0,0,0,0,9,3,0],
                      [0,2,5,9,3,0,8,0,7],
                      [0,3,0,7,0,4,2,5,0],
                      [4,0,7,0,0,0,0,0,1]]
        self.winner = True
        self.possible = [[[1,2,3,4,5,6,7,8,9] for i in range(9)] for j in range(9)]

    def get_board(self):
        print("Enter number if current position have value.")
        print("Enter '0' if current position dont have value.")
        for i in range(9):
            for j in range(9):
                self.board[i][j] = int(input(f"provide value for pos{i}{j}:"))
            print('')

    def print_board(self):
        for i in range(9):
            print('|',end=' ')
            for j in range(9):
            
                print(self.board[i][j] ,end=' ')
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
                if self.board[i][j] == 0:
                    self.winner = True
                    return

        self.winner = False
    
    def add_possible_row(self, a,b):
        for m in range(9):
            if self.board[a][m] != 0:
                if self.board[a][m] in self.possible[a][b]:
                    self.possible[a][b].remove(self.board[a][m])
          

    def add_possible_column(self, a,b):
        
        for m in range(9):
            if self.board[m][b] != 0:
                if self.board[m][b] in self.possible[a][b]:
                    self.possible[a][b].remove(self.board[m][b])


    def add_possible_square(self,a,b):
        m = (a//3) *3
        n = (b//3) * 3
        for m in range(m, m+3):
            for n in range(n, n+3):
                if self.board[m][n] != 0:
                    if self.board[m][n] in self.possible[a][b]:
                        self.possible[a][b].remove(self.board[m][n])
            n = (b//3) * 3


    def is_empty_val(self,a,b):
        if self.board[a][b] == 0:
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
                if self.board[a][m] != 0:
                    if self.board[a][m] in self.possible[a][r]:
                        self.possible[a][r].remove(self.board[a][m])

        for c in col:
             for m in range(9):
                if self.board[m][b] != 0:
                    if self.board[m][b] in self.possible[c][b]:
                        self.possible[c][b].remove(self.board[m][b])
            
    def add_possible_grid(self, a, b):
        val = self.board[a][b]

        for m in range((a//3)*3, (a//3)*3 +3):
            for n in range((b//3)*3, (b//3)*3 +3):
                if self.board[m][n] ==0:
                    if val in self.possible[m][n]:
                        self.possible[m][n].remove(val)


    def check_possible_with_row(self, a, b=0):
        #E.g  board [6,7,0,9,0,0,4,2,3]
        # possible [[],[],[5,8],[],[1,5,8],[5,8],[],[],[]]
        #  index    [0,1,2,3,4,5,6,7,8] 
        # here 4th index col can only have value '1' 
        row=list()
        row=self.get_empty_row(a,b)
        
        valueRow = 0
        for col in row:
            for val in self.possible[a][col]:
                count =0
                for eachCol in row:
                        if val not in self.possible[a][eachCol]:
                            count = count + 1
                if count == len(row) - 1:
                    valueRow = val
        for col in row:
            if valueRow in self.possible[a][col]:
                self.board[a][col] = valueRow
                self.add_possible_row_col(a,col)
                self.add_possible_grid(a,col)
                self.possible[a][col].clear()

    def check_possible_with_col(self, b, a=0):
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
                self.board[row][b] = valueCol
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
            

    def check_intersection_row(self,a):
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
                    self.add_possible_other_row(a,val,square)
            row1.clear()

    def check_intersection_col(self,b):
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
                    self.add_possible_other_col(b,val,square)
            col1.clear()



    def check_intersection(self):
        for i in range(9):
            self.check_intersection_row(i)

        for j in range(9):
            self.check_intersection_col(j)
    
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
    

    def check_naked_pair(self):
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
                                self.add_possible_except_pair_col(j,row1,row2)
                   
            colPair.clear()         

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
                    if self.board[i][j] == 0:
                        if val in self.possible[i][j]:
                            self.possible[i][j].remove(val)

    def add_possible_grid_interscetion_claiming_col(self, val, b, a1, a2):

        for i in range(a1//3*3, (a1//3*3)+3):
            for j in range(b//3*3,(b//3*3)+3):
                if j != b:
                    if self.board[i][j] == 0:
                        if val in self.possible[i][j]:
                            self.possible[i][j].remove(val)


    def check_intersection_claiming(self):
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

    def check_possible_square_each_naked_triple(self,a,b):
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
                                self.add_possible_naked_triple_square(a,b,sq,DoubleList)
                            DoubleList.clear()
                        TripleList.clear()
                    elif len(sqPoss) ==3:
                        DoubleList = self.get_combination_2(sqPoss,len(sqPoss), 2)
                        if self.is_naked_triple_square(sq,DoubleList):
                                self.add_possible_naked_triple_square(a,b,sq,DoubleList)
                        DoubleList.clear()        
            sqPoss.clear()


    def check_naked_triple(self):
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
                                self.add_possible_naked_triple_row(a,row,DoubleList)
                            DoubleList.clear()
                        TripleList.clear()
                    elif len(rowPoss) ==3:
                        DoubleList = self.get_combination_2(rowPoss,len(rowPoss), 2)
                        if self.is_naked_triple_row(a,row,DoubleList):
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
                                self.add_possible_naked_triple_col(b,col,DoubleList)
                            DoubleList.clear()
                        TripleList.clear()
                    elif len(colPoss) ==3:
                        DoubleList = self.get_combination_2(colPoss,len(colPoss), 2)
                        if self.is_naked_triple_col(b,col,DoubleList):
                                self.add_possible_naked_triple_col(b,col,DoubleList)
                        DoubleList.clear()        
            colPoss.clear()

        for i in range(3): # check square
            for j in range(3):
                self.check_possible_square_each_naked_triple(i,j)

    def check_possible(self):
        for i in range(9):
            self.check_possible_with_row(i)

        for j in range(9):
            self.check_possible_with_col(j)

    def get_empty_square(self,a,b):
        sq = list()
        k=0
        for i in range(a*3,(a*3)+3):
            for j in range(b*3, (b*3)+3):
                if self.board[i][j] ==0:
                    sq.append([i,j])
        return sq


    def check_possible_square_each(self, a, b):
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
                self.board[i][j] = val
                self.add_possible_row_col(i,j)
                self.add_possible_grid(i,j)
                self.possible[i][j].clear()
    

    def check_possible_square(self):
        for i in range(3):
            for j in range(3):
                self.check_possible_square_each(i,j)


    def add_possible(self): # removes possible candidates for each row, col and square
        for i in range(9):
                for j in range(9):
                    if self.board[i][j] == 0:
                        self.add_possible_row(i,j) #
                        self.add_possible_column(i,j)
                        self.add_possible_square(i,j)
                    else:
                        self.possible[i][j].clear()
                            

    def add_values(self): # add values to the board if one possible available in the cell
        for i in range(9):
            for j in range(9):
                if len(self.possible[i][j]) != 9:
                    if len(self.possible[i][j]) == 1:
                        self.board[i][j] = self.possible[i][j].pop()
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
            self.check_intersection_claiming()
            self.check_naked_triple()
            self.is_board_contains_zero()
            

            if self.winner == False:
                self.print_board()
                print("You have won")
                break
            
        
        

if __name__ == "__main__":
    player = Sd()
    #player.get_board()
    player.print_board()
    player.play() # this code will solve till challenging sudoku