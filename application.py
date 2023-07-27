from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn import metrics 
import warnings
import pickle
warnings.filterwarnings('ignore')


file = open("Notebook\model.pkl","rb")
gbc = pickle.load(file)
file.close()

application = Flask(__name__)

@application.route("/", methods=["GET", "POST"])
def phishingDecat():
    if request.method == "POST":
        qty_dot_url=int(request.form.get('qty_dot_url'))
        qty_hyphen_url=int(request.form.get('qty_hyphen_url'))
        qty_underline_url=int(request.form.get('qty_underline_url'))
        qty_slash_url=int(request.form.get('qty_slash_url'))
        time_domain_expiration=int(request.form.get('time_domain_expiration'))
        ttl_hostname=int(request.form.get('ttl_hostname'))
        qty_mx_servers=int(request.form.get('qty_mx_servers'))
        
        
        
        new_data = ([[qty_dot_url,qty_hyphen_url,qty_underline_url,qty_slash_url,time_domain_expiration,ttl_hostname,qty_mx_servers]])
        predict = file.predict(new_data)
        
        if predict[0] == 1:
            result = 'Phishing'

        else:
            result = 'Non  phishing'

        return render_template('predictdata.html',result=result)

    else:
        return render_template('home.html')
        
        
        


         
         
        


if __name__ == "__main__":
    application.run(host="0.0.0.0")