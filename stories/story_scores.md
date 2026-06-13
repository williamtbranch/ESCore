# Current Story Scores (AVD / UL)

Date: 2026-06-13
Scope: All current stories except Moby_Dick (per request)

| Story | Path | Tokens | In Freq List | Unique Lemmas | AVD | UL (exact) | UL (rounded) |
|---|---|---:|---:|---:|---:|---:|---:|
| John and Alice | stories/John_and_Alice/story.txt | 750 | 750 | 76 | 113.33 | 19.7 | 20 |
| La Llorona | stories/La_Llorona/La_Llorona.txt | 2123 | 2119 | 220 | 527.00 | 26.0 | 26 |
| Nadie Lo Vio Morir - Episode 0001 | stories/Nadie_Lo_Vio_Morir/episode_0001.txt | 1635 | 1633 | 107 | 261.00 | 23.1 | 23 |
| Nadie Lo Vio Morir - Episode 0002 | stories/Nadie_Lo_Vio_Morir/episode_0002.txt | 1688 | 1685 | 113 | 207.67 | 22.2 | 22 |
| Pedro y Maria | stories/Pedro_y_Maria/pedro_y_Maria.txt | 409 | 409 | 68 | 274.67 | 23.3 | 23 |
| Un Lugar Bueno | stories/Un_Lugar_Bueno/Un_Lugar_Bueno.txt | 3764 | 3757 | 119 | 185.33 | 21.7 | 22 |
| Fisherman and Wife | stories/Fisherman_and_wife/story.txt | 1347 | 1347 | 152 | 265.00 | 23.2 | 23 |

Notes:
- Scores generated with the local standalone scorer in this workspace (`avd_ul_score.py`).
- This is ESCore's own difficulty metric, not a 1:1 replica of WeaveLang. A verb-form
  rescue step corrects spaCy mis-lemmatizations (enclitic imperatives like `díselo`,
  guillemet-mistagged verbs like `«Vuelve`) that otherwise rank as spuriously rare.
  This lowered the prior UL values by ~1 across dialogue-heavy stories; the new numbers
  reflect the corrected (more accurate) difficulty ordering.
