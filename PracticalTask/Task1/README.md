# Python 


## 1. File Extension Checker

**Script:** `task1.py`  
**Description:**  
Prompts the user to enter a file name and prints its extension. If the file has no extension or it's unknown, a warning is displayed.

### Usage:
```bash
python3 task1.py
```
**Example interaction:**
```
Enter the file name (e.g., document.txt): report.pdf
File extension: .pdf
```

---

## 2. Unique Integer Tuple Processor

**Script:** `task2.py`  
**Description:**  
Removes duplicates from a list of integers, converts it to a tuple, and displays the minimum and maximum values.

### Usage:
```bash
python3 task2.py
```
**Example interaction:**
```
Enter a list of integers separated by spaces: 1 2 3 2 1 4
Tuple without duplicates: (1, 2, 3, 4)
Minimum value: 1
Maximum value: 4
```

---

## 3. Access Log User-Agent Analyzer

**Script:** `task3.py`  
**Description:**  
Reads an access log file, counts the number of unique User-Agent strings, and displays request statistics for each of them.

### Usage:
```bash
python3 task3.py
```
**Example interaction:**
```
Enter the path to the access.log file: ../../../../../Downloads/access.log.5
Total unique User-Agents: 5
...
```

---

## 4. Character Occurrence Counter

**Script:** `task4.py`  
**Description:**  
Counts how many times each character appears in an input string and displays the result in the format char:count.

### Usage:
```bash
python3 task4.py
```
**Example interaction:**
```
Enter a string to analyze: pythonnohtyppy
Character counts: p:3, y:3, t:2, h:2, o:2, n:2
```

---

## 5. System Info CLI Utility

**Script:** `task5.py`  
**Description:**  
Displays system information (distro, memory, CPU, user, load average, IP) based on the passed command-line arguments.

### Usage:
```bash
python3 task5.py [labels]
```

### Available options:
| Argument | Description             |
|----------|-------------------------|
| -d       | Show distro info        |
| -m       | Show memory info        |
| -c       | Show CPU info           |
| -u       | Show current user       |
| -l       | Show system load avg    |
| -i       | Show IP address         |

**Example:**
```bash
python3 task5.py -d -m -c -u -l -i
```

---
