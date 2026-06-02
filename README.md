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

cd fastapi-product-app

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

RuntimeError: Directory 'uploads' does not exist