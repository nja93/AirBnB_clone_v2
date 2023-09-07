#!/bin/bash
# Install Nginx if it's not already installed
sudo apt-get update
sudo apt-get install -y nginx

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file for testing 
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create or recreate the symbolic link
sudo rm -f /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve /data/web_static/current/ at /hbnb_static/
nginx_config="/etc/nginx/sites-available/default"
nginx_alias="location /hbnb_static/ { alias /data/web_static/current/; }"
if ! grep -q "$nginx_alias" "$nginx_config"; then
    sudo sed -i "/server_name _;/a \ \ \ \ $nginx_alias" "$nginx_config"
fi

# Restart Nginx to apply changes
sudo service nginx restart
