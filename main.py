import parsing_norway
import app

if __name__ == '__main__':
    parsing_norway.get_and_save_information()
    app.start_flask()