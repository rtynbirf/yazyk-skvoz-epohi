#!/bin/bash
# Проверка: какие шрифты Google Fonts реально поддерживают кириллицу.
# Сравниваем с настоящим User-Agent (иначе API отдаёт ttf без unicode-range).
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
fonts=(
  "Forum" "Ruslan+Display" "Alegreya" "Oranienbaum" "EB+Garamond"
  "Prata" "Old+Standard+TT" "Oswald" "Bitter" "Podkova" "PT+Serif"
  "Poiret+One" "Jost" "Montserrat" "Unbounded" "Inter" "JetBrains+Mono"
  "Cormorant" "Grenze+Gotisch" "Playfair+Display" "Cormorant+Unicase" "Vollkorn"
)
printf "%-22s %s\n" "FONT" "CYRILLIC"
for f in "${fonts[@]}"; do
  css=$(curl -s --max-time 15 "https://fonts.googleapis.com/css2?family=${f}:ital,wght@0,400;0,700;1,400&display=swap" -A "$UA")
  if echo "$css" | grep -q '/\* cyrillic \*/'; then
    printf "%-22s YES\n" "$f"
  else
    printf "%-22s NO\n" "$f"
  fi
done
