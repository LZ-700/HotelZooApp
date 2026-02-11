from app import create_app
from app import db

app = create_app()

for rule in app.url_map.iter_rules():
    print(rule)

if __name__ == "__main__":
    app.run(debug=True)

print(db.engine.table_names())
with app.app_context():
    db.create_all()