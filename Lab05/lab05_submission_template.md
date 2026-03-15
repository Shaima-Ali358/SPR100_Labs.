# Lab05 - File System Persistence, Hiding, and Detection

**Student Name:** [Your Full Name]  
**Student ID:** [Your Student ID]  
**Course Section:** [Your Section]  
**Date:** [YYYY-MM-DD]

---

## Part 1: Persistence and Concealment

### 1) Hidden Names and Locations (dotfiles)
#### Evidence (outputs/excerpts) and Notes
```
[paste relevant `ls -la` excerpts that show hidden paths]
```
#### Analysis
- What became hidden and why? Explain how dotfiles affect listings and traversal.

### 2) Extended Attributes (xattrs)
#### Evidence (outputs/excerpts) and Notes
```
[paste relevant `getfattr -d` excerpts for the file]
```
#### Analysis
- Where is data stored? What are the visibility/backup implications?

### 3) Immutable Bit Demonstration
#### Evidence (before/after)
```
[paste `lsattr` excerpts and the failed/denied write evidence]
```
#### Analysis
- Describe behavior before/after immutable. How would you safely reverse it?

### 4) Shell RC Login Hook
#### Evidence
```
[paste the added ~/.bashrc line(s) and recent lines from hook.log]
```
#### Analysis
- What did you add, when does it run, and what are the risks of RC file changes?

### 5) systemd User Service (preferred)
#### Unit File Content (paste your file)
```
~/.config/systemd/user/lab05-demo.service
-----------------------------------------
[Unit]
Description=Lab05 benign demo (user)

[Service]
Type=oneshot
ExecStart=/bin/bash -lc 'echo "[Lab05 demo] systemd user service ran: $(date)" >> ~/SPR100_Labs/Lab05/work/hook.log'

[Install]
WantedBy=default.target
```
#### Verification Evidence
```
[paste tail of hook.log and status/log excerpts that confirm execution]
```
#### Analysis
- How does a user service persist? What confirmed it ran? Why is `--user` important?

### 6) Crontab @reboot (if systemd user unavailable)
#### Evidence
```
[paste your crontab entry (not commands) showing the @reboot line]
```
#### Analysis
- Where are user cron jobs stored on your system? When would this run?

---

## Part 2: Detection and Mitigation

### 1) Enumerate Hidden Files
#### Evidence
```
[paste relevant `ls -la` / `find` excerpts that show hidden file paths]
```
#### Analysis
- Which paths looked suspicious? Why?

### 2) Inspect Metadata, ACLs, and xattrs
#### Evidence
```
[paste relevant `stat`, `getfacl`, and `getfattr` excerpts]
```
#### Analysis
- What did the metadata and ACL/xattrs reveal about access and labels?

### 3) Detect Startup Hooks
#### Evidence
```
[paste excerpts that show .bashrc hook lines, systemd user service listing/status, and any @reboot entries]
```
#### Analysis
- Which mechanisms were active? How would you prioritize investigation?

### 4) Live Monitoring with inotifywait
#### Evidence
```
[paste several lines showing events recorded]
```
#### Analysis
- What events occurred and what did they indicate?

### 5) Mitigation Steps (Before/After Evidence)
#### Evidence
```
[paste before/after snippets proving each cleanup: RC hook removed, unit disabled/removed, @reboot removed, xattrs cleared]
```
#### Analysis
- For each mechanism you created, explain how you detected it and how you removed it safely.

---

## Reflection
1. Where should defenders look first for user‑level persistence on Linux?
2. What are strengths/limits of ACLs and xattrs for concealment and for defense?
3. Why is execute (`x`) on directories relevant for detection (traversal)?
4. What operational risks should you consider before deleting suspicious files (e.g., immutable, ownership, backups)?

---

## Appendix (Optional)
- Extra logs, screenshots, or notes that support your answers.


