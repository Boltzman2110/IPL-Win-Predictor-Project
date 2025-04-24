# IPL-Win-Predictor-Project


 🏏 IPL Win Predictor

A Machine Learning-powered web application that predicts the winning probability of a team during an ongoing IPL match. It leverages real-time match data (like score, overs, and wickets) and provides predictions using a logistic regression model.

 🚀 Project Overview

This project is built using:
- **Machine Learning** for prediction (Logistic Regression)
- **Streamlit** for the frontend interface
- **Pickle** for model loading
- **Pandas** for data preprocessing and input handling

 🔮 What It Does

- Accepts live match input from the user
- Calculates key features like:
  - Runs left
  - Balls left
  - Current Run Rate
  - Required Run Rate
- Predicts winning probability using a trained ML model
- Displays results dynamically in an interactive web interface

---

 🧠 Tech Stack

| Technology      | Description                                      |
|-----------------|--------------------------------------------------|
| Python          | Programming Language                             |
| Streamlit       | Frontend Framework                               |
| Scikit-learn    | Machine Learning Modeling                        |
| Pandas          | Data Manipulation                                |
| Pickle          | Model Serialization                              |

---

 

 📂 Project Structure

```
IPL-Win-Predictor/
├── app.py              # Streamlit app script
├── pipe.pkl            # Pre-trained ML pipeline
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
└── ...
```

---

## 🛠️ How to Run the App Locally

 1. Clone the Repository
```bash
git clone https://github.com/your-username/IPL-Win-Predictor.git
cd IPL-Win-Predictor
```

 2. Create a Virtual Environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

 3. Install Requirements
```bash
pip install -r requirements.txt
```

 4. Run the App
```bash
streamlit run app.py
```

---

## 🌐 Live Demo

🔗 [Deployed on Hugging Face Spaces](https://huggingface.co/spaces/Boltzman2110/IPL-Win-Predictor)

---

## 🧪 Example Usage

1. Select the **batting** and **bowling** teams.
2. Choose the **host city**.
3. Enter the **target score**, **current score**, **overs completed**, and **wickets fallen**.
4. Click **Predict Probability** to see which team is more likely to win.

---

## 🤝 Team Collaboration

- Code versioned and managed on GitHub
- Integrated development across machine learning, frontend (UI/UX), and data processing
- Teamwork in implementing the model, building the frontend, and testing functionalities

---

## 📈 Future Scope

- Integration of **live API data feed** for automatic updates
- Expand prediction to **international T20 matches**
- Incorporate advanced features like **weather**, **toss results**, and **player form**
- Deploy on cloud platforms for wider accessibility

---




## 💬 Contact

For suggestions or collaborations, feel free to connect:
- [Panchal Sujal](https://github.com/Boltzman2110)
- Email: sujalpanchal1206@gmail.com
```


