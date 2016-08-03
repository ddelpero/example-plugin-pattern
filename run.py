from app import create_app


app = create_app()

#app.plugins['toaster'].do_plugin_stuff()
app.do_plugins()

print(repr(app.plugins))
