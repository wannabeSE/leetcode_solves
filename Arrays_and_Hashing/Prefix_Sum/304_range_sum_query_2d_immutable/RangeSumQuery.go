package main

import "fmt"

type NumMatrix struct {
	matrix [][]int
}

func Constructor(matrix [][]int) NumMatrix {
	m := matrix
	prefixMatrix := make([][]int, len(matrix)+1)
	for i := range prefixMatrix {
		prefixMatrix[i] = make([]int, len(matrix[0])+1) //this line fill up that index with 0 as we are using `make` the 2nd param will fill up that index with that many 0s
	}
	for i := range m {
		for j := range m[0] {
			// current = m[i][j]
			// left = prefixMatrix[i+1][j]
			// above = prefixMatrix[i][j+1]
			// diagonal = prefixMatrix[i][j] {as (r_0, c_0) will be added in every cell so we have to deduct it to so that it does not alter the calculation by adding the same value twice}
			// Building padded 2D prefix at cell (i, j) in the ORIGINAL matrix.
			// Stored at prefix[i+1][j+1] because row 0 / col 0 of prefix are zeros.
			//
			// Goal: prefix[i+1][j+1] == sum of ALL cells from (0,0) through (i,j).
			//
			// Split that rectangle into four blocks:
			//
			//            cols 0 .. j-1          col j
			//          +------------------+------------+
			// rows     |                  |            |
			// 0..i-1   |        A         |     B      |
			//          |  (top-left)      |  (top)     |
			//          +------------------+------------+
			// row i    |        C         |     D      |
			//          |  (left)          |  (current) |
			//          +------------------+------------+
			//
			// Already computed:
			//   above  = prefix[i][j+1]   = sum(A) + sum(B)     // origin → (i-1, j)
			//   left   = prefix[i+1][j]   = sum(A) + sum(C)     // origin → (i, j-1)
			//   overlap= prefix[i][j]     = sum(A)              // origin → (i-1, j-1)
			//   current= m[i][j]          = D                   // only the new cell
			//
			// above + left = A+B + A+C = 2*A + B + C
			// so A is counted twice → subtract overlap once:
			//
			//   prefix[i+1][j+1] = above + left - overlap + current
			//                    = (A+B) + (A+C) - A + D
			//                    = A + B + C + D
			prefixMatrix[i+1][j+1] = prefixMatrix[i+1][j] + prefixMatrix[i][j+1] + m[i][j] - prefixMatrix[i][j]
		}
	}
	return NumMatrix{matrix: prefixMatrix}
}

func (this *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
	//the formula for first subtraction is to subtract the right-top from the (row2, col2) cause it is the max in col2
	//the formula for the next is to subtract the left-top from the (row2+1, col1) {***row2+1 as the array have padding of 0s on the left and top**} cause it is the max in col1.
	//all [+1] operation is to shift the position since the prefixMatrix has padding of 0s on the top and left.
	return (this.matrix[row2+1][col2+1] - this.matrix[row1][col2+1]) - (this.matrix[row2+1][col1] - this.matrix[row1][col1])
}
func matPrinter(m *[][]int) {
	for _, v := range *m {
		fmt.Println(v)
	}
}
func colPrinter(m *[][]int) {
	for i := range (*m)[0] {
		fmt.Println("i", i)
		for j := 1; j < len((*m)); j++ {
			fmt.Println("j", j)
			(*m)[j][i] = (*m)[j-1][i] + (*m)[j][i]
			fmt.Printf("Row %d Col %d the value -> %d \n", i, j, (*m)[j][i])
		}
	}
}
func main() {
	matrix := [][]int{{3, 0, 1, 4, 2}, {5, 6, 3, 2, 1}, {1, 2, 0, 1, 5}, {4, 1, 0, 1, 7}, {1, 0, 3, 0, 5}}
	m2 := [][]int{{7, 7, 0}, {-4, -7, 7}, {-4, 0, -2}, {-8, -5, 6}}
	nm := Constructor(matrix)
	nm2 := Constructor(m2)
	fmt.Println(nm, nm2)
	fmt.Println(nm.SumRegion(2, 1, 4, 3))
	fmt.Println(nm2.SumRegion(1, 0, 2, 2))
	fmt.Println(nm2.SumRegion(3, 2, 3, 2))
}
