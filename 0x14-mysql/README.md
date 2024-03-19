# Project: 0x14 MySQL

## Description

This project focuses on MySQL setup, administration, and replication within a DevOps and SysAdmin context. It involves installing MySQL, configuring users and permissions, setting up database replication, and implementing backup strategies. By completing the tasks in this project, participants will gain a deeper understanding of MySQL database management, replication, and backup strategies.

## Concepts

Throughout this project, you will explore the following key concepts:

- Fresh Reset and Installation of MySQL 5.7
- Database Administration
- Web Stack Debugging
- Primary-Replica Clusters
- Database Backup Strategies

## Learning Objectives

Upon completing this project, you should be able to:

- Explain the main role of a database
- Define a database replica and its purpose
- Understand the importance of storing database backups in different physical locations
- Implement database backup strategies and verify their effectiveness

## Requirements

- Operating System: Ubuntu 16.04 LTS
- Editors: vi, vim, emacs
- All Bash scripts should end with a new line
- All Bash scripts must be executable and pass Shellcheck without any error
- Use `#!/usr/bin/env bash` as the first line in all Bash scripts
- Complete Task #3 of the SSH project for web-01 and web-02
- Ensure proper README.md file at the root of the project folder

## Tasks

### 0. Install MySQL

Install MySQL 5.7.x on both web-01 and web-02 servers.

### 1. Let us in!

Create a MySQL user named `holberton_user` on both web-01 and web-02 with appropriate permissions.

### 2. If only you could see what I've seen with your eyes

Set up a database named `tyrell_corp` on web-01, containing a table named `nexus6` with at least one entry.

### 3. Quite an experience to live in fear, isn't it?

Create a new user `replica_user` on the primary MySQL server (web-01) for replication purposes.

### 4. Setup a Primary-Replica infrastructure using MySQL

Establish a Primary-Replica infrastructure with MySQL, hosting primary on web-01 and replica on web-02.

### 5. MySQL backup

Write a Bash script to generate a MySQL dump, compress it, and create a backup archive.

## Repository Information

- GitHub Repository: [alx-system_engineering-devops](https://github.com/waltertaya/alx-system_engineering-devops)
- Directory: 0x14-mysql

## Authors

@waltertaya
This project is authored by Sylvain Kalache, co-founder at Holberton School.

## License

© 2024 ALX. All rights reserved.
