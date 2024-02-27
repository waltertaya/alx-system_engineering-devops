# 0x0C. Web server

* Child Process - Is a process created by another process.
* Nginx (pronounced "engine x") is a web server that can also be used as a reverse proxy, load balancer, mail proxy and HTTP cache.
* The software was created by Russian developer `Igor Sysoev` and publicly released in 2004.
* Nginx is free and open-source software, released under the terms of the 2-clause BSD license. A large fraction of web servers use Nginx, often as a load balancer.
* A load balancer is the device or service that sits between the user and the server group and acts as an invisible facilitator, ensuring that all resource servers are used equally.
* A reverse proxy is a server that sits in front of web servers and forwards client(e.g web browser) requests to those web servers. Reverse proxies are typically implemented to help increase security, performance and reliability.
* HTTP cache stores a response associated with a request and reuses the stored response for subsequent requests.
* As of June 2022, W3Tech's web server count of all web sites ranked Nginx first with 33.6%. Apache was second at 31.4% and Cloudflare Server third at 21.6%. As of March 2022, Netcraft estimated that Nginx served 22.01% of the million busiest websites with Apache a little ahead at 23.04%. Cloudflare at 19.53% and Microsoft Internet Information Services at 5.78% rounded out the top four servers for the busiest websites. Some of Netcraft's other statistics show Nginx ahead of Apache.
* A 2018 survey of Docker usage found that Nginx was the most commonly deployed technology in Docker containers.[16] In OpenBSD version 5.2 (November 2012), Nginx became part of the OpenBSD base system, providing an alternative to the system's fork of Apache 1.3, which it was intended to replace, but later in version 5.7 (November 2014) it was removed in favor of OpenBSD's own httpd(8).
* Nginx is easy to configure in order to serve static web content or act as a proxy server.
* Nginx can be deployed to also serve dynamic content on the networking using FastCGI, SCGI handlers for scripts, WSGI application servers or Phusion Passenger modules, and can serve as a software load balancer.
* Nginx uses an asynchrous event driven aproach, rather than threads, to handle requests.

## How To Set Up Nginx Server Blocks(Virtual Hosts) on Ubuntu

* When using the Nginx web server, server blocks (similar to virtual hosts in Apache) can be used to encapsulate configuration details and host more than one domain on a single server.

* In this guide, we’ll discuss how to configure server blocks in Nginx on an Ubuntu 16.04 server.

1. Create directories for each domain:
   ```bash
   sudo mkdir -p /var/www/example.com/html
   sudo mkdir -p /var/www/test.com/html
   ```

2. Set ownership of directories to the current user:
   ```bash
   sudo chown -R $USER:$USER /var/www/example.com/html
   sudo chown -R $USER:$USER /var/www/test.com/html
   ```

3. Set permissions for directories:
   ```bash
   sudo chmod -R 755 /var/www
   ```

4. Create index.html files for each domain:
   ```bash
   nano /var/www/example.com/html/index.html
   nano /var/www/test.com/html/index.html
   ```

5. Copy default Nginx server block configuration:
   ```bash
   sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/example.com
   ```

6. Modify server block configuration files:
   ```bash
   sudo nano /etc/nginx/sites-available/example.com
   sudo nano /etc/nginx/sites-available/test.com
   ```

7. Create symbolic links to enable server blocks:
   ```bash
   sudo ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/
   sudo ln -s /etc/nginx/sites-available/test.com /etc/nginx/sites-enabled/
   ```

8. Edit nginx.conf file to adjust server_names_hash_bucket_size:
   ```bash
   sudo nano /etc/nginx/nginx.conf
   ```

9. Test Nginx configuration:
   ```bash
   sudo nginx -t
   ```

10. Restart Nginx to apply changes:
   ```bash
   sudo systemctl restart nginx
   ```

Following these steps will set up Nginx server blocks for hosting multiple domains on a single Ubuntu 16.04 server.

## Root and sub domain

1. **Initial Testing on Default/Test Domain**: Landing pages are initially accessible under a default/test domain provided by Landingi for testing purposes, allowing users to review and verify the functionality of their landing pages.

2. **Importance of Having a Domain Name**: Assigning a landing page to a custom domain name enhances its professional appearance and instills trust in visitors, especially for commercial purposes. It also resolves potential issues with advertising campaigns, page indexing, and firewall blocking.

3. **Definition of Internet Domain**: An internet domain is a textual representation of an IP address, making it easier for users to remember and access websites.

