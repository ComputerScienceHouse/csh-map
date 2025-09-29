# Flask config
DEBUG = True
IP = '127.0.0.1'
PORT = '6969'
SERVER_NAME = 'localhost:6969'
SECRET_KEY = ''

# LDAP config
LDAP_URL = 'ldaps://stone.csh.rit.edu'
LDAP_BIND_DN = 'krbprincipalname=map/os-router-nrh.csh.rit.edu@CSH.RIT.EDU,cn=services,cn=accounts,dc=csh,dc=rit,dc=edu'
LDAP_BIND_PW = ''

# OpenID Connect SSO config
MAP_OIDC_ISSUER='https://sso.csh.rit.edu/auth/realms/csh'
MAP_OIDC_CLIENT_ID='map'
MAP_OIDC_CLIENT_SECRET=''
MAP_OIDC_LOGOUT_REDIRECT_URIS=['localhost:6969/logout']

PLUG_SUPPORT = False
