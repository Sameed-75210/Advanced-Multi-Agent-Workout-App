# 🏋️‍♂️ **AI-Powered Personalized Workout Assistant**

This project is an **AI-powered fitness assistant** that generates **personalized workout plans** using **Langflow**, **Astra DB**, **Streamlit**, and **OpenAI's GPT-3**. The system incorporates **Retrieval-Augmented Generation (RAG)** to provide context-aware responses based on user profiles and preferences stored in the **vector database**.

---

## 🚀 **Features**

- **User Profile Management**:  
  Collect and manage user profiles with details like age, weight, height, fitness goals, and preferences.
  
- **AI-Powered Workout Generation**:  
  Ask the AI for **personalized workout routines** (e.g., leg day, strength training, etc.). The AI takes into account **user profiles** and **dislikes** (e.g., avoiding leg press).
  
- **Notes Management**:  
  Users can save personal notes (e.g., exercises they like or dislike) and have the AI tailor responses based on these notes.
  
- **Retrieval-Augmented Generation (RAG)**:  
  The AI leverages a **knowledge base** stored in a **vector database (Astra DB)** to provide personalized answers. RAG enhances the response by retrieving relevant information from stored profiles and notes.

- **Multi-Agent System**:  
  Utilizes Langflow's **agents** to handle different tasks like managing notes, fetching workout routines, and interacting with the Astra DB.

- **Interactive Streamlit App**:  
  A web interface built with Streamlit for easy user interaction — users can input data, ask questions, and receive responses.

---

## 🛠️ **Tech Stack**

### **Frontend**
- **[Streamlit](https://streamlit.io/)**: A fast and interactive framework for building web apps in Python. Streamlit is used to build the user interface, where users can input their data, interact with the AI, and view workout routines.

### **Backend**
- **[Langflow](https://github.com/logspace-ai/langflow)**: A framework to design **flow-based applications** using LLMs. It orchestrates the entire process of data flow, including **AI inference**, **retrieval from Astra DB**, and **agent interactions**.
  
- **[OpenAI API](https://platform.openai.com/)**: Provides **GPT-3** for natural language processing and response generation. It is used to generate the workout routines based on user input and profile data.
  
- **[Astra DB](https://www.datastax.com/astra/db)**: A **vector database** used to store **user notes** and other relevant workout information. It allows semantic search, ensuring that relevant data is fetched to inform the AI's responses.

### **Vector Store**
- **Astra DB with Vector Search**: The **vector database** stores user profiles and notes. It supports **semantic search**, which is key to the **RAG** approach, allowing the AI to retrieve relevant information before generating a response.

---

## 🏗️ **System Architecture & Interaction**

### **Components Interaction**:

1. **Frontend (Streamlit)**:
   - Collects user inputs (profile, preferences, goals, questions).
   - Displays the AI-generated responses (workout plans, tips, etc.).

2. **User Profile & Notes (profiles.py)**:
   - The `Profile` dataclass stores user information.
   - User preferences and exercise notes (likes/dislikes) are saved and used for personalized responses.

3. **Langflow Agents**:
   - Langflow's **agents** handle different tasks such as:
     - **Input Processing**: Collecting and cleaning user input (e.g., exercise preferences).
     - **Knowledge Base Querying**: Retrieving relevant notes or workout history from Astra DB.
     - **AI Inference**: Generating personalized workout plans with OpenAI's API.
   
4. **Astra DB (Database)**:
   - Stores user profiles and notes in vector format for semantic retrieval.
   - Facilitates efficient querying of workout-related data using **semantic search**.

5. **RAG (Retrieval-Augmented Generation)**:
   - **Langflow** integrates **RAG** by retrieving contextually relevant data from Astra DB before generating responses using **OpenAI**.
   - The knowledge base is used to provide context-aware, personalized results.

6. **LangChain**:
   - **Chains** different steps (user input → retrieval → inference → output) and ensures seamless execution of tasks.
   
7. **OpenAI API**:
   - The core of the system that generates the **workout routine** after collecting all necessary context (user profile, notes, etc.).

---

## 🌐 **Flow Diagram**

<img width="1920" height="1017" alt="image" src="https://github.com/user-attachments/assets/a7337eaa-91d5-4226-8ebf-7af7582a1067" />

*The above image shows the Langflow architecture where the input is processed, queried from Astra DB, parsed, and the output is generated using OpenAI.*

---

## 🔧 **Installation & Setup**

1. **Clone the repository**:
```bash
git clone https://github.com/your-username/workout-assistant.git
cd workout-assistant

Set up your .env file:
Create a .env file in the project root directory and include your API keys:

LANGFLOW_API_KEY=your_langflow_api_key
ASTRA_DB_APPLICATION_TOKEN=your_astra_db_token
ASTRA_ENDPOINT=your_astra_endpoint
OPENAI_API_KEY=your_openai_api_key


Run the Langflow backend:

langflow run


Run the Streamlit app:

streamlit run main.py

📡 How to Use

Enter your profile details (age, weight, height, and fitness goals).

Add notes (e.g., exercise preferences or dislikes).

Ask the AI to generate a workout routine (e.g., “Can you create a leg day workout?”).

Get the personalized workout plan displayed directly in the Streamlit app.

🔮 Future Improvements

Add user authentication for saving personalized data across sessions.

Visualize workout progress (e.g., charts, stats).

Enable meal plan recommendations alongside workouts.

Deploy the system on cloud platforms (AWS/GCP).

👨‍💻 Author

Built with ❤️ using Streamlit + Langflow + Astra DB + OpenAI.
