...
echo [$(date)]: "START"
echo [$(date)]: "Creating Conda Envioronment with Python 3.8"
conda create --prefix ./env python==3.8 -y
echo [$(date)]: "Activating env"
source activate ./env
echo [$(date)]: "Installing Dev Requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "End......."
