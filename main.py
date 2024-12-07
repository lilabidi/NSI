from pyscript import document, create_proxy

def calculate_square(event):
    input_value = document.querySelector("#inputNumber").value
    result_div = document.querySelector("#result")
    
    if input_value:
        try:
            number = float(input_value)
            square = number ** 2
            result_div.innerText = f"The square of {number} is {square}."
        except ValueError:
            result_div.innerText = "Please enter a valid number."
    else:
        result_div.innerText = "Please enter a number."

# Create a proxy for the event handler
proxy = create_proxy(calculate_square)

# Attach the proxy function to the button's click event
document.querySelector("#calculateButton").addEventListener("click", proxy)
