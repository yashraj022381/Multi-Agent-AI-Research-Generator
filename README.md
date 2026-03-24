# Multi-Agent AI Research-Generator
### Powered by CrewAI + Groq + Tavily + Streamlit
🤖 A multi-agent AI system that researches, writes, edits &amp; fact-checks reports on any topic using CrewAI + Groq + Tavily + Streamlit

1. ## 🌐 Live Demo

    👉 **[Try it Live on Streamlit Cloud](https://multi-agent-ai-research-generator-eelc2ntyyqhh5qyyezmgd8.streamlit.app/)**
    ```
2. Introduction
 - A production-ready multi-agent AI system that researches, writes, edits & fact-checks reports on any topic — fully            automated using a team of 4 specialized AI agents. 

3. 🧠 How It Works
 - This project uses 4 specialized AI agents working in a sequential pipeline:
  
   User Input (Topic)
        ↓
   🔍 Researcher Agent  →  Searches web with Tavily API (3 sources)
        ↓
   ✍️  Writer Agent     →  Writes structured Markdown report (600 words)
        ↓
   ✏️  Editor Agent     →  Polishes for clarity, flow & formatting
        ↓
   ✅  Fact-Checker     →  Verifies claims → VERIFIED / UNVERIFIED / INCORRECT
        ↓
   📄 Final Polished Report (saved as .md file)

 4. ✨ Features

   🔍 Real-time web search using Tavily API
   ✍️ Auto-generated structured reports with Executive Summary, Trends, Challenges & Outlook
   ✏️ AI-powered editing for clarity and professional tone
   ✅ Automatic fact-checking with VERIFIED / UNVERIFIED / INCORRECT labels
   📄 Download reports as .md files
   📁 Past reports saved and accessible from sidebar
   🌐 Streamlit dashboard — no terminal needed
   ⚡ Powered by Groq — ultra-fast LLaMA3 inference (free tier)


 5. 🛠 Tech Stack
    
     Component                Technology
     🤖 Agent Framework       CrewAI
     🧠 LLM                   Groq — llama3-70b-8192
     🔍 Web Search            Tavily API
     🖥️ Frontend              Streamlit
     🐍 Language              Python 3.11+



 6. 📁 Project Structure
     multi-agent-research-generator/
     ├── agents.py          # 4 AI agents: Researcher, Writer, Editor, Fact-Checker
     ├── tasks.py           # Task definitions for each agent
     ├── crew.py            # CrewAI orchestration & pipeline runner
     ├── app.py             # Streamlit web dashboard
     ├── requirements.txt   # Python dependencies
     ├── .env.example       # Environment variable template
     ├── outputs/           # Generated reports saved here
     │   └── .gitkeep
     └── README.md


 7. 🚀 Quick Start
   i) Clone the repository
      bash
        git clone https://github.com/your-username/multi-agent-research-generator.git
        cd multi-agent-research-generator
    
  ii) Create virtual environment
      bash
        python -m venv venv
      # Windows
        venv\Scripts\activate
      # Mac/Linux
        source venv/bin/activate

  iii) Install dependencies
       bash
         pip install -r requirements.txt

   iv) Set up API keys
       Copy the example file and add your keys:
        bash
          cp .env.example .env

   Your .env file:
   envGROQ_API_KEY=your_groq_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   OPENAI_API_KEY=sk-no-key-needed
   OPENAI_BASE_URL=https://api.groq.com/openai/v1

   v) Get FREE API Keys
      Service       URL                      Free Tier
      Groq          console.groq.com✅       Free
      Tavily        app.tavily.com✅         Free

   vi) Run the app
      bash
       # Streamlit Dashboard (recommended)
         streamlit run app.py
       # Terminal only
         python crew.py

 8. 💡 Example Topics to Try
  - ✅ AI trends in Indian fintech 2026
  - ✅ Generative AI in Indian healthcare 2025
  - ✅ Electric vehicles adoption India 2026
  - ✅ UPI payment trends Q1 2026
  - ✅ Blockchain in supply chain management 2026
  - ✅ Climate tech startups India 2026


 9. 📦 Requirements
  - txtcrewai==0.28.8
  - crewai-tools==0.1.6
  - groq==0.4.2
  - tavily-python==0.3.3
  - streamlit==1.32.0
  - python-dotenv==1.0.1
  - langchain-groq==0.1.3

 10. ☁️ Deploy to Streamlit Cloud (Free)

  - Push your code to GitHub (make sure .env is in .gitignore)
  - Go to share.streamlit.io
  - Connect your GitHub repo
  - Add secrets in Streamlit Cloud → Settings → Secrets:

    GROQ_API_KEY = "your_groq_key"
    TAVILY_API_KEY = "your_tavily_key"
    OPENAI_API_KEY = "sk-no-key-needed"
    OPENAI_BASE_URL = "https://api.groq.com/openai/v1"

  - Click Deploy — your app gets a public URL! 🎉


 11. 🔧 Troubleshooting
     Error                           Fix
   - ImportError:                    Use TavilySearchTool instead
     TavilySearchResults
   - verbose=2 ValidationError       Change to verbose=True
   - Model not found (404)           Use groq/llama3-70b-8192
   - Rate limit (413/429)            Add max_rpm=3 to Crew, shorten task descriptions
   - OpenAI Auth Error (401)         Set OPENAI_BASE_URL in .env
   - memory=True errors              Set memory=False in Crew

 12. 🗺️ Roadmap

   - Add PDF export option
   - Support parallel agent execution
   - Add more LLM providers (Gemini, Claude)
   - Email report delivery
   - Multi-language report support
   - FastAPI backend for API access


 13. 🤝 Contributing
   - Contributions are welcome! Please feel free to submit a Pull Request.

   i) Fork the project
  ii) Create your feature branch (git checkout -b feature/AmazingFeature)
 iii) Commit your changes (git commit -m 'Add AmazingFeature')
  iv) Push to the branch (git push origin feature/AmazingFeature)
   v) Open a Pull Request

14. 📄 License
  - This project is licensed under the MIT License — see the LICENSE file for details.

 15. 🙏 Acknowledgements

      - CrewAI — Multi-agent framework
      - Groq — Lightning-fast LLM inference
      - Tavily — AI-optimized search API
      - Streamlit — Rapid web app framework

 16. 👤 Author
  Yashraj Jagdale

GitHub: https://github.com/yashraj022381
LinkedIn: www.linkedin.com/in/yashraj-jagdale-2784b6297

<p align="center">Built with ❤️ using CrewAI + Groq + Tavily + Streamlit</p>


