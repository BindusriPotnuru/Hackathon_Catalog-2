import random

class Quiz:
    def __init__(self):
        self.questions = [
            {"question": "What is the capital of Andhra Pradesh?", "answer": "Amaravati"},
            {"question": "What is the capital of Arunachal Pradesh?", "answer": "Itanagar"},
            {"question": "What is the capital of Assam?", "answer": "Dispur"},
            {"question": "What is the capital of Bihar?", "answer": "Patna"},
            {"question": "What is the capital of Chhattisgarh?", "answer": "Raipur"},
            {"question": "What is the capital of Goa?", "answer": "Panaji"},
            {"question": "What is the capital of Gujarat?", "answer": "Gandhinagar"},
            {"question": "What is the capital of Haryana?", "answer": "Chandigarh"},
            {"question": "What is the capital of Himachal Pradesh?", "answer": "Shimla"},
            {"question": "What is the capital of Jharkhand?", "answer": "Ranchi"},
            {"question": "What is the capital of Karnataka?", "answer": "Bengaluru"},
            {"question": "What is the capital of Kerala?", "answer": "Thiruvananthapuram"},
            {"question": "What is the capital of Madhya Pradesh?", "answer": "Bhopal"},
            {"question": "What is the capital of Maharashtra?", "answer": "Mumbai"},
            {"question": "What is the capital of Manipur?", "answer": "Imphal"},
            {"question": "What is the capital of Meghalaya?", "answer": "Shillong"},
            {"question": "What is the capital of Mizoram?", "answer": "Aizawl"},
            {"question": "What is the capital of Nagaland?", "answer": "Kohima"},
            {"question": "What is the capital of Odisha?", "answer": "Bhubaneswar"},
            {"question": "What is the capital of Punjab?", "answer": "Chandigarh"},
            {"question": "What is the capital of Rajasthan?", "answer": "Jaipur"},
            {"question": "What is the capital of Sikkim?", "answer": "Gangtok"},
            {"question": "What is the capital of Tamil Nadu?", "answer": "Chennai"},
            {"question": "What is the capital of Telangana?", "answer": "Hyderabad"},
            {"question": "What is the capital of Tripura?", "answer": "Agartala"},
            {"question": "What is the capital of Uttar Pradesh?", "answer": "Lucknow"},
            {"question": "What is the capital of Uttarakhand?", "answer": "Dehradun"},
            {"question": "What is the capital of West Bengal?", "answer": "Kolkata"},
            {"question": "What is the capital of Andaman and Nicobar Islands?", "answer": "Port Blair"},
            {"question": "What is the capital of Chandigarh (Union Territory)?", "answer": "Chandigarh"},
            {"question": "What is the capital of Dadra and Nagar Haveli and Daman and Diu?", "answer": "Daman"},
            {"question": "What is the capital of Lakshadweep?", "answer": "Kavaratti"},
            {"question": "What is the capital of Delhi?", "answer": "New Delhi"},
            {"question": "What is the capital of Puducherry?", "answer": "Puducherry"},
            {"question": "What is the capital of Jammu and Kashmir?", "answer": "Srinagar (Summer), Jammu (Winter)"},
            {"question": "What is the capital of Ladakh?", "answer": "Leh"}
        ]
        self.score = 0

    def start_quiz(self):
        print("Welcome to the States and Union Territories Capitals Quiz!")
        
        # Randomly select 5 questions
        selected_questions = random.sample(self.questions, 5)
        
        for i, q in enumerate(selected_questions):
            print(f"Q{i+1}: {q['question']}")
            user_answer = input("Your answer: ").strip()
            if user_answer.lower() == q["answer"].lower():
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is {q['answer']}\n")

        self.show_result()

    def show_result(self):
        print(f"Quiz completed! Your final score is {self.score}/5")
        if self.score == 5:
            print("Excellent! You got all the answers correct.")
        elif self.score >= 3:
            print("Good job! You passed the quiz.")
        else:
            print("Better luck next time!")

if __name__ == "__main__":
    quiz = Quiz()
    quiz.start_quiz()
