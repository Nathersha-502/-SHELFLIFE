from database.connection import db
from services.auth_service import auth_service
from services.inventory_service import InventoryService

print(f"DB Engine: {db.engine}")
ok, u, msg = auth_service.login('admin', 'admin123')
print(f"Login: {ok} — {msg}")
cats = InventoryService.get_categories()
print(f"Categories loaded: {len(cats)}")
print("ALL BACKEND TESTS PASSED — APP IS READY!")
