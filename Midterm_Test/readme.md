# SPR100 Midterm Test

**Course:** SPR100 - Introduction to Computer Systems and Security  
**Duration:** 80 minutes  
**Coverage:** Labs 01A, 01B, 02A, 02B, 03  
**Form:** Semi-open-book (see Rules)  
**Weight:** 20% of final grade
**Total Marks:** 20 marks

---

## Purpose

This midterm test evaluates your understanding of computer systems and security concepts covered in Labs 01-03. Unlike lab submissions where research and discussion is encouraged, this test requires individual independent work to demonstrate your personal mastery of the material.

---

## Rules (Semi‑Open‑Book)

- All works should be done on the security lab computer. You may NOT use your own personal computer. 
- You may use: textbooks, manuals, your own lab notes and previous submissions, and your VMs on your SSD. 
- You may NOT use: Internet browsing (except GitHub), online searches, AI assistants, or collaboration with other students.
- **Academic Integrity:** Any form of cheating, plagiarism, or unauthorized collaboration will result in immediate failure and academic integrity violation.

---

## Question Policy during the Test
- No question related to the Test Tasks will be answered. For example, the following questions will not be answered during the test:
   - "Am I supposed to do XXXXX in the task YYY?"
   - "How do I copy XXXXX in VM? How do I move file into/out of the VM?"
   - "Is it OK if I submit this XXXXX to the answer sheet YYYY?"
   - "I am having this error XXXX when I excute the script YYYY, what should I do?"
   - "Can you confirm XXXX is what I am supposed to do/submit for the Task YYYY?"
   Remember, this is a test, not a lab session where you can ask for help. Make your own best judgement on what to do.
- If you meet technical issues during the test caused by your Security lab Computer, no help will be provided. Please rasie your hand and ask to change to another computer.


---

## What You Will Submit

Create a folder named `midterm` at the root of your `SPR100_Labs` repository and place your completed answer sheet inside:

```
SPR100_Labs/
├── Lab01A/
├── Lab01B/
├── Lab02A/
├── Lab02B/
├── Lab03/
└── midterm/
    └── midterm_answer_sheet.md
```

Use the provided template file: `Midterm_Test/midterm_answer_sheet.md`.  
Copy it into your `SPR100_Labs/midterm/` folder and fill it in.

---

## How to Submit (with REQUIRED finalization command)

From your `SPR100_Labs` folder:

```bash
#REQUIRED finalization command

# If you are using Linux (Your own Ubuntu VM or Matrix), use Linux terminal:
git commit --allow-empty -m "Midterm" && git commit --allow-empty -m "Completed" && git push

# If you are using Windows VM, use Windows PowerShell:
git commit --allow-empty -m "Midterm" ; git commit --allow-empty -m "Completed" ; git push
```

- If you don't use this command to push your midterm answers in the end, your midterm submission cannot be graded by the marking scripts and you marks will be deducted. 

---

## Test Tasks

Complete the following tasks and record the requested information in your `midterm_answer_sheet.md`. 
   - ⚠️ WARNING: Brackets `[` and `]` in your `midterm_answer_sheet.md` are placeholders. Replace them with your actual answers and REMOVE the brackets. If any brackets remain in your responses, the marking script will not recognize the answer and you may receive 0 for that item.

---

### Task 1: The Archivist (6 marks)

**Task Description:** In the Windows citadel, the Guild Archivist requires a truthful system ledger from your machine. First, write down what you directly observe. Then, perform a brief script ritual to mint a single-line token that seals those facts for later verification.

**Environment:** Windows 10 VM

1. Change your username from `Student` to your own Seneca sutdent's username (e.g., `jsmith123`).
   - **Hint**: In Lab01, you have changed your password to your `Student` account, so you can change username at the same place where you changed the password.
   - **Hint**: How do you confirm the username you changed is working?
      - You want to make sure when you run the `powershell` script in later steps you are running it under the new username, otherwise you cannot get full marks for this task.
2. Manually record these information about your Windows 10 VM in your answer sheet:
   - Hostname (COMPUTERNAME)
   - OS name/edition 
   - Signed-in username
   - CPU count (logical)
   - Total physical memory (bytes)
   - Total disk capacity (sum of all fixed drives, bytes)
3. Run `powershell` and execute the script (in the `Midterm_Test` folder) with your student number (digits only):
   ```powershell
   ./task1.ps1 [YourStudentNumber]
   ```
   - Copy and paste the output string (one line only) into your answer sheet. 

- `NOTE`: After executing the `task1.ps1` script, if you see some red error messages like this:
```powershell
.\task1.ps1 : File C:\task1.ps1 cannot be loaded because running scripts is disabled on this system. For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1
+ .\task1.ps1
+ ~~~~~~~~~~~
+ CategoryInfo          : SecurityError: (:) [], PSSecurityException
+ FullyQualifiedErrorId : UnauthorizedAccess 
```
- -- It means that you haven't prepared this test by running our previous released "`Midterm Test Simulation`", which also includes a `hello.ps1` script for you to practice and run. You may give up this task and continue with the rest of the test. Remember: Always prepare for your tests. 

---

### Task 2: The Witness for Registrar (6 marks)

**Task Description** In the Ubuntu province, the Guild Registrar needs a truthful identity scroll for your machine. First, you must write down what you witness with your own eyes. Then, perform a short ritual to mint a single-line token that seals those facts for the Registrar to verify.

**Environment:** Ubuntu VM 

**Your Quest (Using Ubuntu VM):**
1. Use the username `[YourSenecaStudentUsername]` to perform the rest of this task.
   - Hint: In Lab03, you have learned some commands for changing/adding users.
2. Manually record these information about your Ubuntu VM in your answer sheet (based on Lab02B topics):
   - Hostname of your Ubuntu VM
   - Signed-in username
   - CPU architecture
   - CPU model name
   - CPU count (logical)
   - CPU frequency (MHz)
   - Total physical memory (bytes)
   - Available physical memory (bytes)
   - Total disk capacity (sum of all disk devices, bytes)
   - Linux kernel version
3. Excute the bash script with your student number (digits only):
   ```bash
   ./task2.sh [YourStudentNumber]
   ```
   - Hint: the script file needs to be executable.
   - Copy and paste the output string (one line only) into your answer sheet. Do not decode it during the test.

---

### Task 3: The Apprentices (8 marks)

**Task Description:** In the quiet halls of the Systems Guild, an apprentice engineer releases some invisible helpers into an Ubuntu realm. Each helper carries a backpack of a different weight and works quietly for a fixed time while a lantern slowly dims from bright to dark. Your mission is to witness what truly happens and bring back proof.

**Your Quest (Using Ubuntu VM):**
Summon the helpers and start the lantern timer:
   ```bash
   python3 task3.py
   ```
   - Observe in during the run and record:
     - Number of child processes (count only what you see)
     - Approximate increase in total memory usage (in MB) of each child process
     - Record all child process PIDs you see
   - Record from the program output: Copy and paste the token (one line) into your answer sheet.
   - `IMPORTANT NOTE`: You may run the python program multiple times. However, the PIDs will be different each time you run the program, and your observation will be different. You need to record the PIDs you see each time you run the script, and record the program output `token` the exact same run that you execute the python program. For example: 
       - If you run the program and record the token to put on the answer sheet, and didn't record the PIDs and other observations, then you run the python script again and record the PIDs and other observations, the token will be different and you will have to use the new token to put on the answer sheet.


---


**Good luck! Remember to work systematically and document everything clearly.**
