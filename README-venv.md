
mkdir venv

##

cd  /Users/jaspervanblokland/Documents/GitHub/TYPETR-Store 

python -m venv venv --prompt=TYPETR-Store

source venv/bin/activate

pip install --upgrade pip

pip install pillow
pip install numpy

pip install git+https://github.com/typemytype/drawbot

###

python build-003.py
