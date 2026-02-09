#!/usr/bin/env bash
set -euo pipefail

# Generator for family-level adjacency matrices.
# Uses:
# - HESPERIA_FAMILIES_SETUP_V0.1.txt
# - HESPERIA_FAMILIES_PASSES_matrix_v0_1.csv
#
# Produces:
# 1) HESPERIA_FAMILIES_BASE_links_v0_1.csv
#    - Canonical family-level links from the setup file:
#      INTERNAL_PRE, INTERNAL_NEXT, EXTERNAL_PRE, EXTERNAL_NEXT.
# 2) HESPERIA_FAMILIES_FULL_matrix_v0_1.csv
#    - Full directed graph over families:
#      * 2 INTERNAL edges per family (prev/next) = 576
#      * all PASS and STOP edges from the passes matrix (88)
#      = 664 edges total.

root_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$root_dir"

setup_file="HESPERIA_FAMILIES_SETUP_V0.1.txt"
passes_matrix="HESPERIA_FAMILIES_PASSES_matrix_v0_1.csv"

if [[ ! -f "$setup_file" ]]; then
  echo "Missing $setup_file" >&2
  exit 1
fi

if [[ ! -f "$passes_matrix" ]]; then
  echo "Missing $passes_matrix" >&2
  exit 1
fi

echo "Generating HESPERIA_FAMILIES_BASE_links_v0_1.csv ..."
{
  echo "from_global_id,from_area_id,to_global_id,to_area_id,link_type"
  awk -F',' 'NR>1 {
    gid=$1; area=$2; prev_area=$4; next_area=$5;
    ip=$9; inext=$10; ep=$11; en=$12;
    printf "%s,%s,%s,%s,INTERNAL_PRE\n",  gid, area, ip,    area;
    printf "%s,%s,%s,%s,INTERNAL_NEXT\n", gid, area, inext, area;
    printf "%s,%s,%s,%s,AREA_HOP_PRE\n",  gid, area, ep,    prev_area;
    printf "%s,%s,%s,%s,AREA_HOP_NEXT\n", gid, area, en,    next_area;
  }' "$setup_file"
} > HESPERIA_FAMILIES_BASE_links_v0_1.csv

echo "Generating HESPERIA_FAMILIES_FULL_matrix_v0_1.csv ..."
tmp_edges="$(mktemp)"
trap 'rm -f "$tmp_edges"' EXIT

# Internal edges: prev and next within the same Area ring of 24 Families.
awk -F',' 'NR>1 {
  gid=$1; area=$2;
  ip=$9; inext=$10;
  printf "%s,%s,%s,%s,INTERNAL,1.0\n", gid, area, ip,    area;
  printf "%s,%s,%s,%s,INTERNAL,1.0\n", gid, area, inext, area;
}' "$setup_file" > "$tmp_edges"

# Append all PASS/STOP edges from the passes matrix (using existing fields).
awk -F',' 'NR>1 {
  from_gid=$4; from_area=$5; to_gid=$6; to_area=$7; etype=$8; w=$9;
  printf "%s,%s,%s,%s,%s,%s\n", from_gid, from_area, to_gid, to_area, etype, w;
}' "$passes_matrix" >> "$tmp_edges"

{
  echo "edge_id,from_global_id,from_area_id,to_global_id,to_area_id,edge_type,weight"
  nl -w3 -s',' "$tmp_edges" | awk -F',' '{printf "E%03d,%s\n", $1, $2}'
} > HESPERIA_FAMILIES_FULL_matrix_v0_1.csv

echo "Done."
