from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

familyDict = {
    'Mohammed' : {'gender' : 'Male', 'age' : 36},
    'Esraa' : {'gender' : 'Female', 'age' : 32},
    'Arwa' : {'gender' : 'Female', 'age' : 7},
    'Muaz' : {'gender' : 'Male', 'age' : 5}
    }

# ===============================================================================================
@app.route("/")
def hello():
    return("WELCOME TO MY FAMILY PAGE")
# ===============================================================================================
@app.route("/<member>")   #Example: /Arwa
def getData(member):
    member = member.title()  #arwa, ARWA ===> Arwa
    if member not in familyDict.keys():
        return(render_template('sorryTemp.html'))
    else:
        return(render_template('familyDataTemp.html', member = member, familyDict = familyDict))
# ===============================================================================================
@app.route("/addmember", methods = ['GET', 'POST'])
def addMember():
    if request.method == 'POST':
        nameVar = request.form.get('nameVar').title()
        genderVar = request.form.get('genderVar').title()
        ageVar = request.form.get('ageVar')
        familyDict[nameVar] = {'gender' : genderVar, 'age' : ageVar}
        return(redirect(url_for('getData', member = nameVar)))
    else:
        return(render_template('createForm.html'))


if __name__ == '__main__' :
   app.run(debug = True)
