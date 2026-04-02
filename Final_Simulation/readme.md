# SPR100 Final Test Simulation

Course: SPR100 - Introduction to Computer Systems and Security  
Length: 80 minutes (simulation practice)  
Coverage: Labs 04, 05, 06
Form: Semi-open-book (see Rules)  

---

## Purpose

This simulation lets you practice the exact workflow and expectations for the real midterm. If you completed and understood the labs by yourself, this should feel straightforward.

---

## Rules (Semi‑Open‑Book)

- All works should be done on the security lab computer. You may NOT use your own personal computer. 
- You may use: textbooks, manuals, your own lab notes and previous submissions, and your VMs on your SSD. 
- You may NOT use: Internet browsing (except GitHub), online searches, AI assistants.  

---

## What You Will Submit

Create a folder named `final` at the root of your `SPR100_Labs` repository and place your completed answer sheet inside:

```
SPR100_Labs/
├── Lab01A/
├── ...
└── final/
    └── final_answer_sheet.md
    └── bandwidth.py
```

Use the provided template file: `Final_Test/Final_Simulation/Final_answer_sheet.md`.  
Copy it into your `SPR100_Labs/final/` folder and fill it in.

---

## How to Submit (with REQUIRED finalization command)

From your `SPR100_Labs` folder:

```bash
#REQUIRED finalization command

# If you are using Linux (Your own Ubuntu VM or Matrix), use Linux terminal:
git commit --allow-empty -m "Final" && git commit --allow-empty -m "Completed" && git push

# If you are using Windows VM, use Windows PowerShell:
git commit --allow-empty -m "Final" ; git commit --allow-empty -m "Completed" ; git push
```

- If you don't use this command to push your final test answers in the end, your  submission cannot be graded by the marking scripts and you marks will be deducted. 

---

## Mock Tasks (Simple Practice) for this Final Simulation

Perform these tasks and record outputs/answers in your `Final_answer_sheet.md`.


### Task 1


Imagine that Alice is in Toronto and Bob is in Vancouver, now Alice is driving a car carrying 100 Hard Drives of data to Bob, each Hard Drive has 16TB of data. Alice plans to spend 3 days to arrive at Bob's place. 

Please calculate the bandwidth of Alice's car in data transfer rate (e.g., X MB/s, Y GB/s.)

Please also complete the python program for the part of bandwith calculation, and we provide a python program template here: `Final_Test/Final_Simulation/bandwidth.py` to calculate the bandwidth of Alice's car in data transfer rate, with the input of the number of Hard Drives, each hard drive's data size (in TB) and the number of days Alice plans to spend to arrive at Bob's place. The python program can be executed like this:

```bash
python bandwidth.py --hard-drives 100 --data-size 16 --days 3
```

- NOTE: Most parts of the python program are already completed, you only need to modify the parts that are used to calculate the bandwidth of Alice's car.


Please submit your completed python program in your `final` folder.


- **Bandwidth:** [Fill your answer here]
- **Explanation of your calculation:** [Fill your answer here] 
- **Lines you modified in the python program:** 
```python
[Fill your answer here]
```
- **Output of your python program:** 
```
[Fill your answer here]
```

### Task 2

Please run the python program we provide here: `Final_Test/Final_Simulation/final.py` and run `tshark` or `wireshark` to capture the network traffic of the python program.

Please try to find out what did the python program do, by identifying:
- What website does the python program access?
- What protocol(s) are used by the python program?
- What did the python program do in network level during the execution of it?

- **Website URL:**  [Fill your answer here] 
- **Protocols:**  [Fill your answer here] 
- **Explanation of what the python program does:**  [Fill your answer here]


---

