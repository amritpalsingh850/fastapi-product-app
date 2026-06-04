python -m venv venv

venv\Scripts\activate

pip install fastapi uvicorn sqlalchemy psycopg2-binary python-multipart python-dotenv



https://github.com/amritpalsingh850/fastapi-product-app.git

…or create a new repository on the command line
echo "# fastapi-product-app" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/amritpalsingh850/fastapi-product-app.git
git push -u origin main

…or push an existing repository from the command line

git remote add origin https://github.com/amritpalsingh850/fastapi-product-app.git
git branch -M main
git push -u origin main

on server

Connect via SSH
ssh azureuser@<PUBLIC_IP>
ssh azureuser@98.70.65.215
98.70.65.215

cd /home/azureuser

git clone <your-repo-url>
git clone https://github.com/amritpalsingh850/fastapi-product-app.git

cd fastapi-product-app

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

RuntimeError: Directory 'uploads' does not exist

mkdir uploads

uvicorn app.main:app --host 0.0.0.0 --port 8000

sudo nano /etc/systemd/system/fastapi.service

sudo nano /etc/systemd/system/fastapi-one.service


sudo nano /etc/nginx/sites-available/fastapi


sudo systemctl restart nginx
sudo systemctl status nginx


http://98.70.65.215/uploads/5fff2244-55af-45e4-89a3-c0804769b682.png


Self-Signed Certificate (Testing Only)

sudo mkdir -p /etc/nginx/ssl

sudo openssl req -x509 -nodes -days 365 \
-newkey rsa:2048 \
-keyout /etc/nginx/ssl/fastapi.key \
-out /etc/nginx/ssl/fastapi.crt

update nginx configration



https://chatgpt.com/c/6a1d72e3-1b2c-8322-97ce-22f0e68cde5f