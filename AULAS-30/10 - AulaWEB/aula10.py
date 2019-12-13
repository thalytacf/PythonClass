
name_page = 'CalculatorHBSIS'

from flask import Flask, render_template, request
from calc_impot import *
app = Flask(__name__)

@app.route ('/')
def home():
    return render_template ('calc_hbsis.html', title=name_page)


@app.route ('/calculate')
def calculate():
    n1 = int (request.args['n1'])
    n2 = int (request.args['n2'])
    r_sume = calc_soma(n1, n2)
    r_subtraction = calc_sub (n1,n2)
    r_multiplication = calc_mult(n1, n2)
    r_division = calc_div1(n1, n2)
    r_divisionfra = calc_div2(n1, n2)
    r_rest = calc_resto(n1, n2)
    r_root = calc_raiz(n1, n2)
    results = {'sume':r_sume, 'sub':r_subtraction, 'mult':r_multiplication, 'div':r_division, 'divfra':r_divisionfra, 'rest':r_rest, 'root':r_root}
    return render_template('result.html'
    ,n1 = n1
    ,n2 = n2
    ,sume = r_sume
    ,subtraction = r_subtraction
    ,multiplication = r_multiplication
    ,division = r_division
    ,divisionfra =  r_divisionfra
    ,rest = r_rest
    ,root = r_root)
app.run()