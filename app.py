from flask import Flask, render_template, request
import random

app = Flask(__name__)

toppings = [
    "망고", "청포도", "바나나", "오렌지", "블루베리", "키위", "자몽", "크림슨포도",
    "카카오닙스", "아몬드", "초코칩", "오레오", "코코넛청크", "로투스크럼블", "캐슈넛"
    "몬스터 그래놀라", "시나몬 그래놀라", "초코 그래놀라", "첵스", "콘프로스트", "미니찹쌀떡",
    "꿀스틱", "딸기청", "사과잼", "복숭아잼"

]

@app.route('/', methods=['GET', 'POST'])
def recommend_topping():
    if request.method == 'POST':
        num_toppings = int(request.form.get('topping-num', 1))  

        random_toppings = random.sample(toppings, num_toppings)  
        recommendation = ', '.join(random_toppings)  
        
        return render_template('result.html', recommendation=recommendation)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

