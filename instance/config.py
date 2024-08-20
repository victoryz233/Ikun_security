#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : yds
# @Time    : 18-5-10
# @File    : config.py
# @Desc    : ""

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    def __init__(self):
        pass

    WEB_USER = 'admin'  # Web Auth User
    WEB_PASSWORD = '1xx'  # Web Auth Password
    POCSUITE_PATH = basedir + '/../yandi/views/modules/scanner/pocsuite_plugin/'
    AWVS_REPORT_PATH = basedir + '/../yandi/static/download/'  # static file download
    WEB_HOST = '0.0.0.0'  # Web Server Host
    WEB_PORT = 5000  # Web Server Port
    UPDATE_URL = ""  # check update
    VERSION = '1.1.0'  # scanner version
    AWVS_URL = 'https://172.23.144.1:3443'  # Acunetix Web Vulnerability Scanner Url
    AWVS_API_KEY = "1986ad8c0a5b3df4d7028d5f3c06e936cc64ca74776b04a9480cba201b17eeb33"  # Acunetix Web Vulnerability Scanner API Key


class ProductionConfig(Config):
    DB_HOST = '127.0.0.1'  # MongoDB Host
    DB_PORT = 27017  # MongoDB Port (int)
    DB_NAME = 'fuxi'  # MongoDB Name
    DB_USERNAME = 'ikun'  # MongoDB User
    DB_PASSWORD = '123456789'  # MongoDB Password
    CONFIG_NAME = 'fuxi'  # Scanner config name
    PLUGIN_DB = 'dev_plugin_info'  # Plugin collection
    TASKS_DB = 'dev_tasks'  # Scan tasks collection
    VULNERABILITY_DB = 'dev_vuldb'  # Vulnerability collection
    ASSET_DB = 'dev_asset'  # Asset collection
    CONFIG_DB = 'dev_config'  # Scanner config collection
    SERVER_DB = 'dev_server'  # Asset server collection
    SUBDOMAIN_DB = 'dev_subdomain'  # Subdomain server collection
    DOMAIN_DB = 'dev_domain'  # Domain server collection
    GITHUB_DB='dev_github' #新添加的github探测
    SUBGITHUB_DB='dev_subgithub' #新添加的github探测子内容
    PORT_DB = 'dev_port_scanner'  # Port scan collection
    AUTH_DB = 'dev_auth_tester'  # Auth tester tasks collection
    ACUNETIX_DB = 'dev_acunetix'  # Acunetix scanner tasks collection
    WEEKPASSWD_DB = 'dev_week_passwd'  # Week password collection
    MAIL_TASK_DB =  'dev_task_mail'# mail task
    MAIL_DB ='dev_mail' # mail task then data
    TODO_DB='dev_todo' #add todolist


