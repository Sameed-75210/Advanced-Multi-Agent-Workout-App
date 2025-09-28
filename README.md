# AI-Powered Personalized Workout Assistant

An **AI-powered fitness assistant** that generates **personalized workout plans** using **Langflow**, **Astra DB**, **Streamlit**, and **OpenAI's GPT-3**. The system employs **Retrieval-Augmented Generation (RAG)** to deliver context-aware responses based on user profiles and preferences stored in a **vector database**.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [System Architecture & Interaction](#system-architecture--interaction)
- [Flow Diagram](#flow-diagram)
- [Installation & Setup](#installation--setup)
- [How to Use](#how-to-use)
- [Future Improvements](#future-improvements)
- [Author](#author)

---

## Features

- **User Profile Management**  
  Manage user profiles with age, weight, height, fitness goals, and preferences.

- **AI-Powered Workout Generation**  
  Receive personalized workout routines (e.g., leg day, strength training), tailored to user profiles and dislikes.

- **Notes Management**  
  Save personal notes about exercise likes/dislikes; AI customizes plans accordingly.

- **Retrieval-Augmented Generation (RAG)**  
  Uses a vector database (Astra DB) to retrieve relevant context for personalized answers.

- **Multi-Agent System**  
  Langflow agents manage notes, fetch workouts, and interact with Astra DB.

- **Interactive Streamlit App**  
  Simple web interface for user interaction—input data, ask questions, receive tailored plans.

---

## Tech Stack

**Frontend**
- [Streamlit](https://streamlit.io/): Fast and interactive Python web app framework.

**Backend**
- [Langflow](https://github.com/logspace-ai/langflow): Flow-based LLM orchestration and agent framework.
- [OpenAI API](https://platform.openai.com/): GPT-3 for natural language processing and workout generation.
- [Astra DB](https://www.datastax.com/astra/db): Vector database for storing user notes and workout data.

**Vector Store**
- Astra DB with Vector Search: Semantic search enables RAG by retrieving contextually relevant info.

---

## System Architecture & Interaction

### Component Overview

1. **Frontend (Streamlit)**
   - Collects user data (profile, preferences, goals, questions).
   - Displays AI-generated workout plans and tips.

2. **User Profile & Notes (`profiles.py`)**
   - `Profile` dataclass stores user details.
   - Notes on exercise likes/dislikes personalize responses.

3. **Langflow Agents**
   - Handle:
     - Input processing
     - Knowledge base querying (Astra DB)
     - AI inference (OpenAI)

4. **Astra DB**
   - Stores profiles and notes as vectors for fast semantic retrieval.

5. **RAG (Retrieval-Augmented Generation)**
   - Langflow retrieves relevant context from Astra DB before generating responses via OpenAI.

6. **OpenAI API**
   - Core engine for generating personalized workout routines.

---

## Flow Diagram

<img width="1920" height="1017" alt="Langflow System Architecture" src="https://github.com/user-attachments/assets/a7337eaa-91d5-4226-8ebf-7af7582a1067" />

*Above: Langflow architecture—input is processed, queried from Astra DB, parsed, and output is generated via OpenAI.*

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Sameed-75210/Advanced-Multi-Agent-Workout-App.git
cd Advanced-Multi-Agent-Workout-App
```

### 2. Set Up Environment Variables

Create a `.env` file in the project root:

```
LANGFLOW_API_KEY=your_langflow_api_key
ASTRA_DB_APPLICATION_TOKEN=your_astra_db_token
ASTRA_ENDPOINT=your_astra_endpoint
OPENAI_API_KEY=your_openai_api_key
```

### 3. Run Backend (Langflow)

```bash
langflow run
```

### 4. Run Frontend (Streamlit)

```bash
streamlit run main.py
```

---

## 📡 How to Use

1. Enter profile details (age, weight, height, goals).
2. Add notes (exercise preferences/dislikes).
3. Ask the AI for a workout routine (e.g., “Can you create a leg day workout?”).
4. Get your personalized plan directly in the Streamlit app.

---

## Future Improvements

- Add user authentication for persistent profiles
- Visualize workout progress (charts, stats)
- Enable meal plan recommendations alongside workouts
- Cloud deployment (AWS/GCP)

---

## Author

**Muhammad Sameed**  
_Data Scientist_

Built with Streamlit + Langflow + Astra DB + OpenAI.
