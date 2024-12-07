from pyscript import document

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

