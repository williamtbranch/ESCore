# Nadie Lo Vio Morir Series Vocabulary

This file tracks vocabulary unlocked for the Nadie Lo Vio Morir series.

- Active series whitelist: `stories/Nadie_Lo_Vio_Morir/whitelist.txt`
- Rule: when a word is unlocked for the series, add it to the active whitelist
  and use it by construction in the next 2 to 3 episodes unless it is clearly
  one-off or structural.
- Selection principle: balance story-driven needs with high-frequency beginner
  usefulness from `assets/frequency_list.txt`.
- Helper command:

```powershell
python suggest_series_unlocks.py --story-dir "stories\Nadie_Lo_Vio_Morir" --count 10
```

## Unlock Log

| Episode | Word | Rank | Type | Why unlocked | Reuse through | Status |
|---|---:|---:|---|---|---|---|
| 0001 | noche | 157 | story noun | Needed to anchor scene timing and night visits clearly. | 0004 | active |
| 0001 | episodio | 1876 | structural label | Needed for episode wrapper and header language. | ongoing | active |
| 0002 | creer | 50 | core verb (full paradigm) | The series' thematic engine: the village believed words, not evidence. Taught via existing scaffold (*pensar que son verdad* → *creer*). | 0005 | active |
| 0002 | día | 60 | story noun (+ días) | Contrast-pair with `noche` (Ep 1 unlock); enables the two-day deadline clock. Taught by direct night/day contrast in the opening lines. | 0005 | active |

## Candidate Intake Notes

- Prefer words the next episode genuinely wants.
- Prefer words the episode can teach from neighboring sentences.
- Use frequency rank as a guide, not a command.
- If a word keeps recurring across multiple stories or series, consider a
  proposal to move it into the global core.