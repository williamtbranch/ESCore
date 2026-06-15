# Current Story Scores (AVD / UL)

Date: 2026-06-13
Scope: All current stories (updated with 0.85 coverage i-score)

| Story | Path | Tokens | In Freq List | Unique Lemmas | AVD | UL (exact) | UL (rounded) | i-Level (0.85) | iRank |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| John and Alice | stories/John_and_Alice/story.txt | 750 | 750 | 76 | 113.33 | 19.7 | 20 | 18.7 | 90 |
| Un Lugar Bueno | stories/Un_Lugar_Bueno/Un_Lugar_Bueno.txt | 3764 | 3757 | 119 | 185.33 | 21.7 | 22 | 18.8 | 91 |
| Nadie Lo Vio Morir - Episode 0001 | stories/Nadie_Lo_Vio_Morir/episode_0001.txt | 1482 | 1482 | 107 | 277.00 | 23.4 | 23 | 21.1 | 158 |
| Nadie Lo Vio Morir - Episode 0002 | stories/Nadie_Lo_Vio_Morir/episode_0002.txt | 1688 | 1686 | 113 | 207.67 | 22.2 | 22 | 20.4 | 135 |
| Fisherman and Wife | stories/Fisherman_and_wife/story.txt | 1347 | 1347 | 152 | 265.00 | 23.2 | 23 | 22.7 | 233 |
| Moby Dick - Chapter 001 (Loomings) | stories/Moby_Dick/chapters/Chapter_001_Loomings/story.txt | 1743 | 1743 | 125 | 668.00 | 27.0 | 27 | 24.0 | 320 |
| Moby Dick - Chapter 002 (The Carpet-Bag) | stories/Moby_Dick/chapters/Chapter_002_The_Carpet_Bag/story.txt | 1029 | 1029 | 95 | 1476.33 | 30.1 | 30 | 25.4 | 453 |
| Pedro y Maria | stories/Pedro_y_Maria/pedro_y_Maria.txt | 409 | 409 | 68 | 274.67 | 23.3 | 23 | 24.5 | 367 |
| La Llorona | stories/La_Llorona/La_Llorona.txt | 2123 | 2119 | 220 | 527.00 | 26.0 | 26 | 22.9 | 248 |

Notes:
- Scores generated with the local standalone scorer in this workspace (`avd_ul_score.py`).
- This is ESCore's own difficulty metric, not a 1:1 replica of WeaveLang. A verb-form
  rescue step corrects spaCy mis-lemmatizations (enclitic imperatives like `díselo`,
  guillemet-mistagged verbs like `«Vuelve`) that otherwise rank as spuriously rare.
  This lowered the prior UL values by ~1 across dialogue-heavy stories; the new numbers
  reflect the corrected (more accurate) difficulty ordering.
