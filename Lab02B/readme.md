# 🐧 Lab02B - Understanding CPU and Memory: Linux Ubuntu VM Analysis

**Course:** SPR100 - Introduction to Computer Systems and Security  
**Lab Number:** Lab02B  
**Weight:** 2% of final grade  
**Duration:** 1 hour 45 minutes  
**Due Date:** [Insert due date] (11:59 PM before the start of the next lab session)

---

## 🎯 Learning Objectives

By the end of this lab, you will be able to:

1. **Set up and configure a Linux Ubuntu Virtual Machine** using VMware Workstation
2. **Analyze CPU specifications and performance** using Linux system tools and commands
3. **Examine memory hierarchy and system registers** through Linux-specific exploration
4. **Apply Linux system administration skills** for performance monitoring and analysis

---

## 📋 Pre-Lab Requirements

### Required Software
- **VMware Workstation Pro** (Recommended)
- **Ubuntu Image** (Download from Security Lab: On your security lab computer, open `File Explorer` --> Click Address Bar --> `\\mydrive\courses\SPR100\`)

### Required Knowledge
- Completion of **Lab02A** (Windows VM Analysis)
- Basic understanding of Linux command line
- Familiarity with virtualization concepts
- Understanding of CPU and memory concepts from Lab02A and lecture

---

## 🚀 Lab Activities

### Part 1: Ubuntu VM Setup and Configuration (15 minutes)

#### 1.1 Create Ubuntu VM
1. **Download Ubuntu Image:**
   - On your security lab computer, open `File Explorer` --> Click Address Bar --> `\\mydrive\courses\SPR100\`
   - Download `Ubuntu` image and save it to your own SSD drive.
   - Note: If you have done it in `Lab01B`, you can skip this step.

2. **Create Configuration Report:**
   ```markdown
   ## VM Configuration Summary
   - **Hypervisor:** [VMware Workstation Pro/VirtualBox]
   - **Version:** [Version number]
   - **CPU Cores:** [Number allocated]
   - **Memory:** [RAM allocated]
   - **Storage:** [Disk size and type]
   - **Network:** [Adapter type and configuration]
   ```

### Part 2: Linux System Analysis (45 minutes)

In your Ubuntu VM:

#### 2.0 Using APT Package Manager
In this lab, if you encounter any package that you don't have, and youneed to install it on your Ubuntu VM, you should use `APT Package Manager`. So **don't raise your hand and say: "I don't have XXX installed/I don't have XXX command"**. 

For example, our default Ubuntu VM does not have `ifconfig` command, when you input `ifconfig`, you will see `command not found` or similar message and prompt you to install `network-tools` package. Then you can type the following command to install `network-tools` package which contains the program to let you execute `ifconfig` command:
```bash
sudo apt update
sudo apt install network-tools
```

For the use of `APT Package Manager`, you can refer to the following documentations:
- [APT Package Manager Documentation](https://manpages.ubuntu.com/manpages/jammy/man8/apt.8.html)
- Other Ubuntu APT tutorials you can find on the Internet by doing some search online.

#### 2.1 CPU Analysis
1. **System Information Commands:**
   ```bash
   # Get CPU information
   cat /proc/cpuinfo

   # take a look at the output
   # tip: use `less` command to view the output: `cat /proc/cpuinfo | less`
   # think: why using less is better?
   
   # Get processor architecture
   uname -m
   
   # Get number of CPU cores
   nproc
   
   # Get CPU model name
   grep "model name" /proc/cpuinfo
   
   # Get CPU frequency
   grep "cpu MHz" /proc/cpuinfo

   ```

2. **Task Manager Equivalent (`htop`):**
   - Type `htop` and press Enter
   - Document:
     - CPU utilization graphs
     - Number of CPU cores visible
     - Current CPU usage percentage
     - Process list and CPU usage
   - Read: [htop Documentation](https://htop.dev/)

3. **Get more CPU information in your Ubuntu VM:**
   ```bash
   # Get processor information
   lscpu
   
   # Get CPU performance counters
   top -n 1 | grep "Cpu(s)"
   ```

#### 2.2 Memory Analysis
1. **Memory Specifications:**
   - **In System Information (previous commands):**
     1. Use `free -h` to see memory summary
        - Investigate: What does each number mean here?
     2. Use `cat /proc/meminfo` for detailed memory info
     3. Document:
        - Total physical memory
        - Available physical memory
        - Virtual memory size
        - Buffer and cache information
        - **Important:** While keeping record of these information in your notes, also find out what they are. You will need to understand these concepts for future quizzes and tests.

2. **`htop` Memory Analysis:**
   - In htop, observe memory usage graphs
   - Document:
     - Memory usage patterns
     - Physical memory composition
     - Memory usage by processes

3. **Linux Memory Commands:**
   ```bash
   # Get memory information
   free -h
   
   # Get memory performance
   cat /proc/meminfo | grep -E "MemTotal|MemFree|MemAvailable"
   ```
   - Think: What does the above command mean?

#### 2.3 System Performance Monitoring
1. **Performance Monitor Equivalent in your Ubuntu VM:** 
   - **Create a simple performance monitoring script:**
     ```bash
     # Monitor CPU and memory for 2 minutes
     for i in {1..24}; do
       echo "Sample $i:"
       echo "CPU Usage: $(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)%"
       echo "Memory Usage: $(free | grep Mem | awk '{printf "%.1f", $3/$2 * 100.0}')%"
       echo "---"
       sleep 5
     done
     ```
   - **Think**: You have learned about `bash scripting` in OPS Unix course. What do you think this script is doing? How do you run it? Can you write a similar script to monitor something else? 

2. **Resource Monitor Equivalent:**
   - Use `htop` for real-time resource monitoring
   - Monitor CPU and memory usage during different activities
   - Do some tasks to observe the performance of your Ubuntu VM, and record the peak usage of CPU and memory during different tasks.
     - **Think**: How do you monitor `htop` screen while doing these tasks at the same time?
         - Trick: Using `tmux` to split screen. [tmux Documentation](https://manpages.ubuntu.com/manpages/jammy/man1/tmux.1.html)
     - **Think**: Regarding "Do some tasks", what do you think you can do in Linux command line to make CPU and/or memory usage higher? You may do some search online to find out the answer, and make sure you record what you have done in your report. 
   - Document peak usage during different tasks and make notes in your report.

### Part 3: Security and Virtualization Analysis (15 minutes)

#### 3.1 Virtualization Security Features
1. **Linux Security Features:**
   - Check AppArmor status: `sudo aa-status`
       - If you don't have the `aa-status` command, what do you read in the terminal message? What do you think you need to install?
       - [AppArmor Documentation](https://wiki.ubuntu.com/AppArmor) -- you will need it in future labs.
   - Check firewall status: `sudo ufw status`
       - For `uft`, can you find out some information about it online and find where the configuration of it should be? What are the default rules? Make sure you document these information in your report.

2. **VM Isolation:**
   - **File System Isolation:**
     1. Create a test file on Ubuntu user's home folder
     2. Check if it appears on host system
     3. Document the isolation effectiveness and what is the reason for this isolation
   
   - **Process Isolation:**
     1. Open htop in VM
     2. Note the VM processes (should not show host processes)
     3. Document what you observe and explain why this isolation is important

#### 3.2 Performance Observation
1. **CPU Performance Test:**
   - **CPU Usage Comparison:**
     1. Note CPU usage in htop
     2. Compare with your host system CPU usage
     3. Document any differences and explain why this difference is happening

2. **Memory Performance Test:**
   - **Memory Usage Test:**
     1. Open multiple applications in VM (Terminal, Calculator, Text Editor)
     2. Monitor memory usage in htop
     3. Document what you have done and how memory usage changes

---

## 📝 Documentation Requirements

### Required Documentation Template

Create a comprehensive lab report using the following template structure:

```markdown
# Lab02B - Linux Ubuntu VM CPU and Memory Analysis Report

**Student Name:** [Your Full Name]  
**Student ID:** [Your Student ID]  
**Course Section:** [Your Section Number]  
**Completion Date:** [YYYY-MM-DD]  
**Lab Duration:** [Actual time taken]

---

## Part 1: Ubuntu VM Setup and Configuration

### 1.1 VM Configuration Summary
- **Hypervisor:** [VMware Workstation Pro/VirtualBox]
- **Version:** [Version number]
- **CPU Cores:** [Number allocated]
- **Memory:** [RAM allocated]
- **Storage:** [Disk size and type]
- **Network:** [Adapter type and configuration]

### 1.2 VM Installation and Startup Process
- **Ubuntu ISO Source:** [Download location]
- **Installation Method:** [How Ubuntu was installed]
- **Startup Time:** [Time from power-on to login screen]
- **User Account Created:** [Username used]
- **Initial VM State:** [Any issues or observations]

---

## Part 2: Linux System Analysis

### 2.1 CPU Analysis Results

#### System Information Commands
- **Processor Information:** [Key details from cat /proc/cpuinfo]
- **Architecture:** [Output of uname -m]
- **Number of Cores:** [Output of nproc]
- **CPU Model Name:** [Output of grep "model name" /proc/cpuinfo]
- **CPU Frequency:** [Output of grep "cpu MHz" /proc/cpuinfo]

#### htop CPU Analysis
- **Current CPU Usage:** [Percentage observed]
- **Number of CPU Cores Visible:** [Count]
- **CPU Utilization Pattern:** [Describe what you observed]
- **Process CPU Usage:** [List top CPU-consuming processes]

#### Linux Command Outputs
    # Processor Information Command Output:
    [Paste the output of: lscpu]

    # CPU Performance Output:
    [Paste the output of: top -n 1 | grep "Cpu(s)"]

### 2.2 Memory Analysis Results

#### System Information Memory Details
- **Total Physical Memory:** [Amount in GB/MB from free -h]
- **Available Physical Memory:** [Amount in GB/MB]
- **Memory Usage Pattern:** [Describe memory usage graphs in htop]
- **Buffer and Cache Information:** [Key lines from /proc/meminfo]

#### Linux Memory Commands Output
    # Memory Information:
    [Paste the output of: free -h]

    # Memory Performance:
    [Paste the output of: cat /proc/meminfo | grep -E "MemTotal|MemFree|MemAvailable"]

### 2.3 System Performance Monitoring Results

#### Performance Monitoring Script
- **Monitoring Duration:** [2 minutes]
- **Sample Interval:** [5 seconds]
- **CPU Usage Range:** [Minimum - Maximum %]
- **Memory Usage Range:** [Minimum - Maximum %]
- **Performance Patterns Observed:** [Describe any patterns or spikes]

#### htop Resource Monitor Observations
- **Peak CPU Usage:** [Highest observed percentage]
- **Peak Memory Usage:** [Highest observed usage]
- **Resource Usage During Activities:** [Describe what happened when you performed different tasks]

---

## Part 3: Security and Virtualization Analysis

### 3.1 Linux Security Features Status
- **AppArmor Status:** [Enabled/Disabled, status details]
- **UFW Firewall Status:** [Status]
- **UFW Rules Summary:** [List key rules or defaults]
- **System Updates Status:** [Available updates, last update]

### 3.2 VM Isolation Test Results

#### File System Isolation
- **Test File Created:** [Name and location of test file]
- **Host System Check:** [Did the file appear on host? Yes/No]
- **Isolation Effectiveness:** [Describe how well the isolation works and why]

#### Process Isolation
- **VM Processes Observed:** [List some key processes you saw]
- **Host Processes Visible:** [Were any host processes visible? Yes/No]
- **Isolation Observations:** [Describe what you observed about process separation and why it matters]

### 3.3 Performance Observation Results

#### CPU Performance Comparison
- **VM CPU Usage:** [Typical usage percentage]
- **Host CPU Usage:** [Typical usage percentage]
- **Performance Differences:** [Describe differences and likely reasons]

#### Memory Performance Test
- **Applications Opened:** [List applications you opened]
- **Initial Memory Usage:** [Before opening apps]
- **Final Memory Usage:** [After opening apps]
- **Memory Behavior Observations:** [Describe how memory usage changed]

---

## Analysis and Conclusions

### Key Findings
1. **CPU Performance:** [Summarize CPU analysis findings]
2. **Memory Performance:** [Summarize memory analysis findings]
3. **Virtualization Overhead:** [Describe any performance impact of virtualization]
4. **Security Features:** [Summarize security observations]

### Technical Insights
- **Linux System Understanding:** [What did you learn about Linux CPU and memory?]
- **Virtualization Concepts:** [What did you learn about VM isolation?]
- **Performance Monitoring:** [What did you learn about Linux performance tools?]

### Challenges and Solutions
- **Challenges Faced:** [List any difficulties encountered]
- **Solutions Applied:** [How did you resolve the challenges?]
- **Lessons Learned:** [What would you do differently next time?]

---

**Report Completion Time:** [Total time spent on lab]  
**Confidence Level:** [Rate your understanding 1-10]  
**Questions for Instructor:** [List any remaining questions]
```

---


## 🔗 Additional Resources

### Documentation
- [VMware Workstation Documentation](https://docs.vmware.com/en/VMware-Workstation-Pro/)
- [VirtualBox Documentation](https://www.virtualbox.org/manual/)
- [Ubuntu Documentation](https://ubuntu.com/tutorials)

### Tools
- [htop](https://htop.dev/) - Interactive process viewer
- [Linux Performance Tools](https://brendangregg.com/linuxperf.html)
- [Ubuntu System Administration](https://tldp.org/LDP/sag/html/)

---

## 📤 Submission Instructions

- Please refer to the [readme.md](../readme.md) file of the Labs root directory (one level above from this Lab02B folder) for detailed submission instructions.

### What to Submit
1. **Complete Lab02B folder** with all required files
2. **README.md** with comprehensive documentation

### Submission Process
1. Navigate to your lab folder:
   ```cmd
   cd [YOUR_LAB_FOLDER]\SPR100_Labs\Lab02B\
   ```

2. Add all files:
   ```cmd
   git add .
   ```

3. Commit with descriptive message:
   ```cmd
   git commit -am "Complete Lab02B - Linux Ubuntu VM CPU and Memory Analysis"
   ```

4. Push to GitHub:
   ```cmd
   git push origin main
   ```

---
