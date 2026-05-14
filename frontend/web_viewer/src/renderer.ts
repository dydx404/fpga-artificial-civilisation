const palette: Array<[number, number, number]> = [
  [44, 162, 95],
  [222, 45, 38],
  [49, 130, 189],
  [117, 107, 177]
];

export function renderStrategyGrid(
  canvas: HTMLCanvasElement,
  strategies: Uint8Array,
  width: number,
  height: number
): void {
  const context = canvas.getContext("2d");
  if (!context) {
    return;
  }

  canvas.width = width;
  canvas.height = height;
  const image = context.createImageData(width, height);

  for (let idx = 0; idx < strategies.length; idx += 1) {
    const colour = palette[strategies[idx] & 3];
    const out = idx * 4;
    image.data[out] = colour[0];
    image.data[out + 1] = colour[1];
    image.data[out + 2] = colour[2];
    image.data[out + 3] = 255;
  }

  context.putImageData(image, 0, 0);
}

export function randomDemoFrame(width: number, height: number, generation: number): Uint8Array {
  const frame = new Uint8Array(width * height);
  for (let y = 0; y < height; y += 1) {
    for (let x = 0; x < width; x += 1) {
      const wave = Math.sin((x + generation) * 0.08) + Math.cos((y - generation) * 0.06);
      frame[y * width + x] = wave > 0 ? 0 : 1;
    }
  }
  return frame;
}

