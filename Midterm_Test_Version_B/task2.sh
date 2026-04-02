#!/usr/bin/env bash

set -euo pipefail

_b(){ printf '%s' "$1" | base64 -d 2>/dev/null; }
H=$(_b aXBoYWRkcg);N=$(_b IG5hbWU);U=$(_b IHVuYW1l);NW=$(_b IG5ldHdvcms);UF=$(_b IHByb2Nlc3M);MU=$(_b IG1lbW9yeQ);DU=$(_b IGRpc2s);Vk=$(_b IHZlcnNpb24)

err(){ echo "$1"; exit 1; }
[[ $# -eq 1 ]] || err "Usage: ./task2.sh <student_number_digits_only>"
student_number="$1"; [[ "$student_number" =~ ^[0-9]+$ ]] || err "ERROR: Student number must contain digits only"

hostname_val="$(hostname)"
if [[ -r /etc/os-release ]]; then . /etc/os-release; os_name_val="${PRETTY_NAME:-Linux}"; else os_name_val="$(uname -s) $(uname -r)"; fi
username_val="${USER:-$(id -un)}"

# Get network interfaces (excluding loopback)
network_interfaces_val=$(ip -br addr show 2>/dev/null | grep -v lo | head -5 || echo "N/A")

# Get running process count
process_count_val=$(ps -eo pid 2>/dev/null | wc -l || echo "0")

# Get memory info in different units
if [[ -r /proc/meminfo ]]; then
    mem_total_kb=$(awk '/^MemTotal:/ {print $2}' /proc/meminfo)
    mem_available_kb=$(awk '/^MemAvailable:/ {print $2}' /proc/meminfo)
    mem_total_mb=$((mem_total_kb / 1024))
    mem_available_mb=$((mem_available_kb / 1024))
    memory_val="${mem_total_mb}MB total, ${mem_available_mb}MB available"
else
    memory_val="N/A"
fi

# Get disk usage for root
disk_usage_val=$(df -BG / 2>/dev/null | awk 'NR==2 {print $2}' || echo "N/A")

# Get kernel version
kernel_val=$(uname -r 2>/dev/null || echo "N/A")

json_escape(){ local s=${1//\\/\\\\}; s=${s//\"/\\\"}; s=${s//$'\n'/\\n}; s=${s//$'\r'/\\r}; s=${s//$'\t'/\\t}; printf '%s' "$s"; }

hn=$(json_escape "$hostname_val"); osn=$(json_escape "$os_name_val"); un=$(json_escape "$username_val")
ni=$(json_escape "$network_interfaces_val"); pc=$(json_escape "$process_count_val")
mv=$(json_escape "$memory_val"); dv=$(json_escape "$disk_usage_val"); kv=$(json_escape "$kernel_val")

json=$(printf '{"hostname":"%s","os_name":"%s","username":"%s","network_interfaces":"%s","process_count":"%s","memory":"%s","disk_root":"%s","kernel":"%s","student_number":"%s"}' "$hn" "$osn" "$un" "$ni" "$pc" "$mv" "$dv" "$kv" "$student_number")

printf '%s' "$json" | base64 | tr -d '\n'; echo
