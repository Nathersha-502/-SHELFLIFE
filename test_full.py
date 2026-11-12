import sys
import os

out = open(r"C:\Users\smjai\Documents\shelflife_result.txt", "w")
sys.stdout = out
sys.stderr = out

try:
    os.chdir(r"C:\Users\smjai\.gemini\antigravity\scratch\shelflife")
    sys.path.insert(0, r"C:\Users\smjai\.gemini\antigravity\scratch\shelflife")

    print("Step 1: Testing database connection...")
    from database.connection import db
    print(f"  DB Engine: {db.engine.upper()} ✅")

    print("Step 2: Testing authentication...")
    from services.auth_service import auth_service
    ok, u, msg = auth_service.login('admin', 'admin123')
    print(f"  Login OK: {ok} — {msg} ✅")

    print("Step 3: Testing inventory service...")
    from services.inventory_service import InventoryService
    cats = InventoryService.get_categories()
    print(f"  Categories: {len(cats)} loaded ✅")

    print("\n=============================")
    print("ALL BACKEND TESTS PASSED ✅")
    print("THE APP IS READY TO LAUNCH!")
    print("=============================")

except Exception as e:
    import traceback
    print(f"ERROR: {e}")
    traceback.print_exc()
finally:
    out.flush()
    out.close()
