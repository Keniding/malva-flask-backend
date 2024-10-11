from waitress import serve
from app import create_app

app = create_app()
# serve(app, host='0.0.0.0', port=8000)

if __name__ == '__main__':
    # app.run(debug=True)
    serve(app, host='0.0.0.0', port=8000)
    
# malva-flask-backend on  master [!?] via 🐍 v3.12.3 
# ❯ python -m venv myenv
# ∙

# malva-flask-backend on  master [!?] via 🐍 v3.12.3 took 7s
# ❯ myenv\Scripts\activate
# ∙

# malva-flask-backend on  master [!?] via 🐍 v3.12.3 (myenv) 

# myenv\Scripts\activate
