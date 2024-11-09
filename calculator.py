from flask import Flask, jsonify, request

app = Flask(__name__)

# Calculator operations
def calculate(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return "Cannot divide by zero" if b == 0 else a / b
    elif operation == "modulus":
        return a % b
    elif operation == "power":
        return a ** b
    else:
        return "Invalid operation"

# Single API endpoint for all operations
@app.route('/calculate', methods=['POST'])
def calculate_endpoint():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    operation = data.get('operation')
    
    # Perform the calculation
    result = calculate(a, b, operation)
    return jsonify(result=result)

@app.route('/salman-divide', methods=['GET'])
def divide():
    # Get query parameters 'a' and 'b' from the URL
    a = request.args.get('a')
    b = request.args.get('b')
    
    # Validate that both 'a' and 'b' are provided
    if a is None or b is None:
        return jsonify(error="Missing 'a' or 'b' parameter"), 400
    
    try:
        # Convert 'a' and 'b' to floats
        a = float(a)
        b = float(b)
    except ValueError:
        return jsonify(error="'a' and 'b' must be numbers"), 400

    # Handle division by zero
    if b == 0:
        return jsonify(error="Cannot divide by zero"), 400
    
    # Perform the division
    result = a / b
    return jsonify(result=result)

if __name__ == "__main__":
    app.run(debug=True)
