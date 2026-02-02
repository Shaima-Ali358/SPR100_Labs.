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
