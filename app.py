import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Hardcoded laptop data with upgradeable components info
laptops = [
    {
        "id": 1,
        "name": "Lenovo IdeaPad 3 15ADA05",
        "price_rub": 45000,
        "upgrades": {
            "processor": "No",
            "graphics_card": "No",
            "ram": "Yes, up to 12GB",
            "storage": "Yes, supports SSD upgrade"
        }
    },
    {
        "id": 2,
        "name": "Acer Aspire 5 A515-56",
        "price_rub": 70000,
        "upgrades": {
            "processor": "No",
            "graphics_card": "No",
            "ram": "Yes, up to 20GB",
            "storage": "Yes, supports SSD upgrade"
        }
    },
    {
        "id": 3,
        "name": "ASUS VivoBook 15 X515EA",
        "price_rub": 65000,
        "upgrades": {
            "processor": "No",
            "graphics_card": "No",
            "ram": "Yes, up to 16GB",
            "storage": "Yes, supports SSD upgrade"
        }
    },
    {
        "id": 4,
        "name": "HP 15s-fq2717ur",
        "price_rub": 60000,
        "upgrades": {
            "processor": "No",
            "graphics_card": "No",
            "ram": "Yes, up to 16GB",
            "storage": "Yes, supports SSD upgrade"
        }
    },
    {
        "id": 5,
        "name": "Dell Inspiron 15 3501",
        "price_rub": 75000,
        "upgrades": {
            "processor": "No",
            "graphics_card": "No",
            "ram": "Yes, up to 16GB",
            "storage": "Yes, supports SSD upgrade"
        }
    }
]

@app.route("/")
def index():
    return render_template("index.html", laptops=laptops)

@app.route("/laptop_info/<int:laptop_id>")
def laptop_info(laptop_id):
    laptop = next((l for l in laptops if l["id"] == laptop_id), None)
    if laptop:
        return jsonify(laptop["upgrades"])
    else:
        return jsonify({"error": "Laptop not found"}), 404
    
if __name__ == '__main__':
    app.run(debug=True)(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))