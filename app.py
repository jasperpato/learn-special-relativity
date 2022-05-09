import os
import sys
from app import create_app

sys.path.insert(0, os.path.dirname(__file__))

app=create_app()

if __name__ == "__main__" and len(sys.argv) > 1:
    app.run(debug=True)
