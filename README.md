# Get Start

To get started with this project, follow these steps:
 1. Clone the repository to your local machine using `git clone https://github.com/aliahadmd/Django-Ideal-Template.git`
 2. Install all necessary dependencies by running `npm install` in the project directory
 3. Create a virtual environment for the project using `python -m venv env`
 4. Activate the virtual environment by running `source env/bin/activate` on Mac/Linux or `.\env\Scripts\activate` on Windows
 5. Install all necessary Python packages by running `pip install -r requirements.txt`
 6. Run `python manage.py makemigrations` to create the initial migrations
 8. Run `python manage.py migrate` to migrate the database
 9. Run `python manage.py migrate` to apply the migrations
 10. Run the project locally using `python manage.py runserver`
 11. Access the project at `http://localhost:8000/` in your browser


# Django Production Deployment Guide

This guide outlines the steps to deploy a Django application on a VPS server using PM2, Gunicorn, and Nginx.

## Prerequisites
- A VPS server (e.g., DigitalOcean, Linode, AWS EC2)
- SSH access to your server
- A domain name (optional, but recommended)

## Step 1: Update and Upgrade Packages

```bash
sudo apt update
sudo apt upgrade -y
```

## Step 2: Install Required Packages

```bash
sudo apt install python3-pip python3-venv nginx -y
```
or, can be use pyenv (recommanded)

## Step 3: Set Up Python Virtual Environment

```bash
mkdir ~/myproject
cd ~/myproject
python3 -m venv venv
source venv/bin/activate
```

## Step 4: Install Gunicorn

```bash
pip install gunicorn
```

## Step 5: Install PM2

```bash
sudo apt install nodejs npm -y
sudo npm install pm2@latest -g
```
or, install nvm for nodejs (recommanded)

## Step 6: Set Up Your Django Project

Clone your project or create a new one:

```bash
git clone https://github.com/yourusername/yourproject.git
# OR
django-admin startproject myproject
```


## Step 7: Collect Static Files

```bash
python manage.py collectstatic
```

## Step 8: Create Gunicorn Config File

Create `gunicorn_config.py` in your project directory:

```python
bind = "127.0.0.1:8000"
workers = 3
```
or (recommanded)

```python
import multiprocessing

#change port as your wish
bind = "127.0.0.1:8001" 
workers = multiprocessing.cpu_count() * 2 + 1
# create a folder called log and use pwd to see actual path and then add path/log/gunicorn-access.log and path/log/gunicorn-error.log
accesslog = "/home/dev/app/Django-Ideal-Template/log/gunicorn-access.log"
errorlog = "/home/dev/app/Django-Ideal-Template/log/gunicorn-error.log"
```

## Step 9: Create PM2 Ecosystem File

Create `ecosystem.config.js` in your project directory:

```javascript
// edit based on your project path
module.exports = {
    apps: [{
      name: "Django-Ideal-Template",
      script: "/home/dev/app/Django-Ideal-Template/venv/bin/gunicorn",
      args: "--config gunicorn_config.py core.wsgi:application",
      cwd: "/home/dev/app/Django-Ideal-Template",
      interpreter: "/home/dev/app/Django-Ideal-Template/venv/bin/python",
    }]
  }
```

## Step 10: Start Your Application with PM2

```bash
pm2 start ecosystem.config.js
```

--------------- Optional step if u se cloudflare 

## Step 11: Configure Nginx

Create a new Nginx configuration file:

```bash
sudo nano /etc/nginx/sites-available/myproject
```

Add the following configuration:

```nginx
server {
    listen 80;
    server_name your_domain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/yourusername/myproject;
    }

    location / {
        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_pass http://127.0.0.1:8000;
    }
}
```

## Step 12: Enable the Nginx Configuration

```bash
sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

## Step 13: Set Up SSL with Let's Encrypt (Optional but Recommended)

```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d your_domain.com
```

## Step 14: Final Steps

1. Configure your firewall to allow HTTP (80) and HTTPS (443) traffic.
2. Set up database backups.
3. Configure monitoring for your application.

Remember to replace `yourusername`, `your_domain.com`, and other placeholders with your actual information.

## pm2 commands

To ensure that PM2 and your application start automatically when your VPS reboots, follow these steps:

- Generate the PM2 startup script:

    ```bash
    pm2 startup
    ```
    This command will output a line starting with `sudo env PATH=....` Copy this entire line and run.



- Save the current PM2 process list:

    ```bash
    pm2 save
    ```

   This command saves the current list of running PM2 processes, ensuring they will be restarted when PM2 starts.


- After the server restarts, SSH back in and check if your application is running:

    ```bash
    pm2 list
    ```

- To check the status of your application, run the following command

    ```bash
    pm2 status
    ```


- To stop your application:
  ```bash
  pm2 stop django_app
  ```

- To restart your application:
  ```bash
  pm2 restart django_app
  ```

- To delete your application:
  ```bash
  pm2 delete django_app
  ```

- To view logs:
  ```bash
  pm2 logs django_app
  ```

- To monitor CPU and Memory usage:
  ```bash
  pm2 monit
  ```

