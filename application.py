from app.settings import APP_PORT
from app import views as application


def main() -> None:
    application.app.run(port=APP_PORT)


if __name__ == "__main__":
    main()
