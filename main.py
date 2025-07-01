questions = {
    "What is the capital of Australia?" : "Canberra",
    "Who painted the Mona Lisa?" : "Leonardo da Vinci",
    "What is the chemical symbol for gold?" : "Au",
    "In what year did World War II end?" : "1945",
    "Which planet is known as the Red Planet?" : "Mars",
    "What is the smallest planet in our solar system?" : "Mercury"
}

score = 0

for question in questions:
    print(question.upper())
    userInp = input("Your Answer : ").lower()
    correctAns = questions[question].strip().lower()
    if userInp == correctAns:
        score += 1

print(f"Your got {score} out of {len(questions)} correct !!!")