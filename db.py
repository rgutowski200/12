import streamlit as st

try:
    from supabase import create_client
except Exception:
    create_client = None

class _MissingSupabase:
    def __getattr__(self, name):
        raise RuntimeError("Supabase is not configured. Add SUPABASE_URL and SUPABASE_ANON_KEY to Streamlit secrets.")

try:
    url = st.secrets.get("SUPABASE_URL") or st.secrets.get("supabase_url")
    key = st.secrets.get("SUPABASE_ANON_KEY") or st.secrets.get("supabase_anon_key")
    supabase = create_client(url, key) if create_client and url and key else _MissingSupabase()
except Exception:
    supabase = _MissingSupabase()
