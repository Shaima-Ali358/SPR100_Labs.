# Lab06 - Network Traffic Analysis with tshark (Wireshark CLI)

**Student Name:** [Your Full Name]  
**Student ID:** [Your Student ID]  
**Course Section:** [Your Section]  
**Date:** [YYYY-MM-DD]  
**VM Interface Used:** [e.g., eth0/ens33/any/lo]  
**tshark Version:** [output of: tshark -v]

---

## 0) Workspace and Environment

### Workspace Path
```
$ pwd
[paste output; should be ~/SPR100_Labs/Lab06/work]
```

### Interfaces and Permissions
```
$ tshark -D
[paste relevant output]

$ groups
[paste output; confirm wireshark group if configured]
```

### Notes
- [Briefly describe any permission/configuration steps you took (e.g., newgrp wireshark, re-login)]

---

## Part 1: Install and Explore tshark

### Commands and Outputs
```
$ tshark -v
[paste relevant output]

$ tshark -D
[paste relevant output]

# 10-second capture (replace interface name if different)
$ tshark -i eth0 -a duration:10 -w lab06_basic.pcapng
[paste brief evidence it ran]

$ tshark -r lab06_basic.pcapng -q -z io,stat,1
[paste the io,stat table or key lines]

$ tshark -i any -f "udp port 53" -a duration:8 -w lab06_dns_only.pcapng
[paste brief evidence it ran]

$ tshark -r lab06_basic.pcapng -Y "http"
[paste 2-5 lines if any; or state none]

$ tshark -r lab06_basic.pcapng \
  -T fields -E header=y -E separator=, \
  -e frame.number -e frame.time_relative -e _ws.col.Protocol \
  -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e udp.srcport -e udp.dstport \
  > lab06_basic_fields.csv
[paste first 5 lines of CSV]
```

### Analysis
- [Which interface(s) are active and why?]
- [Explain capture vs display filters in your own words.]
- [How did you distinguish TCP vs UDP in the CSV fields?]

---

## Part 2: Recognize TCP vs UDP Across Concurrent Activities

### Activities Performed
```
# In separate terminals or sequentially during capture window:
$ ping -c 6 1.1.1.1
$ dig +short senecapolytechnic.ca
$ curl -s -o /dev/null -w "%{http_code}\n" http://example.com
$ dig A www.google.com
```

### Capture and Protocol Identification
```
$ tshark -i eth0 -a duration:20 -w lab06_multi.pcapng
[paste brief evidence it ran]

# ICMP
$ tshark -r lab06_multi.pcapng -Y "icmp" -T fields -e frame.number -e ip.src -e ip.dst | head
[paste output]

# DNS
$ tshark -r lab06_multi.pcapng -Y "dns" -T fields -e frame.number -e ip.src -e ip.dst -e dns.qry.name | head
[paste output]

# HTTP (if present)
$ tshark -r lab06_multi.pcapng -Y "http" -T fields -e frame.number -e ip.src -e ip.dst -e http.request.method -e http.host | head
[paste output or state none]
```

### Stats and Conversations
```
$ tshark -r lab06_multi.pcapng -q -z io,stat,1,"COUNT(tcp) TCP","COUNT(udp) UDP","COUNT(icmp) ICMP","COUNT(dns) DNS"
[paste the summary line(s)]

$ tshark -r lab06_multi.pcapng -q -z conv,tcp -z conv,udp
[paste top few conversations]
```

### Exported Dataset
```
$ tshark -r lab06_multi.pcapng \
  -T fields -E header=y -E separator=, \
  -e frame.time_relative -e _ws.col.Protocol -e ip.src -e ip.dst \
  -e tcp.flags -e tcp.len -e udp.length -e dns.qry.name \
  > lab06_part2.csv
[paste 5–10 representative rows]
```

### Analysis
- [Which activities produced ICMP vs UDP vs TCP?]
- [How did you determine client vs server roles from ports/IPs?]
- [What did the io,stat counts and conversations reveal about traffic patterns?]

---

## Part 3: Security-Focused Analysis (Scan Pattern and TLS Metadata)

### SYN Pattern on Loopback
```
# Generate localhost connection attempts
$ for p in 22 80 443 8000 8080 53; do (echo > /dev/tcp/127.0.0.1/$p) >/dev/null 2>&1 || true; done

# Capture and analyze
$ tshark -i lo -a duration:10 -w lab06_security_lo.pcapng
$ tshark -r lab06_security_lo.pcapng -Y "tcp.flags.syn==1 && tcp.flags.ack==0" \
  -T fields -e frame.time_relative -e ip.src -e ip.dst -e tcp.dstport | sort -n | head -20
[paste output]
```

### TLS Metadata (SNI/Version)
```
$ curl -s https://example.com >/dev/null
$ tshark -i any -a duration:8 -w lab06_tls.pcapng
$ tshark -r lab06_tls.pcapng -Y "tls.handshake.extensions_server_name" \
  -T fields -e frame.time_relative -e ip.dst -e tls.handshake.extensions_server_name -e tls.record.version | head
[paste output]
```

### Analysis
- [Explain why SYN without ACK can indicate scanning.]
- [What SNI hostnames and TLS versions did you observe, and what do they imply?]

---

## Reflection
1. [What is the difference between capture filters (-f) and display filters (-Y)? Provide one scenario for each.]
2. [How can you reliably identify TCP vs UDP traffic using tshark output or fields?]
3. [What can TLS metadata (e.g., SNI, version) reveal even when payloads are encrypted?]
4. [What ethical and legal boundaries must you respect when capturing network traffic?]

---

## Artifacts Checklist (Required Filenames)

Please ensure these files are saved in `~/SPR100_Labs/Lab06/work/` with EXACT names:
- [ ] lab06_basic.pcapng
- [ ] lab06_dns_only.pcapng
- [ ] lab06_basic_fields.csv
- [ ] lab06_multi.pcapng
- [ ] lab06_part2.csv
- [ ] lab06_security_lo.pcapng
- [ ] lab06_tls.pcapng

---

## Troubleshooting Notes (Optional)
- [Document any issues (permissions, interfaces) and how you resolved them.]


