// depend on input.js to get RAW_DATA global
class DATA {
  constructor() {
    this.loto = [];
    this.boards = [];
  }

  initNumbers() {
    // Doesn't work since null origin is forbidden by cors
    // when opening file:index.html in a browser (server-less)
    fetch("scripts/input.txt")
      .then(response => response.text())
      .then(data => {
        //console.log(data);
        this.loto = data
          .split("\n\n", 1)[0]
          .split(",")
          .map(Number);
      })
      .catch(error => console.error(error));

    //console.log(RAW_DATA);
    //this.loto = RAW_DATA
    //  .split("\n\n", 1)[0]
    //  .split(",")
    //  .map(Number);
    //console.log({ loto: this.loto });
  }

  initBoards() {
    // Doesn't work since null origin is forbidden by cors
    // when opening file:index.html in a browser (server-less)
    fetch("scripts/input.txt")
      .then(response => response.text())
      .then(data => {
        //console.log(data);
        this.boards = data
          .slice(data.indexOf("\n\n")+2) // ignore the number list
          .trim()
          .split("\n\n") // split boards
          .map((board) => {
            return board
              .split("\n") // split rows
              .map((row) => {
                return row
                  .trim()
                  .split(/\s+/) // split numbers
                  .map((value) => {
                    return { value: Number(value)}
                  });
              });
          });
      })
      .catch(error => console.error(error));


    //console.log(RAW_DATA);
    //this.boards = RAW_DATA
    //  .slice(RAW_DATA.indexOf("\n\n")+2) // ignore the number list
    //  .split("\n\n") // split boards
    //  .map((board) => {
    //    return board
    //      .split("\n") // split rows
    //      .map((row) => {
    //        return row
    //          .trim()
    //          .split(/\s+/) // split numbers
    //          .map((value) => {
    //            return { value: Number(value)}
    //          });
    //      });
    //  });
    //console.log({ boards: this.boards });
  }

  drawBoards(ctx, color) {
    // draw boards sqrt(n) x sqrt(n)
    let quotient = Math.sqrt(this.boards.length);
    //console.log({ quotient: quotient});
    let board_size = {
      width: ctx.canvas.width / quotient,
      height: ctx.canvas.height / quotient,
    };

    for (let i = 0; i < this.boards.length; ++i) {
      let board_pos = {
        x: (i % 10) * board_size.width,
        y: parseInt(i / 10) * board_size.height,
      };
      this.drawBoard(this.boards[i], ctx, color, board_pos, board_size);
    }
  }

  drawBoard(board, ctx, color, pos, size) {
    ctx.globalAlpha = color.alpha;
    ctx.strokeStyle = color.stroke;
    let cell_size = {
      width: size.width / board[0].length,
      height: size.height / board.length,
    };
    for (let row = 0; row < board.length; ++row) {
      for (let col = 0; col < board[0].length; ++col) {
        let value = board[row][col].value;
        if (value === 'marked') {
          ctx.fillStyle = color.marked;
        } else if (value === 'bingo') {
          ctx.fillStyle = color.bingo;
        } else {
          ctx.fillStyle = color.fg;
        }
        ctx.fillRect(
          pos.x + col * cell_size.width,
          pos.y + row * cell_size.height,
          cell_size.width,
          cell_size.height);
      }
    }
  }

  markCells(num) {
    this.boards.forEach((board) => {
      board.forEach((row) => {
        row.forEach((cell) => {
          if (cell.value === num) {
            cell.value = 'marked';
          }
        });
      });
    });
  }

  checkBingo() {
    this.boards.forEach((board) => {
      this.checkBoard(board);
    });
  }

  checkBoard(board) {
    // check horizontal
    for (let row = 0; row < board.length; ++row) {
      let bingo = true;
      for (let col = 0; col < board[row].length; ++col) {
        let value = board[row][col].value;
        if (value !== 'marked') {
          bingo = false;
          break;
        }
      }
      if (bingo) {
        //console.log("bingo!");
        for (let col = 0; col < board[row].length; ++col) {
          board[row][col].value = 'bingo';
        }
      }
    }
    // check vertical
    for (let col = 0; col < board[0].length; ++col) {
      let bingo = true;
      for (let row = 0; row < board.length; ++row) {
        let value = board[row][col].value;
        if (value !== 'marked') {
          bingo = false;
          break;
        }
      }
      if (bingo) {
        //console.log("bingo!");
        for (let row = 0; row < board[0].length; ++row) {
          board[row][col].value = 'bingo';
        }
      }
    }
  }
}
