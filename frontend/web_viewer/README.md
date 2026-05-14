# Web Viewer

This is a minimal TypeScript canvas viewer scaffold. It currently renders a synthetic strategy field so frontend work can start before the PYNQ stream is ready.

## Setup

```bash
cd frontend/web_viewer
npm install
npm run dev
```

## Planned Protocol

The viewer should eventually subscribe to JSON metrics and binary or encoded frame data from the PYNQ TCP/WebSocket bridge.

