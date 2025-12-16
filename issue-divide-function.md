## 🔥 Critical: divide() function crashes on zero division

### Problem Description
The `divide()` function in `src/calculator.py` has no validation for division by zero, causing the application to crash with `ZeroDivisionError`.

### Current Code
```python
def divide(a, b):
    return a / b
```

### Issue
When a user attempts to divide by zero (e.g., `divide(10, 0)`), the function throws an unhandled `ZeroDivisionError` exception, causing the entire application to crash.

**Example:**
```python
result = calculate("divide", 10, 0)
# ZeroDivisionError: division by zero
```

### Expected Behavior
The function should:
1. Check if the divisor `b` is zero before attempting division
2. Raise a clear, descriptive error message or return a safe value
3. Prevent application crashes

### Proposed Solution
```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

### Impact
- **Severity**: CRITICAL 🔥
- **User Experience**: Application crashes unexpectedly
- **Data Loss Risk**: Any unsaved work is lost on crash

### Labels
- 🔥critical
- 🐛bug

### Milestone
v0.1-survival
