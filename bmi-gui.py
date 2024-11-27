import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        height_cm = float(entry_height.get())
        weight_kg = float(entry_weight.get())
        
        # Convert height from cm to meters
        height_m = height_cm / 100
        
        # Calculate BMI
        bmi = weight_kg / (height_m ** 2)
        
        # Determine BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"
        
        # Display the result
        result_text = f"BMI: {bmi:.2f}\nCategory: {category}"
        label_result.config(text=result_text)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for height and weight.")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Input fields for height and weight
label_height = tk.Label(root, text="Height (cm):")
label_height.grid(row=0, column=0, padx=10, pady=10)

entry_height = tk.Entry(root)
entry_height.grid(row=0, column=1, padx=10, pady=10)

label_weight = tk.Label(root, text="Weight (kg):")
label_weight.grid(row=1, column=0, padx=10, pady=10)

entry_weight = tk.Entry(root)
entry_weight.grid(row=1, column=1, padx=10, pady=10)

# Calculate button
button_calculate = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
button_calculate.grid(row=2, column=0, columnspan=2, padx=10, pady=20)

# Label to display the result
label_result = tk.Label(root, text="BMI: \nCategory: ")
label_result.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
