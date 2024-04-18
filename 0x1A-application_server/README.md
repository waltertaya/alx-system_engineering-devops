# 0x1A Application Server

This repository contains the projects completed for the 0x1A Application Server curriculum at ALX System Engineering & DevOps. The projects focus on setting up an application server, integrating it with Nginx, and serving dynamic content using Flask and Gunicorn.

## Projects

### 0. Set up development with Python

In this project, we set up a development environment for testing and debugging our AirBnB clone v2 web framework on `web-01`.

**Requirements:**

- Complete task #3 of the SSH project for `web-01`.
- Install the `net-tools` package.
- Git clone your AirBnB_clone_v2 repository.
- Configure `web_flask/0-hello_route.py` to serve content from `/airbnb-onepage/` on port 5000.

**Example:**

```bash
# Terminal 1
ubuntu@229-web-01:~/AirBnB_clone_v2$ python3 -m web_flask.0-hello_route

# Terminal 2
ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5000/airbnb-onepage/
```

### 1. Set up production with Gunicorn

In this project, we set up a production environment using Gunicorn on `web-01`, port 5000.

**Requirements:**

- Install Gunicorn and required libraries.
- Serve the same content as the previous task from port 5000.

**Example:**

```bash
# Terminal 1
ubuntu@229-web-01:~/AirBnB_clone_v2$ gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
```

### 2. Serve a page with Nginx

Configure Nginx to serve content from `/airbnb-onepage/` and proxy requests to the Gunicorn process.

**Requirements:**

- Serve the page both locally and on its public IP on port 80.
- Proxy requests to the process listening on port 5000.

### 3. Add a route with query parameters

Expand the web application by adding a service for Gunicorn to handle with query parameters.

**Requirements:**

- Proxy requests to the route `/airbnb-dynamic/number_odd_or_even/<int:n>` to a Gunicorn instance on port 5001.

### 4. Serve your AirBnB clone

Serve the AirBnB clone v4 web dynamic on `web-01`.

**Requirements:**

- Serve content from `web_dynamic/2-hbnb.py` on port 5003.
- Set up Nginx to point to the Gunicorn instance.
- Serve static assets found in `web_dynamic/static/`.

### 5. Deploy it!

Set up the Gunicorn process to run by default using systemd.

**Requirements:**

- Write a systemd script to start a Gunicorn process.
- Bind the process to port 5003.
- Log errors and access in `/tmp/airbnb-error.log` and `/tmp/airbnb-access.log`.

### 6. No service interruption

Write a Bash script to reload Gunicorn gracefully.

**Example:**

```bash
sylvain@ubuntu$ ps auxf | grep gunicorn
sylvain@ubuntu$ ./4-reload_gunicorn_no_downtime
sylvain@ubuntu$ ps auxf | grep gunicorn
```

## Repository

- **GitHub repository**: [alx-system_engineering-devops](https://github.com/waltertaya/alx-system_engineering-devops)
- **Directory**: `0x1A-application_server`
