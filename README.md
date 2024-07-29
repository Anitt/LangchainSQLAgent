# LangChain SQL Agent

This project is a web-based application that uses the Langchain RAG framework with OpenAI  and Langchain Agents to respond to natural language queries directed at an SQLite database. This TexttoSQL application leverages Flask and Gradio for the backend and provides an interactive interface for users.  This Application is integrated with Langsmith for testing , debugging and Development of Generative AI Applicatons.

# Problem Addressed

The SQL Agent in LangChain addresses the complex problem of bridging the gap between natural language and structured database querying, enabling Stakeholders/LeadershipTeam to interact with SQL databases without requiring technical expertise in SQL syntax, thereby making data access easy and enhancing decision-making capabilities.

# Then GenAI Framework and tools used with rationale behind their selection

## OpenAI's GPT 3.5 Turbo:

Rationale: Advanced language models for accurate natural language understanding and SQL query generation with good support and documenation for API usage.

## LangChain Framework:

Rationale: Integrated environment for combining language models with data sources, facilitating natural language interaction with databases. Powerful Framework providing seamless integration with LLM with customization and flexibility. 

## SQLDatabase Utility:

Rationale: Facilitates seamless integration with SQL databases, including schema introspection and query execution.

## Schema Introspection Tools(SQL Agent):

Rationale: Extracts metadata about tables, columns, and relationships to ensure accurate SQL query generation.

## Custom Prompt Templates:

Rationale: Enhances language model responses by providing specific context, improving the relevance and accuracy of generated SQL queries.

## Langsmith:

Rationale: Integrated with this application for testing , debugging and development of Text to SQL product. Using langsmith underhood implmentation and function's can be understood and debugged which helps 
developers for testing and development of applications.

# Architecutre and Workflow  

## User Interaction:

The user inputs a natural language query through the Gradio interface (User UI).

## Query Handling (Gradio):

Gradio acts as the frontend interface, where user inputs are collected and sent to the Flask server.

## Request Routing (Flask):

Flask, functioning as the backend server, receives the query from Gradio. It processes the request and forwards it to the LangChain SQL Agent.

## Language Understanding (OpenAI GPT-3.5):

The LangChain SQL Agent uses OpenAI's GPT-3.5 model to understand and interpret the natural language query.

## Schema Retrieval:

The Schema Introspection Module within the LangChain SQL Agent retrieves necessary schema details from the SQL Database.

## Prompt Customization:

The Prompt Template Module customizes the prompt for GPT-3.5 based on the schema and user query.

## SQL Query Generation:

The LangChain SQL Agent generates an SQL query using GPT-3.5 based on the customized prompt and schema information.

## Execution and Data Retrieval:

The Query Execution Module executes the generated SQL query on the SQL Database and retrieves the results.

## Result Formatting:

Result Augmentation (Optional with RAG):

If additional context or explanations are needed, the results might be reprocessed by GPT-3.5 using the retrieved information to provide a more detailed or natural language explanation.

## Response Delivery:

Flask sends the formatted results back to the Gradio interface.

## User Feedback:

The user views the response through the Gradio interface.

## Monitoring and Logging:

All interactions, including queries and responses, are logged using LangSmith.

# RAG Integration Overview :

## Retrieval Component:

Retrieves relevant schema information, past queries, or contextual data to support accurate query generation.

## Generation Component: 

Uses GPT-3.5 to generate or refine SQL queries and optionally, format or contextualize results based on the retrieved information.

# Back-End Database

Have Used Sqlite DB for Demo purpose . HR Sample Database was loaded into SQlite DB with below schema and relationshhip .