4. **Definition of Domain Name**: A domain name consists of a second-level domain, a dot, and a top-level domain. It serves as the identity of a website and can be purchased from domain registrars.

5. **Limitations on Redirecting Root/Naked Domains**: Landingi supports redirection only via the A record to an IP address and does not currently support direct landing pages under naked domains. Subdomains are recommended instead.

6. **Definition of Subdomain**: A subdomain is a subdivision of a domain name, placed before the root domain name and separated by a dot. Subdomains are used for organizing content and campaigns.

7. **Usage of Subdomains with Paths/Subfolders**: Landing pages can be published to subdomains with subfolders (paths) in the URL, allowing for organized content presentation. Each subdomain can have multiple paths, and there's no limit to the number of landing pages per path.

## HTTP requests

1. **HTTP Methods**:
    - **GET**: Retrieves data from a server using a URI.
    - **HEAD**: Similar to GET but transfers only the status line and headers.
    - **POST**: Sends data to the server, typically used for form submissions.
    - **PUT**: Replaces all current representations of a resource with uploaded content.
    - **DELETE**: Removes all representations of a resource.
    - **CONNECT**: Establishes a tunnel to a server.
    - **OPTIONS**: Describes communication options for a resource.
    - **TRACE**: Echoes the contents of an HTTP request for debugging.

2. **Functionality**:
    - **GET**: Retrieves data specified by URL parameters.
    - **HEAD**: Retrieves header information without an entity-body.
    - **POST**: Sends data to the server for processing, e.g., form data.
    - **PUT**: Stores entity-body at a specified URL.
    - **DELETE**: Deletes a file specified by URL.
    - **CONNECT**: Establishes a network connection to a web server.
    - **OPTIONS**: Obtains supported HTTP methods and server options.
    - **TRACE**: Echoes HTTP request contents for debugging.

3. **Example Requests**:
    - Each method is demonstrated with an example request and server response, illustrating their usage and expected outcomes.

## HTTP redirection

1. **Redirects**: Redirecting a URL means sending users and search engines to a different URL than the one they initially requested. The three common types of redirects are 301, 302, and Meta Refresh.

2. **Types of Redirects**:
   - **301 Moved Permanently**: Passes full link equity to the redirected page and is recommended for SEO.
   - **302 Found**: Used for temporary URL changes.
   - **Meta Refresh**: Executes redirects on the page level and is not recommended for SEO.

3. **SEO Best Practices**:
   - Use 301 redirects for permanent URL changes.
   - Avoid meta refreshes for redirects due to poor usability and loss of link equity.
   - Ensure proper implementation to maintain SEO value during content transfer or domain changes.

4. **Implementation**:
   - Most modern CMS platforms offer built-in solutions for managing redirects.
   - .htaccess file for Apache servers: Common method for implementing redirects with directives like Redirect and mod_rewrite.
   - PHP: Example of implementing a 301 redirect using PHP.
   - JavaScript: Not recommended for SEO purposes due to potential indexing issues, but can be implemented with window.location.

## Status Codes

## Log files on Linux

* Log files in Ubuntu Linux are stored in the `/var/log` directory.

* Common log files and their purposes include:
- `/var/log/messages`: General log messages
- `/var/log/boot`: System boot log
- `/var/log/debug`: Debugging log messages
- `/var/log/auth.log`: User login and authentication logs
- `/var/log/daemon.log`: Logs from running services like squid and ntpd
- `/var/log/dmesg`: Linux kernel ring buffer log
- `/var/log/dpkg.log`: Log of binary package installations and other information
- `/var/log/faillog`: User failed login log file
- `/var/log/kern.log`: Kernel log file
- `/var/log/lpr.log`: Printer log file
- `/var/log/mail.*`: Log files for mail server messages
- `/var/log/mysql.*`: MySQL server log file
- `/var/log/user.log`: All userlevel logs
- `/var/log/xorg.0.log`: X.org log file
- `/var/log/apache2/*`: Apache web server log files directory
- `/var/log/lighttpd/*`: Lighttpd web server log files directory
- `/var/log/fsck/*`: fsck command log
- `/var/log/apport.log`: Application crash report / log file

* View log files at the shell prompt using commands like `tail`, `more`, `less`, and `grep`. Example: `tail -f /var/log/apport.log`.

* View log files using GUI tools like the GNOME System Log Viewer, which provides a graphical interface for easier log management, including log monitoring, statistics display, and a calendar to track trends and problems.

## Use of `scp`

```bash
scp -i PATH_TO_SSH_KEY PATH_TO_FILE USERNAME@IP:~/
```
