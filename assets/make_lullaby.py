"""Synthesize a gentle music-box lullaby bed for the Sun & Moon pilot.

55 s total: 50 s of music matched to the video, 5 s fade tail.
Music-box timbre (sine + decaying harmonics), slow vi-IV-I-V progression
in C major, soft low pad underneath. Output: 44.1 kHz 16-bit stereo WAV.
"""
import numpy as np
import wave

SR = 44100
BPM = 60.0
BEAT = 60.0 / BPM          # 1 s per beat
BAR = 4 * BEAT             # 4 s per bar

NOTE_FREQS = {}
NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
for octave in range(2, 7):
    for i, n in enumerate(NAMES):
        midi = 12 * (octave + 1) + i
        NOTE_FREQS[f"{n}{octave}"] = 440.0 * 2 ** ((midi - 69) / 12)


def music_box(freq, dur, amp):
    """Music-box pluck: bright attack, exponential decay, slight shimmer."""
    n = int(dur * SR)
    t = np.arange(n) / SR
    env = np.exp(-t * 2.2) * np.minimum(t * 200, 1.0)
    tone = (1.00 * np.sin(2 * np.pi * freq * t) +
            0.45 * np.sin(2 * np.pi * freq * 2 * t) * np.exp(-t * 4.0) +
            0.18 * np.sin(2 * np.pi * freq * 4.01 * t) * np.exp(-t * 6.0) +
            0.06 * np.sin(2 * np.pi * freq * 5.98 * t) * np.exp(-t * 8.0))
    shimmer = 1.0 + 0.004 * np.sin(2 * np.pi * 5.0 * t)
    return amp * env * tone * shimmer


def pad(freq, dur, amp):
    """Soft slow pad: detuned sines with gentle swell."""
    n = int(dur * SR)
    t = np.arange(n) / SR
    a = min(1.2, dur / 3)
    env = np.minimum(t / a, 1.0) * np.minimum((dur - t) / a, 1.0)
    tone = (np.sin(2 * np.pi * freq * t) +
            0.6 * np.sin(2 * np.pi * freq * 1.003 * t) +
            0.4 * np.sin(2 * np.pi * freq * 0.997 * t))
    return amp * env * tone


TOTAL = 55.0
L = np.zeros(int(TOTAL * SR))
R = np.zeros(int(TOTAL * SR))


def place(buf, sig, at):
    i = int(at * SR)
    j = min(i + len(sig), len(buf))
    buf[i:j] += sig[: j - i]


# 13 bars: Am F C G | Am F C G | F G Am | C (held) + tail
CHORDS = ['Am', 'F', 'C', 'G', 'Am', 'F', 'C', 'G', 'F', 'G', 'Am', 'C', 'C']
CHORD_NOTES = {
    'Am': ['A3', 'E4', 'A4', 'C5'],
    'F':  ['F3', 'C4', 'A4', 'C5'],
    'C':  ['C3', 'G3', 'E4', 'G4'],
    'G':  ['G3', 'D4', 'B4', 'D5'],
}
PAD_ROOT = {'Am': 'A2', 'F': 'F2', 'C': 'C2', 'G': 'G2'}

# Arpeggio: eighth-note broken chord, mostly left channel
for bar, ch in enumerate(CHORDS):
    t0 = bar * BAR
    notes = CHORD_NOTES[ch]
    pattern = [0, 1, 2, 3, 2, 1, 2, 3]
    if bar == len(CHORDS) - 1:                      # final bar: single soft chord
        for k, nn in enumerate(notes):
            s = music_box(NOTE_FREQS[nn], 6.0, 0.10)
            place(L, s, t0 + 0.02 * k)
            place(R, 0.7 * s, t0 + 0.02 * k)
        break
    for k, idx in enumerate(pattern):
        s = music_box(NOTE_FREQS[notes[idx]], 2.5, 0.085)
        place(L, s, t0 + k * BEAT / 2)
        place(R, 0.55 * s, t0 + k * BEAT / 2)
    p = pad(NOTE_FREQS[PAD_ROOT[ch]], BAR + 0.5, 0.045)
    place(L, 0.8 * p, t0)
    place(R, p, t0)

# Melody: sparse lullaby line, mostly right channel (enters bar 3)
# (note, start beat, length in beats)
MELODY = [
    ('E5', 8, 1), ('D5', 9, 1), ('C5', 10, 2),
    ('D5', 12, 1), ('E5', 13, 1), ('D5', 14, 2),
    ('E5', 16, 1), ('G5', 17, 1), ('E5', 18, 2),
    ('D5', 20, 1.5), ('B4', 21.5, 0.5), ('D5', 22, 2),
    ('E5', 24, 1), ('D5', 25, 1), ('C5', 26, 2),
    ('A4', 28, 1), ('C5', 29, 1), ('D5', 30, 2),
    ('E5', 32, 2), ('D5', 34, 2),
    ('C5', 36, 4),
    ('E5', 40, 1), ('D5', 41, 1), ('C5', 42, 2),
    ('D5', 44, 2), ('B4', 46, 2),
    ('C5', 48, 4),
]
for note, beat, ln in MELODY:
    s = music_box(NOTE_FREQS[note], max(2.2, ln + 1.2), 0.13)
    place(R, s, beat * BEAT)
    place(L, 0.5 * s, beat * BEAT)

# Master: gentle fade in/out, normalize to a quiet bed level
mix = np.stack([L, R], axis=1)
t = np.arange(len(mix)) / SR
fade_in = np.minimum(t / 2.0, 1.0)
fade_out = np.clip((TOTAL - t) / 6.0, 0.0, 1.0)
mix *= (fade_in * fade_out)[:, None]
mix = np.tanh(mix * 1.2)                      # soft limit
mix *= 0.55 / max(1e-9, np.abs(mix).max())    # headroom: bed, not foreground

out = (mix * 32767).astype(np.int16)
path = "sun-and-moon-lullaby.wav"
with wave.open(path, 'wb') as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes(out.tobytes())
print(f"wrote {path}: {TOTAL}s, peak {np.abs(mix).max():.2f}")
