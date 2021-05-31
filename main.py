import flask
from flask import Flask, request, render_template
#from sklearn.externals import joblib
import numpy as np
from scipy import misc

from keras.models import load_model

app = Flask(__name__)

# 메인 페이지 라우팅
@app.route("/")
@app.route("/index")
def index():
    return flask.render_template('index1.html')

# 데이터 예측 처리
@app.route("/predict", methods=['GET', 'POST'])
def make_predecion():
    if request.method == 'POST':
        # 업로드 파일 처리 분기
        file = request.files['image']
        if not file:
            return render_template('index1.html', label="No Files")

        # 이미지 픽셀 정보 읽기
        # 알파 채널 값 제거 후 1차원 Reshape
        img = misc.imread(file)
        img = img[:, :, :3]
        img = img.reshape(1, -1)

        # 입력 받은 이미지 예측
        prediction = model.predict(img)

        # 예측 값을 1차원 배열로부터 확인 가능한 문자열로 변환
        label = str(np.squeeze(prediction))

        # 숫자가 10일 경우 0으로 처리
        if label == '10':
            label = '0'

        # 결과 리턴
        return render_template('index.html', label=label)

if __name__ == '__main__':
    # 모델 로드
    model = load_model('model.h5')
    #model = joblib.load('./model/model.pkl')
    #app.run(host='0.0.0.0', port=8000, debug=True)
    app.run()