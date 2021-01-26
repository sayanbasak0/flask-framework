from flask import Flask,render_template,request,url_for,redirect
from bokeh.plotting import figure,show
from bokeh.io import output_notebook
import numpy as np
from bokeh.embed import file_html,components
from bokeh.resources import CDN

mylink="/"

app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def index():
    trig_func = {"Sin":np.sin,
                 "Cos":np.cos,
                 "Tan":np.tan}
    if request.method == 'POST':
        if request.form.get('mytrig') in trig_func.keys():
            x = np.linspace(-2*np.pi,2*np.pi,100)
            y = trig_func[request.form.get('mytrig')](x)
            p = figure(width=300, height=200)
            p.line(x,y)
            p.xaxis.axis_label = 'Angle'
            p.yaxis.axis_label = request.form.get('mytrig')+"(angle)"
            script, div = components(p)
            return render_template('index1.html', script=script, div=div, triga=trig_func.keys(), custom_link=mylink)
        else:
            return render_template('index1.html', div="Select Sin/Cos/Tan!", custom_link=mylink)

    elif request.method == 'GET':
#         print(request)
        return render_template('index1.html', div="Select something.", triga=trig_func.keys(), custom_link=mylink)
    
@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8000)
