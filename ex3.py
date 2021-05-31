from werkzeug import secure_filename
from flask import Flask, render_template, request, redirect
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'JPG', 'JPEG', 'PNG', 'GIF', 'BMP'])
app = Flask(__name__)
@app.route('/fileUpload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        #확장자 이미지파일인 경우
        if file and allowed_file(file.filename):
            file.save('uploads/' + secure_filename(file.filename))
            return redirect(url_for('main_page'))
        #확장자 이미지파일 아닐 경우
        return render_template('index1.html', data="이미지 파일만 업로드하세요.")
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS