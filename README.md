# Ex.05 Design a Website for Server Side Processing
## Date:30.04.25
## Name:Roshini S
## Reg.no:212223230174

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
math.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculate Power of a Lamp</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4; /* Light background color */
            margin: 0;
            padding: 0;
        }

        h1 {
            text-align: center;
            color: #0a0909;
            margin-top: 40px;
        }

        form {
            background-color: rgb(177, 104, 174);
            max-width: 400px;
            margin: 30px auto;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }

        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
        }

        input[type="number"] {
            width: 100%;
            padding: 8px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 6px;
        }

        button {
            background-color: #d915a1;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 16px;
            width: 100%;
        }

        button:hover {
            background-color: #d6131a;
        }

        p {
            margin-top: 20px;
            text-align: center;
            font-size: 18px;
            color: #222;
        }
    </style>
</head>
<body>
    <h1>Calculate Power of a Lamp</h1>
    <form method="post">
        <label for="intensity">Intensity (I) in amperes:</label>
        <input type="number" id="intensity" name="intensity" required>
        
        <label for="resistance">Resistance (R) in ohms:</label>
        <input type="number" id="resistance" name="resistance" required>
        
        <button type="submit">Calculate</button>
        
        <p id="result">The power of the lamp is: </p>
    </form>

    <script>
        // Function to calculate the power based on the formula P = I^2 * R
        document.querySelector('form').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent form submission

            var intensity = parseFloat(document.getElementById('intensity').value);
            var resistance = parseFloat(document.getElementById('resistance').value);

            // Power calculation: P = I^2 * R
            var power = Math.pow(intensity, 2) * resistance;

            // Display result
            document.getElementById('result').textContent = 'The power of the lamp is: ' + power.toFixed(2) + ' watts';
        });
    </script>
</body>
</html>

```
## HOMEPAGE:
![Screenshot 2025-04-30 160229](https://github.com/user-attachments/assets/d46990e9-a313-40a4-a8b9-86d625457738)


## RESULT:
The program for performing server side processing is completed successfully.
