from flask import Flask, render_template,request
import joblib

app=Flask(__name__)
model=joblib.load(r"./diabetic_lr_79_joblib.pkl")


@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit',methods=["POST"])
def form_data():
    #names=['pregs','plas','pres','skin','test','mass','pedi','age','class']
    pregs=int(request.form.get("pregs"))
    plas=int(request.form.get("plas"))
    pres=int(request.form.get("pres"))
    skin=int(request.form.get("skin"))

    test=int(request.form.get("test"))
    mass=int(request.form.get("mass"))
    pedi=int(request.form.get("pedi"))
    age=int(request.form.get("age"))

    print(pregs,plas,pres,skin)
    print(test,mass,pedi,age)

    x_data=[pregs,plas,pres,skin,test,mass,pedi,age]
    result=model.predict([x_data])
    print(result)
    if result[0] == 1:
        return "Diabetic"
    else:
        return "not diabetic"
    

@app.route('/contact')
def contact():
    return 'Contacts'

if __name__=='__main__':
    app.run(debug=True)