
from flask import Flask, render_template,request
import pymongo
import urllib

mongo = pymongo.MongoClient('mongodb+srv://22_Omprakash:'+urllib.parse.quote("Opsr@2410")+'@invoice.wu80e.mongodb.net/Invoice?retryWrites=true&w=majority', tls=True, tlsAllowInvalidCertificates=True)
db = pymongo.database.Database(mongo, 'Task')
col = pymongo.collection.Collection(db, 'taskdata')

app=Flask(__name__)


@app.route('/api/branch')
def fun():
    q=request.form.get('q')
    limit=request.form.get('limit')
    offset=request.form.get('offset')
    x=col.find({'branch':q})
    for i in x:
        print(i)
    return 'success'
    # a={"branches": [{"ifsc": "ABNA0000001","bank_id": "110","branch": "RTGS-HO",      "address": "414 EMPIRE COMPLEX, SENAPATI BAPAT MARG LOWER PAREL WEST MUMBAI 400013","city": "MUMBAI","district": "GREATER BOMBAY","state": "MAHARASHTRA"}]}
    # return a


if __name__=='__main__':
    app.run(debug=True)