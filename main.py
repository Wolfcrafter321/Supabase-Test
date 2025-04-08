import json
import supabase
from supabase import create_client, Client
from pprint import pprint as pp

# read url and data
with open("supabase-key.txt", "r", encoding="utf-8") as f:
    supa_key = json.load(f)

# NOTE: var: type ... 【:】型アノテーション
supabase: Client = create_client(supa_key["url"], supa_key["anon-key"])

# 例：データを追加
data = {
    "address": "192.168.0.0",
    "note": "It's testing!"
}
for i in range(10):
    res = supabase.table("Ping").insert(data).execute()
