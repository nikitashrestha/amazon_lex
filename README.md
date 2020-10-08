# Weather Bot using Amazon Lex

Amazon LEX is one of the most popular API based Amazon AI services that allows to build interactive and conversational interfaces into any application using voice and text.

Created a simple bot on amazon lex, that gives weather report of a particular place based on user query.

The weather bot always gives the temperature of that place and the weather status (either cloudy or clear).
Based on the information provided by the API, there might be some extra information ( like if it is raining or snowing or windy) and also the extent to which such scenario is occuring ( like is it mild or heavy).

- The `weather bot` created is able to answer questions like:
How's the weather, tell me today's weather

- Once the user types their question, the `weather bot` consumes it and ask user the place for which they want the weather       report.

- Once the user provides the name of place, the `weather bot` immediately triggers the lambda function with the queried place.

- The lamda function then make a call to `openweathermap API` to fetch the weather details, perform some analysis on the response and finally sends the response back to `weather bot`.

The `weather bot` is also able to provide `voice assistant` to the users.

## API used to extract weather details

Used openweathermap API to extract details of weather condition based on particular place. This is the most popular API used to query weather status base on geographicl regions, city, country and many more.

You can find details of its implementation [here](https://openweathermap.org/current) 


