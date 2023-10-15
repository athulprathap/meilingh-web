from flask import Flask, render_template, request, url_for
import logging
from psylist_dbase import *

app = Flask(__name__)

nodata = [['','No Data Found for this phone number, please check phone number and try again','','']]




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/psylist', methods=['GET','POST'])
def search():
	if request.method == 'POST':
		try:
			mobilenumber = request.form.get('mobile')
			if mobilenumber.isdigit() == False:
				return render_template('search.html', sessiondata=nodata)
			mobilenumber = int(request.form.get('mobile'))
			newarray = []
			for entry in psylist_data:
				if entry[1] == str(mobilenumber):
					newarray.append(entry)
			if newarray == []:
				return render_template('search.html', sessiondata=nodata)
			return render_template('search.html', sessiondata=newarray)
			newarray = []
		except:
			pass
	return render_template('search.html')



if __name__ == '__main__':
 	app.run(host='0.0.0.0', port='8080', debug=True)
