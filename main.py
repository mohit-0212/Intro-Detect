from flask import Flask, request, render_template
from werkzeug import secure_filename
import os
import cv2
from time_out import out


upload = os.path.basename('uploads')
extension = ['avi','mp4','mkv']

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = upload

def allowed_extension(fname):
	# return fname
	fname = fname.split(".")
	if len(fname)==1:
		return False
	else:
		if fname[-1].lower() in extension:
			return True
		else:
			return False

@app.route('/', methods=['POST','GET'])
def index():
	return render_template('index.html')


@app.route('/upload', methods=['POST','GET'])
def upload():
	if request.method == 'POST':
		vid = request.files['file']
		if vid and allowed_extension(vid.filename):
			vid_name = secure_filename(vid.filename)
			path = os.path.join(app.config['UPLOAD_FOLDER'], vid_name)
			vid.save(path)
			mins, secs = out(path)
			# face, modi, kejru = "No","No","No"
			# if pred[0]!=0:
			# 	face = "Yes"
			# 	if pred[1]==1:
			# 		modi = "Yes"
			# 	if pred[2]==1:
			# 		kejru = "Yes"
			# # return result
			# result = "/"+result
			return render_template("output.html", mins= mins, secs= secs)
			# return "file uploaded"

if __name__=="__main__":
	app.run(debug=True)



