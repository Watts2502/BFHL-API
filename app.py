from flask import Flask, request, jsonify
import re

app = Flask(__name__)

FULL_NAME = "Shrivatsa Naik"
DOB = "25022004"
EMAIL = "shrivatsa.prashant2022@vitstudent.ac.in"
ROLL_NUMBER = "22BRS1085"

@app.route("/bfhl", methods=["POST"])
def bfhl():
    try:
        data = request.get_json()
        arr = data.get("data", [])

        odd_numbers = []
        even_numbers = []
        alphabets = []
        special_characters = []
        total_sum = 0

        for item in arr:
            if item.isdigit():
                num = int(item)
                if num % 2 == 0:
                    even_numbers.append(num)
                else:
                    odd_numbers.append(num)
                total_sum += num
            elif re.match("^[a-zA-Z]+$", item):
                alphabets.append(item.upper())
            else:
                special_characters.append(item)

        concat_string = ""
        all_alpha = "".join(x for x in arr if re.match("^[a-zA-Z]+$", x))
        rev = all_alpha[::-1]
        for i, ch in enumerate(rev):
            concat_string += ch.upper() if i % 2 == 0 else ch.lower()
        
        response = {
            "is_success": True,
            "user_id": f"{FULL_NAME.lower().replace(' ', '_')}_{DOB}",
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(total_sum),
            "concat_string": concat_string
        }

        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({
            "is_success": False,
            "error": str(e)
        }), 400

if __name__ == "__main__":
    app.run(debug=True)