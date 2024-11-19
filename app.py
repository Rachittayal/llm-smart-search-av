import gradio as gr
import pickle
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

with open("model/course_emb.pkl", "rb") as f:
    course_emb = pickle.load(f)

df = pd.read_excel("analytics_vidhya_courses_Final.xlsx")

model = SentenceTransformer('all-MiniLM-L6-v2')

def search_courses(query, top_n=5):
    query_embedding = model.encode([query])
    
    similarities = cosine_similarity(query_embedding, course_emb)
    
    top_n_idx = similarities[0].argsort()[-top_n:][::-1]
    
    return df.iloc[top_n_idx][["Course Title", "Course Description"]]

def gradio_interface(query):
    top_courses = search_courses(query)
    results = []
    for idx, row in top_courses.iterrows():
        results.append(f"Title: {row['Course Title']}\nDescription: {row['Course Description']}\n")
    return "\n".join(results)
iface = gr.Interface(fn=gradio_interface, inputs=gr.Textbox(label="Enter your search query"), outputs="text")

iface.launch(share=True)
