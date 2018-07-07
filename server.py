from star_wars import app #from the folder, import your app

if __name__ == '__main__': #run the app
    app.run(debug = True, threaded=True, host='localhost', port=5555)
    