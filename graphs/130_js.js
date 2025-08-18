/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solve = function(board) {

    if (!board || board.length === 0) return;

    const rows = board.length;
    const cols = board[0].length;

    // Step 1: DFS from border-connected 'O's, mark them as '#'
    function dfs(row, col) {
        if (row < 0 || col < 0 || row >= rows || col >= cols || board[row][col] !== 'O') return;
        board[row][col] = '#'; // we mark as escaped
        dfs(row+1, col);
        dfs(row-1, col);
        dfs(row, col+1);
        dfs(row, col-1);
    }

    // we run DFS for every border cell with 'O'
    for (let row = 0; row < rows; row++) {
        dfs(row, 0);
        dfs(row, cols - 1);
    }
    for (let col = 0; col < cols; col++) {
        dfs(0, col);
        dfs(rows - 1, col);
    }

    // Step 2: we flip all remaining 'O' to 'X'
    // Step 3: we flip '#' back to 'O'
    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            if (board[row][col] === 'O') board[row][col] = 'X';
            else if (board[row][col] === '#') board[row][col] = 'O';
        }
    }

};