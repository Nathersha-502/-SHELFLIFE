"""SHELFLIFE — Entry Point"""
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

if __name__ == "__main__":
    try:
        from gui.app import SHELFLIFEApp
        app = SHELFLIFEApp()
        app.mainloop()
    except Exception as e:
        logging.critical(f"Fatal error: {e}", exc_info=True)
        raise
