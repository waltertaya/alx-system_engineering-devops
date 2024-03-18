# **Firewall Configuration**

## **Introduction:**

This project focuses on configuring firewall settings on a server using the Uncomplicated Firewall (ufw) utility. The tasks involve blocking all incoming traffic except for specific TCP ports and setting up port forwarding to redirect traffic from one port to another.

## **Tasks:**

### **0. Block all incoming traffic but (mandatory):**

    - Configure ufw to block all incoming traffic on the server, except for TCP ports 22 (SSH), 443 (HTTPS SSL), and 80 (HTTP).
    - Provide the ufw commands used for configuration.

### **1. Port forwarding (advanced):**

    - Configure the firewall on web-01 to forward traffic from port 8080/TCP to port 80/TCP.
    - Copy the modified ufw configuration file to demonstrate the changes made for port forwarding.

## **Concepts:**

    - Web stack debugging: Understanding how to debug and troubleshoot web server issues using tools like telnet.

## **Background Context:**

The absence of a firewall can leave servers vulnerable to unauthorized access and attacks. Hence, configuring firewalls is crucial for securing server environments.

## **Resources:**

    - What is a firewall: Provides an overview of firewall concepts and functionalities.
    - Web stack debugging: Explains the use of telnet for checking socket connections and debugging web stack issues.

## **Repository Details:**

    - GitHub repository: [alx-system_engineering-devops](https://github.com/waltertaya/alx-system_engineering-devops)
    - Directory: 0x13-firewall
    - Files:
      - 0-block_all_incoming_traffic_but: Contains ufw commands for blocking incoming traffic except for specified ports.
      - 100-port_forwarding: Demonstrates the configuration for port forwarding using ufw.

## **Copyright:**

    - © 2024 ALX. All rights reserved.
    - @waltertaya
