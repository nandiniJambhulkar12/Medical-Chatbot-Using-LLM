<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
# Medical-Chatbot-Project

=======
# Medical-Chatbot-Using-LLM
MediBot AI is an intelligent medical chatbot powered by advanced Large Language Models (LLMs). It helps users with basic health queries using Retrieval-Augmented Generation (RAG), combining LLMs with medical documents for accurate, context-aware answers.
>>>>>>> 4a31ea7020a0b3215be5959cc1e5e84acc40acd4


# How to run?
### STEPS:

Clone the repository

```bash
Project repo: https://github.com/
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n medibot python=3.10 -y
```

```bash
conda activate medibot
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


### Create a `.env` file in the root directory and add your Pinecone &  Together credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
TOGETHER_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


```bash
# run the following command to store embeddings to pinecone
python store_index.py
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up localhost:
```


### Techstack Used:

- Python
- LangChain
- Flask
- GPT
- Pinecone

=======
<<<<<<< HEAD
# Medical-Chabot-Using-LLM
MediBot AI is an intelligent medical chatbot powered by advanced Large Language Models (LLMs). It helps users with basic health queries using Retrieval-Augmented Generation (RAG), combining LLMs with medical documents for accurate, context-aware answers.
>>>>>>> f2ce92e3274aad5d3bd8418498a1713fd7e02b27
=======
# new-chatbot
>>>>>>> 67ea60b52cfa03464e837c8ded7ef3df3939641a
=======

>>>>>>> 4a31ea7020a0b3215be5959cc1e5e84acc40acd4
