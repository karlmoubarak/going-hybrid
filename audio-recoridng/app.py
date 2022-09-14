 # encoding=utf8 

# # # # # # # # # # # # # # # # # # # # # # # # 
# REQUIREMENTS
# # # # # # # # # # # # # # # # # # # # # # # # 
import os
import datetime
from flask import *



# # # # # # # # # # # # # # # # # # # # # # # # 
# GETTING STARTED
# # # # # # # # # # # # # # # # # # # # # # # # 
UPLOAD_FOLDER = 'files'
app = Flask(__name__, static_url_path='', static_folder="static", template_folder="templates")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# # # # # # # # # # # # # # # # # # # # # # # # 
# PAGES
# # # # # # # # # # # # # # # # # # # # # # # # 

######################### HOMEPAGE
@app.route('/')
def root():
    return render_template('index.html')


@app.route('/save-record', methods=['POST'])
def save_record():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also submit an empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    ct = datetime.datetime.now()
    file_name = str(ct)
    full_file_name = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
    file.save(full_file_name)
    return '<h1>Success</h1>'


if __name__ == '__main__':
    app.run()
