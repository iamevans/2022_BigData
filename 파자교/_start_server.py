import server

app = server.create_app()
app.run(debug=True, host='127.0.0.1', port=5000)