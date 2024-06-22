module.exports = {
    apps: [{
      name: "Django-Ideal-Template",
      script: "/home/dev/app/Django-Ideal-Template/venv/bin/gunicorn",
      args: "--config gunicorn_config.py core.wsgi:application",
      cwd: "/home/dev/app/Django-Ideal-Template",
      interpreter: "/home/dev/app/Django-Ideal-Template/venv/bin/python",
    }]
  }