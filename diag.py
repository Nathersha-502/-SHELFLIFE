import sys, os, traceback

LOG = r"C:\Users\smjai\Documents\shelflife_result.txt"

def write(msg):
    with open(LOG, "a") as f:
        f.write(msg + "\n")

# Clear log
open(LOG, "w").close()

write("=== SHELFLIFE DIAGNOSTIC ===")
write(f"Python: {sys.version}")
write(f"CWD: {os.getcwd()}")

try:
    os.chdir(r"C:\Users\smjai\.gemini\antigravity\scratch\shelflife")
    sys.path.insert(0, r"C:\Users\smjai\.gemini\antigravity\scratch\shelflife")
    write(f"Working dir set: {os.getcwd()}")
except Exception as e:
    write(f"CHDIR FAIL: {e}")

write("\n[1] Testing config import...")
try:
    import config
    write("    config OK")
except Exception as e:
    write(f"    FAIL: {e}\n{traceback.format_exc()}")

write("\n[2] Testing database.schema import...")
try:
    import database.schema as schema
    write(f"    schema OK — seed entries: {len(schema.DEFAULT_SEED)}")
except Exception as e:
    write(f"    FAIL: {e}\n{traceback.format_exc()}")

write("\n[3] Testing database.connection import...")
try:
    from database.connection import db
    write(f"    DB engine: {db.engine}")
except Exception as e:
    write(f"    FAIL: {e}\n{traceback.format_exc()}")

write("\n[4] Testing auth_service...")
try:
    from services.auth_service import auth_service
    ok, u, msg = auth_service.login("admin", "admin123")
    write(f"    Login: {ok} — {msg}")
except Exception as e:
    write(f"    FAIL: {e}\n{traceback.format_exc()}")

write("\n[5] Testing inventory_service...")
try:
    from services.inventory_service import InventoryService
    cats = InventoryService.get_categories()
    write(f"    Categories: {len(cats)}")
except Exception as e:
    write(f"    FAIL: {e}\n{traceback.format_exc()}")

write("\n=== ALL DONE ===")
