from flask import Flask,render_template,request,url_for,redirect
from bokeh.models.annotations import Title
from bokeh.plotting import figure,show
from bokeh.io import output_notebook
import numpy as np
from bokeh.embed import file_html,components
from bokeh.resources import CDN

mylink="/"

app = Flask(__name__)


@app.route('/',methods = ['POST', 'GET'])
def index():
    funcs = {
             "Sine":                 [np.sin, -2*np.pi,2*np.pi,-1.0001,1.0001, "Sin(%s)"],
             "Cosine":               [np.cos, -2*np.pi,2*np.pi,-1.0001,1.0001, "Cos(%s)"],
             "Tangent":              [np.tan, -2*np.pi,2*np.pi,-4,4, "Tan(%s)"],
             "Cosecant":             [np.vectorize(lambda t: 1/np.sin(t)), -2*np.pi,2*np.pi,-4,4, "Csc(%s)"],
             "Secant":               [np.vectorize(lambda t: 1/np.cos(t)), -2*np.pi,2*np.pi,-4,4, "Sec(%s)"],
             "Cotangent":            [np.vectorize(lambda t: 1/np.tan(t)), -2*np.pi,2*np.pi,-4,4, "Cot(%s)"],
             "Parabola":             [np.vectorize(lambda t: t**2), -1,1,0,1, "(%s)^2"],
             "Hyperbola":            [np.vectorize(lambda t: 1/t), -4,4,-4,4, "1/(%s)"],
             "Exponential":          [np.exp, -3,3,0,20, "exp(%s)"],
             "Gaussian":             [np.vectorize(lambda t: (np.exp(-t**2/2)/np.sqrt(2*np.pi))), -3,3,0,0.5, "N({%s}|0,1)"],
             "Logarithm":            [np.log, 0.0001,5,-4,2, "log(%s)"],
             "Sigmoid":              [np.vectorize(lambda t: 1/(1+np.exp(-t))), -5,5,0,1, "Sigmoid(%s)"],
             "Hyperbolic tangent":   [np.tanh, -5,5,-1.0001,1.0001, "Tanh(%s)"],
             "Hyperbolic cosine":    [np.cosh, -3,3,0,10, "Cosh(%s)"],
             "Hyperbolic sine":      [np.sinh, -3,3,-10,10, "Sinh(%s)"],
             "Hyperbolic cotangent": [np.vectorize(lambda t: 1/np.tanh(t)), -5,5,-5,5, "Coth(%s)"],
             "Hyperbolic secant":    [np.vectorize(lambda t: 1/np.cosh(t)), -5,5,0,1, "Sech(%s)"],
             "Hyperbolic cosecant":  [np.vectorize(lambda t: 1/np.sinh(t)), -5,5,-5,5, "Csch(%s)"],
             "Sine cardinal":        [np.sinc, -5,5,-0.3,1.0001, "Sinc(%s)"],
            #  "ReLU":                 [np.vectorize(lambda t: np.max([0.0,t])), -1,1,-0.0001,1, "ReLU(%s)"],
            }
    div=f'<img src="{mylink}static/Image-Of-Whats-Up.jpg" />'
    if request.method == 'POST':
        myfn = request.form.get('myfunc')
        if myfn in funcs.keys():
            fn,ln,rn,bn,tn,yn = funcs[myfn]
            xn = request.form.get('typed_xlabel')
            x = np.linspace(ln,rn)
            y = fn(x)
            p = figure(width=450, height=372, x_range=(ln, rn), y_range=(bn, tn))
            p.line(x,y)
            p.xaxis.axis_label = xn
            p.yaxis.axis_label = yn%(xn)
            titl = Title()
            titl.text = myfn
            p.title = titl
            script, div = components(p)
            return render_template('index1.html', funcs=[""]+list(funcs.keys()), div=div, script=script, custom_link=mylink)
        else:
            return render_template('index1.html', funcs=[""]+list(funcs.keys()), div=div, script="Select something.", custom_link=mylink)

    elif request.method == 'GET':
        return render_template('index1.html', funcs=[""]+list(funcs.keys()), div=div, script="Select something.", custom_link=mylink)
    
@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(port=33507, debug=True)
