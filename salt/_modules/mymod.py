# This overrides the original test module
def hello():
	return 'hello!'

# salt '*' saltutil.sync_all
# salt '*' mymod.hello
