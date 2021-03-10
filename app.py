from decouple import config
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config('POSTGRES')

db = SQLAlchemy(app)

# entity needs to be placed after app and db is created
from entity.output import Output
from entity.input import Input

# can be used to creade tables from the entity classes
db.create_all()

@app.route('/output')
def show_output():
    output = Output.query.all()
    results = [
        {
            "id": res.id,
            "userId": res.user_id,
            "amount": res.amount,
            "note": res.note,
            "time_created": res.time_created
        } for res in output]
    return {"count": len(results), "output": results}


@app.route('/input')
def show_input():
    input = Input.query.all()
    results = [
        {
            "id": res.id,
            "userId": res.user_id,
            "amount": res.amount,
            "note": res.note,
            "time_created": res.time_created
        } for res in input]
    return {"count": len(results), "input": results}


@app.route('/output/new', methods=['GET'])
def new_output():
    if 'user_id' and 'amount' in request.args:
        user_id = str(request.args.get('user_id'))
        amount = float(request.args.get('amount'))
        # note is optional, if no value present it will use an empty string
        note = str(request.args.get('note', ''))
        output = Output(user_id=user_id, amount=amount, note=note)
        db.session.add(output)
        db.session.commit()
        return 'Output created!'
    else:
        return "No User and/or amount provided!"

@app.route('/input/new', methods=['GET'])
def new_input():
    if 'user_id' and 'amount' in request.args:
        user_id = str(request.args.get('user_id'))
        amount = float(request.args.get('amount'))
        # note is optional, if no value present it will use an empty string
        note = str(request.args.get('note', ''))
        input = Input(user_id=user_id, amount=amount, note=note)
        db.session.add(input)
        db.session.commit()
        return 'Input created!'
    else:
        return "No User and/or amount provided!"

@app.route('/input/delete', methods=['GET'])
def delete_input():
    if 'id' in request.args:
        id = str(request.args.get('id'))
        Input.query.filter_by(id=id).delete()
        db.session.commit()
        return 'Input deleted!'
    else:
        return "No ID provided!"

@app.route('/output/delete', methods=['GET'])
def delete_output():
    if 'id' in request.args:
        id = str(request.args.get('id'))
        Output.query.filter_by(id=id).delete()
        db.session.commit()
        return 'Output deleted!'
    else:
        return "No ID provided!"


if __name__ == '__main__':
    app.run()
