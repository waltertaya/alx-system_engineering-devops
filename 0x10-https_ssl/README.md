# Project Title: HTTPS SSL Configuration

## Description

This project focuses on configuring HTTPS SSL for a web server using HAProxy. The tasks involve setting up SSL termination, creating certificates using certbot, and ensuring encrypted traffic is properly handled. Additionally, HAProxy is configured to redirect HTTP traffic to HTTPS automatically.

## Tasks

### Task 0: World wide web

- **Description:** Configure domain zone to point subdomains to specific IPs and create a Bash script to display information about subdomains.
- **Requirements:**
  - Add subdomains www, lb-01, web-01, and web-02 to the domain.
  - Write a Bash script to display information about subdomains.
  - The script must accept domain and subdomain parameters.
  - Use `awk` and at least one Bash function.
  
### Task 1: HAproxy SSL termination

- **Description:** Configure HAProxy to accept encrypted traffic for the subdomain www and serve encrypted traffic.
- **Requirements:**
  - HAProxy must listen on port TCP 443 and accept SSL traffic.
  - HAProxy must serve encrypted traffic returning the root of the web server.
  - Share HAProxy configuration as the file `1-haproxy_ssl_termination`.

### Task 2: No loophole in your website traffic

- **Description:** Configure HAProxy to automatically redirect HTTP traffic to HTTPS.
- **Requirements:**
  - HAProxy should transparently redirect HTTP traffic to HTTPS with a 301 response.
  - Share HAProxy configuration as the file `100-redirect_http_to_https`.

## Repository Structure

- **GitHub Repository:** [alx-system_engineering-devops](https://github.com/waltertaya/alx-system_engineering-devops)
- **Directory:** 0x10-https_ssl

## Scripts and Configurations

1. **0-world_wide_web**
   - Bash script to configure domain zone and display subdomain information.

2. **1-haproxy_ssl_termination**
   - HAProxy configuration file for SSL termination.

3. **100-redirect_http_to_https**
   - HAProxy configuration file for redirecting HTTP traffic to HTTPS.

## Usage

1. Clone the repository:

   ```Bash
   git clone https://github.com/alx-system_engineering-devops.git
   ```

2. Navigate to the directory:

   ```Bash
   cd 0x10-https_ssl
   ```

3. Execute the scripts and configurations accordingly.

## Author

- Walter
- Sylvain Kalache, co-founder at Holberton School

---
Copyright © 2024 ALX, All rights reserved.
