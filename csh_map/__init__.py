import os
import requests
from flask import Flask, render_template, redirect, url_for, session
from csh_map.ldap import ldap_init, get_onfloors, get_groups
from flask_pyoidc.flask_pyoidc import OIDCAuthentication
from flask_pyoidc.provider_configuration import ProviderConfiguration, ClientMetadata

app = Flask(__name__)

if os.path.exists(os.path.join(os.getcwd(), "config.py")):
    app.config.from_pyfile(os.path.join(os.getcwd(), "config.py"))
else:
    app.config.from_pyfile(os.path.join(os.getcwd(), "config.env.py"))

# Disable SSL certificate verification warning
requests.packages.urllib3.disable_warnings()

ldap_init(app)

APP_CONFIG = ProviderConfiguration(
    issuer=app.config['OIDC_ISSUER'],
    client_metadata=ClientMetadata(
        **app.config['OIDC_CLIENT_METADATA']
    )
)
auth = OIDCAuthentication({'app': APP_CONFIG}, app)

@app.route("/")
@auth.oidc_auth('app')
def index():
    return render_template('index.html',
                           username=session['userinfo'].get('preferred_username', ''),
                           onfloors=get_onfloors(app),
                           groups=get_groups(app))

@app.route('/logout')
@auth.oidc_logout
def logout():
    return redirect(url_for('index'), 302)
