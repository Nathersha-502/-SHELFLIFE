import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_NAME = os.getenv("DB_NAME", "shelflife_db")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
SECRET_KEY = os.getenv("SECRET_KEY", "shelflife_secret")

APP_NAME = "SHELFLIFE"
APP_VERSION = "2.0.0"
APP_THEME = "dark"

COLORS = {
    "bg_primary":    "#0F1117",
    "bg_secondary":  "#1A1D2E",
    "bg_card":       "#1E2235",
    "bg_sidebar":    "#141625",
    "accent":        "#6C63FF",
    "accent_hover":  "#7C73FF",
    "success":       "#00C896",
    "warning":       "#FFB547",
    "danger":        "#FF5C6A",
    "info":          "#4FC3F7",
    "text_primary":  "#F0F0F0",
    "text_secondary":"#9BA3C2",
    "border":        "#2A2D45",
    "safe":          "#00C896",
    "watch":         "#FFB547",
    "urgent":        "#FF5C6A",
    "expired":       "#7B7B9B",
}

STATUS_COLORS = {
    "SAFE":    "#00C896",
    "WATCH":   "#FFB547",
    "URGENT":  "#FF5C6A",
    "EXPIRED": "#7B7B9B",
}

RISK_THRESHOLDS = {
    "EXPIRED": 0,
    "URGENT":  7,
    "WATCH":   14,
}
