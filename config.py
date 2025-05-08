import os



class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7943910018:AAHSlow0bLn3FQ0sJweZuWTBiCm9gW-wt6I")
      API_ID = int(os.environ.get("APP_ID", 26191149))
      API_HASH = os.environ.get("API_HASH", "c9763bb66ef232ab6b5a753689557d86")
      CAPTION_TEXT = os.environ.get("CAPTION_TEXT", "`{file_name}`")
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "nil")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "Anubhav Chauhan")
