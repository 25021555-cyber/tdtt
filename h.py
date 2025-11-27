<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Chúc mừng sinh nhật!</title>
  <style>
    :root{--bg:#0f172a;--card:#0b1220;--accent:#ff6b6b;--accent2:#ffd166;--glass:rgba(255,255,255,0.06)}
    *{box-sizing:border-box}
    html,body{height:100%;margin:0;font-family:Inter,ui-sans-serif,system-ui,Segoe UI,Roboto,"Helvetica Neue",Arial}
    body{background:linear-gradient(160deg,#0b1220 0%, #071132 50%, #02142a 100%);color:#eef2ff;display:flex;align-items:center;justify-content:center;padding:24px}

    .card{width:100%;max-width:980px;background:linear-gradient(180deg,rgba(255,255,255,0.02),transparent);border-radius:18px;padding:28px;box-shadow:0 10px 30px rgba(2,6,23,0.6);backdrop-filter:blur(6px);border:1px solid rgba(255,255,255,0.04);display:grid;grid-template-columns:1fr 380px;gap:24px}

    .left{padding:18px}
    h1{margin:0 0 6px;font-size:34px;letter-spacing:-0.5px}
    p.lead{margin:0 0 16px;color:#cbd5e1}

    .name-input, .msg-input{width:100%;padding:10px 12px;border-radius:10px;border:1px solid rgba(255,255,255,0.06);background:transparent;color:inherit;font-size:16px}
    label{font-size:13px;color:#94a3b8}
    .controls{display:flex;gap:10px;margin-top:12px}
    .btn{background:var(--accent);color:#0b1220;padding:10px 14px;border-radius:10px;border:none;font-weight:600;cursor:pointer}
    .btn.ghost{background:transparent;border:1px solid rgba(255,255,255,0.06);color:var(--accent2)}

    .preview{margin-top:18px;padding:14px;border-radius:12px;background:linear-gradient(90deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));border:1px solid rgba(255,255,255,0.03)}
    .preview .card-inner{display:flex;align-items:center;gap:14px}
    .cake{width:76px;height:76px;border-radius:12px;background:linear-gradient(180deg,#ffd166,#ff9a9e);display:flex;align-items:center;justify-content:center;font-weight:700;color:#2b2b2b}
    .message{flex:1}
    .message h2{margin:0;font-size:20px;color:#fff}
    .message p{margin:4px 0 0;color:#cbd5e1}

    /* right column */
    .right{padding:18px;border-left:1px dashed rgba(255,255,255,0.02)}
    .actions{display:flex;flex-direction:column;gap:10px}
    .confetti-canvas{position:absolute;pointer-events:none;inset:0}

    footer{margin-top:12px;color:#9aa4b2;font-size:13px}

    /* small screens */
    @media (max-width:880px){.card{grid-template-columns:1fr;max-width:720px}.right{border-left:none;border-top:1px dashed rgba(255,255,255,0.02)}}
  </style>
</head>
<body>
  <div class="card" id="app">
    <div class="left">
      <h1>Chúc mừng sinh nhật!</h1>
      <p class="lead">Tạo lời chúc sinh nhật nhanh và đẹp. Nhập tên và thông điệp, sau đó nhấn "Tạo" để xem trước.</p>

      <div>
        <label for="name">Tên người nhận</label>
        <input id="name" class="name-input" placeholder="Ví dụ: Linh" value="Bạn thân">
      </div>

      <div style="margin-top:12px">
        <label for="message">Lời chúc</label>
        <textarea id="message" rows="4" class="msg-input" placeholder="Viết lời chúc ở đây...">Chúc mừng sinh nhật! Chúc bạn luôn vui, khỏe, và thành công!</textarea>
      </div>

      <div class="controls">
        <button class="btn" id="apply">Tạo & Hiển thị</button>
        <button class="btn ghost" id="toggleMusic">Bật nhạc</button>
        <button class="btn ghost" id="download">Tải về</button>
      </div>

      <div class="preview" id="preview">
        <div class="card-inner">
          <div class="cake" id="cake">🎂</div>
          <div class="message">
            <h2 id="previewName">Chúc mừng, Bạn thân!</h2>
            <p id="previewMsg">Chúc mừng sinh nhật! Chúc bạn luôn vui, khỏe, và thành công!</p>
          </div>
        </div>
      </div>

      <footer>Thiết kế đẹp, responsive — chia sẻ cho bạn bè nhé!</footer>
    </div>

    <div class="right">
      <h3>Tuỳ chọn</h3>
      <div class="actions">
        <label><input type="checkbox" id="showConfetti" checked> Hiện pháo hoa (confetti)</label>
        <label><input type="checkbox" id="showCandles" checked> Hiện nến trên bánh</label>
        <label>Chọn chủ đề màu:
          <select id="theme">
            <option value="default">Tươi sáng</option>
            <option value="pink">Hồng ấm</option>
            <option value="blue">Xanh dịu</option>
            <option value="dark">Tối thanh lịch</option>
          </select>
        </label>
      </div>

      <div style="margin-top:18px">
        <h4>Chia sẻ nhanh</h4>
        <button class="btn ghost" id="shareLink">Sao chép liên kết (mock)</button>
      </div>
    </div>

    <canvas id="confetti" class="confetti-canvas"></canvas>
  </div>

  <audio id="bgm" loop preload="auto">
    <source src="https://cdn.pixabay.com/download/audio/2022/03/15/audio_9a9a9c3b9b.mp3?filename=happy-birthday-10986.mp3" type="audio/mpeg">
  </audio>

  <script>
    // Elements
    const nameEl = document.getElementById('name');
    const msgEl = document.getElementById('message');
    const applyBtn = document.getElementById('apply');
    const previewName = document.getElementById('previewName');
    const previewMsg = document.getElementById('previewMsg');
    const cake = document.getElementById('cake');
    const toggleMusic = document.getElementById('toggleMusic');
    const bgm = document.getElementById('bgm');
    const confettiCanvas = document.getElementById('confetti');
    const showConfetti = document.getElementById('showConfetti');
    const showCandles = document.getElementById('showCandles');
    const themeSelect = document.getElementById('theme');
    const downloadBtn = document.getElementById('download');
    const shareBtn = document.getElementById('shareLink');

    // Apply button
    applyBtn.addEventListener('click', ()=>{
      const n = nameEl.value.trim() || 'Bạn';
      previewName.textContent = `Chúc mừng, ${n}!`;
      previewMsg.textContent = msgEl.value.trim() || 'Chúc mừng sinh nhật!';

      // cake content
      cake.textContent = showCandles.checked ? '🎂' : '🍰';

      // confetti
      if(showConfetti.checked){ startConfetti(); }
    });

    // Music
    let musicOn = false;
    toggleMusic.addEventListener('click', ()=>{
      musicOn = !musicOn;
      if(musicOn){ bgm.play(); toggleMusic.textContent='Tắt nhạc'; toggleMusic.classList.remove('ghost'); }
      else { bgm.pause(); bgm.currentTime=0; toggleMusic.textContent='Bật nhạc'; toggleMusic.classList.add('ghost'); }
    });

    // Theme switch
    themeSelect.addEventListener('change', ()=>{
      const t = themeSelect.value;
      document.documentElement.style.setProperty('--accent','#ff6b6b');
      document.documentElement.style.setProperty('--accent2','#ffd166');
      if(t==='pink'){ document.documentElement.style.setProperty('--accent','#ff9bb3'); document.documentElement.style.setProperty('--accent2','#ffd6e0'); }
      if(t==='blue'){ document.documentElement.style.setProperty('--accent','#6ea8fe'); document.documentElement.style.setProperty('--accent2','#c6e2ff'); }
      if(t==='dark'){ document.documentElement.style.setProperty('--accent','#7c5cff'); document.documentElement.style.setProperty('--accent2','#a59bff'); }
    });

    // Download preview as image (simple)
    downloadBtn.addEventListener('click', async ()=>{
      // use html2canvas idea but implement simple SVG snapshot
      const rect = document.getElementById('preview').getBoundingClientRect();
      const svg = `<svg xmlns='http://www.w3.org/2000/svg' width='${rect.width}' height='${rect.height}'>`+
                  `<foreignObject width='100%' height='100%'><div xmlns='http://www.w3.org/1999/xhtml' style='font-family:Inter,sans-serif;color:#111'>`+
                  encodeURIComponent(document.getElementById('preview').outerHTML) +
                  `</div></foreignObject></svg>`;
      const blob = new Blob([svg],{type:'image/svg+xml;charset=utf-8'});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a'); a.href = url; a.download = 'chuc-mung-sinh-nhat.svg'; a.click(); URL.revokeObjectURL(url);
    });

    // Share (mock)
    shareBtn.addEventListener('click', ()=>{
      navigator.clipboard?.writeText('https://example.com/chuc-mung?name='+encodeURIComponent(nameEl.value)).then(()=>{
        alert('Đã sao chép liên kết (ví dụ).');
      }).catch(()=>{ alert('Không thể sao chép — hãy thử thủ công.'); });
    });

    // Simple confetti implementation
    const ctx = confettiCanvas.getContext('2d');
    let confettiPieces = [];
    let confettiRAF = null;

    function resize(){ confettiCanvas.width = window.innerWidth; confettiCanvas.height = window.innerHeight; }
    window.addEventListener('resize', resize); resize();

    function startConfetti(){
      if(confettiPieces.length>0) return; // already running
      for(let i=0;i<120;i++){
        confettiPieces.push({
          x: Math.random()*confettiCanvas.width,
          y: Math.random()*confettiCanvas.height - confettiCanvas.height/2,
          r: (Math.random()*6)+4,
          d: Math.random()*30+10,
          color: randomColor(),
          tilt: Math.random()*10-5,
          speed: Math.random()*2+1
        });
      }
      confettiLoop();
      setTimeout(()=>stopConfetti(),4000);
    }
    function stopConfetti(){ confettiPieces = []; }

    function confettiLoop(){
      ctx.clearRect(0,0,confettiCanvas.width,confettiCanvas.height);
      confettiPieces.forEach(p=>{
        p.y += p.speed + Math.sin(p.d);
        p.x += Math.sin(p.d);
        p.tilt += 0.05;
        drawPiece(p);
      });
      if(confettiPieces.length>0) confettiRAF = requestAnimationFrame(confettiLoop);
    }
    function drawPiece(p){
      ctx.beginPath(); ctx.moveTo(p.x, p.y);
      ctx.lineTo(p.x + p.r*Math.cos(p.tilt), p.y + p.r*Math.sin(p.tilt));
      ctx.lineWidth = p.r/2; ctx.strokeStyle = p.color; ctx.stroke();
    }
    function randomColor(){ const colors=['#ff6b6b','#ffd166','#6ee7b7','#7c5cff','#6ea8fe','#ff9bb3']; return colors[Math.floor(Math.random()*colors.length)]; }

    // Optional: start with preview applied
    applyBtn.click();
  </script>
</body>
</html>
