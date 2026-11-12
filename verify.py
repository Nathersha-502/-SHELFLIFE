import sys
mods = [
    'database.connection',
    'services.auth_service',
    'services.inventory_service',
    'services.recommendation_engine',
    'services.transfer_service',
    'services.audit_service',
    'services.demand_analysis_service',
    'services.notification_service',
    'gui.components.sidebar',
    'gui.components.header',
    'gui.components.table',
    'gui.components.cards',
    'gui.components.charts',
    'gui.components.dialogs',
    'gui.views.dashboard_view',
    'gui.views.inventory_view',
    'gui.views.products_view',
    'gui.views.recommendations_view',
    'gui.views.demand_view',
    'gui.views.transfers_view',
    'gui.views.sales_view',
    'gui.views.branches_suppliers_view',
    'gui.views.users_view',
    'gui.views.audit_view',
    'gui.views.settings_view',
    'gui.app',
]
ok = 0
fail = 0
for m in mods:
    try:
        __import__(m)
        print(f'OK: {m}')
        ok += 1
    except Exception as e:
        print(f'FAIL: {m} -> {e}')
        fail += 1
print(f'\n{"="*40}')
print(f'{ok}/{len(mods)} modules OK  |  {fail} FAILED')
if fail == 0:
    print('APP IS READY TO LAUNCH!')
