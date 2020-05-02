from flaskapp import app
from flask_wtf.csrf import CSRFProtect

if __name__ == "__main__":
    
    app.run(host="127.0.0.1", debug=True)
