# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 15:27:47 2020

@author: ZuroChang
"""


#from datetime import datetime
from flask import current_app
from flask import render_template, redirect, url_for
from flask_login import current_user
from . import main
from ..email import Email
from .Config import FolderPath


@main.route('/', methods=['GET','POST'])
def index():
    if current_user.is_authenticated:
        return(render_template('index.html'))
    
    return(redirect(url_for('authorization.login')))


@main.route('/mail')
def _mail():
    _Email=Email(main,Subject='This is a test mail',
        Recipients=['zurochang@gmail.com'],
        Cc=[]
    )
    _Email.Content(Body='This is the content of test mail')
    
    FP=FolderPath()
    for entry in ['001.pdf']:
        _Email.AttachAttachment(SourceFolder=FP.PDF,
            File=entry
        )
    _Email.Send()
    
    return({'Status':200})

@main.route('/chart')
def chartJS():
    current_app.logger.info("simple page info...")
    return(render_template('chart.html'))