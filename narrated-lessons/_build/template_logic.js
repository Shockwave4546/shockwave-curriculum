let current = 0;
let playing = false;
let pauseTimer = null;

const screenInner = document.getElementById('screenInner');
const captionEl = document.getElementById('caption');
const captionText = document.getElementById('captionText');
const sceneCountEl = document.getElementById('scenecount');
const progressFill = document.getElementById('progressFill');
const btnPlay = document.getElementById('btnPlay');
const hint = document.getElementById('hint');
const narrator = document.getElementById('narrator');
const btnCC = document.getElementById('btnCC');
let captionsOn = true;

const BIG_PAUSE_MS = 800;
const CONTINUATION_PAUSE_MS = 350;
const CODE_READING_MS_PER_CHAR = 12;
const CODE_READING_MS_CAP = 2500;

function codeReadingExtraMs(screenHtml){
  const blocks = screenHtml.match(/<pre class="code"[^>]*><code>[\s\S]*?<\/code><\/pre>/g) || [];
  let chars = 0;
  blocks.forEach(block => { chars += block.replace(/<[^>]+>/g, '').length; });
  if (chars === 0) return 0;
  return Math.min(CODE_READING_MS_CAP, Math.round(chars * CODE_READING_MS_PER_CHAR));
}

function renderBeat(i, animate){
  const beat = BEATS[i];
  screenInner.innerHTML = beat.screen;
  if (animate){
    screenInner.style.animation = 'none';
    void screenInner.offsetWidth;
    screenInner.style.animation = '';
  }
  captionText.textContent = beat.speak;
  captionEl.classList.add('live');
  sceneCountEl.textContent = (i+1) + ' / ' + BEATS.length;
  progressFill.style.width = (i / (BEATS.length - 1) * 100) + '%';
}

function stopSpeechAndTimer(){
  narrator.pause();
  narrator.currentTime = 0;
  if (pauseTimer) { clearTimeout(pauseTimer); pauseTimer = null; }
}

function speakCurrent(){
  narrator.src = AUDIO[current];
  narrator.onended = () => {
    if (playing) {
      const nextBeat = BEATS[current + 1];
      const pauseMs = (nextBeat && nextBeat.continues)
        ? CONTINUATION_PAUSE_MS
        : BIG_PAUSE_MS + codeReadingExtraMs(BEATS[current].screen);
      pauseTimer = setTimeout(() => advance(true), pauseMs);
    }
  };
  narrator.onerror = () => { if (playing) advance(true); };
  narrator.play().catch(() => {});
}

function advance(auto){
  if (current >= BEATS.length - 1){
    setPlaying(false);
    return;
  }
  current++;
  renderBeat(current, true);
  if (playing) speakCurrent();
}

function goPrev(){
  stopSpeechAndTimer();
  if (current > 0) current--;
  renderBeat(current, true);
  if (playing) speakCurrent();
}

function goNext(){
  stopSpeechAndTimer();
  advance(false);
  if (playing) speakCurrent();
}

function setPlaying(val){
  playing = val;
  document.getElementById('iconPlay').style.display = playing ? 'none' : '';
  document.getElementById('iconPause').style.display = playing ? '' : 'none';
  hint.style.visibility = playing ? 'hidden' : 'visible';
  if (playing){
    speakCurrent();
  } else {
    stopSpeechAndTimer();
  }
}

document.getElementById('btnPlay').addEventListener('click', () => setPlaying(!playing));
btnCC.addEventListener('click', () => {
  captionsOn = !captionsOn;
  captionEl.hidden = !captionsOn;
  btnCC.classList.toggle('off', !captionsOn);
  btnCC.title = captionsOn ? 'Hide captions' : 'Show captions';
});
document.getElementById('btnPrev').addEventListener('click', goPrev);
document.getElementById('btnNext').addEventListener('click', goNext);
document.getElementById('btnRestart').addEventListener('click', () => {
  stopSpeechAndTimer();
  current = 0;
  renderBeat(current, true);
  if (playing) speakCurrent();
});
document.getElementById('progress').addEventListener('click', (e) => {
  const rect = e.currentTarget.getBoundingClientRect();
  const pct = (e.clientX - rect.left) / rect.width;
  stopSpeechAndTimer();
  current = Math.max(0, Math.min(BEATS.length - 1, Math.round(pct * (BEATS.length - 1))));
  renderBeat(current, true);
  if (playing) speakCurrent();
});
document.addEventListener('keydown', (e) => {
  if (e.code === 'Space'){ e.preventDefault(); setPlaying(!playing); }
  else if (e.code === 'ArrowRight'){ goNext(); }
  else if (e.code === 'ArrowLeft'){ goPrev(); }
});

renderBeat(0, false);
