<h3>Contagious Disease Forcast</h3>
Web application too big to upload to Github due to volume of predictive data, please see link at end of document to see our project in DevPost
<h3>Inspiration</h3>
The spread of diseases is a vital facet of healthcare research. Also of interest was the socioeconomic factor of unemployment rate and how this would affect access to healthcare and other factors that influence the spread of disease.

<h3>What it does</h3>
Creates a visualization of the percentage of all deaths that are flu deaths as well as the unemployment rate for 121 United States cities. With weekly data ranging from 1990 to 2016, we have mapped the percentage of all deaths that are flu deaths as well as unemployment rate at that time and location. Looking to the future, we have created a K-Nearest Neighbors model to predict influenza deaths using factors such as location, year, week, and most importantly, unemployment rate.

<h3>How we built it</h3>
Using data sets from the Centers for Disease Control and Prevention and The Department of Labor, we built a visualization using javascript leaflets with state color varying by flu severity and individual city flu mortality and unemployment rates. The K-Nearest neighbors model was created using SciKit-Learn to predict future flu data based on the prior datasets. Built on a local host, this web visualization is also enabled for iPad, iPhone 6+, iPhone 6, and a variety of other mobile devices.

<h3>Challenges we ran into</h3>
From computer problems to training a model, the process of creating a working visualization proved to have many challenges. Leverages rest APIs for Javascript libraries and correctly importing the data to the end product. Working with such large datasets, it was difficult to ensure the proper format and clean data. Implementing CSS libraries also proved to be a challenge, as well as training a model and creating predictions.

<h3>Accomplishments that we're proud of</h3>
We are proud of every element of our final product. The visualization of the flu data on the U.S. map with the specific coloring related to severity, the specific city data, the week slider, and overall design of the visualization are all elements that we are proud of. An accomplishment we are particularly proud of is the K-Nearest Neighbor model and it's predictions.

<h3>What we learned</h3>
Throughout this process, we have learned how to train a K-Nearest Neighbor model and make predictions based on that data. We have also learned many new elements of web design and how to deal with all of the challenges we have encountered over the past two days. This experience has also helped us develop many new collaborative and problem solving skills, as well as how to develop under pressure and with limited time.

<h3>What's next for Where in the World is Flu-men Sandiego?</h3>
An improved prediction model with more socioeconomic data would be a wonderful improvement to Where in the World is Flu-men Sandiego. With more time, we could extend the model beyond just the flu to include the spread of other diseases. We have also considered using airport data to determine if a relationship exists between transportation and the spread of disease.

<h3>Built with</h3>
Python, Python Machine learning Libraries, Javascript APIS, Bootstrap, MongoDB, Pandas, and much love

<h3>Devpost URL</h3>
https://devpost.com/software/where-in-the-world-is-flu-men-sandiego
