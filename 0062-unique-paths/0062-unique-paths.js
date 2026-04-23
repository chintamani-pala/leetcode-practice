/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
 function createGrid(rows, columns, initialValue = 0) {
  let grid = [];
  for (let i = 0; i < rows; i++) {
    grid[i] = [];
    for (let j = 0; j < columns; j++) {
      grid[i][j] = initialValue; 
    }
  }
  return grid;
}
var uniquePaths = function(m, n) {
    var grid = createGrid(m,n)
    for(let i = 0; i<n; i++){
        grid[0][i] = 1
    }
    for(let i=0; i<m; i++){
        grid[i][0] = 1;
    }
    for(let i=1;i<m;i++){
        for(let j=1; j<n;j++){
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
        }
    }
    return grid[m-1][n-1]
};