# Project Title: Web Stack Debugging #1

## Description

This project involves debugging an issue with Nginx not listening on port 80 in an Ubuntu container. The task includes identifying the problem and creating Bash scripts to automate the fix. Two scripts are provided: one addressing the fix with the minimum number of commands and another, an advanced version, ensuring the fix is concise and follows strict Bash scripting requirements.

## Tasks

### Task 0: Nginx likes port 80

- **Description:** Find and fix the issue preventing Nginx from listening on port 80.
- **Requirements:**
  - Nginx must be running and listening on port 80 of all server's active IPv4 IPs.
  - Write a Bash script to configure the server to meet the above requirements.

### Task 1: Make it sweet and short

- **Description:** Build upon Task 0, creating a more concise Bash script.
- **Requirements:**
  - Bash script must be 5 lines or less.
  - Must adhere to usual Bash script requirements.
  - Ensure service (init) correctly reports that Nginx is not running.

## Repository Structure

- **GitHub Repository:** [alx-system_engineering-devops](https://github.com/waltertaya/alx-system_engineering-devops)
- **Directory:** 0x0E-web_stack_debugging_1

## Scripts

1. **0-nginx_likes_port_80**
   - Bash script to fix the issue with Nginx not listening on port 80.
   - Requirements are met as specified in Task 0.

2. **1-debugging_made_short**
   - Advanced Bash script for a more concise fix based on Task 0.
   - Follows strict Bash script requirements and ensures a short solution.

## Usage

1. Clone the repository:

   ```Bash
   git clone https://github.com/alx-system_engineering-devops.git
   ```

2. Navigate to the directory:

   ```Bash
   cd 0x0E-web_stack_debugging_1
   ```

3. Execute the scripts:

   ```Bash
   ./0-nginx_likes_port_80
   ./1-debugging_made_short
   ```

## Author

- Walter
- Sylvain Kalache

---
Copyright © 2024 ALX, All rights reserved.
