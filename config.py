# ------------------
# CONFIGURATION FILE
# ------------------

# 1. API KEY
# This is intentionally empty for security. The key will be loaded from Streamlit Secrets during deployment.
API_KEY = ""

# 2. SEARCH PARAMETERS (Defaults, can be overridden in the app)
MAX_COMMENTS = 100

# 3. BRAND & COMPETITOR DEFINITIONS
COMPETITORS = {
    'Atomberg': ['atomberg'],
    'Crompton': ['crompton'],
    'Orient': ['orient electric', 'orient'],
    'Havells': ['havells'],
    'Usha': ['usha'],
    'Luminous': ['luminous']
}

# 4. SCORING WEIGHTS
MENTION_WEIGHTS = {
    'title': 10,
    'description': 5,
    'comments': 1
}