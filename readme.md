<h2>Introduction:</h2>
This web application is built to analyze whether the given dataset follows Benford's Law. Benford's Law is a statistical phenomenon that states that in many naturally occurring datasets, the first digit is more likely to be small than large. The law has practical applications in fields such as accounting, fraud detection, and image processing.

<h2>Functionality:</h2>
The web application allows the user to upload a CSV file containing the dataset to be analyzed. The application then calculates the frequency distribution of the first digits in the dataset and compares it with the expected distribution based on Benford's Law. Finally, the application displays the results in the form of a table and a graph.

<h2>Technologies used:</h2>

>Python 3.9

>Pyramid 2.0.5

>Jinja2 3.0.2

>Plotly 5.5.0

>HTML5

>CSS3

<h2>Files:</h2>

benford.py: contains the code for calculating the Benford's Law distribution.
home.jinja2: contains the HTML code for the web application.
styles.css: contains the CSS code for styling the web application.
main.py: contains the main code for running the web application.

<h2>Installation:</h2>
To run the web application, the following packages need to be installed:

>Pyramid: pip install pyramid

>Jinja2: pip install pyramid_jinja2

>Plotly: pip install plotly

To start the server, navigate to the directory containing main.py and run the following command:

>python main.py

The server will start on port 6543.

<h2>Usage:</h2>

>Open a web browser and navigate to http://localhost:6543/.
>Click the "Choose File" button and select a CSV file to upload.
>Click the "Upload" button to upload the file.
>If the file follows Benford's Law, the application displays a table and a graph showing the distribution of the first digits in the dataset.
>If the file does not follow Benford's Law, the application displays a message indicating that the dataset does not follow Benford's Law.

>curl -X POST -F "csvfile=@benford_satisfy.csv" http://localhost:6543/json

>curl -X POST -F "csvfile=@benford_satisfy.csv" http://localhost:6543/json

for direct access to endpoint with json

<h2>Conclusion:</h2>
This web application provides a simple and user-friendly way to determine whether a given dataset follows Benford's Law. The application can be used in a wide range of fields where Benford's Law is applicable, such as accounting, fraud detection, and image processing.


<br>


<h2>BY: Amit Duwal</h2>

