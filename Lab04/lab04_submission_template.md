# Lab04 - File System Security & Access Control

**Student Name:** [Your Full Name]  
**Student ID:** [Your Student ID]  
**Course Section:** [Your Section]  
**Date:** [YYYY-MM-DD]

---

## Part 1: File Metadata and Permissions

### Commands and Outputs
```
$ ls -la
[paste relevant output]

$ stat secret.txt
[paste relevant output]
```

### Analysis
- Explain ownership, mode (symbolic and octal), and timestamps you observed.
- Why is directory execute (x) required for traversal?

---

## Part 2: POSIX ACLs — Finer-Grained Access

### Commands and Outputs
```
$ getfacl secret.txt
[paste relevant output]

$ setfacl -m u:fsuser:r-- secret.txt && getfacl secret.txt
[paste relevant output]
```

### Analysis
- What does the ACL mask do? Which entries does it affect?
- Why did fsuser read succeed and write fail?

---

## Part 3: Extended Attributes and Encryption

### Commands and Outputs
```
$ setfattr -n user.note -v "tag:confidential" notes.txt && getfattr -d notes.txt
[paste relevant output]

$ zip -r secure_bundle.zip projects && \
  openssl enc -aes-256-cbc -salt -in secure_bundle.zip -out secure_bundle.zip.enc
[paste relevant output]
```

### Analysis
- Security considerations of xattrs (visibility, backup, portability).
- Key/password handling and recovery risks for encrypted archives.



---

## Reflection
1. When would ACLs be preferred over group changes or multiple groups?
2. How does the ACL mask affect effective permissions?
3. Why is execute (x) on directories required for traversal?
4. What operational risks do extended attributes and ad‑hoc encryption introduce?