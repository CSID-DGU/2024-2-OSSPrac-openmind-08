from flask import Flask, render_template, request
from flask import Flask, render_template, request

app = Flask(__name__)

# 메인 입력 페이지
@app.route('/')
def input():
    return render_template('input.html')

# 결과 페이지로 입력 데이터를 전송하고 처리
@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = dict()
        result['Name'] = request.form.get('name')
        result['StudentNumber'] = request.form.get('StudentNumber')
        result['Gender'] = request.form.get('gender')  # 팀원 1
        result['Programming Languages'] = request.form.getlist('languages')  # 팀원 2
        result['Programming Languages'] = ', '.join(result['Programming Languages'])  # 목록을 문자열로 변환
        return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

