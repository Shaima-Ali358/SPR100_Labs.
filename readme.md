# 📚 Lab Submission Guidelines

- **Course:** SPR100 - Introduction to Computer Systems and Security  
- **School** School of Information Technology Administration and Security  
- **Institution:** Seneca Polytechnic
- **Instructor:** Prof. Suranjit Paul
- **Instructor Contact:** suranjit.paul@senecapolytechnic.ca

---

## 🎯 Overview

All lab assignments in this course must be submitted through GitHub. This document provides comprehensive guidelines for proper lab submission, formatting, and evaluation criteria.

---

## 📋 Submission Requirements

### 1. 🔧 GitHub Repository Setup

- **Repository Name:** `SPR100_Labs` (Do NOT contain your own name/info in the repository name! Note symbol `_` and `-` are different.)
- **Give your instruction access** by adding your instructor as a collaborator in repository `Settings` page
- **Branch:** Use `main` branch for all submissions

**General Advice:**
1. Try not to use web browser for Git/GitHub related tasks, it is known to be prone to errors.
2. Use (and learn) command-line Git instead.
3. For Markdown preview, you can use VScode or web browser.


### 2. 📁 Required File Structure

Each lab submission must follow this structure:

```
SPR100_Labs/
├── Lab01A/
│   ├── README.md          # Lab documentation and reflection
│   ├── documents/         # Supporting documentation
│   ├── images/           # Screenshots and diagrams
│   ├── code/             # Source code files
│   └── [other lab-specific files]
├── Lab01B/
│   ├── README.md
│   └── [lab-specific content]
├── Lab02/
│   ├── README.md
│   └── [lab-specific content]
├── Lab03/
│   ├── README.md
│   └── [lab-specific content]
└── ...
```

### 3. 📝 README.md Requirements

Every lab folder must contain a `README.md` file with the following information:

```markdown
# [Lab Title] - [Brief Description]

**Student Name:** [Your Full Name]  
**Student ID:** [Your Student ID]  
**Lab Number:** [LabXX]  
**Completion Date:** [YYYY-MM-DD]  
**Course:** SPR100 - Introduction to Computer Systems and Security  
**Course Section Number:** (e.g. NAA, NBB, ...)
```

## 🚀 Submission Process

### Step 1: Complete Your Lab Work
1. Follow the lab instructions carefully
2. Complete all required exercises and documentation
3. Review your work to ensure it is complete
4. Create or update your README.md file

### Step 2: Prepare for Submission
1. Navigate to your lab folder in PowerShell:
   ```cmd
   cd [YOUR_LAB_FOLDER]\SPR100_Labs\
   ```

2. Check Git status:
   ```cmd
   git status
   ```

3. Add all new/modified files:
   ```cmd
   git add .
   ```

4. Commit your changes with a descriptive message:
   ```cmd
   git commit -am "Complete Lab01A - [Brief description of work completed]"
   ```

### Step 3: Submit to GitHub
1. Push your changes:
   ```cmd
   git push origin main
   ```

2. Verify your submission on GitHub.com

---

## 📊 Evaluation Criteria

### 📖 Documentation (30%)
- **README.md completeness** - All required sections present
- **Code comments** - Clear, meaningful comments in code files
- **Screenshots** - Relevant evidence of work completed
- **Reflection quality** - Thoughtful analysis of learning experience

### ⚙️ Technical Implementation (40%)
- **Functionality** - Code works as intended
- **Code quality** - Clean, readable, well-structured code
- **Best practices** - Following industry standards and course guidelines
- **Error handling** - Appropriate error handling and validation

### 🎨 Submission Quality (30%)
- **File organization** - Proper folder structure and naming
- **Git usage** - Meaningful commit messages and proper version control
- **Timeliness** - Submitted before deadline
- **Professional presentation** - Clean, professional appearance

---

## ⏰ Late Submission Policy

- **Due Date:** In general, each lab is due 11:59 PM before the start of the next lab session
- **Late Penalty:** 10% deduction per day, up to 3 days maximum
- **Extensions:** Must be requested via email to your instructor at least 24 hours before the due date
- **Study Week/Final Week:** Labs can be due for two weeks during these periods

---

## ⚠️ Common Submission Issues

### ❌ Avoid These Mistakes
- Chaning repository name or removing the repository 
   - no matter what happens, you do not need to delete your own repository or you will lose all history of your lab submissions. (ask instructor to restore the repository
- Missing README.md files or incomplete documentation
- Poor file organization
- Vague commit messages
- Additional files that are not related to the lab
   - It is a serious violation of academic integrity and will be reported to the academic integrity office if you include malicious code.
- Submitting after deadline without extension

### ✅ Best Practices
- Start early and work consistently
- Document your work as you go
- Test everything before submission
- Use descriptive commit messages
- Include relevant screenshots
- Write thoughtful reflections
- Follow the exact folder structure

---

## 🆘 Getting Help

### 🛠️ Technical Support
- **Git Issues:** Check [Git Documentation](https://git-scm.com/doc)
- **Markdown Help:** Use [Markdown Guide](https://www.markdownguide.org/)
- **GitHub Issues:** Visit [GitHub Guides](https://guides.github.com/)
- [Command Line Challenge](https://cmdchallenge.com/)
- [Markdown Practice](https://www.markdowntutorial.com/)
- [GitHub Skills](https://skills.github.com/)

---
