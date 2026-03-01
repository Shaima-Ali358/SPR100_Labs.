# 🔐 Lab04 - File System Security & Access Control

**Course:** SPR100 - Introduction to Computer Systems and Security  
**Lab Number:** Lab04  
**Weight:** 6% of final grade  
**Duration:** 90 minutes
**Due Date:** 2026/Mar/19 (11:59 PM before the start of the next lab session)

---

## 🎯 Learning Objectives

By the end of this lab, you will be able to:

1. Inspect and interpret file system metadata (ownership, mode, timestamps)
2. Configure and test Unix permissions (rwx) on files and directories
3. Apply POSIX ACLs for finer‑grained access control and verify effective permissions
4. Explore extended attributes and their security implications
5. Practice basic file confidentiality measures (archive + symmetric encryption)


---

## 📋 Pre-Lab Requirements

### Required Software
- Ubuntu VM from previous labs (Lab02B and Lab03)
- Git (for submission)
- Python 3.x
- `acl` package (for `getfacl`/`setfacl`)
- `zip` and `openssl` for basic encryption demo

Install missing tools:
```bash
sudo apt update
sudo apt install -y acl zip openssl
```

---

## 🚀 Lab Activities

### Part 1: File Metadata and Permissions (30 minutes)

References:
**Please read the references when you are not familiar with them or wondering what you are doing. Google is your friend, search for more references and tutorials when you need to.**
- [ls(1) — list directory contents](https://man7.org/linux/man-pages/man1/ls.1.html)
- [stat(1) — file status](https://man7.org/linux/man-pages/man1/stat.1.html)
- [chmod(1) — change file mode bits](https://man7.org/linux/man-pages/man1/chmod.1.html)
- [GNU Coreutils: Mode structure (permissions)](https://www.gnu.org/software/coreutils/manual/html_node/Mode-Structure.html)
- [adduser(8) — add a user](https://man7.org/linux/man-pages/man8/adduser.8.html)
- [sudo(8) — execute command as another user](https://man7.org/linux/man-pages/man8/sudo.8.html)

1. Create a working directory and sample files:
```bash
mkdir -p ~/SPR100_Labs/Lab04/work
cd ~/SPR100_Labs/Lab04/work
echo "confidential: $(date)" > secret.txt
echo "team notes" > notes.txt
mkdir -p projects/teamA
```

2. Inspect metadata and ownership:
```bash
ls -la
stat secret.txt
```
- Record: owner, group, size, mode (symbolic and octal), and timestamps.

3. Configure permissions (chmod) and test:
```bash
chmod 600 secret.txt      # rw-------
chmod 644 notes.txt       # rw-r--r--
chmod 750 projects        # rwxr-x---
chmod 750 projects/teamA  # rwxr-x---
ls -la
```
- Explain why directory execute (x) is required for traversal.

4. Attempt access from another test user (demonstrate denial):
```bash
sudo adduser fsuser --disabled-password --gecos ""
sudo -u fsuser bash -c 'cat ~/SPR100_Labs/Lab04/work/secret.txt || echo "denied"'
```
- Document and explain what the above two commands do, the outcomes, and the reasons.
  - Hint: directory execute (x) controls traversal; file read requires r on the file and x on each directory in the path.

---

### Part 2: POSIX ACLs — Finer-Grained Access (30 minutes)

References: **Please read the references when you are not familiar with them or wondering what you are doing. Google is your friend, search for more references and tutorials when you need to.**
- [setfacl(1) — set file access control lists](https://man7.org/linux/man-pages/man1/setfacl.1.html)
- [getfacl(1) — get file access control lists](https://man7.org/linux/man-pages/man1/getfacl.1.html)
- [acl(5) — POSIX Access Control Lists](https://linux.die.net/man/5/acl)
- [id(1) — print real and effective user and group IDs](https://man7.org/linux/man-pages/man1/id.1.html)

1. Enable and verify ACL tools:
```bash
getfacl secret.txt
```
2. Grant a specific user read‑only via ACL without changing base mode:
```bash
sudo -u fsuser bash -c 'id'
setfacl -m u:fsuser:r-- secret.txt
getfacl secret.txt
```
- Note the `mask` entry and the `+` in `ls -l` output.
- Document and explain what the above commands do, the outcomes, and the reasons.
  - Note: The ACL mask limits the effective permissions of named user/group entries (but not the file owner or "other").


3. Test effective permissions:
```bash
sudo -u fsuser bash -c 'cat ~/SPR100_Labs/Lab04/work/secret.txt && echo OK'
sudo -u fsuser bash -c 'echo x >> ~/SPR100_Labs/Lab04/work/secret.txt || echo "write denied"'
```
- Explain why read works and write is denied.

4. Directory ACL for collaborative access:
```bash
setfacl -m g:fsuser:rx projects/teamA
setfacl -R -m d:g:fsuser:rx projects  # default ACL for new items
getfacl projects/teamA
```
- Create a file in `projects/teamA` and verify fsuser access.

5. Remove ACLs and re‑test:
```bash
setfacl -b secret.txt
getfacl secret.txt
```
- Observe fallback to base rwx behavior.
- Document and explain what the above commands do, the outcomes, and the reasons.

---

### Part 3: Extended Attributes and Basic Encryption (30 minutes)

References:
- [setfattr(1) — set extended attributes](https://manpages.debian.org/setfattr)
- [getfattr(1) — get extended attributes](https://manpages.debian.org/getfattr)
- [zip(1) — package and compress files](https://linux.die.net/man/1/zip)
- [openssl-enc(1) — symmetric cipher routines](https://www.openssl.org/docs/man1.1.1/man1/openssl-enc.html)
- [shred(1) — overwrite a file to hide its contents](https://man7.org/linux/man-pages/man1/shred.1.html)

1. Explore extended attributes (if supported):
```bash
sudo apt install -y attr
setfattr -n user.note -v "tag:confidential" notes.txt
getfattr -d notes.txt
```
- Discuss security considerations of xattrs (visibility, backup behavior).

2. Archive and encrypt a folder (confidential handoff demo):
```bash
zip -r secure_bundle.zip projects
openssl enc -aes-256-cbc -salt -in secure_bundle.zip -out secure_bundle.zip.enc
```
- Do some search on the internet to find out what `openssl` is and why it can be used for encrypting files
- Record where keys/passwords are stored; discuss recovery risks.
  - Decrypt example (for reference): `openssl enc -d -aes-256-cbc -in secure_bundle.zip.enc -out secure_bundle.zip`

3. Clean up sensitive artifacts:
```bash
shred -u secure_bundle.zip
```

---


## 🧪 Deliverables

- Submit a `README.md` in `Labs/Lab04/` folder.
- In the end of the README.md, you should include the answers to the reflection prompts below:

```
### Reflection Prompts
1. When would ACLs be preferred over group changes or multiple groups?
2. How does the ACL mask affect effective permissions?
3. Why is execute (x) on directories required for traversal?
4. What operational risks do extended attributes and ad‑hoc encryption introduce?
```

- You can use the following template to write your own `README.md` for submission:
    - [Lab 04 Submission Template](Lab04/lab04_submission_template.md)




---

## 🛠️ Optional Scripts (If you you are interested in using `Python` to do this lab again, you can use the following scripts)

Use the provided Python helpers (optional):
- `file_acl_demo.py` — programmatically set chmod/ACL and verify access
- `fs_inspect.py` — inspect metadata, timestamps, xattrs

---

## 📤 Submission Instructions

Follow the same submission flow as Lab03. Commit all artifacts in `Labs/Lab04/`:
1. Your lab `README.md` with documentation and answers
2. Push to GitHub before the deadline

Suggested commit message:  
"Complete Lab04 - File System Security & Access Control"

---

