from jinja2 import Environment, FileSystemLoader, meta
def page(file):
	env = Environment(loader=FileSystemLoader('templates'))
	template_source = env.loader.get_source(env,file)
	parsed_content = env.parse(template_source)
	dic=meta.find_undeclared_variables(parsed_content)
	return (dict.fromkeys(dic,''))
f=page('test.html')
print(f)
