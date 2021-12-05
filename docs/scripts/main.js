// Color Structure
let color = {
  data: 0,
  bg: "#000",
  fg: "#111",
  marked: "#DDD",
  bingo: "#001F3F",
  stroke: "#FFF",
  alpha: 1.0,
};
// Animation
let param = {
  sleep: 100,
};

//////////////////////////////////////////
// data struct
let data = new DATA();

let size = 1024;
let canvas = document.createElement("canvas");
canvas.style.position = "absolute";
canvas.style.top = "0";
canvas.style.left = "0";
canvas.width = canvas.height = size;
ctx = canvas.getContext("2d");
document.body.appendChild(canvas);

// GUI
let gui = new dat.GUI({ load: JSON });
gui.add(color, "data", /*min=*/ 0, /*max=*/ 0, /*step=*/ 1);
let colorGUI = gui.addFolder("Color");
{
  colorGUI.addColor(color, "bg");
  colorGUI.addColor(color, "fg");
  colorGUI.addColor(color, "marked");
  colorGUI.addColor(color, "bingo");
  colorGUI.addColor(color, "stroke");
  colorGUI.add(color, "alpha", 0.25, 1.0, 0.125);
  //colorGUI.open();
}
let paramsGUI = gui.addFolder("Params");
{
  paramsGUI.add(param, "sleep", 0, 4000, 50);
  //paramsGUI.open();
}
gui.close();

data.initNumbers();
data.initBoards();

let current = 0;

async function update() {
  ctx.restore();
  ctx.save();

  ctx.translate(0, 0);
  ctx.canvas.width = window.innerWidth;
  ctx.canvas.height = window.innerHeight;

  drawBG(ctx, color);
  data.checkBingo();
  data.drawBoards(ctx, color);

  // Remove next number or reset the board
  if (current < data.loto.length) {
    data.markCells(data.loto[current++]);
  } else {
    current = 0;
    data.initBoards();
  }
  await new Promise((r) => setTimeout(r, `${param.sleep}`));
  requestAnimationFrame(update);
}

function drawBG(ctx, color) {
  ctx.globalAlpha = 1;
  ctx.fillStyle = `${color.bg}`;
  ctx.fillRect(0, 0, ctx.canvas.width, ctx.canvas.height);
}

update();
