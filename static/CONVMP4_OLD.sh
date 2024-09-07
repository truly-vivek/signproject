
#!/usr/bin/bash
# Convert *.gif into *.mp4, skip if already exists.

outdir="."

for path in *.gif; do
  out="${outdir}/${path/.gif/}.mp4"
  [[ -f "$out" ]] && continue
  ffmpeg -f gif -i "${path}" "${out}"
done
