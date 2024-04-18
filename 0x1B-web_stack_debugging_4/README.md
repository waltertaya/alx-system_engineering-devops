# 0x1B. Web stack debugging #4

## Overview

This project focuses on debugging various issues with a web server setup featuring Nginx on an Ubuntu 14.04 LTS environment. The tasks include:

1. **Sky is the limit, let's bring that limit higher**
    - Debug and optimize the Nginx server configuration to handle a high volume of requests without any failures.
  
2. **User limit**
    - Modify the OS configuration to allow the holberton user to log in without encountering "Too many open files" errors.

---

## Task Descriptions

### 0. Sky is the limit, let's bring that limit higher

- **Objective:** Optimize Nginx server configuration to handle high traffic and minimize failed requests.
  
- **Steps Taken:**
  - Benchmarked the server using ApacheBench to identify performance issues.
  - Debugged and updated the Nginx configuration.
  - Re-benchmarked the server to verify the improvements.
  
- **File:** [0-the_sky_is_the_limit_not.pp](0-the_sky_is_the_limit_not.pp)

### 1. User limit

- **Objective:** Modify OS configuration to resolve "Too many open files" errors for the holberton user.
  
- **Steps Taken:**
  - Identified the issue with the holberton user encountering "Too many open files" errors.
  - Modified the OS configuration to increase the user limits.
  - Verified the changes by logging in as the holberton user and checking the `/etc/passwd` file.
  
- **File:** [1-user_limit.pp](1-user_limit.pp)

---

## Environment

- **OS:** Ubuntu 14.04 LTS
- **Tools:** ApacheBench, Nginx, Puppet

---

## How to Use

### For Task 0:

```bash
puppet apply 0-the_sky_is_the_limit_not.pp
```

### For Task 1:

```bash
puppet apply 1-user_limit.pp
```

---

## Authors

- ALX
- @waltertaya

---

## Repository

- **GitHub Repository:** [alx-system_engineering-devops](https://github.com/waltertaya/alx-system_engineering-devops)
- **Directory:** 0x1B-web_stack_debugging_4
