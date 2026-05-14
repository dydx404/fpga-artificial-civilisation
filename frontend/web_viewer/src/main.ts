import { randomDemoFrame, renderStrategyGrid } from "./renderer";

const root = document.querySelector<HTMLDivElement>("#app") ?? document.body.appendChild(document.createElement("div"));
root.innerHTML = `
  <main class="shell">
    <section class="toolbar">
      <h1>FPGA Artificial Civilisation Engine</h1>
      <div id="stats">generation 0</div>
    </section>
    <canvas id="world"></canvas>
  </main>
`;

const style = document.createElement("style");
style.textContent = `
  html, body, #app { margin: 0; width: 100%; height: 100%; background: #101216; color: #f5f7fb; font-family: system-ui, sans-serif; }
  .shell { min-height: 100%; display: grid; grid-template-rows: auto 1fr; }
  .toolbar { display: flex; justify-content: space-between; align-items: center; gap: 16px; padding: 12px 16px; border-bottom: 1px solid #2b3038; }
  h1 { font-size: 18px; font-weight: 650; margin: 0; letter-spacing: 0; }
  #stats { font-variant-numeric: tabular-nums; color: #c9d1dd; }
  #world { width: 100%; height: calc(100vh - 54px); image-rendering: pixelated; object-fit: contain; background: #050609; }
`;
document.head.appendChild(style);

const canvas = document.querySelector<HTMLCanvasElement>("#world");
const stats = document.querySelector<HTMLDivElement>("#stats");
if (!canvas || !stats) {
  throw new Error("viewer elements were not created");
}

const width = 192;
const height = 128;
let generation = 0;

function tick(): void {
  const frame = randomDemoFrame(width, height, generation);
  renderStrategyGrid(canvas, frame, width, height);
  const cooperation = frame.reduce((count, value) => count + (value === 0 ? 1 : 0), 0) / frame.length;
  stats.textContent = `generation ${generation} | cooperation ${cooperation.toFixed(3)} | demo feed`;
  generation += 1;
  window.requestAnimationFrame(tick);
}

tick();

