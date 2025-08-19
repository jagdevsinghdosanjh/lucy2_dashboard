window.onload = () => {
  const logo = document.getElementById('logo');

  // === Input values (to be dynamically injected later) ===
  const vix = window.vix || null;
  const rsi = window.rsi || null;
  const macd = window.macd || null;
  const signal = window.macdSignal || null;

  let duration = 4; // default breath cycle

  // === Priority Logic ===
  if (vix !== null) {
    duration = Math.max(2, 30 / vix);
    console.log("Animating based on VIX");
  } else if (rsi !== null) {
    duration = Math.max(2, 10 - (rsi / 15));
    console.log("Animating based on RSI");
  } else if (macd !== null && signal !== null) {
    const divergence = Math.abs(macd - signal);
    duration = Math.max(2, 6 - divergence * 2);
    console.log("Animating based on MACD divergence");
  }

  logo.style.animationDuration = `${duration.toFixed(2)}s`;
};

// const vix = 18; // example VIX value
// document.getElementById('logo').style.animationDuration = `${Math.max(2, 30/vix)}s`;

// // Example RSI value (replace with dynamic input later)
// const rsi = 65;

// // Map RSI (0–100) to breath speed: higher RSI = faster pulse
// const duration = Math.max(2, 10 - (rsi / 15)).toFixed(2);
// document.getElementById('logo').style.animationDuration = `${duration}s`;

// // Example MACD values
// const macd = 1.2;
// const signal = 0.8;

// // Calculate divergence
// const divergence = Math.abs(macd - signal);

// // Map divergence to pulse intensity
// const duration = Math.max(2, 6 - divergence * 2).toFixed(2);
// document.getElementById('logo').style.animationDuration = `${duration}s`;