![image](https://github.com/user-attachments/assets/460c156d-a7b0-4b7e-859e-03861a5b543f)

# Key Chanllenges faced

  ## 1 .Initial Approach and Challenges:

  Initially started the project using LangChain Chains to handle natural language queries and generate SQL queries. However, encountered significant challenges with this approach. LangChain Chains lacked explicit 
  functions to manage schema details and understand table relationships. This limitation made it difficult to handle complex database schemas and accurately generate SQL queries based on user inputs.

  To address this, I provided the complete schema as input to the language model (LLM) through prompts. While ChatGPT's context length allowed to temporarily overcome these challenges as the database was not that large 
  and it worked properly, 
  this approach proved impractical for enterprise databases with hundreds of tables. The manual inclusion of schema details in prompts was cumbersome and not scalable for large-scale implementations.

 ## Solution and Breakthrough:

  The introduction of LangChain Agents significantly addressed these issues. Unlike Chains, LangChain Agents are designed to automatically introspect the schema and understand the relationships between tables. This 
  capability allows the Agents to accurately identify user intent and determine which tables to query without requiring manual schema input.

  The use of LangChain Agents was a major breakthrough, as it streamlined the query generation process and provided a scalable solution for managing complex databases. This advancement improved the accuracy of query 
  generation and made the system more adaptable to large enterprise environments.

## Summary

## Schema Management and Query Generation:
  
  ## Challenge: 
     Initially, used LangChain Chains required manually providing schema details, which was impractical for large databases and complex queries.
  ## Solution: 
     LangChain Agents provided a significant improvement by automatically introspecting the schema, understanding table relationships, and accurately generating SQL queries based on user input.

## 2 . Challenge with Testing and Evaluation:

  One significant challenge we faced was testing and debugging the application effectively. It was crucial to understand the internal processes and decisions made by the system once a user's input query was passed to the 
  language model (LLM). Without clear visibility into the underlying workings, it was difficult to identify issues and ensure the accuracy of query generation.

  ## Solution with Langsmith:

  To address this challenge, we explored various tools and found that LangChain's Langsmith component provided the necessary capabilities for tracing and debugging. Langsmith allows us to track and visualize the internal 
  operations of the LangChain components, including the different calls made and the processing steps involved.

  By integrating Langsmith into our system, we gained valuable insights into the LLM's interactions and the flow of data through the application. This enhanced visibility enabled us to effectively monitor and evaluate 
  the system's performance, identify and resolve issues, and ensure that the query generation process was functioning as intended.

# Prerequisites

- Python 3.9 or higher
- Flask
- OpenAI API Key
- Langchain
- SQLite3
- Gradio
- Langsmith
  
# File Structure

1.app.py: The Flask application file that handles API requests and serves the web application.

2.Models/agent.py: This file contains the Langchain Agents used to interface between OpenAI and the SQL database.

3.index.html: The main HTML file located in the templates directory, responsible for the user interface layout.

4.routes.py: Defines the routes and logic for handling different API endpoints in the Flask application.

5.database.db: The SQLite database file storing the movie reviews and labels.

6.templates/: Directory containing additional HTML templates for the web interface.

7.requirements.txt: List of required Python packages necessary to run the application.

8.Gradio_interface.py : Front end for the web application.

9.Database/create_database.py :  Create script for creating a HR database in Sqlite.

10.Database/insert.py : script for populating values in the created tables.


## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/LangChainSQLAgent.git
   cd LangChainSQLAgent
2. ## Create and activate a virtual environment:

    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. ## Install the required packages:

    pip install -r requirements.txt

4. ## Set up the environment variables:

   OPENAI_API_KEY=your-openai-api-key


## Usage

1. ## Run the Flask application:

     flask run
   
2. ## Open your web browser and go to http://127.0.0.1:5000 to access the web application.

## File Structure

1.app.py: The Flask application file that handles API requests and serves the web application.

2.Models/agent.py: This file contains the Langchain Agents used to interface between OpenAI and the SQL database.

3.index.html: The main HTML file located in the templates directory, responsible for the user interface layout.

4.routes.py: Defines the routes and logic for handling different API endpoints in the Flask application.

5.database.db: The SQLite database file storing the movie reviews and labels.

6.templates/: Directory containing additional HTML templates for the web interface.

7.requirements.txt: List of required Python packages necessary to run the application.

8.Gradio_interface.py : Front end for the web application.


## Screenshots

![image](https://github.com/Anitt/LangChainDatabaseAgent/assets/32222717/b6a2655f-66ff-410f-9079-ed7c85243441)


![image](https://github.com/Anitt/LangChainDatabaseAgent/assets/32222717/f0a87868-be99-4194-a933-029148b553c5)

# Gradio Interface Screenshots

![image](https://github.com/Anitt/LangChainDatabaseAgent/assets/32222717/401e55ca-a23d-403b-a618-e958be33b0f2)


![image](https://github.com/Anitt/LangChainDatabaseAgent/assets/32222717/03d868b6-45b9-4bbf-8e40-ddeac8ef58f4)





   

