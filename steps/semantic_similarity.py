# The MIT License (MIT)
#
# Copyright (c) 2024 Aliaksei Bialiauski
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Similarity between repository dimensions.
"""
import numpy as np
import pandas as pd
from steps.similar import similar

heads = [
    "java-samples",
    "Awesome Docker Compose samples",
    "Java maven samples",
    """
    🌟 Awesome LLM Apps A curated collection of awesome LLM apps built with RAG and AI agents. This repository features LLM apps that use models from OpenAI, Anthropic, Google, and even open-source models like LLaMA that you can run locally on your computer. 📑 Table of Contents 🤔 Why Awesome LLM Apps? 📂 Featured Projects 💻 Local Lllama-3 with RAG 🎯 Generative AI Web Search Assistant 💬 Chat with GitHub Repo 📈 AI Investment Agent 🗞️ AI Journalist Agent 💰 AI Personal Finance Agent 🛫 AI Travel Agent 📰 Multi-Agent AI Researcher 📄 Chat with PDF 💻 Web Scraping AI Agent 📨 Chat with Gmail 📽️ Chat with YouTube Videos 🔎 Chat with Arxiv Research Papers 📝 Chat with Substack Newsletter 🚀 Getting Started 🤝 Contributing to Opensource 🤔 Why Awesome LLM Apps? 💡 Discover practical and creative ways LLMs can be applied across different domains, from code repositories to email inboxes and more. 🔥 Explore apps that combine LLMs from OpenAI, Anthropic, Gemini, and open-source alternatives with RAG and AI Agents. 🎓 Learn from well-documented projects and contribute to the growing open-source ecosystem of LLM-powered applications. 📂 Featured Projects 💻 Local Lllama-3 with RAG Chat with any webpage using local Llama-3 and Retrieval Augmented Generation (RAG) in a Streamlit app. Enjoy 100% free and offline functionality. 🎯 Generative AI Web Search Assistant Get pinpointed answers to your queries by combining search engines and LLMs using OpenAI's GPT-4 and the DuckDuckGo search engine for accurate responses. 💬 Chat with GitHub Repo Engage in natural conversations with your GitHub repositories using GPT-4. Uncover valuable insights and documentation effortlessly. 📈 AI Investment Agent AI investment agent that compares the performance of two stocks and generates detailed stock reports with company insights, news, and analyst recommendations to help you make smart investment choices. 🗞️ AI Journalist Agent AI-powered journalist agent that generates high-quality articles using OpenAI GPT-4o. It automates the process of researching, writing, and editing articles, allowing you to create compelling content on any topic with ease. 💰 AI Personal Finance Agent AI-powered personal finance planner that generates personalized financial plans using OpenAI GPT-4o. It automates the process of researching, planning, and creating tailored budgets, investment strategies, and savings goals. 🛫 AI Travel Agent AI-powered travel Agent that generates personalized travel itineraries using OpenAI GPT-4o. It automates the process of researching, planning, and organizing your dream vacation, allowing you to explore exciting destinations with ease. 📰 Multi-Agent AI Researcher Use a team of AI agents to research top HackerNews stories and users with GPT-4 to generate blog posts, reports, and social media content on autopilot. 📄 Chat with PDF Engage in intelligent conversation and question-answering based on the content of your PDF documents. Simply upload and start asking questions. 💻 Web Scraping AI Agent Intelligently scrape websites using OpenAI API and the scrapegraphai library. Specify the URL and extraction requirements, and let the AI agent handle the rest. 📨 Chat with Gmail Interact with your Gmail inbox using natural language. Get accurate answers to your questions based on the content of your emails with Retrieval Augmented Generation (RAG). 📽️ Chat with YouTube Videos Dive into video content with interactive conversation and question-answering based on YouTube videos. Provide a URL and engage with the video's content through natural language. 🔎 Chat with Arxiv Research Papers Explore the vast knowledge in arXiv research papers through interactive conversations using GPT-4 and unlock insights from millions of research papers. 📝 Chat with Substack Newsletter Chat with a Substack newsletter using OpenAI's API and the Embedchain library in a Streamlit app. Leverage GPT-4 for precise answers based on newsletter content. 🚀 Getting Started Clone the repository bash
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git Navigate to the desired project directory bash
cd awesome-llm-apps/chat_with_gmail Install the required dependencies bash
pip install -r requirements.txt Follow the project-specific instructions in each project's README.md file to set up and run the app. 🤝 Contributing to Opensource Contributions are welcome! If you have any ideas, improvements, or new apps to add, please create a new GitHub Issue or submit a pull request. Make sure to follow the existing project structure and include a detailed README.md for each new app. Thank you community for the support 🙏 🌟 Don’t miss out on future updates! Star the repo now and be the first to know about new and exciting LLM applications with RAG.
    """,
    "awesome,awesome-list"
]
dimensions = ["repo", "description", "description", "readme", "topics"]
similarities = []
for head, dimension in zip(heads, dimensions):
    similarity = {
        "head": head,
        "dimension": dimension,
        "similar": " ".join(similar(dimension, head))
    }
    similarities.append(similarity)
frame = pd.DataFrame(similarities).to_csv("similar.csv", index=False)
